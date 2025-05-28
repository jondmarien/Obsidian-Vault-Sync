---
title: Armoring and Evasion
author:
  - Jon Marien
created: 2025-03-19
published: 2025-03-19
tags:
  - classes
  - INFO43921
---

| Title                | Author                       | Created        | Published      | Tags                                               |
| -------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Armoring and Evasion | <ul><li>Jon Marien</li></ul> | March 19, 2025 | March 19, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# Armoring
## __Armoring > Anti-Static Analysis__

Anti-analysis armoring techniques are meant to hinder the process of malware analysis.

Static analysis involves superficially looking at the contents of a file on the disk without running it.

If we compile a C code, the binary created is different from the actual source code. It creates a level of obfuscation that hides the actual intention of the source code. Using certain programming languages like VB and .NET, it can create higher degrees of  __unreadability in the compiled executable__ .

To add to this  __encryption and compression__ , you can further hide the actual contents of a file on disk.

## __Armoring > Anti-Dynamic Analysis__

* Static analysis fails if the samples use encryption or packing. So, malware can be identified using dynamic analysis by executing it.
* But if the malware has some techniques to detect that it is getting analyzed, it tries to avoid showing it’s real behavior during execution
* The following are the steps we used for setting up the dynamic analysis environment and then using the environment to carry out an analysis.
  * 1.	Install a guest OS on a virtualization software (a.k.a. hypervisors like VMWare, VirtualBox, or Qemu).
  * 2.	Install our dynamic analysis tools like ProcMon, Process Hacker, Wireshark, and so forth, on the guest OS.
  * 3.	Analyze malware samples under execution, and execute the tools to observe the artifacts dropped by malware.

## __Anti-Dynamic Analysis__

* From the following, can you think how malware can detect that it is getting analyzed?
  * Malware can use extremely simple techniques like identifying the number of CPUs, the size of RAM, and so forth to find out if they are executed in an analysis environment.
  * Malware can try to locate the artifacts created by the software used during the analysis process. For example, the virtualization software, the dynamic analysis tools, all leave certain artifacts in the guest analysis VM machine.

### __1-Identifying Analysis Environment__
- Malware can use these attributes to find out if it is an analysis machine. As an example, if the malware discovers there is CPU or RAM size below 4 GB or hard disk size is below 100 GB, then it can easily assume that it is executing in an analysis environment.
- A system used by a regular person can have many more attributes. Here are some of the attributes that malware can use to figure out it is being analyzed.
	- Number of processes.
	- Types of software.
	- Duration after login.
	- Data in clipboard.
	- Execution history of tools.
	- Presence of files.

### __2-Analysis Tool Identification__
The analysis tools we install in our analysis VM create files on the system, including other artifacts like registry keys. When we run these analysis tools, they also pop up as processes. Malware is known to check for the presence/installation of various such analysis tools and the presence of their processes to figure out if they are in an analysis environment.

For example, certain analysis tools are installed at specific known locations, while others may be standalone executable and can be placed in any location. Malware can try to look out for the ones that are installed in specific locations on the system. To do this, the malware browses through the files on the system using the `FindFirstFile` and `FindNextFile` APIs to locate the blacklisted files. Table 19-1 shows two such folder names searched by malware for the presence of some of these analysis tools on the system.

![](M11-2-Armoring%20and%20Evasion-2024_0.png)

- Installation of certain tools can also result in the creation of certain registry entries on the guest OS by these tools. Malware can also look out for such registry entries to identify the presence of tools. The registry entries are queried using the `RegQueryValueExA` API. The following lists some of the registry keys the malware might look for to search for the presence of analysis tools.
	- `SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Sandboxie`
	- `SOFTWARE\SUPERAntiSpyware​.​com`
	- `SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\wireshark.exe`

Malware certainly must look out for the process related to the analyzing tools.

Malware iterates through the list of processes using the `CreateToolhelp32Snapshot`, `Process32First`, `Process32Next` APIs and then compare the process names on the system to its own list of blacklisted analysis tools process names using a string comparison API like `StrStrIA`.

The following is a list of some of the  __analysis tool processes:__

- SUPERAntiSpyware.exe
- SandboxieRpcSs.exe
- DrvLoader.exe
- ERUNT.exe
- SbieCtrl.exe
- SymRecv.exe
- irise.exe
- tcpdump.exe
- windbg.exe
- WinDump.exe
- Regshot.exe
- PEBrowseDbg.exe
- ProcessHacker.exe
- procexp.exe
- IrisSvc.exe
- apis32.exe
- wireshark.exe
- dumpcap.exe
- wspass.exe
- ZxSniffer.exe
- Aircrack-ng
- ollydbg.exe
- observer.exe

As an exercise, open the malware Sample-19-2 using IDA and go to the address at 0x401056, as seen in Figure 19-1.

![](M11-2-Armoring%20and%20Evasion-2024_1.png)

As seen in the screenshot, the sample uses an armoring technique where it lists the processes running on the system using the set of APIs we previously mentioned and then checks if any of the process names obtained matches wireshark.exe, the analysis tool.

To bypass the armoring techniques, analysts happen to intentionally change the name of their analysis tool executables, so that when they do start up as a process or even on disk, they don’t have their real tool name, basically fooling the malware. To double-bypass this anti-anti-analysis trick by malware analysts, malware instead try to find out the true name of a process by using the window class of the process and not by its file or process name. When a program with a user interface is created, it has a window class. Using the FindWindow API , malware can find out if any process on the system has a particular window class.

As an exercise, go to the 0x401022 address in Sample-19-2 using IDA or OllyDbg. As you can see in Figure 19-2, the sample calls the Findwindow API to see if any process has the OllyDbg window class, which checks if OllyDbg is running on the system.

![](M11-2-Armoring%20and%20Evasion-2024_2.png)

On detecting the presence of such analysis tools, their registry keys, their processes, the malware does not execute fully, and in most cases, exhibits benign activity or exits itself yearly. Since the actual behavior is not exhibited, you cannot conclude if it is malware in such cases.

This is where __string analysis__ can help us __identify if such an anti-analysis technique exists__  in the malware. Usually, the list of files, registries, and processes that the malware looks out for are present in the malware process’ memory or even in its static strings if the sample is not packed. So you can opt to inspect the virtual memory in case your dynamic analysis using API logs from APIMiner does not give you a conclusive result.

To further strengthen your verdict that these strings indicate an armoring technique, and to exactly know the usage of these strings by the malware sample, you can use references (XREFs) to these strings in the debugger or disassembler to locate the code that uses these strings.

### __3-Virtual Machine Identification__
The guest OS in a virtual machine can have certain processes, files, registries, and so forth that indicate the use of a specific type of virtualization software. Because of the presence of these artifacts created by this hypervisor software inside our analysis VMs, virtual machines can be identified by malware in the same way as the analysis tools were in the previous section. The following is a list of files, processes, registry keys, and services created by various hypervisor platforms in their Windows Guest operating systems. Some of the files are present in `C:\windows\system32\drivers` for VMWare Windows Guest operating systems.

Table 19-3 lists some of the files present in `C:\windows\system32` for VirtualBox Windows Guest operating systems.

![](M11-2-Armoring%20and%20Evasion-2024_3.png)

![](M11-2-Armoring%20and%20Evasion-2024_4.png)

Like the processes that are created, there are services that run inside the guest OS for a hypervisor platform. Table 19-5 are the names of some of these services that are created in the operating systems running on various hypervisor platforms.

![](M11-2-Armoring%20and%20Evasion-2024_5.png)

Table 19-6 lists some of the registry keys that are created inside the guest operating systems for various virtualization hypervisor platforms used.

![](M11-2-Armoring%20and%20Evasion-2024_6.png)

### __4-Detecting Simulated Hardware__
Virtualization is all about emulating the actual hardware components with the help of software programs. You can say the CPU, hard disk, network cards, RAM, and even the instruction sets supported everything is simulated by the underlying virtualization software, especially when it is being run in emulation mode. Malware can try to detect these emulation environments. Let’s see how various such emulated components can be identified by malware.

#### __5-Detecting Simulated Hardware__:  __Detecting Processor Type__
The CPU on the system can be identified by using CPUID instruction.

If CPUID instruction is executed with EAX=1, the instruction returns various data for the CPU on the system in the EAX, EBX, ECX, and EDX registers. But what we are interested in is the thirty-first bit of the value returned in the ECX register, which is set to 1 if the underlying platform is a hypervisor (i.e., we are running from inside a VM, and 0 if it is a physical CPU). Listing 19-1 shows sample code that can be used to identify that the underlying CPU is that of a hypervisor platform and not of a physical CPU.

![](M11-2-Armoring%20and%20Evasion-2024_7.png)

Similar to the example, if the CPUID instruction is executed with EAX set to *0X40000000*, it gets the hypervisor vendor signature to EBX, ECX, and EDX registers. Listing 19-2 shows an example assembly code that can be used to get the hypervisor vendor name/signature using the CPUID instruction.

![](M11-2-Armoring%20and%20Evasion-2024_8.png)

After execution of these instructions inside our analysis VM running on top of VMWare hypervisor platform, the registers should be set to the following values.

Do you see what these register values mean? If you reverse them and decode the bytes into the printable ASCII character equivalent, the registers hold the string VMwa waer reVM, which indicates that the hypervisor platform is VMWare.

![](M11-2-Armoring%20and%20Evasion-2024_9.png)

### __6-Detecting Network Device__
VMWare and VirtualBox provide network interface cards (NIC) to the guest operating systems, which are emulated.

These emulated NICs made available to the guest operating systems running on that hypervisor platform need a mac address to uniquely identify that network card which is made up of six bytes in a format like xx:xx:xx:xx:xx:xx.

The MAC addresses on VMWare for their guest operating systems start with fixed byte sequences like 00:0C:29, 00:1C:14, 00:05:69 and 00:50:56. The first three bytes of MAC addresses used by VirtualBox for its guest operating systems start with 08:00:27.

Malware is known to obtain the mac address of the NICs on the system and check if they match any of the known NIC MAC address sequences used by the hypervisor platforms, to detect if they are inside an analysis VM environment.

## __Communication Port__
The IN instruction is a Ring 0 instruction, which executes in a kernel mode only if it is a real CPU. If the instruction is executed from a user-mode application, it raises an exception if it is a real CPU. But if the instruction is executed from a user-mode application inside VMWare guest OS, it returns the magic value of VMWare in the EBX register.

![](M11-2-Armoring%20and%20Evasion-2024_10.png)

## __Armoring > Anti-Debugging__
* Anti-debugging tricks can fall into two categories.
  * The malware detects the debuggers and then executes the code that does not carry out malicious activity.
  * The malware uses certain code to confuse the debugger regardless of whether they detect the presence of the debugger or not.

## __Anti-Debugging Using Debugger Detection__
Let’s have a look at techniques by which malware can find out if they are getting debugged. When a sample is debugged, the debugger can alter some data structures and code in the process that it is debugging. A process environment block (PEB) is one such data structure. Let’s have a look at how malware can use the PEB to find out if it is getting debugged.

### __1- PEB-Based Debugging Detection__
- When a process is getting debugged, some of the data structures that correspond to the process are altered. One of the most important data structures is the PEB. The data structure contains various information about its process. The following lists the important fields in PEB that can identify if the process is being debugged.
	- `BeingDebugged` located at 0x2 bytes from the start of PEB.
	- `NtGlobalFlags` located at 0x68 bytes from the start of PEB.
	- `ProcessHeap` located at 0x18 bytes from the start of PEB.
- Now the PEB structure of a running process can be accessed using the FS segment register. The following instruction in List 19-5 can be used to read the address of PEB into the EAX register.

![](M11-2-Armoring%20and%20Evasion-2024_11.png)

With the PEB in our hands, we/malware can access its various members/fields that can tell if it is being debugged. As you learned earlier, the `BeingDebugged` field in the PEB is located 2 bytes from its starting point. If the value of this field is set to 1, it indicates that the executable is being debugged. Listing 19-7 shows sample assembly code to detect if the process is being debugged using the `BeingDebugged` field in the PEB.

![](M11-2-Armoring%20and%20Evasion-2024_12.png)

Another field in the PEB in which a debugger leaves its footprint is the `NtGlobalFlags` field. This field is located at the offset` 0x68` from the start of PEB. The flags in `NtGlobalFlags` define how heaps are allocated in the program. Under debugger allocation happens in a manner that is different when compared to a debugger not being present. The following flags in the field are set to 1 in the presence of debuggers `FLG_HEAP_ENABLE_TAIL_CHECK`, `FLG_HEAP_ENABLE_FREE_CHECK`, and `FLG_HEAP_VALIDATE_PARAMETERS`. The following code in Listing 19-8 can check if the flag values are set to 1 in `NtGlobalFlags`.

![](M11-2-Armoring%20and%20Evasion-2024_13.png)

PEB has another field `ProcessHeap` that can be used to identify if the process is getting debugged. The `ProcessHeap` field also has another two subfields `Flags` and `ForceFlags`, which also determine if the process is being debugged. The `Flags` field is located at offset 0xC inside `ProcessHeap`, while `ForceFlags` is at `0x10`, both of which are set if the process is being debugged.

![](M11-2-Armoring%20and%20Evasion-2024_14.png)

### __2- EPROCESS-Based Debugging Detection__
`EPROCESS` is a data structure in the kernel that represents a process on the system. The `DebugPort` field in the `EPROCESS` structure can be used to identify if a process is getting debugged. If this field is set to a nonzero value, then it indicates that the process is being debugged. The `DebugPort` field in the `EPROCESS` structure can be accessed by using the `NtQueryInformationProcess` API. 

If the API is called with the second parameter `ProcessInformationClass`, set to `0x7`, which indicates `ProcessDebugPort`, a nonzero value, is returned in the third parameter if the process is being debugged. A value of zero `(0)` is returned if it is not being debugged. Listing 19-10 shows an example C code that shows this API to detect if it is being debugged

![](M11-2-Armoring%20and%20Evasion-2024_15.png)

### __3-Using Windows API to Detect Debugger__
Windows provides APIs which can directly access the PEB and let you know if the process is being debugged. IsDebuggerPresent is one such API that is commonly used by most malware to detect if they are being. The IsDebuggerPresent API works by returning a value of 1 if it detects that the process is being debugged. The pseudocode in Listing 19-11 demonstrates how the API is used by malware

![](M11-2-Armoring%20and%20Evasion-2024_16.png)

Listing 19-12 shows a sample C program that we have compiled into Sample-19-1 in our samples repo. This program checks if it is being debugged and takes either of the branches accordingly.

![](M11-2-Armoring%20and%20Evasion-2024_17.png)

If you run Sample-19-1 standalone using the command prompt, you see that it correctly identifies that the sample is not being debugged and prints the else part of the code, as seen in Figure 19-3.

![](M11-2-Armoring%20and%20Evasion-2024_18.png)

But now open the same sample using OllyDbg and run it, and you see that the sample takes the if branch indicating that it is indeed being debugged as seen in Figure 19-4.

![](M11-2-Armoring%20and%20Evasion-2024_19.png)

- Listed are a few more APIs that can be used to identify if a process is getting debugged.
	- `CheckRemoteDebuggerPresent`
	- `OutputDebugString`
	- `FindWindow`

### __4-Detect Debugging by Identifying Breakpoints__
While analyzing an application, we set different kinds of breakpoints, software, hardware, and memory breakpoints. The debugger sets a software breakpoint at an instruction by replacing the instruction that we are setting a breakpoint with an `INT 3` instruction. The opcode for the instruction is either `CC` or `CD 03`. Malware can search through the entire code block to find these `CC` or `CD 03` bytes to identify the presence of software breakpoints (although it has to use filter conditions to make sure it doesn’t detect some other uses of these very same bytes that are not inserted by the debugger but rather by the compiler in the case of padding).

x86 uses `DR0-DR7` registers to set hardware breakpoints. `GetThreadContext` API can be used to retrieve the state of a thread in a `CONTEXT` data structure. The `CONTEXT` structure contains information related to the state of the thread, which includes the debug registers `DR0-DR7`. Malware that wants to find out if it is being debugged can obtain the `CONTEXT` structure using the API and check the state of the debug registers. If the value of these registers is nonzero, then it is assumed that the hardware breakpoint is set. The listing displays pseudocode to detect hardware breakpoints.

![](M11-2-Armoring%20and%20Evasion-2024_20.png)

### __5-Detect Debugging by Identifying Code Stepping__
When we manually debug a disassembled code, there is a certain lag between execution of two instructions. This lag is even worse if we are single-stepping through the instructions. Malware can identify they are getting debugged by comparing this __time lag between its instruction execution__.

The RTDSC (read timestamp counter) is one most common instructions used by malware to detect code stepping. You can say RTDSC instruction tells the time since the system has booted. The result of the instruction is stored in the EAX register. Listing 19-14 shows how RTDSC instruction can be used to detect if the process is being debugged

![](M11-2-Armoring%20and%20Evasion-2024_21.png)

- Other methods to detect single-stepping through the code:
	- Retrieve the time using APIs like `GetTickCount()`, `QueryPerformanceCounter()`, using which the instruction lag can also be calculated.
	- By using the trap flag in the `EFLAGS` register. To detect if it is being debugged, malware can insert its own exception handler and then set the `TF` bit in the `EFLAGS` register.
		- On further executing the code, if the malware’s exception handler is invoked (an exception should be invoked because the TF bit is set), it indicates that the malware sample is not being debugged. 
	- But if its exception handler is not invoked, it indicates some else (i.e., the debugger) handled the exception that was raised, thereby informing the malware that it is being debugged.

## __Other Anti-Debugging Tricks__
There is a long list of various other anti-debugging tricks used by malware. An example of another trick is when we open a program in a debugger, the  __debugger becomes the parent of the process__ . Malware can check if it has a parent process, and if there is one, it can analyze the parent process to verify if it is a debugger.

Another trick that malware use to detect if they are being debugged is to call interrupts like INT 2D and INT 3, which are meant to be used by debuggers. The Interrupts work differently if they are executed in a process attached to a debugger, as opposed to how it would otherwise work when the process is not debugged.

There may be many other such anti-debugging tricks that may be specific to a debugger.

## __Armoring > Anti-Disassembly Using Garbage Code__
Malware programs can be programmed to have various kinds of garbage assembly code in between valid instructions. The presence of such garbage code makes the disassembled code more unreadable, and hence reverse engineering becomes harder.

These garbage codes inserted are such that their execution of blocks does not alter the functionality of the malware. Listing 19-15, shows an example of a set of instructions which can act as garbage code. The execution of the instructions doesn’t have any real effect on the functionality of the program.

![](M11-2-Armoring%20and%20Evasion-2024_22.png)

## __Fooling Malware Armoring__
The armoring techniques are implemented using both raw assembly instructions and APIs. As an example, CPUID and IN instructions were used to identify the presence of VM. `IsDebuggerPresent` is used to detect if the sample is being debugged. You can try to identify these anti-techniques used by malware by __ locating these special sets of instructions and API in the code__ .

Another easier way is to identify these mechanisms is by  __locating the strings using string analysis__ . For example, you can usually see strings related to virtual machine detection and analysis tools detection in the memory of malware samples.

While implementing sandboxes, make sure you set up your analysis VM to  __mimic an end-users system as much as possible__ . Make use of demonstration tools like `Pafish` to test how effective you have been in hiding your analysis environment.

From a reversing perspective, after identifying the code, instructions, and APIs that implement the armoring in a malware sample process, we can then patch the instructions and register values of the sample process we are debugging. With the process patched, we can alter the code flow to avoid any armoring checks, so that we can reach the actual code of malware and see it’s behavior.