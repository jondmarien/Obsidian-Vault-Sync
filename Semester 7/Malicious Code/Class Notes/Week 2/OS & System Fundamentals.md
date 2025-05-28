---
title: OS & System Fundamentals
author:
  - Jon Marien
created: 2025-01-15
published: 2025-01-15
tags:
  - classes
  - INFO43921
---

| Title                    | Author                       | Created          | Published        | Tags                   |
| ------------------------ | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| OS & System Fundamentals | <ul><li>Jon Marien</li></ul> | January 15, 2025 | January 15, 2025 | [[#classes\|#classes]] |

# OS & System Fundies

# File format

Every file in our OS is binary. The misconception most often heard is that every binary file is an executable file. All kinds of data—executable files, text files, HTML page files, software programs, PDFs, Word documents, PowerPoint slides, videos, audios, games, or whatever else is stored in a computer as file—is in the form of a binary file . But when opened, each file runs or is presented to the user differently based on the file’s extension or data format.

- Install hexeditor plugin for notepad++
	- [NPPHexEdit](https://github.com/chcg/NPP_HexEdit/releases/tag/0.9.5.19)  
- Or use menu plugins>admin plugins to install hexeditor and use plugins>hexeditor

Hashing is used in the malware analysis world to uniquely identify a malware sample.

Hashing only depends on the contents of the file, not file name.

There are mainly three kinds of hashes that are predominantly used in the malware world for files (md5, sha1, and sha256)

HashMyFiles GUI tools, or  md5deep, sha1deep, sha256deep

![](M2_OS_and_System_fundamentals_file_format10.png)

# Identify files

There are two primary ways to identify files:  __file extensions__  and  __file format__ .

__File association__  is a method by which you can associate a file type or extension to be opened by a certain application. Usually, a file extension is the file property that creates an association with an application on the system.

Malware authors use extension faking and thumbnail faking techniques to deceive users into clicking the malware (as will be explained in the next sections). Knowing the correct extension of a file can help thwart some of these malicious techniques.

# Extension faking

![](M2_OS_and_System_fundamentals_file_format11.png)

# Changing Thumbnail

Variety of tools available to change thumbnail

![](M2_OS_and_System_fundamentals_file_format12.png)

# File format

files with the same extension have some specific characters common to them at the very start of the file. For example, ZIP files start with PK. A. PNG file’s second, third, and fourth characters are PNG. Windows DOS executables start with MZ, as shown in Figure 3-12.

These magic bytes are not located randomly in the file. They are part of what is known as the __ file header__  . Every file has a structure or format that defines how data should be stored in the file.

A file—audio, video, executable, PowerPoint, Excel, PDF document—each has a file structure of its own to store its data. This file structure is called a ***file format*** .

![](M2_OS_and_System_fundamentals_file_format13.png)

# Magic Bytes

![](M2_OS_and_System_fundamentals_file_format14.png)

![](M2_OS_and_System_fundamentals_file_format15.png)

![](M2_OS_and_System_fundamentals_file_format16.png)

* Tools to identify file formats:
  * __file__  command-line tool in Linux,
  * __TriD__  present as the trid command-line tool available on Windows, Linux, and macOS, needs to install the dictionary of format types

# Identify the file format
* Run following commands:
  * `echo "Some line" > file1.jpg`
  * `File file1.jpg`

![](M2_OS_and_System_fundamentals_file_format17.png)

#  Trid

Remember to download triddefs.trd as well. It is tehe datasets defining format of various type of files

![](M2_OS_and_System_fundamentals_file_format18.png)

![](M2_OS_and_System_fundamentals_file_format19.png)

# Another example

The data that we deal with may come from network packets, and in some cases, it might include the contents of a file that we are analyzing. Often, the data carries files from malware attackers or contains other files embedded with an outer parent file. Knowing the magic bytes and the general header structure for well-known file formats helps you quickly identify the presence of these files embedded in a huge data haystack, which improves analysis efficiency. For example, Figure 3-15 shows Wireshark displaying a packet capture file carrying a ZIP file in an HTTP response packet. Quickly identifying the PK magic bytes among the packet payload helps an analyst quickly conclude that the packet holds a response from the server returning a zipped file.

![](M2_OS_and_System_fundamentals_file_format110.png)

# Virtual Memory and the Portable Executable (PE) File

A process is defined as a program under execution. Whether a program is clean or malicious, it needs to execute as a process to carry out its desired intention.

We also dissect the PE file format, which is used by all executable files in Windows, and explore how its various headers and fields are used by the OS to load the PE executable program as a process. We also cover other types of PE files, such as DLLs, and explore how they are loaded and used by programs.

# Process Creation

Use sample sample-4-1, change suffix to .exe

![](M2_OS_and_System_fundamentals_file_format111.png)

# Tools: Process hacker or process explorer

![](M2_OS_and_System_fundamentals_file_format112.png)

![](M2_OS_and_System_fundamentals_file_format113.png)

# Virtual Memory

![](M2_OS_and_System_fundamentals_file_format114.png)

![](M2_OS_and_System_fundamentals_file_format115.png)

Virtual memory creates an illusion to a process that there is a huge amount of RAM available exclusively to it, without having to share it with any other processes on the system.

Each process can see a fixed amount of memory or rather virtual memory, which is assigned to it by the OS, irrespective of the actual physical size of the RAM.

The OS divides the virtual memory of a process into small contiguous memory chunks called pages. The size of a page is determined by the OS and is based on the processor architecture, but typically, the default page size is 4 KB (i.e., 4096 bytes).

![](M2_OS_and_System_fundamentals_file_format116.png)

# Demand Paging and the Page Table

![](M2_OS_and_System_fundamentals_file_format117.png)

![](M2_OS_and_System_fundamentals_file_format118.png)

To translate the virtual address of a process into the actual physical address on physical memory, the OS uses a page table.

Windows splits the address range of each process’s virtual memory into two areas: the user space and the kernel space. the kernel space is common to all the processes, but the user space is separate for each process.

![](M2_OS_and_System_fundamentals_file_format119.png)

# Types of Pages

Private pages: These pages are exclusive to the process and are not shared with any other process. For example, the pages holding a process stack, Process Environment Block (PEB), or Thread Environment Block (TEB) are all exclusive to a process and are defined as private pages. Also, pages allocated by calling the VirtualAlloc() API are private and are primarily used by packers and malware to hold their decompressed data and code. Private pages are important for us as you learn to dissect a malware process using its memory in later chapters.

Image pages: These pages contain the modules of the main executable and the DLLs.

Mapped pages: Sometimes, files or parts of files on the disk need to be mapped into virtual memory for use by the process. The pages that contain such data maps are called Mapped. The process can modify the contents of the file by directly modifying the mapped contents in memory. An alternate use of mapped pages is when a part of its memory needs to be shared with other processes on the system.

![](M2_OS_and_System_fundamentals_file_format120.png)

The virtual memory now with the decrypted malware code and data can contain important strings related to malware artifacts like malware name, hacker name, target destinations, URLs, IP addresses, and so forth.

One can also identify if code has been unpacked (more on this in Chapter 7) or injected (more on this in Chapter 10) by malware using the permissions/protections of memory blocks. Usually, injecting code malware allocates executable memory using various APIs that end up being allocated as private pages with read, write, and execute (RWX) protection, which is a strong indicator of code injection or unpacking.

who loaded this program file from the disk into memory, turning it into a process? We explained that it was the OS, but the specific component of the OS that did it is called the Windows loader. But how does the Windows loader know how to load a program as a process, the size of virtual memory it needs, where in the program file the code and the data exist, and where in virtual memory to copy this code and data?every file has a file format.

an executable file on Windows has a PE file format. The PE file format defines various headers that define the structure of the file, its code, its data, and the various resources that it needs.

Sample4-1.exe file format: `MZ` means portable executable (PE)

![](M2_OS_and_System_fundamentals_file_format121.png)

Windows executable is called a portable EXE, or PE file. PE files can further be sub grouped as ***.exe***, ***.dll***, and ***.sys*** files.

The PE file has two components: the headers and the sections. The headers are meant to store meta information, and the sections are meant to store the code, data, and the resources needed by the code to execute. Some of the meta-information stored by the headers include date, time, version of the PE file. The headers also contain pointers/offsets into the sections where the code and the data are located.

![](M2_OS_and_System_fundamentals_file_format122.png)

Use CFF to dissect PE file

Opening an executable program (PE file) in CFF Explorer does not create a process for the sample program. It is only reading the contents of the PE file and displaying to us its structure and contents

The DOS header starts with the `e_magic` field, which contains the DOS signature or magic bytes 4D5A, otherwise known as MZ.

The NT headers begin with the Signature field, which holds the value PE (the hex is 0x5045).

![](M2_OS_and_System_fundamentals_file_format123.png)

![](M2_OS_and_System_fundamentals_file_format124.png)

*Cpu from the imagebase in the header understand where to allocate memory to PE file*.

![](M2_OS_and_System_fundamentals_file_format125.png)

Relative Virtual Address (RVA): With RVA, every reference to an address in virtual memory is an offset from the start of the actual image base address that the process is loaded in its virtual memory.

Assuming the actual image base is 0x400000, the effective AddressOfEntryPoint is 0x401040

![](M2_OS_and_System_fundamentals_file_format126.png)

![](M2_OS_and_System_fundamentals_file_format127.png)

You can verify that 0x400000 is the actual image base of the PE file module in the virtual memory of Sample-4-1.exe by using Process Hacker

![](M2_OS_and_System_fundamentals_file_format128.png)

# Section Data and Section Headers

Section data, or simply sections, contains code, data referenced by the import tables, export tables, and other tables, embedded resources like images, icons, and in case of malware, secondary payloads, and so forth.

The NT headers begin with the Signature field, which holds the value PE (the hex is 0x5045),

![](M2_OS_and_System_fundamentals_file_format129.png)

* File Header:File Header has seven fields,

File header>machine: Modifying it to a wrong type results in a failure to create a process when you double-click it.

![](M2_OS_and_System_fundamentals_file_format130.png)

File header> __NumberOfSections__  field: holds the number of sections present in a PE file. Sections store various kinds of data and information in an executable, including the code and the data. Sometimes viruses, file infectors, and packers (see Chapter 7) modify clean programs by adding new sections with malicious code and data. When they do this, they also need to manipulate this field to reflect the newly added sections.

File header> characteristic

![](M2_OS_and_System_fundamentals_file_format131.png)

Optional Header:An optional header is not optional, and it is important. The Windows loader refers to the many fields in this header to copy and map the PE file into the process’s memory. The two most important fields are AddressOfEntryPoint and ImageBase.

__Data directories__  contain the size and RVA to locations in memory that contain important data/tables/directories, as seen in Figure 4-29. Some of these tables contain information that is used by the loader while loading the PE file in memory. Some other tables contain information that is used and referenced by the code instructions as they are executing.

![](M2_OS_and_System_fundamentals_file_format132.png)

Section data, or simply sections, contains code, data referenced by the import tables, export tables, and other tables, embedded resources like images, icons, and in case of malware, secondary payloads, and so forth.The loader uses this information from the section headers to allocate the right amount of virtual memory, assign the right memory permissions (check the section page permissions), and copy the contents of the section data into memory

# Section Headers Fields

The  __Name__  field contains the section name. The name of a section is decided by a compiler/linker and packers and any other program that generates these PE files. Sections can have names like .text that usually contains code instructions, .data that usually contains data/variables referenced by the code, and .rsrc that usually contains resources like images, icons, thumbnails, and secondary payloads in case of malware.

The names are just suggestions on what it might contain, but it shouldn’t be taken at face value. In fact, for a lot of malware, you may not find sections with names like .text and .data. The packers used by both malware and clean software can use any name of their choice for their sections

# Section Headers Fields (cont.)

A  __virtual address__  is the RVA in which the section is placed in virtual memory. To get the actual virtual address, we add it to the actual image base of the PE file in virtual memory.

A  __raw size__  is the size of the section data in the PE file on the disk.

A  __raw address__  is an offset from the start of the PE file to the location where the section data is located.

Characteristics: permissions(Pages in virtual memory have permissions)

![](M2_OS_and_System_fundamentals_file_format133.png)

![](M2_OS_and_System_fundamentals_file_format134.png)

The section data can be viewed if you select and click any of the section rows in the section header,

The Windows loader reads the data in the section from the disk file, as seen in Figure 4-32, using its Raw Address and Raw Size fields and then copies it into virtual memory.

![](M2_OS_and_System_fundamentals_file_format135.png)

The size loader needs to allocate for the section is given by the Virtual Size field,

the actual address at which it allocates this memory is image base + virtual address

![](M2_OS_and_System_fundamentals_file_format136.png)

# Dynamic-Link Library (DLL)

DLLs, or dynamic-link libraries, hold these functions, more commonly called APIsc (application programming interface), that can be shared and used by other programs, as shown in Figure 4-35.

A DLL is available as a file on Windows with the .dll extension . A DLL file also uses the PE file format to describe its structure and content.

if you double-click a DLL file, it won’t launch a process. This is because a DLL file can’t be used independently and can only be used in combination with another EXE file.

![](M2_OS_and_System_fundamentals_file_format137.png)

![](M2_OS_and_System_fundamentals_file_format138.png)

One of the easiest ways to identify a file as a DLL is by using the file identification tools like TriD and the file command like tools. Another way is by using the Characteristics field in the PE file format.

The loader obtains the list of DLL dependencies for a PE file from the import directory (also called an import table).

![](M2_OS_and_System_fundamentals_file_format139.png)

Run sample-4-1.exe and use tool process hacker.

Dependency Chaining:Sample-4-1.exe depends on msvcrt.dll. But msvcrt.dll being just another PE file also depends on other DLLs. Those DLLs depend on other DLLs, all of which now form a chain, and all the DLLs in this chain are loaded by the Windows loader.

![](M2_OS_and_System_fundamentals_file_format140.png)

![](M2_OS_and_System_fundamentals_file_format141.png)

Export: A DLL consists of APIs that can be used by other executable programs.

![](M2_OS_and_System_fundamentals_file_format142.png)

Import Address Table:An IAT is a table or an array in memory that holds the addresses of all the APIs that are used by a PE file.

![](M2_OS_and_System_fundamentals_file_format143.png)

# Sample-4.3.exe with Sample-4.2.dll

Sample-4.3.exe import sample-4-2.dll

See export for sample4-2.dll in CFF

![](M2_OS_and_System_fundamentals_file_format144.png)

# Sample 4-3.exe (cont.)

See import in sample4-3.exe in CFF

![](M2_OS_and_System_fundamentals_file_format145.png)

Run sample-4-3.exe and see process hacker

the actual image base of Sample-4-2.dll in memory is 0x10000000, making the effective virtual address of HelperFunction2() as 0x10001090.

![](M2_OS_and_System_fundamentals_file_format146.png)

![](M2_OS_and_System_fundamentals_file_format147.png)

![](M2_OS_and_System_fundamentals_file_format148.png)

Why is learning about IAT important? IAT is commonly misused by malware to hijack API calls made by clean software. Malware does this by replacing the address of genuine APIs in the IAT table of a process with addresses of its code, basically redirecting all the API calls made by the process, to its own malicious code.

## **Malware Packers**

* An attacker avoids delivering a raw version of the malware to the victim. Because:
  * Anti-malware products can easily detect it as malicious by using static signatures. 
  * The raw piece of malware can be larger and might take a longer time to download on a victim’s machine.
* The attacker encrypts and packs/compresses the malware.

## **Encryption and Compression**

Encryption is a way to lock the data with a key in such a way that it cannot be accessed without the key. 

AES, Xtea, RC4, Base64 are some of the commonly seen encryption and encoding algorithms used by malware.

Obfuscation is a direct side-effect of encryption, where the actual data is now obfuscated and looks like some sort of garbage data to the naked eye.

Compression is a method to reduce the size of the data. But compression algorithms alter the data it compresses, and one of the direct side-effects of this can also be obfuscation.

 LZMA, LZSS, and APLib are some of the compression algorithms used by malware.

a packer takes the whole original malware payload file developed by the malware attacker and generates a new malware file but which is now compressed and obfuscated.

## **How Packers Work** 

Packer programs take as input a PE executable file and output a new PE executable file, which is now packed. 

An executable PE file mainly has two components: headers and sections. Sections can contain code, data, and resources the program needs. The sections are the main components that need to be compressed to reduce the size of the executable.

The packer program takes both the headers and the sections from the PE file that it is packing and generates new headers and new sections which contain the compressed data.

When generating the new packed executable file, a packer embeds within it a loader code or an unpacking stub code. This unpacking stub code knows the location of compressed code and data in the packed file. It holds logic within itself that can take this compressed code and data, and output into memory the original payload’s uncompressed code and data. 

![](M2_OS_and_System_fundamentals_file_format149.png)

 ## **Cryptors, Protectors, Installers**

__Cryptors__: May compress or encrypt code like packers. Cryptors are meant to give a deceptive appearance of a malware file by changing the external characteristics of the malware to make it look like legitimate software. They may change the icons, thumbnails, and version information.

__Protectors__: Can also obfuscate the malware by replacing the code inside it with the code that does equivalent stuff, but that now looks more convoluted to analyze and understand. For example, take two expressions (A + B) and (A * C / C + B). You have two expressions that do the same thing, but the second expression is hard to read and analyze compared to the first. This is also called code polymorphism .

__Installers__: Are another means to package software but again used by malware. Installers, apart from packing, also provide installation options to the malware.

Some of the popular installers used by malware are MSI, Inno Setup, and autoIT. One of the key differences between clean software and malware installers is that installers used in legitimate software pop up GUI based user interfaces, but it installs malware    __silently__ and executes it.

These days most packers, cryptors, and protectors have incorporated new features where they include anti-debug, anti-VM, anti-analysis, and other armoring code as part of the outer packed loader stub code.

Download UPX packer from https://github.com/upx/upx/releases. 

Unzip and add the path to environment variable.

Use upx command for sample-7-1

See the reduced size of packed file

![](M2_OS_and_System_fundamentals_file_format150.png)

![](M2_OS_and_System_fundamentals_file_format151.png)

The strings are readable on sample7-1 but not in packed version

![](M2_OS_and_System_fundamentals_file_format152.png)

## __Identifying Packed Samples__ 

1. __Entropy__    is the measure of randomness of data or, in our case, the file. Entropy is a common technique to detect encryption and compression since, after compression and encryption, the data looks random or junk-like, leading to higher entropy. On the other hand, an unpacked file has less randomness, thereby having less entropy.
	- We load Sample-7-1-packed in    __PEiD__   , which shows an entropy of 7.8. 

![](M2_OS_and_System_fundamentals_file_format153.png)

2. __Strings__: Whenever you write a program, you end up using many strings in the source code. In malware, many strings that are used in the source code are C2 server domains and IP addresses of C2 servers; the names of analysis tools and VM-related artifacts that the malware tries to check and armor against; URLs and URL formats used for C2 communication; network protocol–based strings; and so forth. When the source code is finally compiled, the generated executable holds these strings. But packing obfuscates these strings, as you learned earlier. Let’s now see how we can identify a packed from an unpacked sample using these strings.
3. __Static Observation of Strings in a File:__ While you are analyzing a malware sample, you can start by loading it in `BinText` or any other such tool that lets you look at its strings.

But you’ve got to be careful. Some strings are common to both packed and unpacked samples, which you should ignore and not consider for figuring out if a sample is packed or unpacked. These are mainly API names, import DLLs, compiler code strings, locales, languages, and so forth.

Let’s now look at Sample-7-2, which is a malware sample. Load this file in BinText so that we can view its strings. If you start scrolling through the strings, you find a lot of human-readable strings that are not junk. 

For example, in Figure 7-10, you see strings like NOTICE, PRIVMSG, DCC SEND, PING, JOIN, #helloThere, which are all related to IRC protocol. If you scroll down further, you find even more strings like USER, NICK, C:marijuana.txt. You also find junk strings, but that is normal since the regular binary code instructions, even though not packed, show up as junk strings. But in packed files, you rarely find meaningful human-readable strings like the ones we saw earlier, which likely indicates that Sample-7-2 is not packed.

 __4- Dynamic Observation of Strings in Memory:__    the unpacking stub loader code runs in the packed sample process at some point in time, which uncompresses the original executable code and data sections into its memory. The uncompressed data in virtual memory contains all the strings which belong to the original payload sample.

Some of the areas and pages in memory you should look for strings are memory areas that are allocated dynamically by the malware for decompression. Under Process Hacker, such pages are shown as private pages with the Commit property and do not belong to any modules. Another area is the one occupied by the main module image.

Test: add .exe extension to sample7-1.packed and run it. See strings in process hacker (memory>string)

![](M2_OS_and_System_fundamentals_file_format154.png)

 __Process Hacker vs Process explorer__ 

One disadvantage with Process Hacker is that it does not have the option to show the strings in the static file like the Image option in Process Explorer. Hence, you must use BinText to view the strings in the static file on the disk, and then use Process Hacker to view the strings in running process’ memory and compare it manually to the static file strings in BinText.

Process Hacker offers is that it lets you choose what kind of pages it should show strings for. Clicking the (Memory>Strings) option lets you choose which type of pages it should show strings from Private, Image, and Mapped. 

 __Identifying Packers__ 

With the packer known, you can blog for tools or techniques about the packer, which might explain how the packer works and how to unpack the sample or better yet help you write an automated unpacker for the sample.

PEiD is a popular tool that can identify packers.

PEiD detects packer based on signature at the first few bytes of the entry point. The signature used by PEiD to identify the packer comes from a signature database located in a file called userdb.txt.

One such userdb.txt signature database file is available at https://handlers.sans.org/jclausing/userdb.txt, which contains signatures not just for UPX but for various other packers.

![](M2_OS_and_System_fundamentals_file_format155.png)

The first bytes are the signature of the packer, here UPX

![](M2_OS_and_System_fundamentals_file_format156.png)

When a packer packs a file, the generated packed file is quite different from the original file, including having different section names.

![](M2_OS_and_System_fundamentals_file_format157.png)

![](M2_OS_and_System_fundamentals_file_format158.png)

Most malware authors out there use their own custom packers to pack their samples. As a result, when you are doing malware analysis, most of the time, you won’t come across any low-hanging fruit when it comes to identifying a packer. Neither are you going to find any resources on the web on how to specifically unpack packed samples.

But there is a solution for almost everything, including unpacking samples packed with custom packers. Chapter 17 discusses some of the undocumented tricks that you can use to unpack and reverse malware, regardless of the packer it is packed with. Debugging is the trick.

One of the most common misconceptions that we have come across is that if a file is packed, it is malware. This is not true. Packing is a technique that is used by both clean software and malware alike for the general requirement of compression and obfuscation.