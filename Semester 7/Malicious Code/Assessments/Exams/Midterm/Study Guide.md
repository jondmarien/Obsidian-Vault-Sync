---
title: Study Guide
author:
  - Jon Marien
created: 2025-02-12
published: 2025-02-12
tags:
  - classes
  - INFO43921
---

| Title       | Author                       | Created           | Published         | Tags                                               |
| ----------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| Study Guide | <ul><li>Jon Marien</li></ul> | February 12, 2025 | February 12, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# Midterm Review
![[image-29.png]]

- Meaning of prompt injection, top 10 LLM, difference between malware and exploit code.
- What is the usage of trid notepad, YARA, strings, packers etc.
- What is entropy, MZ.
- There will be questions similar to assignment 2.
- Find location of DLL (physical address) based on a screenshot.
- Static analysis: thumbnail, extensions, how to find the format of a file (magic byte, cmd in linux).
- DLL injection: classical, persistence mechanisms: from a screenshot explain what type of persistence mechanism.
- Code injection: Understand the 4 steps. She will give us a bunch of APIs and we map which belong to processes and malware.
- Clearly explain APC queue from a diagram screenshot.
- Process Hollowing.

***25 Questions: MCQ, T/F,  Multiple Selection, Written - No practical questions***

# Malicious Code Study Guide
## Quiz
*Instructions: Answer the following questions in 2-3 sentences each.*

1. What vulnerability is present in code that calculates a total charge without validating the quantity variable for a negative value?
2. How can a lack of input validation of user-supplied data, like a website's birthday and homepage fields, lead to a Cross-Site Scripting (XSS) attack?
3. In the example code with the `buildList` function, what happens when a zero value is provided as the `untrustedListSize`?
4. What is the significance of magic bytes in the context of file analysis? Give an example of a file and its corresponding magic bytes.
5. Explain the difference between static and dynamic malware analysis.
6. How does code injection work, and why is it a dangerous technique?
7. Describe what a botnet is and how it can be used maliciously.
8. What is the purpose of DLL injection, and how does it work?
9. What is a "run entry" in the Windows Registry, and how can malware use it for persistence?
10. How does process hollowing work, and what does it achieve?

### Quiz Answer Key

1. The vulnerability lies in the potential to provide a negative quantity, resulting in a negative total. This can cause the program to pay money to the user instead of charging them.
2. If the birthday and homepage fields don't validate user input, a malicious user can inject harmful code, like `<script>` tags. This allows the attacker to execute arbitrary scripts in the context of another user's session.
3. While the code prevents negative values, an input of 0 causes the attempt to access list[0] to throw an exception since a zero sized array will have no valid indexes.
4. Magic bytes are a specific sequence of bytes at the beginning of a file that identify the file's format. For example, a PNG file has the bytes \x89PNG.
5. Static analysis involves examining malware without executing it, using tools like disassemblers, while dynamic analysis involves running the malware in a controlled environment and observing its behavior, such as its actions on the file system or network.
6. Code injection is the process of inserting malicious code into a running process to alter its functionality. This is a dangerous technique as it allows an attacker to gain control over the target application.
7. A botnet is a network of computers infected with malware and controlled by a central attacker. Botnets are used to launch DDoS attacks, send spam, and engage in other malicious activities.
8. DLL injection is the technique of loading a malicious DLL into the memory space of a running process. This enables the malware to execute code in the context of that process.
9. A "run entry" is a registry value that specifies which programs or services to start when a user logs in or the system boots. Malware often creates or modifies these entries for persistence.
10. Process hollowing is a technique where an attacker creates a legitimate process in suspended mode, replaces its memory with malicious code, and then resumes the process. It achieves hiding malicious code within a legitimate process.

## Essay Questions
*Instructions: Write an essay that addresses the following questions.*

1. Describe the various techniques malware uses for persistence on a Windows system, including examples for each.
2. Explain the steps involved in code injection, including various approaches and the APIs commonly used.
3. Compare and contrast DLL injection and process hollowing, discussing their methods, objectives, and strengths and weaknesses.
4. Discuss the OWASP Top 10 LLM vulnerabilities, focusing on prompt injection, its mechanics, and real-world scenarios.
5. Explain the differences between static and dynamic malware analysis, including use cases, advantages, and disadvantages.

### Glossary of Key Terms
**API (Application Programming Interface)**: A set of defined rules and specifications that software programs can follow to communicate with each other.
**Botnet**: A network of computers infected with malware and controlled by a central command.
**Code Injection**: The process of inserting malicious code into a running process.
**Cross-Site Scripting (XSS)**: A type of security vulnerability found in web applications that allows an attacker to inject malicious scripts into web pages.
**DLL (Dynamic-Link Library)**: A library of code that can be shared and used by multiple programs.
**DLL Hijacking**: A technique in which malware places a malicious DLL in a location where it will be loaded by a legitimate application instead of the intended DLL.
**Dynamic Analysis**: Analyzing malware by running it in a controlled environment and observing its behavior.
**File Format**: The structure that defines how data is stored in a file, including its layout, header information, and data encoding.
**Hashing**: A method of transforming data to produce a fixed-size value used for data integrity and identification.
**Import Address Table (IAT)**: A table in a PE file containing the addresses of imported APIs used by the file.
**Magic Bytes**: Specific sequences of bytes located at the beginning of a file used to identify its format.
**Malware**: Malicious software designed to damage or gain unauthorized access to a computer system.
**Memory Forensics**: The analysis of the volatile memory (RAM) of a computer to investigate evidence of malicious activities.
**Mutex**: A synchronization primitive used to ensure that only one thread or process accesses a shared resource at a time.
**Persistence Mechanism**: The techniques a malware uses to ensure that it remains active after a reboot or user logout.
**PE (Portable Executable)**: The file format for executable files, DLLs, and other program files used by Windows.
**Process Hollowing**: A technique where a legitimate process is created in a suspended state and its memory is replaced with malicious code.
**Prompt Injection**: A vulnerability in LLMs where a malicious prompt is designed to manipulate the behavior of the LLM or reveal sensitive data.
**Remote Thread Creation**: Creating a new thread within the address space of another (target) process.
**Run Entry**: A registry value that specifies programs to be executed at system startup or user login.
**Section (PE file)**: A segment of a Portable Executable (PE) file that contains a specific type of data, such as code or data.
**Shellcode**: A small piece of code used as the payload in the exploitation of a software vulnerability.
**Static Analysis**: Analyzing malware without executing it, by examining its structure and code.
**Syscall (System Call)**: An interface between user space programs and the operating system kernel that provides access to kernel functions.
**Virtual Memory**: A memory management technique that provides an illusion of large, contiguous memory space for each process.
**Vulnerability**: A flaw or weakness in a software or system that can be exploited by an attacker.