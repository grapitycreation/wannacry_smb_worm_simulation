# WannaCry simulation & Detection Tool

## Building Executables
```sh
pyinstaller --onefile --add-data "gui.exe;." wannacry.py
pyinstaller --noconfirm --onefile detect.py
```
For real-world malware, use the `--noconsole` option to hide the console window.

---

**WannaCry:**
- Search for files with specific target extensions on the local system.
- Encrypt them using AES encryption, and rename them with a new extension (.mu).
- Achieve persistence by adding itself to Windows startup via the registry.
- Propagate itself to other computers in the same LAN by copying its executable via SMB (port 445) to shared folders on accessible hosts.
- Store the infection timestamp in the registry and automatically delete encrypted files after a set expiration period.
- Provide a decryption routine to restore files if the correct key is supplied.

---

**Detection Tool:**
- Monitor for mass file modifications (potential ransomware activity).
- Detect suspicious `.exe` file writes and executions.
- Monitor abnormal SMB (port 445) connections.
- Watch for any registry changes in common persistence keys under `HKCU` and `HKLM` (such as Run, RunOnce, Services, etc.).
- Alerts are printed to the console. Modified files are logged to `suspicious_modified_files.log`.

---

**Key:**  `TWpJMU1qQTBOekVrTWpJMU1qQTBORFFq`

---

**Notes:**  
**Run as Administrator** for full monitoring capabilities (especially registry and network).


---

**Warning:**  
This is a sample ransomware and detection tool for research and educational purposes only.  
**Do not run on production or personal systems. Use in a controlled lab environment.**