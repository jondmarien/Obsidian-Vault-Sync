---
title: Steps of Process Hollowing
author:
  - Jon Marien
created: 2025-02-12
published: 2025-02-12
tags:
  - classes
  - INFO43921
---

| Title                      | Author                       | Created           | Published         | Tags                                               |
| -------------------------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| Steps of Process Hollowing | <ul><li>Jon Marien</li></ul> | February 12, 2025 | February 12, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# Process Hollowing
Process hollowing is a technique used by malware to hide its presence and activity by running malicious code within a legitimate process. The steps involved in process hollowing are:

*   **Start a legitimate process in a suspended state:** The malware begins by launching a legitimate system process, such as `calc.exe`, but in a suspended state using APIs like `CreateProcessA`, `CreateProcessW`, `CreateProcessInternalW`, or `CreateProcessInternalA`. This means that the process is created but its main thread is not yet running.
    *   Malware does this so that when a user looks at Task Manager, the malware is hidden as a legitimate process with a normal path.
*  **Create a section and view:** The malware creates a section object using `NtCreateSection()` and maps a view of this section into the address space of the suspended process, as well as into its own process.
     *   The views act as a mirror image, so any changes made by the malware to its own view are reflected in the target process's view.
   *   Alternatively, the malware can allocate memory in the target process using `VirtualAllocEx()` and copy its code using `WriteProcessMemory()` instead of using sections and views.
*   **Hollow out the legitimate process:** The malware replaces the original code and data of the legitimate process with its own malicious code.
    *   This is achieved by writing the malicious code into the memory region allocated/mapped in the target process using `WriteProcessMemory()` or by writing to its own view, which is mirrored in the view of the target process.
    *   In effect, the malware scoops out the original code of the legitimate process and replaces it with its own malicious code.
*   **Modify the thread context and resume execution:** The malware modifies the main thread's context in the target process to point to the injected malicious code.
    *   It does so by getting the thread's context using `GetThreadContext()`, modifying the instruction pointer (EIP) to point to the injected code, and setting the modified context using `SetThreadContext()`.
    *   Finally, the malware resumes the thread using `ResumeThread()`, which causes the target process to execute the injected code instead of its original code.
    *   The process now runs with its original path, but is now running malicious code.

Process hollowing is a sophisticated technique that allows malware to evade detection by masquerading as a legitimate process. By starting with a clean process but replacing its code, the malware makes it more difficult to detect via simple checks on running processes.
