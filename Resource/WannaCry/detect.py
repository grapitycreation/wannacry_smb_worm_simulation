import os
import time
import threading
import psutil
import winreg
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

# === CONFIG ===
WATCH_PATHS = [os.environ.get("USERPROFILE", "C:\\"), "C:\\Users\\Public", "C:\\Temp"]
SUSPICIOUS_EXTENSIONS = [".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".jpg", ".png", ".csv", ".zip", ".rar", ".mp3", ".mp4"]
SUSPICIOUS_WRITE_DIRS = ["AppData", "Temp", "Public"]
EXE_EXT = ".exe"
MOD_THRESHOLD = 30
MOD_TIME_WINDOW = 10
SMB_CONN_THRESHOLD = 1
PERSISTENCE_KEYS = [
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows"),
    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"),
]
WHITELISTED_PROCESSES = [
    "OneDrive.exe", "OneDriveStandaloneUpdater.exe", "FileCoAuth.exe", "Microsoft.SharePoint.exe"
]

def now(): return datetime.now().strftime("[%H:%M:%S]")

# === 1. Monitor file modification burst ===
class MassModificationDetector(FileSystemEventHandler):
    def __init__(self):
        self.mod_times = deque()

    def on_modified(self, event):
        if any(event.src_path.lower().endswith(ext) for ext in SUSPICIOUS_EXTENSIONS):
            self.mod_times.append(time.time())
            # Log modified files
            try:
                with open("suspicious_modified_files.log", "a", encoding="utf-8") as logf:
                    logf.write(f"{datetime.now()} - {event.src_path}\n")
            except Exception as e:
                print(f"[!] Cannot write log for {event.src_path}: {e}")
            while self.mod_times and time.time() - self.mod_times[0] > MOD_TIME_WINDOW:
                self.mod_times.popleft()
            if len(self.mod_times) >= MOD_THRESHOLD:
                print(f"{now()} [ALERT] Mass file modification detected ({len(self.mod_times)} files)!")

# === 2. Monitor for .exe file writes ===
class SuspiciousExeWriteDetector(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.lower().endswith(EXE_EXT):
            if any(d in event.src_path for d in SUSPICIOUS_WRITE_DIRS):
                print(f"{now()} [ALERT] Suspicious .exe write to: {event.src_path}")

# === 3. Monitor SMB connections ===
def monitor_smb_connections():
    while True:
        conns = psutil.net_connections(kind='tcp')
        smb_conns = [c for c in conns if c.raddr and c.raddr.port == 445]
        for c in smb_conns:
            print(f"{now()} SMB connection: laddr={c.laddr}, raddr={c.raddr}, pid={c.pid}")
        if len(smb_conns) > SMB_CONN_THRESHOLD:
            print(f"{now()} [ALERT] High number of SMB (445) connections: {len(smb_conns)}")
        time.sleep(5)

# === 4. Monitor registry persistence ===
def snapshot_registry():
    snapshot = {}
    for root, path in PERSISTENCE_KEYS:
        try:
            key = winreg.OpenKey(root, path)
            values = {}
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    values[name] = value
                    i += 1
                except OSError:
                    break
            snapshot[(root, path)] = values
            winreg.CloseKey(key)
        except FileNotFoundError:
            snapshot[(root, path)] = {}
    return snapshot

def compare_registry_snapshots(old, new):
    changes = []
    for key_id in new:
        old_values = old.get(key_id, {})
        new_values = new.get(key_id, {})
        for name in new_values:
            if name not in old_values:
                changes.append((key_id, name, new_values[name], "NEW"))
            elif old_values[name] != new_values[name]:
                changes.append((key_id, name, new_values[name], "MODIFIED"))
    return changes

def monitor_registry_changes(interval=10):
    print("[*] Monitoring registry persistence keys...")
    prev_snapshot = snapshot_registry()
    while True:
        time.sleep(interval)
        current_snapshot = snapshot_registry()
        changes = compare_registry_snapshots(prev_snapshot, current_snapshot)
        if changes:
            for (root, path), name, value, change_type in changes:
                root_name = "HKCU" if root == winreg.HKEY_CURRENT_USER else "HKLM"
                print(f"[!] Registry {change_type}: {root_name}\\{path}\\{name} = {value}")
        prev_snapshot = current_snapshot

# === 5. Monitor new suspicious processes ===
def monitor_suspicious_processes():
    seen = set()
    while True:
        for p in psutil.process_iter(['pid', 'exe', 'cmdline']):
            try:
                exe_path = p.info['exe']
                if exe_path and exe_path.endswith(EXE_EXT):
                    exe_name = os.path.basename(exe_path)
                    if exe_name in WHITELISTED_PROCESSES:
                        continue  # skip whitelisted processes
                    if p.pid not in seen and any(d in exe_path for d in SUSPICIOUS_WRITE_DIRS):
                        seen.add(p.pid)
                        print(f"{now()} [ALERT] Suspicious process started: {exe_path}")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        time.sleep(5)

# === MAIN ===
if __name__ == "__main__":
    print(f"{now()} [*] Ransomware Behavior Detection Tool Started")

    # Set up watchdog observers
    observer = Observer()
    handler_mod = MassModificationDetector()
    handler_exe = SuspiciousExeWriteDetector()
    for path in WATCH_PATHS:
        if os.path.exists(path):
            observer.schedule(handler_mod, path, recursive=True)
            observer.schedule(handler_exe, path, recursive=True)
    observer.start()

    # Start background threads
    threading.Thread(target=monitor_smb_connections, daemon=True).start()
    threading.Thread(target=monitor_registry_changes, daemon=True).start()
    threading.Thread(target=monitor_suspicious_processes, daemon=True).start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"{now()} [*] Exiting...")
        observer.stop()
    observer.join()