---
title: Process Hollowing
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
  - INFO43921
---

| Title             | Author                       | Created           | Published         | Tags                   |
| ----------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Process Hollowing | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |

# Chapter 11
## **Process Hollowing**

One of the big requirements of malware is that they need   **stealth/hiding** . If a malware process runs on its own and if a user casually browses the Task Manager, they notice a weirdly named malware process running, which might raise their suspicions that it is not a benign process.

To counter this, the malware might   **rename itself**  as svchost.exe, explorer.exe, or with the name of any other system/clean process to beat the scrutiny of a casual observer. But just renaming the malware filename   **doesn’t change the true properties**  of the malware. For example, by default, system programs like svchost.exe, are in the C:Windowssystem32   **directory** .

If you verify the properties of any of the malware file which has renamed it as svchost.exe, you still notice that the path of this process is not C:Windowssystem32svchost.exe, because of which a highly observant user or even anti-malware products can easily catch such malware.

To counter this malware, authors devised a new technique called   **process hollowing** , which works by launching one of the existing systems/clean programs but in a   **suspended state** . Once launched in a suspended state, the malware process scoop/hollow out the actual inner code and data of the target system/clean process, and replace it with its own malicious content. Since the process was originally launched from its own system/clean program on disk, the path of the process still points to the original clean/system program on disk. But, it now holds the malware code running from within the process. The whole process is better explained using Figure 10-27.

![](M5-2-Process%20Hollowing_0.png)

Let’s now try out Sample-10-6, which is an interactive sample.

![](M5-2-Process%20Hollowing_1.png)

1. When you run Sample-10-6.exe as in Figure 10-28, it first starts the calculator process calc.exe in suspended mode, as seen in Figure 10-29.

![](M5-2-Process%20Hollowing_2.png)

![](M5-2-Process%20Hollowing_3.png)

2. Press any key to continue. The sample then creates a section and a view of the section in the calc.exe process . As seen in the output of the sample in Figure 10-28, the view is mapped at address 0x3b0000 in Sample-10-6.exe and address 0xa0000 in calc.exe. You can verify this using Process Hacker, as seen in Figure 10-30. Do note that the addresses might be different when you run the sample, and you can obtain your addresses from the output of your sample run (see Figure 10-28). The NtCreateSection() API creates a section and NtMapViewOfSection()creates a view.

3. You can now press any key to continue. This should continue with the hollowing process, and the sample now   **copies/injects its code into its local view** , which automatically reflects/maps it into the view of calc.exe. Alternatively, do note that the malware can allocate memory in calc.exe and copy/inject its code using VirtualAllocEx() and WriteProcessMemory() , instead of using Section and View.

4. With the hollowing process complete and code injection/copying done, the sample now  **reset the instruction pointer** of the suspended process calc.exe by having it point to the newly injected code in its view, after which it resumes the suspended calc.exe process/thread, which should run the injected code. To reset the instruction pointer to the injected code, the sample uses the GetThreadContext() and SetThreadContext() APIs. To resume the suspended thread, it uses the ResumeThread()API .

![](M5-2-Process%20Hollowing_4.png)

With our injected code now running inside calc.exe, instead of calc.exe’s real calculator program/code running, our injected code will now run which pops up a message box as seen in Figure 10-31. It also creates a file called PROCESS_HOLLOWED_CALCULATOR.txt in the same folder as the sample, which can also be seen in Figure 10-31.

![](M5-2-Process%20Hollowing_5.png)

 **Classical Shellcode Injection**

In classical DLL injection, the DLL is injected via a LoadLibrary(). The end goal of the injector is to inject a full DLL PE file into the target process. We know that with a DLL PE file, it starts with the PE header, and then the code is located somewhere further down, which is what is executed by the Injector using LoadLibrary(). But at the start of the PE file, it is the PE header before the code that holds the information for LoadLibrary() on how to set up the code in memory, including fixing the import table and relocation table.

Shellcode is simply straight code, like the code in a PE file like a DLL or an executable, but there is no PE header accompanying this shellcode. It can’t be loaded by LoadLibrary() or the Windows loader. It has no headers that contain any information that can help a loader for any address relocations fixes or other API dependencies resolution.

From a technique and APIs usage perspective, classical shellcode injection works very similarly to the injection technique we mentioned in the section steps of code injection or classical DLL injection. Memory is allocated in the target process. The shellcode is copied over instead of a full DLL PE file or an executable PE file, and the shellcode is executed directly in the target process. The injector process after injecting the shellcode must do any relocations, and import table fixes manually since there is no Windows loader to do that job.

![](M5-2-Process%20Hollowing_6.png)

 **Reflective DLL Injection**

Malware consists of multiple components, and usually the primary downloader/loader component of the malware downloads secondary components like a malicious DLL/EXE from the C2 server over the network, or its resource section. These malicious DLLs are then injected into other target processes. But with classical DLL injection, the DLL component injected into the target process is a file on the disk, which is loaded using the LoadLibrary() API. The fact that it is a file on disk and you also use LoadLibrary() API to inject into a target process isn’t very stealthy and is easily caught.

Only if there was a way where after obtaining the DLL PE file over the network or from its resource section the malware downloader/loader component could inject and load it directly into the target process without having to write it to file on the disk and without having to use LoadLibrary(). Yes, this is still possible with another technique called reflective DLL injection.

Reflective DLL injection works by having the downloader/loader, double as a Windows loader. So instead of relying on the Windows loader via the call to LoadLibrary() API, the injector process does the job of loading the DLL as a module in memory of a target process. Also, it needs to carry out two important operations otherwise carried out by the Windows loader—fixing the relocation table and the import table which you learned in Chapter 4. We won’t go into the depths of how each of these steps in reflective DLL injection works. As an exercise, there are various resources on the web that you can refer to, to learn how this technique works.

 **Important APIs to Remember**

We can catch malware that uses these code injection techniques a lot of times using mere common sense. We cover these techniques more in Chapter 13. But another easy and important way to catch these techniques used by malware is by using the APIs they use. By using an API Logger like APIMiner, we can easily identify the APIs used by the malware and help identify such code injection techniques. It is important to remember all the various APIs that are used by malware for code injection. At the end of this chapter, we cover APIMiner and use it in conjunction with one of the exercises. As an exercise, we recommend running all the exercises in this chapter using APIMiner and inspect the API log files generated by the tool and use these API logs to identify all these various code injection techniques.

In the previous sections, we listed the various APIs that are used by various code injection techniques. The following list aggregates those APIs. Again, analysts need to remember them to identify malware and the various code injection techniques they use. Do note that this list is not comprehensive. Malware might use variants of the following APIs and might use new undocumented techniques that use other APIs. You should read more about the new techniques and APIs that malware uses and builds up your knowledge base to help us quickly identify malware.

```Windows APIs
CreateProcessA, CreateProcessW,CreateProcessInternalW,CreateProcessInternalA, Process32Next,Process32First, CreateToolhelp32Snapshot, OpenProcess,,VirtualAllocEx, LookupPrivilegeValue, AdjustTokenPrivileges, OpenProcessToken, VirtualProtect, WriteProcessMemory, NtUnmapViewOfSection, NtCreateSection, NtMapViewOfSection, QueueUserAPC, SuspendThread,ResumeThread, CreateRemoteThread, RtlCreateUserThread, NtCreateThreadEx, GetThreadContext, SetThreadContext
```

 **Why Do These Malicious APIs Exist?**

The reason why Microsoft provides these APIs is that they are meant for legitimate use by clean software, like debuggers, but unfortunately, these very same APIs are misused by malware. Debuggers use these APIs to manipulate the virtual memory of remote processes so that breakpoints are set, instructions in memory are altered so on and so forth.