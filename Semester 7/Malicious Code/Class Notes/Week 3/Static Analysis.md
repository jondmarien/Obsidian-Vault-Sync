---
title: Week 3 - Static Analysis
author:
  - Jon Marien
created: 2025-01-22
published: 2025-01-22
tags:
  - classes
  - INFO43921
---

| Title                    | Author                       | Created          | Published        | Tags                   |
| ------------------------ | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Week 3 - Static Analysis | <ul><li>Jon Marien</li></ul> | January 22, 2025 | January 22, 2025 | [[#classes\|#classes]] |

# Chapter 7

## Why Static Analysis?
Static analysis serves as a good first step in the analysis process. By using it, you can often figure out if a sample is malicious or clean without even having to run it. You can even go as far as finding the type, family, and intent of the malware without needing to carry out any dynamic analysis.

When it is hard to conclude anything about the sample you are analyzing, the next step is dynamic analysis. But static analysis is first needed to figure out the various static properties of the sample file and the various analysis lab requirements, environment, tools, and the correct OS to set up before we start dynamic analysis. 

![](M3-1-Static%20Analysis_0.png)

 __Sample Hash for Information Xchange__ 

Be it static analysis or dynamic, the first step always includes checking if others have any thoughts or conclusions on your sample. Often, others have already analyzed your sample or a similar sample that belongs to the same malware family and have blogged a report on its analysis. In other cases, the same sample might have made its way to __VirusTotal__ and other malware analysis platforms.

But uploading samples to these public platforms or __sharing it with others is normally forbidden__, especially if the sample is from your workplace since the samples might also contain sensitive information. This is especially true if the malware component is embedded as a part of a sensitive customer or internal file, or if the sample in question isn’t malware at all, but a sensitive customer benign/clean file.

To get around this, the analysis world uses the file hash to exchange and obtain information about the sample. Almost all platforms, including analysis platforms, reports, and blogs for malware on the Internet, use the hash of a malware file to identify it. This allows one to obtain as well as share information about a malware sample without having to upload it or share it with any public analysis platforms, or even your friends.

* The popular hashes used are **md5, sha1, and sha256**.
  
Hashing Tools:
  * __HashMyFiles__:
    -  www.nirsoft.net/utils/hash_my_files.html in the form of a zipped package with a portable executable
  * Another GUI tool for Windows called __QuickHash__, can take in a file or raw content, and generate MD5, SHA1, and SHA256 hashes. 
	- **QuickHash** can be installed from https://quickhash-gui.org, where it is available in the form of a zipped package containing a portable executable.
  * Alternatively, Windows has the md5deep suite of tools, which comes with three command-line tools: __md5deep, sha1deep, sha256deep__. 
    - Downloaded from https://sourceforge.net/projects/md5deep/ as a zipped portable executable, which you have to extract and add to the PATH environment variable.
  * __Linux__ usually comes preinstalled with command-line tools, 
	  * Namely __md5sum, sha1sum, sha256sum__.

![](M3-1-Static%20Analysis_1.png)
![](M3-1-Static%20Analysis_2.png)

### Figuring Out the File Format 
Malware comes in different file formats: PE executables, .NET executables, Java files, Script files, JavaScript malware, WMI malware, and so forth. They might also be written for different operating systems: Linux, Windows, macOS, or Android. They might be targeted for a specific processor architecture: x86, x64, PowerPC, arm, and so forth. Based on the type and target of the sample file that you are analyzing, you might need different tools and even OS setup or maybe processor type to analyze the sample file.

A good first step is to figure out the format of the file, as that reveals a lot about what the target of the sample looks like.

In Sample-12-2, if you obtain its file format using `trid.exe` (see Figure 12-11), you notice that it is a PE executable file, which means all you need is a Windows OS environment (as well as the analysis tools that we installed in Chapter 2) to run it.

If  we look at Sample-12-4’s file format using trid.exe, it shows us that it is a .NET file: 

- 81.0% (.exe) generic CIL Executable (.NET, Mono, etc.) (73294/58/13). 
- analyzing .NET files on Windows requires specific .NET Frameworks, tools, and decompilers. 
- The .NET Framework may not be installed on your machine, or the wrong version might be installed. 
- Armed with the knowledge that you are dealing with a .NET file, __you can now set up your analysis VM environment with the tools and the right .NET Framework to help you analyze the sample__.
![](M3-1-Static%20Analysis_5.png)

### Code Signer Information 
Using the application details properties as a filtration system to flag and further dissect suspicious malware files is a valid option, but what if a malware attacker creates a malware file and copies all the product-related details from another clean software to his malware file? To counter this and to be sure about an application and its author/owner, there is a process called code signing.

We have similar digital keys, also known as code signing certificates, that are cryptographically generated to sign files. The unique digital signatures generated for the files using these code signing certificates traces back to the original author of the file.

For example, if you are Google, you apply for a code signing certificate from certain authorized vendors who issue these certificates, who vet that you are indeed who you are saying you are. You can now use the issued certificate to sign your apps and distribute them along with the generated digital signature for the app. The user of your app can verify its digital signature to trace it back to Google (you), thereby validating the source/author of the application.

![](M3-1-Static%20Analysis_9.png)
Most software vendors code sign their applications. For example, if you have firefox.exe or chrome.exe, which are the applications for Firefox and Chrome browsers, respectively, you can right-click them to view their digital signatures, as seen in Figure 12-13.

### Digital signature in malware samples 
With malware samples, **most of them are not digitally signed**. If a file is not digitally signed, you want to place the sample under the suspicious list and further dissect it. 

Similarly, some malware actors are known to buy their own digital certificates under various companies they form and sign their malware using the certificate they get, with the hope that their digitally signed application won’t raise any eyebrows.

as an analyst,  you need to remember that just   __ because an application is digitally signed, it doesn’t mean it is clean__   . 

As an analyst, you want to build a malware signer database with the names of the signer/author/company who signed a malware file. So when you find a new malware file that is digitally signed, extract the name of the signer, and add it to your malware signer database. The next time that you see a new sample that is signed by any signer from your malware signer database, you can flag the sample as suspicious and dissect it further.

## String Analysis Statically 

Malware samples are nothing but software programs, and as a part of the final software executable generated, the program includes many strings. These strings often can serve as very good indicators to identify the type, functionality, and intent of the software.

Most malware is packed. While the malware sample is packed using a packer, the data and the strings which are part of the original malware file are obfuscated in the outputted packed file and are not visible anymore.

But under some circumstances, certain chunks of data and strings from the original malware file might escape packing and might still be present in the final packed malware file. Sometimes, the malware authors do not pack malware samples. In other cases, you might also receive an unpacked malware sample for analysis, probably because some other analyst unpacked it and extracted the original malware file out. What this means is you can now view the strings in the unpacked portion of the sample file you are analyzing, giving you a glimpse into the innards for the sample.

To view the strings in the file, one can use the `BinText` tool.

Figure 12-15 shows strings that are related to the IRC protocol, which are used by malware for command-and-control network communication.
![](M3-1-Static%20Analysis_10.png)

![](M3-1-Static%20Analysis_11.png)
