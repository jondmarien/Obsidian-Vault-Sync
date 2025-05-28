---
title: Steps of Code Injection
author:
  - Jon Marien
created: 2025-02-12
published: 2025-02-12
tags:
  - classes
  - INFO43921
---

| Title                   | Author                       | Created           | Published         | Tags                                               |
| ----------------------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| Steps of Code Injection | <ul><li>Jon Marien</li></ul> | February 12, 2025 | February 12, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# Code Injection
Code injection is a technique where malicious code is inserted into a running process. This can allow malware to hide its activity, piggyback on the permissions of legitimate processes, or alter the functionality of the system. The process of code injection typically involves four key steps:

## **Locate the target process**:
*   The injector process first selects the target process into which it will inject its code.
*   Malware uses APIs such as `CreateTool32HelpSnapshot()`, `Process32First()`, and `Process32Next()` to search for the target process by name and retrieve its Process ID (PID).
*   The `OpenProcess()` API is then used to open a handle to the target process. This handle is needed to manipulate the target process's virtual memory, and debug privileges may be required.

## **Inject the code**:
*   **Allocate memory:** The injector process allocates space in the target process's virtual memory using APIs such as `VirtualAllocEx()`.  The allocated memory needs to have the correct permissions (e.g., read, write, and execute) so the injected code can be written to and executed from that location.
*   **Write the code:** The injector process copies its code into the allocated memory using `WriteProcessMemory()`. This effectively transfers the malicious code into the target process's memory space. An alternate method uses section objects and views, where the malware maps a part of its memory to the target process, creating a reflection of the malware's memory in the target. This can be done using `NtCreateSection()` and `NtMapViewOfSection()`.

## **Execute the injected code**:
* After the code is injected, the instruction pointer needs to be redirected to execute the injected code. Several techniques can be used to do this.
* **Remote thread creation:** A new thread is created in the target process that starts its execution at the location of the injected code. APIs like `CreateRemoteThread()`, `RtlCreateUserThread()`, and `NtCreateThreadEx()` are used for this purpose.
	* Creating a new thread can be detected by anti-malware programs.
* **Altering thread context:** The instruction pointer (EIP) of an existing thread in the target process is modified to point to the injected code. APIs such as `GetThreadContext()` and `SetThreadContext()` are used to modify a thread's context.
- **Asynchronous Procedure Call (APC) queueing:** The injected code is queued as an APC to an existing thread's APC queue using the `QueueUserAPC()` API.  When the thread enters an alertable state, the injected code is executed.

These steps are crucial for malware to execute its malicious payload in a system. Code injection can be used to alter the functionality of processes or the entire OS. Understanding these steps is vital for malware analysis and detection.