---
title: Windows Internals
author:
  - Jon Marien
created: 2025-01-29
published: 2025-01-29
tags:
  - classes
  - INFO43921
---

| Title             | Author                       | Created          | Published        | Tags                   |
| ----------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Windows Internals | <ul><li>Jon Marien</li></ul> | January 29, 2025 | January 29, 2025 | [[#classes\|#classes]] |
# Chapter 9
## __Dynamic-Link Library (DLL)__ 
DLLs, or dynamic-link libraries, hold these functions, more commonly called APIs (application programming interface), that can be shared and used by other programs, as shown in Figure 4-35.

A DLL is available as a file on Windows with the .dll extension. A DLL file also uses the PE file format to describe its structure and content.

If you double-click a DLL file, it won’t launch a process. This is because a DLL file can’t be used independently and can only be used in combination with another EXE file.

![](M3-2-Windows%20Internals_0.png)

![](M3-2-Windows%20Internals_1.png)

One of the easiest ways to identify a file as a DLL is by using the file identification tools like TriD and the file command like tools. Another way is by using the Characteristics field in the PE file format.

The loader obtains the list of DLL dependencies for a PE file from the import directory (also called an import table).

![](M3-2-Windows%20Internals_2.png)

Run sample-4-1.exe and use tool process hacker.

   Dependency Chaining:Sample-4-1.exe depends on msvcrt.dll. But msvcrt.dll being just another PE file also depends on other DLLs. Those DLLs depend on other DLLs, all of which now form a chain, and all the DLLs in this chain are loaded by the Windows loader. 

![](M3-2-Windows%20Internals_3.png)

![](M3-2-Windows%20Internals_4.png)

Export: A DLL consists of APIs that can be used by other executable programs. 

![](M3-2-Windows%20Internals_5.png)

Import Address Table: An IAT is a table or an array in memory that holds the addresses of all the APIs that are used by a PE file. 

![](M3-2-Windows%20Internals_6.png)

Sample-4.3.exe import sample-4-2.dll

See export for sample4-2.dll in CFF

![](M3-2-Windows%20Internals_7.png)

See import in sample4-3.exe in CFF

![](M3-2-Windows%20Internals_8.png)

Run sample-4-3.exe and see process hacker

   the actual image base of Sample-4-2.dll in memory is 0x10000000, making the effective virtual address of HelperFunction2() as 0x10001090.

![](M3-2-Windows%20Internals_9.png)

![](M3-2-Windows%20Internals_10.png)

![](M3-2-Windows%20Internals_11.png)

 ## __Why is learning about IAT important?__ 

   IAT (Import Address Table) contains pointers to information that is critical for an executable to do its job: a list of DLLs it depends on for providing the expected functionality. It is commonly misused by malware to hijack API calls made by clean software. Malware does this by replacing the address of genuine APIs in the IAT table of a process with addresses of its code, basically redirecting all the API calls made by the process, to its own malicious code.

### Chapter 5 
Malware misuses and manipulates OS functionalities and features. 

The Windows operating system provides a vast set of APIs called Windows APIs, popularly known as the Win32 API. These APIs are available on both 32-bit and 64-bit Windows OS. Software developers extensively use these APIs to create Windows software that we all use. But they are also used by malware authors to create malicious software.

For os APIs, when it is used in combination with other APIs (i.e., if you see a certain sequence of API calls, it might indicate maliciousness).

You can look at the import table to look at the APIs used by the PE file. Also, you can disassemble the sample to view the APIs used by the sample. But statically looking at these APIs won’t give you an idea about the usage and context of the API call we described in the earlier section. This is where you need dynamic analysis to execute the sample and observe its behavior or debug and reverse engineer the sample to look at its full context.

Exists under the C:\Windows\System32 folder

#### __Important windows DLLs__
- NTDLL.DLL
- KERNEL32.DLL
- KERNELBASE.DLL
- GID32.DLL
- USER32.DLL
- COMCTL32.DLL
- ADVAPI32.DLL
- OLE32.DLL
- NETAPI32.DLL
- COMDLG32.DLL
- WS2_32.DLL
- WININET.DLL

#### __Visual studio DLLs__
- MSVCRT.DLL
- MSVCPxx.DLL
- MSVBVM60.DLL
- VCRUNTIMExx.DLL

![](M3-2-Windows%20Internals_12.png)

You can refer to the list of basic data types at https://docs.microsoft.com/en-us/Windows/win32/winprog/Windows-data-types.

Win32 provides two versions of an API if any of the parameters of the API accepts a string. These are the ASCII and the Unicode variants of the API, which come up with the letters A and W, respectively. The ASCII version of the API accepts an ASCII version of the string, and the Unicode version of the API accepts Unicode wide character strings.

e.g., `CreateFileA()`, `CreateFileW()`

## __Native (NT) Version of the APIs__ 
`CreateFileA() `and `CreateFileW()` are APIs that are provided by the DLL kernel32.dll. But there is another version of this API called `NTCreateFile()`in the DLL ntdll.dll. These APIs provided by ntdll.dll are called NT APIs and are considered low-level APIs. Low level because they are much closer to the kernel. The way it works is when you call `CreateFileA()` and `CreateFileW()`; they internally end up calling `NTCreateFile()` from ntdll.dll, which then calls the kernel using SYSCALLS(covered later in the chapter).

### __Extended Version of an API__ 
Some of the Win32 APIs have an extended version. The extended version of an API has an Ex suffix in its name. The difference between the non-extended and extended version of an API is that the extended version might accept more parameters/arguments, and it might also offer additional functionality. As an example, you can check MSDN for the API `VirtuaAlloc()` and its extended counterpart `VirtualAllocEx()` . Both of these allocate more virtual memory in a process, but `VirtuaAlloc()` can only allocate memory in the current process. In contrast, the extra functionality of `VirtuaAllocEx()` allows you to allocate memory in other processes as well, making it a malware favorite for code injection (covered in Chapter 10).

 __The Undocumented APIs__ 

There are many undocumented APIs in many undocumented DLLs on Windows. The most notorious being the NT APIs in ntdll.dll.

Whenever you get an API like this, the first good place to check for it is a search engine like Google, which should direct you to some blog post by a hacker/researcher if the API is an undocumented one.

The following are well-known Win32 APIs that perform operations on files.

- CreateFile
- WriteFile
- ReadFile
- SetFilePointer
- DeleteFile
- CloseFile

### __APIs for Windows registry__ 
The following are well-known Win32 APIs that perform operations on the Windows registry.

- RegCreateKey
- RegDeleteKey
- RegSetValue

### __APIs for process’s virtual memory__ 

The following are well-known Win32 APIs that perform operations on a process’s virtual memory.

- VirtualAlloc
- VirtualProtect
- NtCreateSection
- WriteProcessMemory
- NtMapViewOfSection

### __APIs for Processes and Threads__ 

The following are well-known Win32 APIs that perform operations related to processes and threads.

- CreateProcess
- ExitProcess
- CreateRemoteThread
- CreateThread
- GetThreadContext
- SetThreadContext
- TerminateProcess
- CreateProcessInternalW

The following are well-known Win32 APIs that perform operations related to DLLs.

- LoadLibrary
- GetProcAddress

### __APIs for services__ 
The following are well-known Win32 APIs that perform operations related to Windows services. They are also commonly used by malware to register a service (as discussed later in the chapter).

- OpenSCManager
- CreateService
- OpenService
- ChangeServiceConfig2W
- StartService

The following are well-known Win32 APIs that perform operations related to mutexes.

- CreateMutex
- OpenMutex

### __Behavior Identification with APIs__ 
Knowing the functionality of an API is not sufficient. You need to understand the context of the API, the parameters supplied to an API, and the set of APIs used in the sequence of APIs—all of which can lead to an easier, faster, and stronger conclusion if the sample is malware or not.

Let’s look at an example. Process hollowing is one of the most popular techniques used by malware. It creates a brand-new process in suspended mode. The API that creates a process is the `CreateProcess()` API. To create a process in suspended mode, the malware needs to pass an argument to it, `dwCreationFlags` having the value of `CREATE_SUSPENDED`, which tells the API to create the process and suspend it. Now a clean program rarely creates a process in suspended mode. Just because a program used `CreateProcess()` doesn’t indicate anything malicious. But the context/parameter (i.e., the `CREATE_SUSPENDED` argument in this API) indicates maliciousness and warrants further investigation.

Consider the API `WriteProcessMemory()`, which allows a process to write into the memory of another remote process. If this API is used stand-alone, it doesn’t indicate maliciousness because clean programs like debuggers also make use of this API to make modifications to the memory of another process. But if you see other APIs also used along with this API like `VirtualAllocEx() `and `CreateRemoteThread()`, you now have a sequence of APIs that are rarely used by clean programs. But this sequence of APIs is commonly used by malware for code injection, and thus indicates maliciousness.

### __Using Handle to Identify Sequences__ 
Every resource on Windows is represented as an object, which can include files, processes, the registry, memory, and so forth. If a process wants to perform certain operations on an instance of any of these objects, it needs to get a reference to this object, otherwise known as a Handle to the object. These handles are used as parameters to APIs, allowing the API to use the handle to know what object it is using or manipulating.

The usage of handles can help us identify APIs that are part of a sequence. API calls that are part of a sequence most often end up using/sharing common handles that point to the same instances of various Windows objects.

For example, take the case of the four APIs shown in Listing 5-3. As you can see, there are two calls to `CreateFile()`, which returns a handle to the file it creates. You can also see two more calls to `WriteFile()`, which takes as an argument the handle to the file it wants to write to, which was obtained from the calls to `CreateFile()` previously. As you can see, API calls (1) and (4) are part of a sequence, and API calls (2) and (3) are part of another sequence. We identified these two sequences by looking for the common handle shared by these API calls.

![](M3-2-Windows%20Internals_13.png)

## __Windows Registry__ 
Windows Registry is a tree-based hierarchical database available on Windows systems. It holds information and settings. Many of the OS components and services started on the system are based on config/settings held in the registry. Not just the OS, but most software uses the registry to hold various config/settings related information related to their software. 

Use regedit to view registery

![](M3-2-Windows%20Internals_14.png)

The data is stored in the hives under keys and subkeys using name-value pairs. 

![](M3-2-Windows%20Internals_15.png)

### __Malware and Registry Love Affair__ 

The registry holds rich information on the system, including various tools on the system, a perfect information source for malware. Malware also frequently use the registry to modify the registry by altering existing keys and name-values, and also by adding their own new data, with new keys and name-values.

### __Altering Registry Information__ 

Malware can modify the registry information to alter the system behavior in its favor, and they do it using Win32 APIs. The most common ones frequently seen in malware are altering the registry values meant to execute software during system boot or user login, called the run entry. Malware modifies these values so that the system automatically starts the malware at system boot. These techniques are called persistence mechanisms in Windows. Malware is known to alter the registry to disable administrative and security software.

### __Querying Information in Registry__ 

We already know that the registry stores information about various system-related information, including system hardware and software tools installed on the system. If your OS is installed on a virtual machine like your analysis VM, the traces of the virtual machine are in the registry.

For example, malware can query for these registry keys and find out if their victim OS is installed on a virtual machine. If so, the malware can assume that it is possibly being analyzed in a malware analysis VM, since VMs are more commonly used by power users like malware analysts and software developers. In this case, the malware might not exhibit it’s real behavior and can fool the analyst.

 ### __Important Directories on Windows__ 

Malware, when executing, is known to try a deceptive approach by copying themselves into various folders/directories on the system, naming themselves after OS system files so that they stay on the system without getting noticed. It is useful for an analyst to know some of the important directory names and what they should contain so that they can catch any such malware behavior. 

 - __system32__    or the path C:\Windows\system32, holds most of the system programs and tools in this directory, including Notepad.exe, which we use to open text files on Windows. smss.exe, svchost.exe, services.exe, explorer.exe, winlogon.exe, calc.exe are some of the system programs placed in this directory by Windows.

 - __Program files__    or path C:\Program Files or C:\Program Files (x86) contains software that is meant to be used by users. Whenever you install new software, it usually gets installed in this folder. Tools like Microsoft Office, browsers like Chrome and Firefox, and Adobe PDF Reader choose this directory by default during their installation process.

 - __User Document and Settings__   :We have a string of directories under this category that is used by applications to store user-specific data. Some of these folders, like AppData and Roaming, are used by malware to copy themselves into these folders and execute them from these folders. The following lists some of the folders where `user` is your user login account name.
	  - **My Documents**: `C:\Users\`\`user\``\Documents`
	  - **Desktop**: `C:\Users\`\`user\``\Desktop`
	  - **AppData**: `C:\Users\`\`user\``\AppData`
	  - **Roaming**: `C:\Users\`\`user\``\AppData\Roaming`

![](M3-2-Windows%20Internals_16.png)

## __What to Look for as a Malware Analyst__ 
Malware dropping their payloads and files into various system folders on the system to hide from users as well as analysts.

Malware is known to name itself after OS system programs to mislead analysts. But the original system Windows path where these programs are located is only C:Windowssystem32 and nowhere else. if you see a process that has one of the names that match any of the OS system programs or more, verify the path of the program to make sure it is located in the directory C:Windowssystem32. If it is any other directory, most likely, the process is malicious, masquerading itself as a system process.

Malware is also known to name itself similar to system programs but with minor variations in the spelling to trick users and analysts. For example, svohost.exe, which looks very similar to the system program/process svchost.exe.

### __Windows Processes__ 
Malware can run on a system by masquerading as a system process, or in other cases, modifying existing running system processes to carry out its malicious intentions by techniques like code injection and process hollowing.

The following lists some of the important system processes.

  - smss.exe
  - wininit.exe
  - winlogon.exe
  - explorer.exe
  - csrss.exe
  - userinit.exe
  - services.exe
  - lsm.exe
  - lsass.exe
  - svchost.exe

### __Attributes of a Process and Malware Anomalies__ 
Choose attribute to be shown in process hacker

![](M3-2-Windows%20Internals_17.png)

![](M3-2-Windows%20Internals_18.png)

**Process Image Path**: This is the path of the program from which the process is created. By default, the binaries of the system processes should be in C:\Windows\system32. Now we know that the system32 folder contains OS system processes. While analyzing malware, if you find a process that has the name of an OS system process, but with an image file path that is not in the C:\Windows\system32 folder, you should treat it as suspicious and investigate it further.

**Process ID (PID)** is a unique ID provided to a process . You cannot infer anything much from this because it is always random. But two of the system processes have fixed PIDs, with `SYSTEM IDLE PROCESS` having a value of 0, and `SYSTEM` having a value of 4. The system should have only one instance of these processes running on the system. So if you notice any process with the same name, but having a PID other than 0 and 4, treat the process as suspicious that requires further investigation.

**Sessions**: Windows is a multiuser operating system, and multiple users can log in at the same time. A session is created for each user who logs in the system, identified by Session ID
- Before Windows assigns a session for a newly logged-in user, while Windows starts, it creates a default session 0, which is a non-interactive session. Session 1 and greater are also created for the first user who logs in. Any more user logins are assigned session numbers in increasing numerical order. But no user can log in to session 0.
	- Most Windows system processes like svchost.exe run under session 0. The processes winlogon.exe, one of the two csrss.exe, explorer.exe, and taskhost.exe belong to the user session, while the rest of the system processes belong to session 0.
- As a malware analyst, if you see a process (supposed to be system process) like svchost.exe, smss.exe or services.exe or any other that is meant to be run under session 0, but it is now running under another session, it is highly suspicious and warrants further investigation.

- `SYSTEM IDLE PROCESS` is the first process in the system, whose direct child process is `SYSTEM`, and they have PIDs 0 and 4, respectively. The rest of the process involves its children. If you draw a tree of system processes in their launch order, it should look like Figure 5-14. Do note that some of these processes like svchost.exe can have multiple instances running.
	- As a malware analyst, while performing malware analysis, you might find some of the malware programs might name themselves with the same name as one of the OS system programs and run. But you also learned that we have a tree hierarchy that should be satisfied, where some of the system processes have very specific parent processes. If you see a process with the same name as a system process, but its parents don’t match the process/parent tree hierarchy specified in Figure 5-14, the process is highly indicative of being malware.

![](M3-2-Windows%20Internals_19.png)

### __Number of Instances in a System Process__ 

Most of the system processes have only one instance executing at any point in time. The only exception to this is csrss.exe, which has two instances running. Another is svchost.exe, which can have multiple instances running. So svchost.exe is a soft target for malware. A lot of malware names itself svchost.exe, with the idea that its process gets lost among clean instances and thereby escapes detection by the user/analyst.

As a malware analyst, other than svchost.exe, we can use the number of system processes to catch malware. If we find more than two instances of csrss.exe or more than one instance of any other system processes (except svchost.exe), then most likely the extra process instance(s) is a malware instance and warrants further investigation.

## __Windows services__ 
Services are special processes that run in the background and are managed by the OS, including having the ability to automatically start on boot, restarting it if it crashes, and so on.

You can see all the services registered on your system by using the Services tool

 __Services under svchost__ 
![](M3-2-Windows%20Internals_20.png)

All services registered are run by the services.exe process, which takes each registered service and launches it either directly, in the case of an executable file, or by using the svchost.exe process

### __DLL Services under Svchost__ 
Services can also be hosted as DLLs under svchost.exe. You can think of svchost.exe as an outer wrapper around the actual service’s DLL file that you register. If the registered service is a DLL, you will not see a separate child process under svchost.exe. Instead, the service DLL is run as a part of a new or one of the existing svchost.exe process instances, which loads the DLL into its memory and uses a thread to execute it.

To list the service DLLs that are run by a single instance of svchost.exe, you can double-click a svchost.exe instance in Process Hacker and go to the Services tab

how do services.exe and svchost.exe get the path to the DLLs that are registered as services that it should load and execute? All the DLL services that are registered are entered and categorized in the registry under the HKLMSOFTWAREMicrosoftWindowsNTCurrentVersionSvchost key categorized by Service Groups

![](M3-2-Windows%20Internals_21.png)

The full list of DLLs registered for this Service Group can be obtained from the HKEY_LOCAL_MACHINE\SYSTEM\Current\ControlSet\Services\\<service_name>\Parameters\ServiceDll key, 

![](M3-2-Windows%20Internals_22.png)

### __Malware as Windows Services__ 
Malware commonly registers itself as a service, either as an executable service or a DLL service. They do this because services provide an OS native method of managing the malware, making sure that it can start on system boot, restart if it crashes, and so on. Services provide a tried-and-tested persistence mechanism for malware. It is an added bonus if it is loaded by svchost.exe, which is a system process, thereby escaping the curious eyes of casual users and analysts.
The three most popular ways that malware registers services are by using the regsvr32.exe command, the sc.exe command, or programmatically by using Win32 APIs. The regsvr32.exe command and the sc.exe command need to register a service (see Listing 5-4).
The following are some of the registry keys in which service entries are made by the system.
  `HKLM\SYSTEM\Current\ControlSet\Services`
  `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\Services\Once`
  `HKLM\Software\Microsoft\Windows\CurrentVersion\Run\Services`

![](M3-2-Windows%20Internals_23.png)

When analyzing a malware sample, watch if the sample registers itself as a service using any commands like `regsvr32.exe` and `sc.exe`. If it does, trace the exe path or the DLL path to the file registered as a service. Usually, malware registers secondary payloads/binaries as a service, and these secondary components may need to be analyzed separately. The use of these commands by malware to register a service can be obtained by tools like ProcMon or by looking at the strings in memory, which we explore in a later chapter.

#### __Example: create service__ 

1. Download Sample-5-1.exe, 
2. Run powershell as adminiatrator, 
3. Use sc command to create service, 
4. Start the service in services, 
5. In Process hacker you can see it started notepad. 
6. But notepad will not be executed as windows dny services to interact with user

 __Example: create service__ 
![](M3-2-Windows%20Internals_24.png)

The kernel is the core functional unit of an OS. The operating system interacts directly with the hardware. The OS usually talks to the hardware via device drivers, which are usually loaded in kernel mode.

To allow user space programs to talk to these devices, the kernel has made syscalls available. Syscalls talk to the actual hardware resources via the drivers, but in a controlled manner, thereby protecting it.

![](M3-2-Windows%20Internals_25.png)

In the section Using Handle To Identify Sequences earlier in this chapter, we describe objects and handles. Everything in Windows is an object. One such important object is a Mutex.

A mutex is a synchronization object in which two or more processes or threads can synchronize their operations and execution. For example, a program wants to make sure that at any point in time only a single instance of its process is running. It achieves this by using a mutex. As the process starts, it programmatically checks if a mutex by a fixed name (e.g., MUTEX_TEST) exists. If it doesn’t, it creates the mutex. Now, if another instance of the same program comes up, the check for a mutex named MUTEX_TEST would fail since another (first) instance of it is already running, which has created the mutex, causing the second instance to exit.

A lot of malware don’t want multiple instances of itself to run.

When analyzing malware, we watch out for mutexes created by looking at the Handles tab in Process Hacker, where if a mutex is present, it lists it as a handle. Alternatively, under dynamic analysis, you can figure out if malware is using a mutex when it calls certain Win32 APIs.

Here's how to create a Windows service using both sc.exe and native PowerShell commands:
1. Using sc.exe:
```pwsh
# Basic service creation
sc.exe create "MyService" binPath= "C:\Path\To\Your\Service.exe"

# More detailed service creation with additional parameters
sc.exe create "MyService" binPath= "C:\Path\To\Your\Service.exe" start= auto DisplayName= "My Custom Service" obj= "LocalSystem"
```
2. Using native PowerShell commands (New-Service):
```pwsh
# Basic service creation
New-Service -Name "MyService" -BinaryPathName "C:\Path\To\Your\Service.exe"

# More detailed service creation
New-Service -Name "MyService" `
           -BinaryPathName "C:\Path\To\Your\Service.exe" `
           -DisplayName "My Custom Service" `
           -StartupType Automatic `
           -Description "Description of my service"
```

Key points to remember:
- For sc.exe, note the required space after the equals sign (e.g., `binPath= ` (with space after \`=\`) not `binPath=`)
- Common startup types:
	- For sc.exe: 
		- boot, system, auto, demand, disabled
	- For PowerShell: 
		- Boot, System, Automatic, Manual, Disabled

Additional Commands:
```pwsh
# Verify service creation
Get-Service -Name "MyService"

# Delete service
# Using sc.exe:
sc.exe delete "MyService"

# Using PowerShell:
Remove-Service -Name "MyService"  # PowerShell 6.0 and later

# For older PowerShell versions, you can use:
(Get-WmiObject -Class Win32_Service -Filter "Name='MyService'").Delete()
```

sc.exe create "INCLASSTESTSERVICE" binPath= "C:\Users\nucle\Documents\Obsidian\Vaults\Cyber Security - ISS\Semester 7\Malicious Code\Class Notes\Week 4\Sample-5-1.exe" start= auto DisplayName= "Malicious Code InClass Test Service" obj= "LocalSystem"

**Start Service if not started:**
![](Windows%20Internals-January-29th-2025-12-41-59.webp)

**Find notepad.exe, click properties, find parent process:**
![](Windows%20Internals-January-29th-2025-12-41-37.webp)
**Supposed to be running from system32, but it is running from Sample-5-1.exe, so it worked properly**:
![](Windows%20Internals-January-29th-2025-12-41-38.webp)