---
title: Assignment 2
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
  - INFO43921
---

| Title        | Author                       | Created           | Published         | Tags                   |
| ------------ | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Assignment 2 | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |

# Assignment 2: Static Malware Analysis
## *Instructions*
1. Perform static analysis on the provided malware samples (two samples) and answer each question in detail.
2. Samples are zipped – first, unzip them, add the .exe extension, and then proceed with the analysis.
3. Use only the tools learned in class; VirusTotal, HybridAnalysis or any other online tools are not allowed for analysis.
4. Include the name of the tool used for each step and provide screenshots as evidence.
5. Put your name in every screenshot (e.g., by writing your name in the command prompt or annotation).

---
## Outline
[Assignment Introduction](#Assignment%202%20-%20Jonathan%20Marien%20-%20991476393%20-%20`chrono`)
[A1-1.exe](#A1-1.exe)
[A1-2.exe](#A1-2.exe)
[References](#References)

----

## Assignment 2 - Jonathan Marien - 991476393 - `chrono`
In reference to the instructions, for #5 -- "Put your name in every screenshot (e.g., by writing your name in the command prompt or annotation)." -- my username is `chrono`, I use this as my moniker online for competitions, within ISSessions, and for general hacking distributions, I use the username `chrono`. Each prompt/screenshot will have this username within it, proving it is mine. Now, on to the assignment!

### A1-1.exe
#### Packed Analysis (2 point)
- Check if the sample is packed.
	- If packed, identify the packer used.
![[image-32.png]]
Yes, the sample is packed, as indicated by the `(Heur)Packer: Compressed or packed data [PE in overlay]`. Also, the overlay section `(Offset=0x0058e0, Size=0x00037200)` suggests additional data appended to the file, which is often used by packers.

To confirm, I also checked the entropy chart, where you can tell some of it has been modified and packed:
![[image-39.png]]

#### File Format (1 point)
- Identify the format of the file (e.g., PE, ELF, Mach-O).

I ran `file` on the `.exe`. Although, I did could have used DiE, and I did not need to add `.exe` as the extension.
The file format is a `PE32 Executable`, 32-bit, as indicated by the `Intel 80386`
![[image-33.png]]
#### Required Libraries or Dependencies (1 point)
- List the libraries/packages required for execution.

After clicking the `Import` button on DiE, you can see all the DLLs and functions that are in use:
![[image-34.png]]

To list them out, I will make a table/chart:

| DLLs (.dll) | Functions          |
| ----------- | ------------------ |
| MSVCRT      | `wcsstr`           |
| SHELL32     | `_snwprintf`       |
| SHLWAPI     | `strstr`           |
| ntdll       | `_snprintf`        |
| KERNEL32    | `_except_handler3` |
| USER32      | `memset`           |
| ADVAPI32    | `memcpy`           |
| ole32       |                    |
| OLEAUT32    |                    |

#### File Hash (2 point)
- Calculate and provide the MD5, SHA1, or SHA256 hash of the file.
	- Hash Lookup Restriction: Do NOT use online tools. Instead, use tools in your machine.

I opted to use `sha256sum` in my Kali WSL2 instance:
![[image-37.png]]

#### DLL Dependencies (1.5 point)
- Identify and list any DLL files used by the malware.

I confirmed the DLL Dependencies with the tool `Dependency Walker`:
![[image-36.png]]
#### Suspicious Strings (2 points)
- Extract strings from the file without executing it.
	- Identify any suspicious indicators (e.g., hardcoded IPs, URLs, commands).

I found a LOT of functions being used, by using`strings` on the exe:
![[image-40.png]]

These look important, too:
![[image-44.png]]

I also found some interesting entries, some of them are the programs running in my system tray, and then a bunch of commonly used passwords. These were all contained in the `.rdata` section:
![[image-41.png]]

Then, it looks like it checks if it is in a sandbox or not, and does some local system commands:
![[image-42.png]]

It looks like it also contains URLs for common anti-malware sites, possibly to cross check:
![[image-43.png]]

I also found more `functions` being used, as well as some weird Cyrillic text, and it can get your clipboard data: 
![[image-45.png]]

It looks like it tries to login with some things:
![[image-46.png]]

Using `strings` further confirmed this:
![[image-47.png]]
#### Research the Sample (2 points)
- Search online for the file name, hash, or extracted strings.
	- Identify if it belongs to a known malware family and provide supporting evidence.

Using the hash from before, `bdbfca1b0d259836ca3420f7d6ab1210`, we can check it on `VirusTotal`. VirusTotal redirects us to the hash `4a99629b3b93b4095ec7299d4d06b7ec79f146b68ee55e5a68674537d0b99ad4`, which has been scanned 100s if not 1000s of times. 

![[image-50.png]]

This site also confirmed the `.dlls` that it loads, among other cool pieces of information:
![[image-51.png]]

I did some extra analysis on this, using `any.run`, and I found the behaviour of the program:
![[image-52.png]]

It spawns `36` total processes, and `2` malicious processes, all in the span of `60s`.
![[image-53.png]]

This piece of malware is specifically a `botnet`, as described and shown with the `sinkhole` tag on the main breakdown of the malware:
![[image-54.png]]

![[image-55.png]]

![[image-56.png]]
![[image-57.png|423x232]]
#### Code Signing (1 point)
- Check if the file is signed by a certificate.
	- If signed, identify the issuer and validity of the certificate.

`SignTool` on Windows was not functioning for me, so I found a tool on linux called `osslsigncode` and it checks if an `.exe` is signed or not. Here is what I found:
![[image-48.png]]
Therefore, it is not signed.

By checking `any.run`, I was able to confirm that it is indeed not signed with a valid, or any, certificate:
![[image-87.png]]
#### Final Thoughts on A1-1
This was a cool piece of malware to look through, as it ends up hiding the execution of A1-1 by attempting to launch the Windows Media Player configuration application.

I was also able to decode the MITRE ATT&CK Matrix for this `.exe`:
![[image-58.png]]

On to the next executable!
### A1-2.exe
#### Packed Analysis (2 point)
- Check if the sample is packed.
	- If packed, identify the packer used.

![[image-59.png]]

At first glance, it does not look like it was packed. Let us check the entropy graph.
![[image-60.png]]
Without cheating (looking at the big blue bar that says "not packed, 79% sure"), if we take a look at the actual entropy value in the top right, we can see that it is under a value of `7` (`6.34382 < 7`), which means it is likely that this `.exe` was not packed.

It does identify as linked to `Polink(2.50)`, for `DLL32`, but again, not packed. It is programmed to be in ASMx86, which is usually a good choice to avoid detection.
#### File Format (1 point)
- Identify the format of the file (e.g., PE, ELF, Mach-O).

I ran `file` on linux again, as that was easiest for me:
![[image-61.png]]

We can see that this is a 32-bit Windows DLL file, for Windows 95 (as seen in DiE), and it is a PE32 Executable. 
#### Required Libraries or Dependencies (1 point)
List the libraries/packages required for execution.

Again, just used the `Imports` tab in DiE:
![[image-62.png]]

Complimentary table:

| DLLs (.dll) | Functions       |
| ----------- | --------------- |
| wsock32     | `inet_addr`     |
| kernel32    | `gethostbyname` |
| urlmon      | `socket`        |
| userenv     | `connect`       |
| ole32       | `closesocket`   |
| user32      | `send`          |
| advapi32    | `select`        |
| wininet     | `recv`          |
| shlwapi     | `setsockopt`    |
|             | `WSAStartup`    |

I did some research, and `advapi32.dll` is used for registry manipulation! Pretty cool!
#### File Hash (2 point)
- Calculate and provide the MD5, SHA1, or SHA256 hash of the file.
	- Hash Lookup Restriction: Do NOT use online tools. Instead, use tools in your machine.

I opted to use `sha256sum` again:
![[image-63.png]]
We can confirm the `sha256` hash in DiE:
![[image-64.png]]

#### DLL Dependencies (1.5 point)
- Identify and list any DLL files used by the malware.

I used `Dependany Walker` again. I found a lot more `.dlls`:
![[image-65.png]]

#### Suspicious Strings (2 points)
 Extract strings from the file without executing it.
	- Identify any suspicious indicators (e.g., hardcoded IPs, URLs, commands).

Using `strings` combined with`grep` and a regex expression to find `URLs` and `.DLLs` within the `.exe`, I found these:
![[image-67.png]]
Found more strings in DiE:
![[image-68.png]]
![[image-70.png]]

Looks like it installs `TeamViewer`, too, making me think that this is some kind of trojan.

And it looks for passwords, and a malicious mutex:
![[image-71.png]]

![[image-72.png]]

All the functions:
![[image-73.png]]

Pretty scary stuff...
#### Research the Sample (2 points)
Search online for the file name, hash, or extracted strings.
	- Identify if it belongs to a known malware family and provide supporting evidence.

Using the hash from before, `436f9776580ea0dceb25215539f4d3b85d0f9eee7d912671c84846e43008f6fe`, if we check in `VirusTotal`, I was correct! It is a trojan!

![[image-74.png]]

Let's do some more research. I went back to `any.run` to further research the possible trojan within the malware sample.

Once again, I found the behaviour graph:
![[image-77.png]]

So, the program starts, and it uses `rundll32.exe` to launch `cmd.exe`, through the parent process `explorer.exe`.  Although it has almost `3,000` registry events, only `4` of them are `write` events:
![[image-78.png]]

It runs `37` total process, with `3` being monitored and only `1` malicious process being spawned:
![[image-79.png]]

There is a trojan within this malware sample called `Pony` or `Fareit`, and it aims to steal creds from browsers, and personal data from the computer. It also uses a `Raccoon` mutex, as mentioned earlier in the report.
![[image-80.png]]

Here is the malicious code general info, where you can see the `pony`, `raccoon`, `stealer`, and `trojan` tags, showing us what this piece of code is known to do:
![[image-81.png]]

| Malware Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Pony/Fareit/Siplog`      | "Pony is a malware with two main functions — stealing information and dropping other viruses with different tasks on infected machines. It has been around since 2011, and it still actively attacks users in Europe and America."                                                                                                                                                                                                                                                                         |
| `Raccoon/Mohazo/Racealer` | "Raccoon is an info stealer type malware available as a Malware as a Service. It can be obtained for a subscription and costs $200 per month. Raccoon malware has already infected over 100,000 devices and became one of the most mentioned viruses on the underground forums in 2019."                                                                                                                                                                                                                   |
| Stealer (General)         | "Stealers are a group of malicious software that are intended for gaining unauthorized access to users’ information and transferring it to the attacker. The stealer malware category includes various types of programs that focus on their particular kind of data, including files, passwords, and cryptocurrency. Stealers are capable of spying on their targets by recording their keystrokes and taking screenshots. This type of malware is primarily distributed as part of phishing campaigns."  |
| Trojan (General)          | "Trojans are a group of malicious programs distinguished by their ability to masquerade as benign software. Depending on their type, trojans possess a variety of capabilities, ranging from maintaining full remote control over the victim’s machine to stealing data and files, as well as dropping other malware. At the same time, the main functionality of each trojan family can differ significantly depending on its type. The most common trojan infection chain starts with a phishing email." |
*All taken from the any.run descriptions of said malware;*

Also found the MITRE ATT&CK Matrix for this sample, too:
![[image-82.png]]

Some more specifics of the malicious executable: 
![[image-85.png|395x228]]
![[image-84.png]]
#### Code Signing (1 point)
Check if the file is signed by a certificate.
	- If signed, identify the issuer and validity of the certificate.

Once again, I used `osslsigncode`, and I could not find a signature or certificate, even with `openssl verify`:
![[image-75.png]]
![[image-76.png]]

#### Final Thoughts on A1-2.exe
By doing extensive research, I found that this malicious sample first executes a process called `rundll32.exe` which is executed with the command line argument of a file path. The second process is `cmd.exe` which is executed with the command line argument of `cmd /K`, which starts a new instance of `cmd` while executing a specified command, and keeps `cmd` running. The third process is `wmpnscfg.exe` which is executed without any command line arguments.

After looking at the immense number of registry events, I was able to gather a few things. First, the registry write events indicate that the process with `PID 1252` is writing to the registry. The specific keys and values being written suggest that the process is modifying the Internet settings cache prefixes and cookies. This behavior could be used by malware to modify or manipulate the browser's cache and cookies, potentially for malicious purposes such as tracking user activity, stealing sensitive information, or executing malicious code.

Pretty scary stuff...Fun assignment though 😄
### References
Here are IEEE-style references for the tools and platforms mentioned in this report, focusing on their application in cybersecurity research and malware analysis:

---

#### **Malware Analysis Platforms**

ANY.RUN, “Interactive Malware Analysis Service,” ANY.RUN, 2024. [Online]. Available: https://any.run. [Accessed: Feb. 15, 2025].
*Relevance: Dynamic malware analysis using real-time behavioral observation.*

VirusTotal, “VirusTotal - Analyze suspicious files and URLs to detect malware,” VirusTotal, 2024. [Online]. Available: https://virustotal.com. [Accessed: Feb. 15, 2025].
*Relevance: Multi-engine scanning, file/URL reputation checks, and artifact analysis.*

---

#### **CLI Tools for Security Analysis**

OpenSSL Software Foundation, OpenSSL Cryptography and SSL/TLS Toolkit, 2024. [Online]. Available: https://www.openssl.org. [Accessed: Feb. 15, 2025].
 *Relevance: Covers cryptographic verification workflows for executables and certificates.*

M. Trojnar, osslsigncode: OpenSSL-based Authenticode signing tool, 2024. [Online]. Available: https://github.com/mtrojnar/osslsigncode. [Accessed: Feb. 15, 2025].
 *Relevance: Covers cryptographic verification workflows for executables and certificates.*

Free Software Foundation, sha256sum - GNU Coreutils Manual, 2024. [Online]. Available: https://www.gnu.org/software/coreutils/manual/html_node/sha2-utilities.html. [Accessed: Feb. 15, 2025].
*Relevance: Explains hashing algorithms for ensuring file integrity in forensic pipelines.*

Free Software Foundation, strings, file, and grep utilities - GNU Binutils Documentation, 2024. [Online]. Available: https://www.gnu.org/software/binutils. [Accessed: Feb. 15, 2025].
*Relevance: Demonstrates text-based pattern matching for identifying suspicious binaries.*

---

#### **Windows Applications**
Horsicq, Detect It Easy (DiE) - PE File Analyzer, 2024. [Online]. Available: https://github.com/horsicq/Detect-It-Easy. [Accessed: Feb. 15, 2025].
*Relevance: Focuses on file header analysis to classify packed or obfuscated executables.*

S. Lee, Dependency Walker (depends.exe) - Windows Module Dependency Analyzer, 2024. [Online]. Available: https://www.dependencywalker.com. [Accessed: Feb. 15, 2025].
  *Relevance: Analyzes DLL hijacking and import table anomalies in Windows executables.*

---
