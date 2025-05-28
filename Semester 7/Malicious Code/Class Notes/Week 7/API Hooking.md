---
title: API Hooking
author:
  - Jon Marien
created: 2025-02-19
published: 2025-02-19
tags:
  - classes
  - INFO43921
---

| Title       | Author                       | Created           | Published         | Tags                                               |
| ----------- | ---------------------------- | ----------------- | ----------------- | -------------------------------------------------- |
| API Hooking | <ul><li>Jon Marien</li></ul> | February 19, 2025 | February 19, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |

# Code/API Hooking

## Motives
One of the motives behind code injection is API hooking.

API hooking is a way to intercept a call made to a legitimate API by a program, just like a middle-man. The intention is varied depending on the needs of the malware.

For example, malware might want to prevent the deletion of its file, and to do so, it might intercept calls to API that deletes files. It might want to intercept calls that pass credentials to the API. It might want to intercept calls that hide its presence in the list of processes in the Task Manager. The list goes on.

Code/API hooking is split into four major steps.

1.	The malware that is the injector process first identifies the target  **process**  whose APIs it wants to intercept/hook.
2.	Now that the target process has been identified, the malware/injector process first injects its code into the target process using code injection. This is where code injection techniques come in.
3.	The injected code is run within the target process.
4.	The injected code, which is now run inside the target process, locates various APIs within the target process and places hooks into them. After placing the hooks, all the calls made to those hooked APIs by the target process are redirected to the malware’s injected code.

### **Identify Hooking Point/Target**

![](M6-1-API%20Hooking_0.png)

You learned about identifying the hooking point or location to place the hook for Interception, basically step 4 from the previous section. Let’s take the example of a Win32 API call made by your program—  DeleteFile  (), as illustrated in Figure 10-33.

When our process makes a call to a Win32 API (  DeleteFile  () in our case), it takes multiple hops via its own IAT (Import Address Table), which holds the address of the  DeleteFile  () function located in Kernel32.dll. This DLL then redirects it to another function,  NtDeleteFile  (), located in ntdll.dll. This DLL then redirects it into the kernel via a  syscall  , which finally talks to the file system driver.

Now there are multiple locations where a hook is placed. It is highlighted in yellow: 1, 2, 3, 4, 5, and 6. At a high level, locations 1, 2, and 3 are user space hook locations and 4, 5, and 6 are kernel space hook locations.

---

## IAT - (Import Address Table)

### **Placing Hooks in User Space**
* Here are two main techniques for placing hooks in the user space:
	* IAT hooking.
	* Inline hooking.

As you can see in the diagram, when a process calls an API like `DeleteFile()`, which is located in another module (`Kernel32.dll`), the process obtains the address of `Kernel32.DeleteFile()` by referring to its **IAT** (import address table). The **IAT** acts like a jump table. Using the address obtained from the **IAT**, the process can jump and reach the function code for `DeleteFile()` located in `Kernel32.dll`.

![](M6-1-API%20Hooking_1.png)

With IAT hooking , all the malware does is replace the address of DeleteFile() in the IAT table to the address of a fake malicious DeleteFile() that the malware provides in its injected code. Now when the process calls DeleteFile() API and refers its IAT, the address of DeleteFile() in IAT points to the fake malware DeleteFile(), thereby redirecting all DeleteFile() API calls to the malicious DeleteFile() in the injected malware code. Figure 10-35 shows IAT hooking in action. You can use Figure 10-34 as a reference and compare it to the changes made by IAT hooking in Figure 10-35.

![](M6-1-API%20Hooking_2.png)

One of the defects of IAT hooking is that sometimes the code in a process might call an API in another DLL without needing to obtain the address of the API it needs from the IAT. So malware modifying the IAT with the address of its malicious code is useless. This defect can be solved by using inline hooking.

With inline hooking, the malware modifies the first few instructions in the real Kernel32.DeleteFile() API by inserting new instructions that effectively transfer the code flow to the malware injected code. This is best illustrated in Figure 10-36.

![](M6-1-API%20Hooking_3.png)

![](M6-1-API%20Hooking_4.png)

### **Why does Malware have/use hooks?**
* Processes perform a lot of operations on the system. Here are some of those.
  1. File Operation: 
	  - File Creation, File Deletion, Writing to file.
1. Registry Operations: 
	- Registry Key Creation, Registry Key Deletion, Setting a value in the registry key.
3.	Process Operations: 
	- Process Creation, Process Termination, Thread Creation, Thread Termination.
4.	Network Communication: 
	- Sending data, Receiving data.

*All these operations can be intercepted and manipulated by API hooking. In the following slides, lets see why a malware hooks.*

### Self-Protection
Self-protection is important to malware. Malware wants to protect its files, processes, and registry entries. For example, the DeleteFile() malware hook and any file deletion APIs to prevent the deletion of its files. Malware is known to hook the TerminateProcess() API and other variants of this API in Windows Task Manager, that terminates/kills a process so that a user is not able to kill any of its processes via the Task Manager.

### Rootkits/Stealth
Rootkits are techniques used by malware to hide their presence and presence of any of their artifacts like files, registry keys, processes, DLLs, network connections created by the malware. Most of the rootkit mechanisms use some form of API hooking to achieve stealth.

### Data Stealing
Win32 APIs implement a lot of functionality on Windows by all kinds of software. All kinds of activities—like pressing a key, copying to clipboard, or browsing the Internet—involve a Win32 API in some way. Malware is known to intercept these APIs to steal data, for example, to monitor our keystrokes, steal our banking credentials. Table 10-1 lists some of the APIs which are usually used (not all of them are hooked since you can log keystrokes without the needing to hook APIs) by keylogger malware, which tries to steal keystrokes of a user.

![](M6-1-API%20Hooking_5.png)

![](M6-1-API%20Hooking_6.png)

### Intercept Network Communication
We obviously can’t leave out network communication. Network APIs can be hooked to intercept the data sent over to the network by legitimate applications. Most of the network communication APIs on Windows resides in the DLL ws2_32.dll, wininet.dll, and wsock32.dll.

DNS traffic can be modified by hooking the APIs listed in Table 10-2. Malware can hook these APIs to modify the IP address returned by these names to redirect the user and legitimate applications to their malicious sites. Similarly, malware can hook these applications to block security software from being able to talk to their website by intercepting their DNS traffic.

![](M6-1-API%20Hooking_7.png)

## Man in Browser Attacks: The Banking Malware
Very similar to network communication, banking transactions are done through web browsers using an HTTP protocol. To carry out an HTTP transaction, the web browser which is the client that we use, uses a sequence of API calls like InternetOpen(), InternetConnect(), HttpOpenRequest(), HttpSendRequest() and InternetReadFile().

HTTPSendRequest() is the API used to carry the data from the user and the browser to the banking server, including our valuable credentials (i.e., the username and password). So if malware wants to tap the credentials sent to the server from the browser, it hooks HTTPSendRequest() API. When a victim tries to log in to the banking site using his credentials, the API now hooked by the malware be intercepted by the malware, which gets the banking credentials from the intercepted data. The malware keeps a copy of the credentials before passing on the data to the server, oblivious to the user. The stolen credentials from the malware are then shared by the malware with its attacker for other nefarious purposes. This technique is called form grabbing.

There is a similar kind of attack tactic called **Web Inject**.

**InternetReadFile**() that the API used by the web browser to receive the data sends from the server to the user. Very similar to the form grabbing technique, malware can hook this API to intercept the data sent back from the server before it can reach you in the browser. The goal of intercepting this data is to modify the *data/web_page_contents*  before handing it off the browser where you view it. Can you think of why it modifies the received response *data/web_page*  from the server?

Well, one well-known example is when the victim tries to open a banking website, the first thing the browser does is, it sends an HTTP/HTTPS request to the banking website, and the server responds with a login web page which has fields for the user’s banking credentials. Malware is known to intercept this login page sent back from the server to the user/browser through the  InternetReadFile  ()hook it has placed and modify the login page before passing it on to the browser. The modifications can include extra fields, like ATM PIN. Now inside the browser, the victim sees the fields for the user credentials and, in addition to that, sees the  **extra field for ATM PIN added**  by the malware via the hook interception. Now when the user fills in the data including the  ATM PIN  , the malware again intercepts the data, including the much sought after ATM PIN by intercepting the communication via the  HTTPSendRequest  () API like it did earlier.

![](M6-1-API%20Hooking_8.png)

![](M6-1-API%20Hooking_9.png)

#### **Important to know!**
*Now you might be wondering that using a secure protocol like HTTPS can protect your data even though the malware can intercept it via hooks. This is not true. HTTPS is useful to protect the traffic after encryption of the data, thereby preventing any snooping of the traffic even if they manage to intercept it. But malware can always intercept the traffic via hooks even before they are even encrypted by your browser, rendering HTTPS useless to main-in-the-browser attacks.*

### **Application of Hooks in Security Software**
Security software needs to monitor system activities for any malware infections. Very similar to malware, many of the antiviruses and  **anti-malware products hook on APIs to monitor **  file, registry, and network activity. Security software also needs to protect themselves from getting deleted, or their processes getting killed, or their processes being injected by malware code. All these require these anti-malware products to hook APIs in both user and kernel space by using the same hooking procedures we explained earlier.

Apart from products like antiviruses, another well-known tool that uses hooks extensively is an  **API logger like **  **APIMiner**  . API loggers hook both user space Win32 APIs, and also system calls in kernel space to identify the various APIs used by a process. API loggers are largely used by malware sandboxes to identify the behavior of malware by logging the Win32 APIs the malware uses. Some of the well known free and open source API loggers are  APIMiner  and Cuckoo Sandbox.

### **Hook Scanning Tools**
Most of the tools called rootkit scanners are actually hook scanners. **GMER** is one of the most popular ones. Another popular one is the **Ring3 API Hook Scanner** from www.novirusthanks.com. Running these hook scanner tools can help us identify if any of the APIs in the system are hooked and thereby identify any malware infection that relies on API hooking.

As we described in the previous section, an important point to remember is that many security software, as well as malware analysis tools, may create hooks in the system. Running your hook scanning tools might pop up these hooks from this security software on your system, which are real hooks, but they can be ignored. It’s good practice to take note of these hook entries from these clean software in case you are performing forensic analysis so that you can learn to ignore them when you look at these entries later on when you are analyzing a malware infection.

These hook scanning tools may bring up some false positives as well. Figure 10-38 displays the scan results for the GMER tool on a clean VM that is running Internet Explorer. As an exercise, please start the Internet Explorer browser and run the GMER tool.

![](M6-1-API%20Hooking_10.png)

The screenshot from GMER shows that Internet Explorer is hooked even though it may not be, or it might be hooked—not by malware, but by one of its own components as a security measure. You need to learn to identify these otherwise benign entries in GMER and ignore them when you analyze a real malware which hooks Internet Explorer and other processes on the system. Let's now dissect the structure of GMER logs, as seen in Figure 10-39.

![](M6-1-API%20Hooking_11.png)

* Here are some of the fields you can look for in the logs
  * Process image path This the path of the image of the hooked process
  * PID PID of the hooked process
  * DLL Name of the DLL in the process whose API is hooked
  * API This is the name of the hooked API in the DLL
  * API address This is the address of the hooked API
  * Jump target This the address of the memory location where the hook redirects the API to
  * Jump module This is the module where the jump target hook is located. This displays the location of the DLL module on disk. If this is not displayed, then it is an unknown module and may lie in injected code in memory, which you can use as a method to identify malicious code injected hooks.

The right way to use hook scanning tools like GMER and Ring3 API Hook Scanner is to first run these tools before you execute malware to analyze it, make a note of the GMER logs and save the logs. Now you run the malware and re-run GMER and save the logs. Now compare the difference in GMER logs before and after running the malware to identify any hooks by the malware.

## **Case Study: DeleteFile() Hooked**

make sure the same folder containing Sample-10-7.exe also has the file Sample-10-7-module.dll. In the same folder, create new text files: hello.txt and malware.txt. The folder contents should look like Figure 10-40.

Sample-10-7.exe injects code into Explorer.exe using one of the code injection techniques we covered earlier in the chapter and then inline hooks the DeleteFileW() API in Kernel32.dll module in Explorer.exe. With the hook in place, it redirects all API calls to Kernel32.DeleteFileW() to its own version of FakeDeleteFile() that checks if the user is trying to delete a file that has the word malware in it. If it does, it blocks the user from deleting the file. If the user tries to delete any file that doesn’t have the word malware in it, it allows the user to delete the file.

![](M6-1-API%20Hooking_12.png)

Double click Sample-10-7.exe.  Try shift+delete malware.txt and hello.txt 

![](M6-1-API%20Hooking_13.png)

Now run the Ring3 API Hook Scanner tool, which scans the system and shows that Explorer.exe has been hooked by our Sample-10-7.exe as seen in Figure 10-44.

![](M6-1-API%20Hooking_14.png)

## **Case Study: Internet Explorer Hooked**

Before you can run the malware executable Sample-10-8.exe, please launch the Internet Explorer browser inside your analysis VM. Now run Sample-10-8.exe. Now run the GMER tool and start the scan. Figure 10-45 displays the scan results of GMER on our system. Do note that the results might vary when compared to the scan results on your system.

![](M6-1-API%20Hooking_15.png)

![](M6-1-API%20Hooking_16.png)

To scan GMER looks and try to identify hooks that are not from the malware Sample-10-8.exe, look for jump targets that don’t lie in an unknown module. Also another way to find the actual hooks is by the process of elimination (i.e., you run GMER with Internet Explorer open before you run the malware sample, obtain the logs and save them). Now execute the malware sample with Internet Explorer open and re-run GMER and save the logs and compare it with the logs you saved earlier. The new entries point to hooks placed by the malware sample you ran.

![](M6-1-API%20Hooking_17.png)

We found that the hooks are in the HTTPSendRequestA and HTTPSendRequestW APIs, and it possibly indicates that we are dealing with malware, which is some sort of banking trojan that possibly intercepts user credentials via these hooks. More accurate details about the malware can only be found out by reverse-engineering the sample.

Now that we have identified the hook, let’s look at the memory location where the malware hook jumps into after intercepting an API call. The addresses as seen in Figure 10-46 are 0x01E816C0 and 0x01E817A0. Please do note the addresses might be different in your GMER logs. If we open the memory tab in process hacker for Internet Explorer, these addresses lie in a memory block that starts from 0x1e80000, as seen in Figure 10-47.

