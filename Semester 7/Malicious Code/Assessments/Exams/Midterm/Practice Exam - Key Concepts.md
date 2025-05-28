Based on the sources provided, here's a breakdown of key concepts for your cybersecurity exam, formatted for short answers, multiple-choice questions (MCQ), and true/false questions:

**I. Core Concepts & Definitions**

*   **Code Injection:**  Malware inserts malicious code into a legitimate process. This allows the malware to hide and use the target's permissions.
*   **DLL Injection:** A specific code injection technique where a malicious DLL is loaded into a target process.
*   **Process Hollowing:** A code injection technique that starts a legitimate process in a suspended state, then replaces its memory with malicious code.
*   **Shellcode Injection:** Injecting raw machine code (shellcode) into a process. Shellcode lacks PE headers, requiring manual relocation and API resolution.
*   **Fileless Attack:** Malware operates without writing files to disk.
*   **Hashing:**  A method to uniquely identify files (including malware) based on content. Common algorithms: MD5, SHA1, SHA256.
*   **Magic Bytes:**  Specific characters at the start of a file that indicate its file type.  For example, MZ indicates a Windows executable.
*   **Vulnerability:** A weakness in a system that can be exploited.
*   **Exploit:** Malicious code that takes advantage of a vulnerability to gain control of a system.
*   **Payload:** The malicious code delivered by an exploit.
*   **Rootkit:** Malware designed to conceal its presence or the presence of other malware on a system.
*   **Spyware/Infostealer:** Malware that steals sensitive data.
*   **Keylogger:** Malware that records keystrokes.
*   **Botnet:** A network of machines infected with malware and controlled by an attacker.
*   **Ransomware:** Malware that encrypts a victim's data and demands payment for its release.
*   **Adware:** Malware that displays unwanted advertisements.
*   **Obfuscation:** Techniques to make code harder to understand, such as renaming variables or removing comments.
*   **Packer/Cryptors:** Programs used to compress and encrypt malware to prevent easy detection.
*   **Persistence Mechanisms:**  Techniques malware uses to ensure it remains active across system reboots.
*   **Prompt Injection:**  Malicious prompts that manipulate the behavior of Large Language Models (LLMs).
*   **Static Analysis:**  Analyzing malware without running it.
*   **Dynamic Analysis:** Analyzing malware by running it in a controlled environment.
*   **Windows Registry:**  A hierarchical database that stores configuration settings for Windows and applications.

**II. Windows Specifics**

*   **PE File Format:**  The standard file format for executables and DLLs in Windows. PE files contain headers and sections.
*   **DLL (Dynamic Link Library):** A file containing code and data that can be used by multiple programs simultaneously.
*   **Windows API (Win32 API):** A vast set of functions available to software developers for creating Windows software. Malware often misuses these APIs.
*   **Image File Execution Options (IFEO):** A registry key used for debugging, which can be misused by malware to launch malicious programs.

**III. Malware Analysis Techniques & Tools**

*   **Static Analysis Tools:** VirusTotal, strings, IDA Pro, Hex Editors, PEiD.
*   **Dynamic Analysis Tools:**  Virtual machines, RegShot, Process Monitor/Hacker, Wireshark, APIMiner.
*   **Hashing Tools:** HashMyFiles, md5deep, sha1deep, sha256deep.
*   **File Identification Tools:** TrID, file command (Linux).

**IV. Persistence Mechanisms (Examples)**

*   **Registry Run Keys:** Malware modifies keys like `HKLM\Software\Microsoft\Windows\CurrentVersion\Run` to execute on startup.
*   **Startup Folders:** Placing executables in startup folders causes them to launch at login.
*   **Windows Services:** Registering malware as a service allows it to run in the background and start automatically.
*   **Scheduled Tasks:** Creating scheduled tasks to execute malware at specific times.

**V. LLM Security**

*   **Prompt Injection:** Crafting malicious prompts to trick LLMs into performing unintended actions. This can include revealing sensitive information or executing malicious code.

**VI. Important APIs**

*   Common Windows APIs used for code injection include: `CreateToolhelp32Snapshot`, `Process32First`, `Process32Next`, `OpenProcess`, `VirtualAllocEx`, `WriteProcessMemory`, `NtCreateSection`, `NtMapViewOfSection`, `CreateRemoteThread`, `RtlCreateUserThread`, `NtCreateThreadEx`, `QueueUserAPC`, `GetThreadContext`, `SetThreadContext`, `LoadLibrary`, `ResumeThread`, `SuspendThread`.
  
  The listed Windows APIs are used in code injection techniques, and while they have legitimate uses, they are often misused in malicious code. Here's a breakdown of those most commonly associated with malicious activity, based on the sources:

*   **`OpenProcess`**: Malware uses this API to gain a handle to a target process. The malware needs the PID of the target process, found using `CreateToolhelp32Snapshot`, `Process32First`, and `Process32Next`. To manipulate the target process's virtual memory, the handle has to be opened in debug mode, requiring debug privileges.
*   **`VirtualAllocEx`**: This API is used to allocate memory in the target process where the malicious code will be written. Malware often requests `PAGE_EXECUTE_READWRITE` permissions for this memory, allowing it to write and then execute the injected code.
*   **`WriteProcessMemory`**: After allocating memory, malware uses this API to copy its malicious code into the allocated space in the target process.
*   **`NtCreateSection` and `NtMapViewOfSection`**: Instead of `VirtualAllocEx` and `WriteProcessMemory`, malware might use these APIs to create a section object and map views of it into both the injector and target processes. This creates a shared memory region, allowing the malware to write code into its own view and have it automatically reflected in the target process's memory.
*   **`CreateRemoteThread`, `RtlCreateUserThread`, and `NtCreateThreadEx`**:  Malware uses these APIs to create a new thread within the target process that starts executing at the beginning of the injected malicious code.
*   **`GetThreadContext` and `SetThreadContext`**: Instead of creating a new thread, malware can modify the context of an existing thread to point its instruction pointer (EIP) to the injected code. This forces the existing thread to execute the malicious code.
*   **`QueueUserAPC`**: This API is used to queue an Asynchronous Procedure Call (APC) to a thread in the target process. When the thread enters an alertable state, it will execute the queued APC, which points to the injected code.

*   **`SuspendThread` and `ResumeThread`**: When using `GetThreadContext` and `SetThreadContext`, the malware often suspends the target thread before modifying its context and resumes it afterward.

*   **`LoadLibrary`**:  In DLL injection, malware uses this function to force the target process to load a malicious DLL. It writes the path to the DLL in the target process's memory and then calls `CreateRemoteThread` or `QueueUserAPC` to execute `LoadLibrary` within the target.

It's important to note that the use of any *single* API from this list doesn't automatically indicate malicious activity. However, a *sequence* of these APIs, particularly `VirtualAllocEx`, `WriteProcessMemory`, and `CreateRemoteThread`, is a strong indicator of code injection and potential malware. Examining the context and parameters of these API calls is crucial for identifying malicious behavior.

**VII. Key Distinctions**

*   **Static vs. Dynamic Analysis:**  Static analysis examines code without execution; dynamic analysis involves running the code in a controlled environment.
*   **User-mode vs. Kernel-mode Injection:** User-mode affects specific processes, kernel-mode impacts the entire system.

This information should provide a solid foundation for answering various types of questions on your cybersecurity exam. Remember to focus on understanding the underlying concepts and how they relate to real-world threats.

