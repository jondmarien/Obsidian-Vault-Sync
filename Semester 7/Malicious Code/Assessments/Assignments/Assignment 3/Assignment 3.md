---
title: Assignment 2
author:
  - Jon Marien
created: 2025-03-16
published: 2025-03-01
tags:
  - classes
  - INFO43921
---

| Title        | Author                       | Created        | Published      | Tags                                                  |
| ------------ | ---------------------------- | -------------- | -------------- | ----------------------------------------------------- |
| Assignment 3 | <ul><li>Jon Marien</li></ul> | March 16, 2025 | March 16, 2025 | [[#classes\|#classes]],<br>[[#INFO43921\|#INFO43921]] |

# Assignment 3: API Hooking

## Setup
1. Launch Internet Explorer on your analysis VM.
2. Run Ass3.exe. Note that, you need to unzip the Ass3.zip and rename the file to .exe before running it.

### Q3-1: Use GMER Tool and Ring 3 to Show API Hooking (8 points)
 
 1. [x] Launch the GMER tool to detect API hooking. (2points) ✅ 2025-03-16
 2. [x] Launch the Ring3 tool to detect API hooking. (2 points) ✅ 2025-03-16
 3. [x] For GMER and Ring3, Put screenshot of the tools results before (1points) and after running the sample (1 point). ✅ 2025-03-16
 4. [x] Explain what the malware doing. (2 points) ✅ 2025-03-16
 5. [x] Explain how you find it API hooking. (2 points) ✅ 2025-03-16
 6. [x] Important: Ensure that your name is included in every screenshot you take during this analysis. ✅ 2025-03-16

### Q3-2: Static Analysis Approaches (4.5 points)
1. [x] Perform static analysis on Ass3.exe using tools like CFF Explorer. (2 points) ✅ 2025-03-16
2. [x] Provide an explanation of what the malware does based on the static analysis findings. (1.5 point) ✅ 2025-03-16
3. [x] Check for any sys files and put screenshot of any you find.(1 point) ✅ 2025-03-16
4. [x] Important: Include your name in every screenshot you provide as part of the analysis. ✅ 2025-03-16

## Answers

### Q3-1: Dynamic Analysis
*Launch GMER and Ring3 + SSDT View (Before Malware is Run)*
![[image-107.png]]

*Show GMER and Ring3 with Malware Running*
As you can see in the image, **SSDT View** and **Ring3 API Hook Scanner** shows 0 hooks being used, but **GMER** shows some values in the **Rootkit/Malware** section, which I will show in a bigger image below.
![[image-109.png]] 
So here, you can see that `Ass3.exe` is using Windows Media Player to act malicious! It is using `wmpnetwk.exe` -- which is the Windows Media Player Network Driver -- to perform the hooking.  
![[image-110.png]]

I decided to use a secondary tool I found [online](https://github.com/brosck/APIHookingDetector/releases/tag/v2.0), called APIHookingDetector, since SSDT View or Ring3 was not functioning. I found that these NT APIs were being hooked:
`NtGetTickCount`
and `NtQuerySystemTime`
![[image-113.png]]
The fact that the `Ass3.exe` sample was hooking into those API calls, is particularly interesting, as they're usually flagged as false positives. But they both affect many **higher-level functions**, which could be a reason as to why the hacker targeted those. They are also both fundamental timing mechanisms. `Ass3.exe` could be using `NtQuerySystemTime` to manipulate timestamps for any given files or logs, which could hide the intrusion. `NtGetTickCount` could be used to affect timing-based operations within the host OS or within security software.

To me, it seems to me that `Ass3.exe`  might be using process injection techniques to load its malicious code into other processes after execution, because of the fact that GMER detected hooking in `wmpnetwk.exe`, while this process shows no obvious signs of malicious modules!

Looking through the handles/registry access, plus the thread stack analysis, and token privileges being used, we can come to a few conclusions:
![[image-114.png]]
![[image-115.png]]
![[image-116.png]]

#### Dynamic Analysis Conclusion
Those conclusions are as follows:
##### Process Analysis

From the modules tab, Ass3.exe appears to be a relatively small executable (40 KB) with standard Windows DLLs loaded. Nothing immediately stands out as malicious in the module list itself, but the small size could indicate a loader or dropper.

###### Handles and Registry Access
The handles tab shows:
- Several Event handles (`0x44, 0x60, 0x64, 0x68, 0x6c, 0x70, 0x74`).
- Registry access to **Image File Execution Options** keys.
- Access to **Control\Session Manager** and **Control\Nls** keys.
- File handles pointing to the executable location in my Downloads folder.

###### Thread Stack Analysis
The stack trace for thread `4588` shows:
- The thread is in a `WaitDelayExecution` state.
- Several `ntdll.dll` functions in the call stack.
- `RtlUserThreadStart` and `NtDelayExecution` functions.
- Calls to `wow64cpu.dll` indicating this is a 32-bit process running on 64-bit Windows.

###### Token Privileges
The token tab reveals:
- The process is running virtualized but not elevated.
- `SeChangeNotifyPrivilege` is enabled (standard).
- `SetTimeZonePrivilege` is disabled, which is interesting given my earlier findings about `NtQuerySystemTime` and `NtGetTickCount` being hooked!

*Process Hacker Ass3.exe properties*
Here, we can see the memory tab which shows some usages of certain `.dll` files.
![[image-108.png]]

After all of this Dynamic Analysis, we can attempt to figure out what the malware is doing. I ran it through IDA free and VirusTotal Graphs to see the attack view from an overview, top-down perspective.
We find some specific function imports that `Ass3.exe` is using: 
![[image-117.png]]

As well as the VirusTotal Attack Graph:
![[image-118.png]]
By following the graph, we can see that once `Ass3.exe` is started, it bundles two unknown files. After that, it executes TWO more malicious samples, both Trojans. One is for Active Directory, and the other for Poisoning, possibly for credentials.
![[image-119.png]]
![[image-120.png]]
After that, it contacts a Microsoft domain, which is completely clear of any malicious files.
Finally, it contacts 9 IPs, with one being malicious, as shown here:
![[image-121.png]]
If a user or program browses to this IP address, a lot of things will happen in the background. For example, it refers a bunch of malicious samples, in different formats, like `exe`, `peexe`, `zip`, `csv`, or a regular file. They are all worms, backdoors, trojans, or straight up malicious `pe` files. This site is also attached to a lot of Ransomware/RAT cases.

We can see here the full list of Process and Service actions:
![[image-123.png]]

We can also confirm the modules that are loaded, found with other tools, and also see what Mutexes were created by this program.
![[image-124.png]]

![[image-125.png]]

In conclusion, I am not sure what this piece of malware is doing, as I cannot find any specific indicators. I know it is a RAT/Trojan, and that it edits a lot of registry files, like the Control Set Sorting IDs. It seems to write data over a remote process, which is `IEXPLORER.EXE`, and creates a Remote Thread. It sets an **inline hook** on `WININET.dll`, and uses it to send an HTTP Request to most likely that malicious site we analyzed earlier. It also repeatedly calls the Sleep function for 2000ms at a time (2s). It creates an event, called `crypt32LogoffEvent`, creates a mutex, opens it, and switches the Hook to use the new event.

It also imports `Kernel32.dll`, and loads `LoadLibraryA`, `GetProcAddress`, `VirtualProtect`, `VirtualAlloc`, `VirtualFree`, and `ExitProcess`.
### Q3-2: Static Analysis
*TRiD and EXIF Results*
![[image-112.png]]
![[image-126.png]]

I couldn't find any `.sys` files. I searched within DiE (Detect it Easy), and CFF as well. Even throughout my other thorough analysis, I couldn't find much. 

#### Static Analysis Conclusion
After looking at `Ass3.exe` through static analysis, I've found some interesting stuff about what this malware is actually doing.

This malware is basically a RAT (Remote Access Trojan) that's pretty sophisticated in how it works. It's not very big - only about 40KB - which makes me think it's probably just the first stage of something bigger.

The most interesting part is how it hooks into those timing functions I mentioned earlier - `NtGetTickCount` and `NtQuerySystemTime`. This is a clever trick because by messing with these functions, it can potentially throw off security tools that rely on timing, or it could be changing timestamps to hide when it was active.

Looking at what it imports from Kernel32.dll (`LoadLibraryA`, `GetProcAddress`, `VirtualProtect`, `VirtualAlloc`, etc.), it's clear this thing is designed to inject code into other processes. This matches what I saw in the dynamic analysis where it was targeting Internet Explorer.

I couldn't find any `.sys` files during my analysis, which tells me this malware is probably sticking to user mode rather than trying to go deeper with kernel-level stuff. That said, it's still pretty sneaky with how it operates.

The **VirusTotal** graph was really helpful in showing the bigger picture - this malware connects to that suspicious IP (`23.216.147.64`) which is linked to all kinds of other malicious stuff. It seems like `Ass3.exe` is just the beginning of what could be a much larger attack.

Based on everything I've found, this malware is designed to:
- Inject itself into legitimate processes.
- Hook API functions to hide itself.
- Communicate with command and control servers.
- Potentially download more malware.
- Mess with registry settings.

It's definitely a multi-stage attack tool that's built to evade detection while setting up for something bigger - possibly ransomware or data theft based on the connections I found in VirusTotal!
## Links I Used
https://www.virustotal.com/gui/ip-address/23.216.147.64
https://www.virustotal.com/graph/23.216.147.64

https://www.virustotal.com/gui/file/9cdb1a336d111fd9fc2451f0bdd883f99756da12156f7e59cca9d63c1c1742ce/behavior
https://www.virustotal.com/graph/g109a9df81c0244b5917bf05a89a1b659abd1f7f23d54442d89c481d470cec326

