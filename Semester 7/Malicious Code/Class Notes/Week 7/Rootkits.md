---
title: Rootkits
author:
  - Jon Marien
created: 2025-02-19
published: 2025-02-19
tags:
  - classes
  - INFO43921
---

| Title    | Author                       | Created           | Published         | Tags                                               |
| -------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| Rootkits | <ul><li>Jon Marien</li></ul> | February 19, 2025 | February 19, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# Rootkits
Rootkits are advanced stealth techniques used by malware, often   **mistaken as a type of malware**, which it isn’t. A rootkit is a feature or functionality or technology used by malware to hide and protect its actual payloads, executables, binaries, files, and any other artifacts created by the malware on the victim’s machine.

A rootkit is created both in user mode and kernel mode. But what are the differences between these two? While user-mode rootkits mostly depend on creating API hooks in user mode processes by injecting code into these processes,   **kernel rootkits require a kernel module/driver to be installed into the kernel**.

User-mode rootkits are specific to a process into which the rootkit code is injected into, while   **kernel-mode rootkits are global.**   For example, if a user-mode rootkit is injected into the Task Manager to hide the malware processes that work great since you won’t find the malware processes if you are looking at the Task Manager. But you can still view the malware processes via other tools like Process Hacker and Process Explorer since the rootkit has not been injected into them. The application of the user-mode rootkit extends only to the process it has been injected into. For it to be truly effective, the user-mode rootkit code has to be injected into every user-mode process that is connected to the stealth you are trying to achieve.

On the other hand, kernel-mode rootkits work using kernel-mode drivers installed by the rootkit. They affect all the tools and processes running on the system since the kernel is a layer used by all the processes on the system. But rootkit-  ing   into the kernel may not be that easy. It is a tedious job to create any kind of kernel code as   **it needs accurate programming code since it might otherwise crash the system.**

## **Request Flow from User to Kernel**

![](M6-2-Rootkits%20in%20Kernel%20Space_0.png)

In the previous chapter, we have seen that a user-mode application calls the code in the kernel to perform low-level operations, and this happens using a system call, or syscall, as illustrated in Figure 11-17. We briefly explained this in Chapter 10.

An API call made from a user application is passed on to the kernel through kernel32.dll and NTDLL.dll. The APIs in NTDLL.dll use syscalls to pass on these API requests to the kernel. On the kernel side, there are corresponding functions that handle the request coming in from these user mode syscalls.

Which services (different from services in the user space) in the kernel handle these  syscalls  ?

The kernel holds a table called the SSDT (system service descriptor table) that holds a list of pointers to these kernel services (functions) that handle incoming  syscalls   from the user space.

So, when a  syscall   comes in, the corresponding kernel service (function) is picked up from the SSDT and invoked to handle the  syscall  .

The invoked kernel service (function) can now carry out the required activity to process the request, which might also involve calling another device driver using IRP packets (I/O Request Packet). For example, a file operation request from the user space gets finally passed to a file system driver, while a network operation request is passed on to the network driver.

## **Injecting Code into Kernel Space**

In kernel mode, there is no concept of a process, so the entire kernel code is one big virtual address space that is shared by the kernel, including the kernel modules and drivers. But how do we inject our code into the kernel? For this, we create what is called a kernel module, using the driver development kit (DDK) or the Windows driver kit (WDK) from Microsoft, which are nothing but frameworks and helper modules and utilities that can help you create kernel modules.

Most kernel modules have a .sys file extension, and it is either an executable file format type or even a DLL. As an example, have a look at the folder C:WindowsSystem32drivers and you note a lot of files with the .sys extension which are all drivers which are all kernel modules. If you open any of the .sys files using the CFF Explorer tool and check Optional Header ➤ Subsystem; it holds a value of   **Native**   as seen in Figure 11-18.

![](M6-2-Rootkits%20in%20Kernel%20Space_1.png)

## **Viewing Loaded Kernel Modules and Drivers**

DriverView   (which we installed in Chapter 2) is a useful tool for viewing all the loaded kernel modules on Windows. Figure 11-19 shows the output of  DriverView   on my system. You can run it as well to view the kernel modules loaded in your system.

The tool displays a lot of columns by default, but we have shrunk the display only to five fields. You can identify the kernel driver by looking into the address of the module. By default, the address of a kernel module should lie above the memory address 0x7FFFFFFF for a 32-bit version of Windows.

 **ntkrnlpa.exe**  (often named as ntoskrnl.exe) is the kernel image and is one of the most important kernel modules responsible for various system functions like hardware abstraction and memory management. It holds the SSDT table that we spoke about earlier, and we cover it in more detail later. It starts at 0x82A13000 and ends at 0x82E25000. Do note that the address might vary on your system. You can also obtain the path of the kernel module file on disk via its properties, which shows it as C:\Windows\system32\ntkrnlpa.exe.

NoteA - kernel executable can have different names: NTOSKRNL.EXE, NTKRNLPA.EXE, NTKRNLMP.EXE, NTKRPAMP.EXE.

![](M6-2-Rootkits%20in%20Kernel%20Space_2.png)

![](M6-2-Rootkits%20in%20Kernel%20Space_3.png)

## Win-10, 64-bit
### **SSDT and How to View It**
An incoming syscall from the user space is handled by kernel functions located in the SSDT (system service descriptor table). These kernel functions that handle these syscalls are called services (not to be confused with the Windows services in the user space you read about in Chapter 5). Let’s call them service functions to avoid any confusion.

Many service functions are defined and held in the kernel, and each of them is defined according to function; they provide to serve various kinds of user-space requests. For example, some of them are for creating and deleting files, creating, modifying, and deleting registry entries, allocating memory, and so forth.

Note: Do not confuse the kernel services with user space Windows services, which are nothing but managed processes in the background. These kernel services are just kernel functions, very similar to how you have APIs in DLLs in user space, where the kernel is like one large DLL, and the kernel services are the APIs it provides.

The SSDT is nothing but a table that contains pointers to these service functions. Each service function pointer has a corresponding index in the SSDT. The pointers in the SSDT point to the memory locations in the kernel code where the service functions reside. The service functions are defined in ntoskrnel.exe(ntkrnlpa.exe) and win32k.ksys kernel modules.

The NovirusThanks SSDT View tool that we installed in Chapter 2 views the contents of the SSDT, as seen in Figure 11-20.

As you can see, the leftmost column displays the index of the service function in the table; the second column displays its name; the third displays the address; and the fourth column shows where the module resides. Look at the entry for the NtDeleteFile service function with index 102. This function is located at 0x2BA66AD in the ntkrnlpa kernel module. You can verify the address range of the ntkrnlpa kernel module using the Driver View tool from Figure 11-20.

![](M6-2-Rootkits%20in%20Kernel%20Space_4.png)

The syscall from the user space uses the index value to transmit the request to the kernel mode and thereby invoke the correct service function in the SSDT, as illustrated in Figure 11-21.

Do note that many of these service functions in the SSDT have a corresponding API in the user space Win32 DLL NTDLL.dll with the same name. A NtDeleteFile in user-space Win32 DLL NTDLL.DLL has a NtDeleteFile in the kernel as a service function whose function pointer is in the SSDT.

![](M6-2-Rootkits%20in%20Kernel%20Space_5.png)

## **Drivers and IRP**
A driver is a kernel module that is separated into three broad categories: function drivers, bus drivers, and filter drivers. The drivers that directly talk to the device they are managing are called function drivers . Filter drivers don’t directly interface with the physical device but sit slightly higher in the device driver path, and their main task is to filter the requests coming into the drivers below it and to the actual device. Bus drivers drive the individual physical buses that the devices are plugged into. These three driver categories have subcategories.

To communicate with the device drivers and the device, the kernel provides a subsystem called the I/O manager, which generates and dispatches what are called I/O request packets (IRP). An IRP is a data structure that has information on the I/O operation needed from the device driver/device, with some of the common request operations being write requests, read requests, control requests, and so forth. When starting up, device drivers can register themselves to handle these I/O request types thereby giving them the ability to service these I/O operation requests.

A device on the system may have multiple drivers associated with them. When the I/O manager creates an IRP and sends it to the device, it flows through all the drivers associated with the device in a sequential manager. This is illustrated in Figure 11-22. A device driver if it has registered to handle the IRP type processes it. A driver can also filter any IRPs headed to the device and even filter/alter them out so that they are no longer passed to the subsequent drivers. An example of such a category of drivers that filter IRP packets are filter drivers.

![](M6-2-Rootkits%20in%20Kernel%20Space_6.png)

## **How to Insert Kernel Modules and Driver?**
* Kernel modules and drivers are loaded into the kernel as a service (Windows services). We have gone through the various ways to create a Windows service in Chapter 5. As a malware analyst, keep in mind all the various techniques to identify the registration of services. It comes in handy when you are analyzing a sample that registers a rootkit kernel module into the kernel via a service.
* To summarize the steps to programmatically register a service using Win32 APIs.
  * 1.The kernel module is dropped by malware into the disk using the CreateFile API.
  * 2.OpenSCManager opens the service manager to register a new service.
  * 3.CreateServiceA registers a new service by supplying the kernel module file that it dropped into the disk in step 1.
  * 4.StartService starts the service created in step 1, which loads the kernel module.
* You most likely see this sequence of APIs in malware that is trying to install a kernel module rootkit . You see this hands-on when we play with some exercises later.

As an analyst, you’ve got to make sure you can differentiate between the sample trying to register and create a regular Windows service and another case where it is trying to create a service that intends to load a kernel module or rootkit. To differentiate between the two, you can use the Subsystem value of the executable file that is registered as a service in the CreateService API from step 3.

A few other APIs can also load a kernel module, which can be used by malware. Two of them are ZWSetSystemInformation and ZwLoadDriver. With the help of the APIMiner tool that logs various APIs used by these rootkit malware samples, we can identify kernel-based malware and rootkits if we see any of them using these APIs.

## **SSDT Rootkits and SSDT Table Hooking**
* SSDT rootkits work by hooking the SSDT, very similar to how user-space rootkits use API hooking, as we saw earlier. To hook the SSDT, you need to locate the address of the SSDT in the kernel. To do so, you need to create a driver that can first locate the SSDT, and that can then traverse the service entries in SSDT and then hook it.
* To locate the SSDT, Windows has a structure called _KeServiceDescriptorTable, which has a pointer that points to the SSDT. Listing 11-2 shows the definition of the structure.
* The structure contains the following fields.
  * ServiceTableBase points to the start of the SSDT.
  * ServiceCounterTableBase tells how many times each service is invoked.
  * NumberOfServices tells the number of services.
  * ParamTableBase is the base address of SSPT (system service parameter table). SSPT is another table that holds the number of bytes needed for the parameters of a service.

![](M6-2-Rootkits%20in%20Kernel%20Space_7.png)

A malware kernel module rootkit once inserted into the kernel first locates 
*`KeServiceDescriptorTable`, from which it can find the base address of the SSDT using the `ServiceTableBase` field. With the SSDT location known, the malware can either replace these service function pointers in the SSDT that it intends to hook/intercept, using a technique similar to IAT hooking (refer to IAT hooking in Chapter 10). The other option is to use inline hooking by going to the actual kernel service function that the malware wants to hook by obtaining the address of the said service function from the SSDT. Then replace the initial bytes of the service function code to redirect to the malicious malware code in its kernel module rootkit (the same as inline hooking in user space also explained in Chapter 10). Both techniques are explained in Figure 11-23.*

![](M6-2-Rootkits%20in%20Kernel%20Space_8.png)

Creating SSDT hooks on 32-bit machines was easy because the kernel exported 
*`KeServiceDescriptorTable`, but Windows stopped it with 64 bits. Hence with 64-bit Windows, SSDT hooking was harder but not impossible.*

Malware can use SSDT hooks to implement rootkits, and it can be used by them to protect and hide their files, processes, registries, and so forth. The advantage of using kernel-based SSDT rootkits is that it applies globally to all processes on the system, unlike user-mode rootkits, where the rootkit must be inserted into every process that you want to rootkit.

## **SSDT Rootkit Exercise**
As an exercise, let’s look at Sample-11-7-ssdt-rootkit. Add the .exe file extension suffix to it. The sample needs to be run as an admin for the kernel module to be inserted into the kernel. To do that right-click the sample and click Run as Administrator. The sample creates a C:hidden folder. Try to access this folder, and it throws an error, as seen in Figure 11-24.

![](M6-2-Rootkits%20in%20Kernel%20Space_9.png)

As analysts, how can we identify and detect an SSDT rootkit? We go back to the APIs that we spoke about earlier that are used by malware to insert kernel modules. These are the service creation APIs. Let’s open a command prompt as an administrator and run the same sample using the APIMiner tool, as seen in Figure 11-25.

Inspecting the API logs from APIMiner point to the same API sequence we spoke about earlier: OpenSCManager, CreateService, and StartService, as seen in Figure 11-26.

![](M6-2-Rootkits%20in%20Kernel%20Space_10.png)

![](M6-2-Rootkits%20in%20Kernel%20Space_11.png)

This only tells you half the picture that the sample is trying to register a service. But it is a Windows service. What proves that we have a rootkit kernel module being inserted by this sample? If you further check the CreateService arguments in your APIMiner API log file, it provides the path of the kernel module C:hiddenrootkit.sys. If you try to access this folder, you are denied permission, as you saw in Figure 11-25, which is a telltale sign that we have a file rootkit.

We can further confirm this by running the GMER tool, which clearly shows us that we have an SSDT rootkit in place, as seen in Figure 11-27.

![](M6-2-Rootkits%20in%20Kernel%20Space_12.png)

Since GMER identifies it as an SSDT rootkit, let’s now run the SSDT View tool, which double confirms if any of the service functions in the SSDT are hooked, and if hooked which ones. As you can see in Figure 11-28, SSDT View shows us that the NtCreateFile service function has been hooked, which in combination with our failure to access C:hiddenrootkit.sys indicates that we have a File Hiding rootkit installed by our sample. We can also infer that it is file hiding rootkit from the name/type of SSDT service function that has been hooked, which in this case is NtCreateFile/ZwCreateFile.

![](M6-2-Rootkits%20in%20Kernel%20Space_13.png)

* As an analyst, it is important to know the various service functions that are targeted by malware to hook to implement rootkits. These are service functions that are hooked in SSDT by implementing rootkits.
  * ZwOpenFile
  * NtCreateFile
  * ZwQueryDirectoryFile
  * ZwTerminateProcess
  * ZwOpenProcess
  * ZwQuerySystemInformation
  * ZwQueryValueKey
  * ZwEnumerateValueKey
  * ZwEnumerateKey
  * ZwSetValueKey
  * ZwCreateKey

## **DKOM Rootkits and Kernel Object Manipulation**
Another way to implement rootkits is by manipulating the list that is returned by the enumeration APIs like the ones that enumerate files, registry, and processes. Some of these lists are created by referring to some of the data structures that are available in the kernel called kernel objects. These rootkits are called direct kernel object manipulation (DKOM).

Before looking into the kernel-mode DKOM rootkits, let’s look at how the object manipulation happens at a very high level.

Figure 11-29 represents a list of processes in the kernel as an object, which is referred throughout the system to display the list of processes. The Process_Mal process object in the middle of the list is a malware process that the malware wants to hide in the Task Manager and any other process viewing tool. To do so and implement the process hiding rootkit, the malware kernel module unlinks that malware process from the list, as seen in Figure 11-30, thereby making all the process viewing tools on the system blind to the presence of this malicious process.

![](M6-2-Rootkits%20in%20Kernel%20Space_14.png)

## **Process Hiding Using DKOM In-Depth**

![](M6-2-Rootkits%20in%20Kernel%20Space_15.png)

We talked about how kernel object manipulation works at a high level to hide processes running on the system. Let’s explore the particulars of how DKOM can hide a process.

In the kernel, each process is represented by an object called EPROCESS. The EPROCESS data structure has multiple fields, including Pcb, which points to the process environment block. A partial view of the various fields of this data structure is seen in Figure 11-31.

The structure and its fields and offsets can be explored using kernel debuggers for Windows like `Windbg`. The EPROCESS objects for all the processes running on the system are connected using a structure called `ActiveProcessLinks`(AP_LINK in Figure 11-32), which further has FLINK and BLINK subfields that contain pointers that point to other EPROCESSes. A FLINK field in an EPROCESS points to the FLINK of the next process, while the BLINK field points to the FLINK in a previous EPROCESS. This results in a doubly-linked list of EPROCESS structures. This is illustrated in Figure 11-32.

Figure 11-32 shows how `EPROCESS` of `PROCESS_1` and `PROCESS_MAL` and `PROCESS_3` are connected into a doubly-linked list. A user-mode API like `NtQuerySystemInformation`, which can retrieve a list of processes in the Task Manager or any other tools, refers to this doubly linked list. The entire list is traversed programmatically using `FLINK` and `BLINK` pointers. A `FLINK` or `BLINK` can reach from one `EPROCESS` to another, and the rest of the fields can be accessed as an offset from these structures from the pointers. A malware rootkit can tamper this doubly linked list to hide its processes.

![](M6-2-Rootkits%20in%20Kernel%20Space_16.png)

To hide a malicious process, the `FLINK` and `BLINK` pointers are disconnected, and then the `EPROCESS` before and after the malicious process is connected by manipulating their pointers. Figure 11-33 explains how this delinking happens.

![](M6-2-Rootkits%20in%20Kernel%20Space_17.png)

## **DKOM Rootkit Exercise**
Let’s run Sample-11-8-dkom-rootkit. Make sure that you add the extension .exe. Let’s run it directly using the APIMiner tool so that you also learn how to identify and detect malware samples that use process hiding rootkits. To do this, open the command prompt as an administrator and run Sample-11-8-dkom-rootkit.exe using APIMiner, as shown in Figure 11-34.

![](M6-2-Rootkits%20in%20Kernel%20Space_18.png)

This sample creates a new process with PID 3964 and then inserts a kernel module that manipulates DKOM to hide this process from the Task Manager. Let’s see how we can analyze this sample.

Running it as a part of APIMIner, there are two API log files generated by our tool, as seen in Figure 11-35.

![](M6-2-Rootkits%20in%20Kernel%20Space_19.png)

APIMiner generates API log files with filenames containing the PIDs of the processes it creates API logs for, which in this case is PID 3964. But if you check Process Hacker as seen in Figure 11-36, you won’t see a process by this PID. This is the first sign that the process is hidden by a rootkit.

![](M6-2-Rootkits%20in%20Kernel%20Space_20.png)

Further inspecting the logs shows us the same sequence of APIs that register a service, as seen in Figure 11-37. But if you further inspect the arguments for CreateService API from the log file, you obtain the path of the file that is being registered as a service, which for us is C:hiddendkom.sys. Inspecting this file using CFF Explorer, you notice that it has the Native Subsystem in Optional Header, indicating that it is a kernel module. This proves that this service creation is to insert a kernel module by the sample.

![](M6-2-Rootkits%20in%20Kernel%20Space_21.png)

To further double confirm that the kernel module inserted is a rootkit, you can run GMER. Either way, if you see a service created by the sample, it probably also makes sense to quickly check with a tool like GMER and Ring3 API Hook Scanner to see if it detects any kind of hooks both in user-space and kernel. Running GMER shows us that we have a process hiding rootkit installed and the PID of the process it is trying to hide, as seen in Figure 11-38.

![](M6-2-Rootkits%20in%20Kernel%20Space_22.png)

## **Rootkits Using IRP Filtering or Filter Driver**
![](M6-2-Rootkits%20in%20Kernel%20Space_23.png)

IRP packets flow from the I/O manager across device drivers so that drivers can carry out operations on the device based on the action requested by the IRP packet. Filter drivers are a category of drivers that are created to filter IRP packets. Filter drivers can also contain logic to carry out other bookkeeping related operations based on the IRP action requested.

Filter drivers give one the flexibility to implement various kinds of middleware. A good example is encryption software. Take the example of a file system driver that processes IRP and ultimately talks to the disk device to carry out various operations like creating, deleting, modifying files, and so forth. This is illustrated in Figure 11-39.

![](M6-2-Rootkits%20in%20Kernel%20Space_24.png)

But we want to implement file encryption functionality, and we can achieve this using a filter driver. A file encryption software may need to encrypt the file contents before it is written to the hard disk, and at the same time, it needs to decrypt the file contents after reading back from the hard disk and returning it to the applications asking for contents of the file. To implement this whole functionality, it can place another driver or be more appropriate a filter driver before the main file system driver, where this new driver is responsible for decrypting and encrypting the contents of the file, as illustrated in Figure 11-40.

![](M6-2-Rootkits%20in%20Kernel%20Space_25.png)

The IRP packet coming from the OS now passes through this file encryption filter driver before reaching the final file system driver , which is responsible for writing to the disk. The file encryption driver is stacked on the top of the actual driver.

This functionality, while good, can also be misused, and malware can use IRP filtering by utilizing filter drivers to implement rootkits. For example, the regular flow of IRP across drivers, as seen in Figure 11-41.

![](M6-2-Rootkits%20in%20Kernel%20Space_26.png)

To implement rootkit functionality, a malware registers a filter driver (kernel module), which sits before the other drivers in the stack, as shown in Figure 11-42.

the malicious filter driver from the malware sees the IRP before the function driver and the other drivers and can carry out various rootkit related functionality by filtering out the IRP packets and carrying out various actions based on the IRP packet contents and actions.

Going back to the file encryption driver, malware can place a malicious driver instead of a file encryption driver, which can hide malicious files and directories and prevent the deletion of its malicious files. Even keystrokes can be logged, and ports can be hidden by inserting malicious drivers to the device drivers stack.

## **Other Ways of Creating Rootkits**
We have covered the most prevalent rootkit techniques used by malware out there. There might be other techniques that can implement rootkits. For example, malware can use its own file system and replace the one used by the OS to hide their artifacts on disk. Whatever the rootkit technique used, the methods to detect and identify malware that uses rootkits are the same as the ones we used in this chapter. Most of the techniques involve seeing mismatches and anomalies and proving these anomalies are malicious.

