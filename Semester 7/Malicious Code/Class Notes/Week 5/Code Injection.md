---
title: Code Injection
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
  - INFO43921
---

| Title          | Author                       | Created           | Published         | Tags                   |
| -------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Code Injection | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |

# Chapter 10

Malware can also force/inject/insert itself into and modify existing running processes, including OS processes and the underlying kernel. Most of these techniques used by the malware for these actions are not the ones discovered or invented by malware attackers, but instead are techniques used by many of the legitimate software, especially anti-malware products.

## **What Is Code Injection?**

Code injection is **a technique*- where **a process can insert a part of or all of its code*- from its own running process **into another target process**, and **get the target process to execute the injected code**.

![](M5-1-Code%20Injection_0.png)

## **Code Injection Motives**
- Code injection is performed in both user mode and kernel mode. Malware mainly uses code injection for the following reasons:
	- Hiding their presence, also known as stealth.
	- Process piggybacking.
	- Altering functionality of another process or entire OS.

A malware process wants to avoid easy identification. If someone were to check the list of processes running on the system using a Task Manager, and an odd-looking process would be found. Similarly, the malware might also want to hide from anti-malware products, like firewalls.

![](M5-1-Code%20Injection_1.png)

## **Process Piggybacking**
If a malware wants to connect to the Internet, a firewall on the system might block this from happening, if it tries to connect from its own created process. The reason could be the firewall on the system might allow only a few well-known processes on the system to connect to the Internet.

Malware can inject its code and run from other legitimate native processes like `explorer`, `svchost`, `winlogon`, and so forth, all of which have permission to connect to the Internet. So by piggybacking on the permission and privileges of these other legitimate processes, the malware was able to bypass restrictions put by the OS policies on its own process.

![](M5-1-Code%20Injection_2.png)

## **Altering Functionality**
Another motive of code injection is to alter the functionality of certain processes or maybe even the entire OS/system. This is largely used by malware for code hooking, rootkits, and API interceptions in attacks such as man-in-the-browser.

Let’s take an example of malware that drops/creates certain files on the system disk, which has the name `MalwareFile.exe` and it doesn’t want either the user or any anti-malware products to delete it. To delete files on the system, the OS provides the `DeleteFile()` Win32 API, which is called by the antivirus or users to delete a file on disk.

Now to prevent deletion of its file `MalwareFile.exe`, all the malware must do is alter the functionality of the `DeleteFile()` API, and it does by code injection and API hooking. The malware alters `DeleteFile()` API, thereby hijacking it and then transfer control to its fake version of the API called `FakeDeleteFile()`. `FakeDeleteFile()` checks if the user is trying to delete `MalwareFile.exe`, and if so, it does not delete it. But if the user is trying to delete any other file other than `MalwareFile.exe`, `FakeDeleteFile()` doesn’t interfere with the behavior, allowing the system/user to delete the file. This technique is called code hooking. 

The process is illustrated in Figure 10-4.

![](M5-1-Code%20Injection_3.png)

## **Code Injection Target**
Malware can inject its code into existing processes running on the system, as well as into the kernel. Alternatively, it can create/spawn a new process off itself in a suspended state and inject code into it.

For user space, we already know that each process has its own private virtual memory space split into user mode and kernel mode address space, as you learned in Chapter 4. The user-mode space of the virtual memory is tampered by another process, even though it is private to the process. If malware injects code into the user-mode part of any other process, only that process is affected by the malware.

Modifying the kernel impacts all processes on the system. But again, injecting into the kernel by adding a kernel module or altering an existing kernel module is not a child’s play. A programmer needs to be extremely careful while playing around with any kernel code, as a small mistake can dramatically impact the system and may lead to a system crash. On the other hand, the kernel is highly protected and not that easy to modify, making it not the most sought-after destination for malware.

## **Popular Code Injection Techniques**
- Process hollowing
- Thread injection
- DLL injection
- Classical DLL injection
- Reflective DLL injection
- Shellcode injection

- Code cave
- QueueUserAPC
- Atom bombing

### **Steps for Code Injection**
- Code injection is largely handled in the following steps.
1. Locate the target for code injection.
2. Inject the code.
	  a. Allocate/create memory/space in the target process of virtual memory.
	  b. Write/inject code into the allocated memory/space in the target
3. Execute the injected code in the target.

### **Steps for Process User-Mode Code Injection**
User-mode code injection involves all the steps discussed, with the only difference being the target is a process. The target process is often referred to as the remote process or target process. The process that does the injection is often called the injector process .

In the following steps, we use pseudo API names called MemAlloc(), WriteRemoteMemory(), and ExecuteInjectedCode() to simplify your understanding.

1. An injector process selects the target process into which it wants to inject its code, as described by Figure 10-5. You can also see that the current instruction pointer in the target process is pointing to and executing the target process’s code.

![](M5-1-Code%20Injection_4.png)

Now that the target process has been figured out, the injector process allocates memory in the target process, and it does so by calling an API `MemAlloc()`, as seen in Figure 10-6.

![](M5-1-Code%20Injection_5.png)

2. Now that memory has been allocated in the target process, the injector process copies its code into the allocated space using the `WriteRemoteMemory()` API , as seen in Figure 10-7.

![](M5-1-Code%20Injection_6.png)

1. After copying the code into the target process, the injector process needs to make sure that the target process runs its injected code and that the instruction pointer point to its code. It does so by calling the `ExecuteInjectedCode()` API. As you can see in Figure 10-8, the instruction pointer now points to and executes the injected code.

![](M5-1-Code%20Injection_7.png)

### **Step 1: Locating the Target Process**
Malware may want to inject its code into system processes like Explorer or `svchost` or browsers like Chrome and Firefox. To inject code into a process, it first needs to open the process using an `OpenProcess()` Win32 API, which takes the PID of the process as a parameter. But how does the malware know the PID of its target process?

For this, malware uses a set of APIs available on Windows to search for the target process by name and, once found, retrieve its PID. The APIs in question are `CreateTool32HelpSnapshot()`, `Process32First()` and `Process32Next()`.

Malware first wants to get a list of all processes running on the system, which it gets using the help of the `CreateTool32HelpSnapshot()` API. This API returns a linked list of processes, where each node represents details of the process, represented by a structure called `PROCESSENTRY32`.

The `PROCESSENTRY32` structure contains various details of the process, including the name and the PID of the process. The returned linked list of processes is then iterated using the help of the `Process32First()` and `Process32Next()` APIs. For each node in the list, if the name of the process matches the name of the process that the malware intends to inject into, the malware uses the PID of that process for its subsequent operations and APIs, including in the call to `OpenProcess()`.

Now you can run Sample-10-1 from the samples repo, which utilizes the code in Listing 10-1 and prints the process name and PID of every process running on the system.

![](M5-1-Code%20Injection_8.png)

![](M5-1-Code%20Injection_9.png)

- Instead of the malware picking a target process from a set of existing processes running on a system, malware is also known to spawn/create a new process out of a native clean program on the system but in a suspended state. After creating this suspended process, it then injects its code into this suspended process and then resume the process but from its injected code. In this case, you see two new sets of additional APIs: `CreateProcess()` or its variations in step 1, and `ResumeThread()` or its variations in step 4.

- The following is a list of the important APIs in step 1 of code injection. As analysts, we need to remember these APIs. It is handy to know them during dynamic analysis, where a detection tool like `APIMiner` can help you visualize the APIs used by a malware process. Knowing that a malware process uses a certain set of APIs, like the ones listed next, helps us investigate whether the malware process is carrying code injection or not.
	 - `CreateToolhelp32Snapshot`
	 - `Process32First`
	 - `Process32Next`
	 - `CreateProcessA`
	 - `CreateProcessW`
	 - `CreateProcessInternalW`
	 - `CreateProcessInternalA`

## **Step 2: Allocating Memory in a Remote Target Process**
Now that we have the PID, we can open a handle to the remote process. Most operations and API calls to the remote process are against the process handle. Do note that the injector process needs to obtain debug privileges to manipulate the virtual memory of the target process, and hence a handle to the process has to be opened in debug mode (`PROCESS_ALL_ACCCESS` covers all privilege types). It does this by calling the `OpenProcess()` API, as seen in Listing 10-2.

![](M5-1-Code%20Injection_10.png)

Every process is treated like an object on Windows. A process object has certain attributes, which include privilege level. A security token is associated with a process that decides which resources a process can access. Certain APIs cannot be successfully called by the process if it does not have the required privileges. 

The injector process can obtain these privileges by adjusting the security tokens. This is done by the injector process by using a sequence of API calls, which include `OpenProcessToken()`, `LookupPrivilegeValue()`, and `AdjustTokenPrivileges()`. Using these APIs, the injector process can adjust its privilege. For more information on the API, you can look it up on MSDN.

After obtaining the handle to the target process, the injector process now allocates memory in the target process by calling the API `VirtualAllocEx()`, as seen in Listing 10-3.

![](M5-1-Code%20Injection_11.png)

`VirtualAllocEx()` allocates memory of the requested `size(size_to_allocate)` in the remote target process identified by the process `HANDLE`. Another thing that you may have noticed is the permission of the memory above `PAGE_EXECUTE_READWRITE`. You learned about page permissions in Chapter 4. When you are specifying `VirtualAllocEx()` API, you can specify the permissions to assign to the allocated memory or rather to the pages in allocated memory. In this particular case, it is all read, write, and execute permissions because the injector process wants to first write code into the memory; hence, it has write permissions. After that, since it wants to execute the written/injected code, it has execute permissions.

To see the APIs in action, we can now run Sample-10-2, which we illustrated in Figure 10-10. Make sure you add the `.exe` extension suffix to the sample. The sample is an interactive sample that you need to run from the command prompt. The sample requests you to start `Notepad.exe` so that it can allocate memory in it. Once you start `Notepad.exe`, you can obtain the PID using Process Hacker, and enter it when the sample requests you to. You can also enter the size and the permissions of the memory you want to allocate in the remote process. The sample then allocates memory using `VirtualAllocEx()`, which you can verify in the remote process (`Notepad.exe`) using Process Hacker.

![](M5-1-Code%20Injection_12.png)

We now verify if the memory is allocated by checking the memory of the Notepad.exe process using Process Hacker, as seen in Figure 10-11. You see a new memory size of `4096` bytes allocated at address `0x1e0000` as described by the sample program output in Figure 10-10. Do note that the output of running the sample might vary on your machine since the address of the memory allocated might be different.

![](M5-1-Code%20Injection_13.png)

- An alternate method to `VirtualAllocEx()` and `WriteProcessMemory()` that is used in steps 2 and 3. In this method, the malware uses sections and views, where it maps a part of its memory to the target process, basically creating a reflection of a part of its memory in the target process. To do so, it uses another set of APIs.
- An alternative to setting `EXECUTE` permissions while allocating memory, the malware can first allocate memory but using just `READ_WRITE` permissions and later after step 3, but before we enter step 4, manually change the permissions of the allocated memory to `EXECUTE` as well using the API `VirtualProtect()`. So while analyzing malware samples, you have to watch out not just for `VirtualAllocEx()` API but also `VirtualProtect()`. If you see a combination of these two APIs operating against a remote process, there’s something fishy going on, and it deserves more investigation from the point of view of code injection and malware infection.
- The following is a list of the important APIs from step 2 in code injection.
  - `OpenProcess`
  - `VirtualAllocEx`
  - `LookupPrivilegeValue`
  - `AdjustTokenPrivileges`
  - `OpenProcessToken`
  - `VirtualProtect`

## **Step 3: Writing into Remote Target Memory**
After space is allocated, the code that needs to be executed in the target process is copied into the target process using WriteProcessMemory() API , as seen in Listing 10-4.

![](M5-1-Code%20Injection_14.png)

To see the APIs in action, we can now run Sample-10-3, which we have illustrated in Figure 10-12. Don’t forget to add the .exe file suffix extension to the sample. The sample is an interactive sample that you need to run from the command prompt, very similar to Sample-10-2 in the previous section, with the extra addition being it writes into the allocated memory the string `MALWARE ANALYSIS AND DETECTION ENGINEERING`. The sample uses the `WriteProcessMemory()` API to write the string into the allocated memory.

![](M5-1-Code%20Injection_15.png)

We now verify if the memory is allocated and the string written to it by checking the contents of the memory location `0x350000` of the `Notepad.exe` process using Process Hacker, as seen in Figure 10-13. Do note that the address location allocated on your system might vary from the one we have specified here. Please pick the allocated address as indicated by the output of this sample process on your system.

![](M5-1-Code%20Injection_16.png)
1. run process hacker
2. run sample-10-3.exe in cmd
3. open notepad and get pid in process hacker and input in cmd

![](M5-1-Code%20Injection_17.png)

The method mentioned in step 2 and step 3, which uses `VirtualAllocEx()` and `WriteProcessMemory()` to allocate memory and code into the target process, is quite common in most malware.

There exists another method of allocating memory and copying code from the injector process into the target process, which involves section objects and views. Before we head into step 4, let’s investigate this alternate technique.

## **Section Object and Section Views**
Section objects and views is a provision by Windows in which a portion of virtual memory belonging to a process is shared/mapped with/into other processes.

There are two processes: the injector process and the target process. The injector process wants to map some of its code and data into the target process. To do this, the injector process first starts by creating a Section object by calling the `NtCreateSection()` API, as seen in Figure 10-14. Creating a section object doesn’t mean any memory is allocated in its virtual memory. Or at least not yet. While creating a Section object, it can also specify its size in bytes.

![](M5-1-Code%20Injection_18.png)

Now that the injector process has created a section, it creates a view of this section, which allocates memory for this section in the virtual memory. The injector process using the `NTMapViewOfSection() `API creates two views of the same section it earlier created: one locally in its own process and another in the target process, as seen in Figure 10-15.

![](M5-1-Code%20Injection_19.png)

![](M5-1-Code%20Injection_20.png)

The multiple views created act as a mirror image. If the injector process modifies the contents in its own view, it automatically is reflected in the view of the target process, as illustrated in Figure 10-16.

Malware is known to use this feature to inject code into a target process, instead of always relying on APIs like `VirtualAllocEx()` and `WriteProcessMemory()`, where malware using sections and views writes its malicious injected code in its own view, and it automatically is copied/reflected in the view of the target process. While any code injection technique can use this method, it is more commonly used in a technique called process hollowing (also called `RunPE`), which we cover in detail in a later section.

The following is a list of the important APIs from step 3 in code injection. As analysts, we need to remember these APIs come in handy during dynamic analysis.
- `WriteProcessMemory`
- `NtUnmapViewOfSection`
- `NtCreateSection`
- `NtMapViewOfSection`

## **Step 4: Executing Code in Remote Process**
Now that the injector process has injected its code into the target process, it now needs to get the target process to run this injected code. Several techniques have been developed to execute the injected code in the target process. The following are the most popular.
  -  **Remote thread creation APIs.*-  
	  - Using APIs like `CreateRemoteThread()` and other similar APIs, the injector process can create threads in the target process.
  - **Asynchronous procedure call (APC) queues**
  - **Altering thread context.*-  
	  - The instruction pointer of an existing current thread in the remote/target process is made to point to the injected code, using the `GetThreadContext()` and `SetThreadContext()` APIs.

## **Remote Thread Creation API**
In this technique, the malware spawn/create a brand-new thread in the target process but pointing this thread it to run from its injected code. This is illustrated in Figure 10-17.

Some of the APIs that are used by malware to create a remote thread are `CreateRemoteThread()`, `RtlCreateUserThread()`, and `NtCreateThreadEx()`.

![](M5-1-Code%20Injection_21.png)

Sample-10-4 is very similar to the earlier samples takes the PID of the target process in which it creates the remote thread. The sample request you to open Notepad.exe to use it as the target process for the exercise. Once you open Notepad.exe, go down to Process Hacker and make a note of no of threads currently used by the Notepad.exe process, as seen in the top right of Figure 10-18. After fully running the sample, you can then recheck the no of threads in Notepad.exe to observe a newly created thread that was created by the injector process Sample-10-4.exe, as seen in the bottom of Figure 10-19.

![](M5-1-Code%20Injection_22.png)

## **Asynchronous Procedure Call (APC) Queues**
Creating a new thread is sometimes an overhead as new resources need to be allocated to start the thread. Creating a new thread in a remote thread can easily be detected by anti-malware products that are listening to the event log and logs such an event as suspicious.

So instead of creating a remote thread to execute the injected code, we can request one of the existing running threads in the remote target process to run the injected code. This is done using an asynchronous procedure call (APC) queue. Let’s now look at how it works.

APC is a method for already executing threads within an application to take a break from their current tasks and perform another queued task or function asynchronously, and then return and continue from where it left off. But a thread can’t just randomly run these tasks/functions that are queued to it. It can only run these tasks when it enters an alertable state.

A thread enters an alertable state when it calls one of these APIs: `SleepEx()`, `WaitForSingleObjectEx()`, `WaitForMultipleObjectsEx()`, `SignalObjectAndWait()`, and `MsgWaitForMultipleObjects()`. When a thread enters an alertable state by calling any of these APIs, it checks its APC queue for any queued task or functions; and if any, it executes them and then returns to where it left off.

To queue a task into the APC queue of the target process, the injector process calls the `QueueUserAPC()` API.

Malware misuses this Windows feature by injecting a malicious code that contains a function in a remote/target process’ memory, then queue that injected function as APC into the remote process’ APC queue.

![](M5-1-Code%20Injection_23.png)

## **Altering the Thread Context**
Every thread in a process has an EIP or instruction pointer, which holds the address of the code/instruction the thread is currently executing. The EIP of a thread is held in the thread’s context. Once the code is injected into the remote target process, an injector process can reset the EIP of a thread on the target process to point to the injected code, thereby forcing the target process to run its injected code.

The following steps carry this out.
1. The remote thread whose context must be modified should be suspended first. If the thread is not suspended already, it is suspended by calling the `SuspendThread()` API.  
2. The current context of the remote thread is obtained using the `GetThreadContext()` API, which returns the context structure, which holds the context of the thread, including the current EIP of the thread.
3. The EIP field in the context structure is modified to point to the address of the injected code that should be executed.
4. With the modified context, the injector process then calls `SetThreadContext()` to reset the instruction pointer of the remote thread to the value set in the EIP field of the context.
5. Call `ResumeThread()` to resume the suspended thread, which now executes from the injected code.

Listing 10-5 shows the structure of the `CONTEXT` struct that holds the context of a thread. It has a field named EIP that points to the address of the current code/instruction that the thread is executing.

![](M5-1-Code%20Injection_24.png)

The following is a list of the important APIs from step 4 in code injection.
- `QueueUserAPC`
- `SuspendThread`
- `ResumeThread`
- `CreateRemoteThread`
- `RtlCreateUserThread`
- `NtCreateThreadEx`
- `GetThreadContext`
- `SetThreadContext`

## **Classical DLL Injection**
Malware is usually delivered as multiple components, where there is a main component like a downloader/loader whose main job is to download secondary components or payloads either from the C2 server or its own resource section and load/run them. These secondary components are an executable PE file, DLL files, and so forth. If it is an executable PE file, the loader can easily run it. With DLLs, it is not that straightforward. Although there are tools like rundll32.exe that can simulate loading and running a DLL, most often with malware, these secondary payload DLLs are rather injected, loaded, and run from another clean target process.

When a process loads a DLL, a DLL module is loaded in memory at any image base address. Now let’s take the example of two processes—`Process1` and `Process2`, both of which load the same DLL file. If `Process1` loads a DLL and it gets loaded at image base address `0x30000`, `Process2`, when it loads the same DLL from disk, it might get loaded at a different image base address `0x40000`. The DLLs need not have the same image base address in two or more different processes, as illustrated in Figure 10-21.

![](M5-1-Code%20Injection_25.png)

But there’s an exception to this rule. There are some system DLLs provided by Windows, which are loaded in all processes at the same image base address. Kernel32.dll is one such DLL. For example, if kernel32.dll is loaded at the 0x30000 address image base in one process, then we can expect that it is loaded at the same image base in every other process’ virtual memory on the system, as illustrated in Figure 10-22.

![](M5-1-Code%20Injection_26.png)

The important point about `kernel32.dll` having the same image base forms the foundation of Classical DLL Injection. With that in mind, the injection of a DLL into a target process is best described by the following steps,
1. DLL lies on the hard disk as a file that needs to be loaded into the target process’s memory.
2. The injector process first allocates memory in the target process, with the size of memory allocation, which is equal to the length of the path of the DLL file. For example, if the path of the DLL file on the disk is C:\Malware.dll, the size it allocates is 15 characters (including the trailing NULL character in the string).
3. It copies the path of the DLL file (i.e., C:\Malware.dll) to the memory allocated in the target process from step 2. Figure 10-23 illustrates steps 1, 2, and 3.

![](M5-1-Code%20Injection_27.png)

The `LoadLibrary()` API is implemented inside `Kernel32.dll`, which loads a DLL from disk into a process’s memory. The injector process needs to somehow force the target process to invoke `LoadLibrary()` while passing to it the path of the DLL so that the DLL is loaded into its address space.

1. The injector process exploits the fact that `KERNEL32.DLL` has the same image base address in both the injector process and target process, which in turn means the address of `LoadLibrary()` API is the same in both the processes. So the injector process just has to obtain the address of `LoadLibrary()` API from its own address space.
2. The injector process obtains the address of `LoadLibrary()` API from its own address space using the code in Listing 10-6.

![](M5-1-Code%20Injection_28.png)

1. Now that the Injector has the address of `LoadLibrary()`, it can use either `CreateRemoteThread()` or `QueueUserAPC()` to force the target process to run `LoadLibrary()`. An additional argument is also supplied to `CreateRemoteThread()` or `QueueUserAPC()` , which in turn pass this argument to `LoadLibrary()` API when they invoke it. The additional argument that is passed is the memory location/buffer in the target process containing the DLL path from step 2. Figure 10-24 illustrates steps 4–7.

![](M5-1-Code%20Injection_29.png)

Let’s now see DLL Injection in action. Copy Sample-10-5b and Sample-10-5 to the C drive. Add the .dll extension suffix to Sample-10-5b so that it is now named Sample-10-5b.dll. Add the .exe extension to Sample-10-5, making it Sample-10-5.exe. Now, Sample-10-5.exe is the injector program, and Sample-10-5b.dll is the DLL to be injected. Sample-10-5.exe is an interactive program, which takes a dummy process’ PID into which it injects the DLL. For the dummy process, we use Notepad. It also asks the user for the full path of the DLL to inject, which in our case is C:\Sample-10-5b.dll. The sample output from Sample-10-5.exe is seen in Figure 10-25.

Once Sample-10-5.exe finishes execution, you see that Sample-10-5b.dll has been loaded into Notepad.exe’s memory as a module/DLL, as seen in Process Hacker Modules tab of the Notepad.exe process, shown in Figure 10-26.

![](M5-1-Code%20Injection_30.png)

Injector is 32 bit so notepad also should be 32 bit. I installed notepad++ 32 bit.

![](M5-1-Code%20Injection_31.png)

![](M5-1-Code%20Injection_32.png)