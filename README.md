# Worm Malware – Simulated WannaCry Propagation via SMB Protocol using Python & Metasploit Framework

## Introduction
This project is a simulation of the infamous WannaCry worm-based ransomware. The goal of this simulation is to replicate key behaviors of WannaCry, including its data encryption, self-propagation through the SMB protocol, persistence techniques, and ransom GUI—within a controlled and safe virtual lab environment.

Through this project, we aim to:
- Provide an educational, hands-on understanding of ransomware internals.
- Explore worm-like propagation strategies within local networks.
- Develop a behavior-based Detection Tool capable of identifying common signs of ransomware activity such as suspicious file modifications, registry changes, and abnormal SMB connections.

By combining offensive (malware simulation) and defensive (detection) perspectives, this project not only visualizes how real-world malware like WannaCry operates but also offers insights into how modern endpoint monitoring solutions can detect and mitigate such threats. Although simplified and sandboxed, the simulation demonstrates core techniques used in actual attacks and serves as a practical platform for further study, training, or research.

## Poster
![Poster](https://github.com/grapitycreation/wannacry_smb_worm_simulation/blob/main/Poster_WannaCry.jpg)

## Operational Workflow
The following diagram illustrates the lifecycle and behavior of the simulated WannaCry worm ransomware in our project:

![Operational Diagram](https://github.com/grapitycreation/wannacry_smb_worm_simulation/blob/main/Operational_Diagram.png)

### Step-by-step Breakdown:
- **Phishing Mail with Malicious Attachment**
The attack begins with a phishing email crafted using tools like Zphisher and Tabular. The email contains a fake login page (e.g., Facebook) that tricks the victim into downloading and executing a disguised ```.exe``` payload.

- **Victim Execution**
Once the victim opens the downloaded file, the malware is activated on the host machine.

- **Scanner**
The worm scans the local network for other hosts with port 445 (SMB) open, identifying potential targets for lateral movement.

- **Encryption**
Files with specific extensions (e.g., .txt, .docx) are encrypted using AES-256-CBC, and renamed with a .mu extension. A unique key is generated and stored for later decryption.

- **Persistence**
To ensure it survives reboots, the malware modifies the Windows Registry (HKEY_CURRENT_USER) and logs the infection timestamp.

- **SMB Propagation**
The worm spreads to other machines in the same network by copying itself into public SMB-shared folders (\\[IP]\Users\Public) on discovered hosts.

- **Deleting When Expired**
If the victim does not decrypt within the allowed time window (e.g., 7 days), the malware automatically deletes the encrypted files using a background daemon thread.

- **Decryption**
If a valid decryption key is entered (e.g., after ransom payment), the user can recover the original files via a GUI built with C#.

## Tools and Platforms Used
The following tools, frameworks, and platforms were used to simulate the WannaCry worm ransomware attack and build the detection mechanisms in a controlled lab environment:

### Development & Programming
- **Python**: Core language used to implement the ransomware logic, encryption, SMB propagation, and detection mechanisms.
- **C# (.NET)**: Used to build the ransom note GUI for the victim, including decryption interface and countdown timer.
- **Visual Studio Code / Visual Studio**: Main IDEs for writing and testing both Python and C# components.

### Malware Simulation
- **yInstaller**: Packaged Python scripts into Windows executable files for realistic malware behavior.
- **Resource Hacker**: Changed the malware executable’s icon (e.g., to a PDF icon) to reduce suspicion and increase the likelihood of execution.

### Phishing Attack Tools
- **Zphisher**: Open-source phishing toolkit to generate fake Facebook login pages and host them using LocalXPose for public access.
- **Tabular**: Used to create realistic phishing email templates to lure victims into executing the malicious payload.

### Encryption & Persistence
- **Cryptography (Python library)**: Used to implement AES-256-CBC encryption with secure padding and IV generation.
- **Windows Registry**: Used for persistence by modifying registry keys to ensure the malware runs on startup and tracks infection time.

### Network Propagation
- **SMB Protocol (Port 445)**: Utilized for lateral movement by copying malware executables to shared folders on other LAN machines.
- **psutil (Python)**: Used to scan SMB connections and manage system processes.

### Detection Mechanism
- **watchdog (Python library)**: File system monitoring to detect suspicious .exe creation events in sensitive directories.
- **winreg (Python)**: Monitored changes in critical Windows Registry keys linked to persistence.
- **psutil**: Detected abnormal processes and monitored active TCP connections to port 445.

### Testing Environment
- **Kali Linux (2024.2)**: Used as the attacker's environment for phishing setup and payload generation.
- **Windows 10 & 11 VMs**: Victim and malware execution environments. Malware was executed and observed on isolated machines.
- **Virtual Network**: Simulated local area network for testing lateral movement and SMB propagation.

## Results and Conclusion
### Results
- **Simulated WannaCry Malware**:
  - Successfully replicated core behaviors of the real WannaCry ransomware, including:
    - AES-256-CBC encryption of victim files with .mu extension.
    - Persistence via Windows Registry modifications.
    - Worm-like SMB propagation across LAN by copying itself to public shared folders.
    - Timed file deletion mechanism after the ransom window expires.
    - A functional GUI ransom interface built with C#.

- **Detection Tool**:
  - Effectively detected behavioral indicators of the simulated malware, such as:
    - Mass file modification within a short time window.
    - Creation of suspicious .exe files in sensitive directories like AppData, Temp, or Public.
    - Unauthorized Registry changes related to persistence.
    - Abnormal SMB connections that may indicate lateral movement.
    - Suspicious or unauthorized processes executing from unknown sources.

All detection events were logged and alerted in real-time with minimal false positives.

### Conclusion
This project successfully demonstrates the inner workings of a WannaCry-inspired worm ransomware within a virtualized lab environment. It provides a practical view into:
- How ransomware can propagate laterally across networks via SMB.
- How persistence, encryption, and timed deletion mechanisms are implemented.
- The importance of behavior-based detection in identifying threats beyond traditional signature matching.

While the simulation does not exploit actual vulnerabilities (e.g., EternalBlue), it provides a safe and educational framework for understanding modern malware techniques. The behavior-based Detection Tool also highlights promising directions for building real-world defense mechanisms.

## Demo
- Attack: https://drive.google.com/file/d/1RoijyKzOYck0lcWgbFPNe9fRe_D9KJxj/view?usp=sharing
- Detection: https://drive.google.com/file/d/1AgOEUl57o-GGlOq8Ykhm3lW84ermeKfu/view?usp=sharing

