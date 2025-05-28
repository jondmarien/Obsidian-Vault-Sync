---
title: Concepts
author:
  - Jon Marien
created: 2025-03-05
published: 2025-03-05
tags:
  - classes
  - INFO43921
---

| Title    | Author                       | Created        | Published      | Tags                                               |
| -------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Concepts | <ul><li>Jon Marien</li></ul> | March 05, 2025 | March 05, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |

## Basic Cybersecurity Concepts, as presented in the sources:
* **Code Injection:** Malware inserts its malicious code into another legitimate process to hide, piggyback on permissions, or alter functionality. This can occur in user-mode (affecting a specific process) or kernel-mode (affecting the entire system). Common techniques involve memory allocation within the target process, writing the malicious code, and then executing it, often using Windows APIs.

* **DLL Injection:** A type of code injection where malware forces a target process to load a malicious DLL. The injector exploits the fact that KERNEL32.DLL has the same image base address in both processes to find the address of LoadLibrary(). It then copies the path of the DLL into the target process's memory and uses CreateRemoteThread or QueueUserAPC to execute LoadLibrary in the target process.

* **Fileless Attack:** A type of attack where malware operates without writing files to disk, making it harder to detect.

* **Hashing:** A technique used to uniquely identify a malware sample based on its content. Common hashing algorithms include MD5, SHA1, and SHA256.

* **Hooking:** Modifying system functions and data structures.

* **Magic Bytes:** Specific characters at the beginning of a file that identify its format. For example, Windows DOS executables start with `MZ`, and ZIP files start with `PK`.

* **Malware:** Software designed to cause harm to a computer system. Types of malware include:
    * **Adware:** Displays unwanted ads.
    * **Banking Malware:** Captures banking credentials. 
    * **Botnet:** A network of infected machines controlled by an attacker.
    * **Cryptominer:** Mines cryptocurrency, consuming system resources.
    * **Downloader:** Downloads other malware.
    * **Keylogger:** Records keystrokes.
    * **Point-of-Sale (PoS) Malware:** Steals credit card information from PoS devices.
    * **Rootkit:** Conceals its activity on the system.
    * **Spyware:** Steals sensitive data.

* **Obfuscation:** Making code difficult to understand.

* **Packer/Cryptors:** Tools used to compress and encrypt malware to avoid detection.

* **Persistence Mechanisms:** Techniques used by malware to ensure it remains active on a system after a reboot. These include registry run keys, startup folders, services, file infection, DLL hijacking, scheduled tasks, and Image File Execution Options (IFEO).

* **Process Hollowing:** A code injection technique where malware starts a legitimate process in a suspended state and replaces its memory with malicious code.

* **Prompt Injection:** An attack that manipulates the behavior of large language models (LLMs) by crafting malicious prompts.

* **Shellcode:** Raw machine code without PE headers that requires manual relocation and API resolution.

* **Static Analysis:** Analyzing malware without executing it. Techniques include file format identification, hashing, string analysis, and examining PE file structure.

* **Vulnerability:** A weakness in a system that can be exploited by an attacker.

* **Windows Registry:** A hierarchical database that stores configuration settings for the operating system and applications.

* **Antivirus:** Software designed to detect and remove malware.
