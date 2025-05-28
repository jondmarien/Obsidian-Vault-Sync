---
title: Persistence Mechanisms
author:
  - Jon Marien
created: 2025-01-29
published: 2025-01-29
tags:
  - classes
  - INFO43921
---

| Title                  | Author                       | Created          | Published        | Tags                   |
| ---------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Persistence Mechanisms | <ul><li>Jon Marien</li></ul> | January 29, 2025 | January 29, 2025 | [[#classes\|#classes]] |
# Chapter 8 
## __Persistence Mechanisms__ 
Malware has different purposes. Banking malware needs to stay in the system and monitor browser activities. A keylogger needs to stay in the system to monitor keystrokes. Ransomware encrypts files on the disk. All the various goals of malware cannot be achieved instantly in a minute, maybe not even in days. In the case of APTs (advanced persistent threats), the malware might need months, if not years, to carry out their desired goals. To run for long periods of time, malware needs to make sure that it persists across system reboots, multiple user logins, system shutdowns, and so forth. 

## __Resources Used for Persistence__ 
All operating systems, including Windows, have provisions to start certain processes automatically when the system boots up or when the user logs in.

Linux has init files as one such mechanism, while Windows has various other mechanisms, such as registry keys, startup folders, services, and so forth, also known as autostart extensibility points (ASEP).

## __Persistence example__ 
The persistence mechanism used by malware also depends on the type and the purpose of the malware. 

Malware that tries to steal data from your browser needs to be coded as a browser module, which is loaded as a plugin when the browser starts. Persistence, in this case, requires the malware to register itself as a browser plugin. 

Alternatively, if it is a binary executable, it can make an entry in one of the run registry keys or place the executable in one of the startup folders.

__Autoruns__   and   __ProcMon__   , which are very useful in detecting persistence mechanisms as we dynamically analyze malware samples.
### Autoruns
**Autoruns** is a tool that scans the system and lists all the programs and services making use of any kind of autostart persistence mechanism. 

Autoruns has multiple tabs at the top that segregates and lists the software and services based on the type of persistence mechanism that is being used. For example, the Logon tab lists the software that persists/autostarts when a user logs into the system. The Services tab lists all the services that are registered on the system. Do note that Autoruns hides entries for software that belong to Microsoft/Windows by default. To view all entries, including signed Microsoft software, you can go to Options and deselect Hide Windows Entries. 

![](M4-2-Persistence%20Mechanisms_0.png)

## ProcMon
* ProcMon, the following are some of the important events related to malware analysis that you can capture.
  * Process creation and shutdown
  * Thread creation and shutdown
  * File creation and deletions
  * Registry entry creations, deletions, and modifications
  * Network activity
* ProcMon also provides advanced filters that let you filter and only view events matching specific type, PID, TID, and other meta-information related to the event. 

![](M4-2-Persistence%20Mechanisms_1.png)

While analyzing malware samples with ProcMon, you can stop the capture of events and clear the events. But just before you execute the malware sample, you can start the capture of events. Once the sample has run, you can stop the capture of events; otherwise, you’d have far too many events, and the ProcMon UI can lag when dealing with a deluge of events.

### __Startup Shell Directories__ 

* Windows provides certain startup directories to autostart applications on the system. Malware usually copies its files into these folders so that the OS automatically starts the malware on bootup. 
  * C:\ProgramData\Microsoft\Windows\StartMenu\Programs\StartUp
  * C:\Users\Username\AppData\Roaming\Microsoft\Windows\StartMenu\Programs\Startup
* The same shell directory path on the system can also be obtained from the Windows registry from a value called Startup under the following keys.
  * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders
  * HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders
  * HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders 
  * HKLM\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders

![](M4-2-Persistence%20Mechanisms_2.png)

* These same startup folders can be easily accessed using shortcut commands in the RUN window provided by Windows OS. To open the RUN window, you can press the Win+R keys simultaneously on your keyboard. Once the window is open, you can access the two folders 
  * `shell:common`startup
  - ` shell:startup`
* Exercise:
  * Download sample-8-1, change extension to .exe
  * Open run: win+R
  * Type shell:common startup to open startup directory
  * Copy sample-8-1.exe to the folder and restart
  * Sample-8-1.exe will be executed at start up
  * verify if Autoruns detects the presence of this program in any of the autostart mechanisms.

1. Reset the VM to your baseline clean snapshot.
2.  Start ProcMon.
3. Stop Capture of Events using CTRL+E.
4. Clear any existing events using CTRL+X.
5. Start Capture of Events using CTRL+E.
6. Repeat the steps from earlier in the section by opening the startup folder using `shell:common` startup. Copy Sample-8-1.exe into the startup folder.
7. Stop Capture of Events using CTRL+E.

![](M4-2-Persistence%20Mechanisms_3.png)

The Windows Registry is a database of configurations and settings, many of which are used by the OS for system setup during bootup. The Windows OS also provides registry keys, also called RUN entries that can autostart programs on system startup. Clean software creates these RUN entries so that they are autostarted when the system starts up, a good example being antivirus software. Malware similarly creates RUN entries so they can persist across system boots, and the system autostarts them when it boots up. The RUN entry is the technique more commonly used by malware to persist on the system.

* There are many RUN entry keys in the registry. The following lists most of them. 
  * HKLM\Software\Microsoft\Windows\CurrentVersion\Run
  * HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
  * HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnceEx
  * HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\ExplorerRun

create a RUN autostart entry for Sample-8-1.exe at HKLMSoftwareMicrosoftWindowsCurrentVersionRun by adding a new value of type String Value. Now restart the system and login back into the system. Notice that Sample-8-1.exe has been automatically launched as a process.

![](M4-2-Persistence%20Mechanisms_4.png)

![](M4-2-Persistence%20Mechanisms_5.png)

1. Reset the VM to your baseline clean snapshot.
2. Start ProcMon.
3. Stop Capture of Events using CTRL+E.
4. Clear any existing events using CTRL+X.
5. Start Capture of Events using CTRL+E.
6. Repeat the steps from earlier in the section by creating a RUN entry for Sample-8-1.exe.
7. Stop Capture of Events using CTRL+E.

![](M4-2-Persistence%20Mechanisms_6.png)

Windows services is a widely used technique by malware. One of the top advantages that malware gains by registering as a service is the autostart mechanism it provides. Windows services can be registered to automatically be started by the OS on system startup.

It also provides resilience against crashes by restarting the service if it exits or crashes, which is a bonus.

re-run the exercise from the “Malware as Windows Services” section in Chapter 5 using Sample-5-1.

![](M4-2-Persistence%20Mechanisms_7.png)

![](M4-2-Persistence%20Mechanisms_8.png)

1. Reset the VM to your baseline clean snapshot.
2. Start ProcMon.
3. Stop Capture of Events using CTRL+E.
4. Clear any existing events using CTRL+X.
5. Start Capture of Events using CTRL+E.
6. Repeat the steps from earlier in the section, by creating and running the service.
7.  Stop Capture of Events using CTRL+E.

![](M4-2-Persistence%20Mechanisms_9.png)

You only want to filter Process Activity. So you can deselect the other buttons while enabling the Show Process Activity button. As seen in Figure 8-16, you can scroll through the events to find an event that shows a new process sc.exe created, which was the command we used earlier to register our BookService service. Double-clicking this event shows you the full command line used for registering our service

![](M4-2-Persistence%20Mechanisms_10.png)

Executable files can be used as persistence mechanisms using a technique called file infection . The malware that uses this technique is also called a file infector or a virus. Viruses infect healthy files on the system and alter the code of the host executable by adding their malicious code into the file. When the infected host executable file starts as a process, it automatically starts the malware or malicious code that is now inserted within it. When a virus infection strikes, it infects every executable on the system.

Identifying this technique is easily done with dynamic analysis. To detect if malware is using this technique, one can check if the sample is making any modifications to executable files on the system. A stronger indicator is if the target files which the sample is modifying are system files located in the system32 folder, since these files shouldn’t be altered by nonsystem processes. `ProcMon` is the ideal tool for this detection task because it shows you all the file-related activity, including modifications to any file on the disk.

The file infection technique can also be considered as a propagation mechanism.
## DLL Hijacking

* Executable files depend on DLL files to function. This includes a dependency on the system-provided DLLs and third-party DLLs. Most executable on Windows needs some well-known system provided DLLs to execute like msvcrt.dll, advap32.dll, and so forth. When an executable has a dependency on any DLL, the Windows loader needs to find and load them into the process’s memory as it is staring the process. But how does the Windows loader know where on the disk these DLLs are located? It gets the information via a fixed order of search paths on the hard disk. The following lists the order of the directories it searches.

1. The directory containing the executable file which is launched as the process
2. C:\windows\system32
3. C:\windows\system
4. C:\windows
5. The current working directory (usually the same as step 1 but can be different)
6. Directories in the PATH environment variable

Malware is known to misuse this feature of the Windows loader to run using a method known as DLL hijacking, also known as DLL search order hijacking. The malware places a malicious DLL file in a search order directory where the actual clean DLL is located. 

For example, consider a case where Adobe Acrobat PDF Reader has a dependency on advapi32.dll, which is a system DLL located in C:windowssystem32. To persist, the malware DLL can rename a malicious payload of it as advapi32.dll and place it in the same folder as the Adobe Acrobat PDF Reader executable file. Now since the directory of the executable file is searched first before the system32 folder, the Windows loader loads the malicious advapi32.dll instead of the clean one located in the system32 folder, thereby loading the malware DLL into the clean process.

The Winlogon.exe process is responsible for taking care of the user logging in to the system. It is responsible for starting processes that the user needs after logon. These programs that are started by WinLogon are placed under the registry key   __HKLM\Software\Microsoft\Windows\NTCurrentVersion\Winlogon__   . The names under this KEY that hold the programs that WinLogon starts are   __Userinit__   ,   __Shell.__ 

The Shell entry holds the value of Explorer.exe by default. It is the Windows File Explorer that we fondly use to browse the folders and files on our system. Malware can modify the value of this entry to add malicious executables of its own that that starts on system startup.

The Userinit value similarly can be modified by malware by adding the path to their malicious executables, that is autostarted on system startup. The paths to the programs in this value should be comma-separated with a trailing comma at the end of the value.

Similar to the cron jobs facility in Linux, the Windows Task Scheduler is a feature provided by Windows OS that allows one to schedule the launch of programs and software at fixed times or fixed intervals. Many malware, including the notorious Shamoon malware family, are known to use this mechanism to persist on the system by scheduling tasks that run them.

As an exercise, let’s create a scheduled task that launches the calculator application, using the command.

`SchTasks /Create /SC minute /TN "test" /TR "C:\windows\system32\calc.exe" /ST   22:15 `

While analyzing samples, we can detect malware that uses this technique very similar to how we did for services, by using a combination of ProcMon and Autoruns. Using ProcMon, you should be able to catch a Process Event by the process SchTasks along with the command line from the command you ran

![](M4-2-Persistence%20Mechanisms_11.png)

{Search for calc in ProcMon}

![](M4-2-Persistence%20Mechanisms_12.png)

* To facilitate software developers to debug applications, Microsoft provides various options in the registry that allows one to open an application under the control of a debugger. some of these options made available by Microsoft are:
  * Image File Execution Option (IFEO)
  * SilentProcessExit

## __Image File Execution Option (IFEO)__ 

IFEO is a popular debugging facility made available on Windows as a key at   __HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\Image file execution options__   . To use this facility, you need to add a value to the application key they want to debug at the registry key location.

Exercise: open the registry key location. In most cases, you should have a subkey called iexplore.exe at the key. If not, you can create a new subkey called iexplore.exe. Now let’s create a string value for the iexplore.exe key located under Image File Execution Options. You can do this by right-clicking the iexplore.exe key ➤ New ➤ String Value. Then set a new name-value, where the name is Debugger, and its value is C:windowssystem32calc.exe, which is the Calculator application. You can now verify this by opening Internet Explorer, which would end up starting the Calculator(calc.exe) program instead, as we specified in the registry.

![](M4-2-Persistence%20Mechanisms_13.png)

## __SilentProcessExit__ 

we can have Windows launch programs when other processes exit.

One option is SilentProcessExit, which uses registry key entries at both   __HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\SilentProcessExit__   and   __HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\Image file execution options__   to achieve this.

As an exercise, you can set Notepad.exe application to be launched when Internet Explorer (iexplore.exe) exits. To do this, we need to set registry values for both keys. Instead of using the graphical editor, we can set the same values using the reg command from the command prompt. Run the three commands in Listing 8-4. Alternatively, if you are comfortable with the registry editor, you can manually set these values.

Listing 8-4Setting Registry Values That Autostarts Notepad When Internet Explorer Exits:

`reg add "HKLM\SOFTWARE\Microsoft\Windows NTCurrentVersion\Image File Execution Options\iexplore.exe" /v GlobalFlag /t REG_DWORD /d 512`

`reg add "HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\SilentProcessExit\iexplore.exe" /v ReportingMode /t REG_DWORD /d 1`

`reg add "HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\SilentProcessExit\iexplore.exe" /v MonitorProcess /d "C:\windows\system32\notepad.exe"`

* In addition to IFEO, there are other options to set debuggers. The following lists some of them.
  * HKLM\SOFTWARE\Microsoft\\.NETFramework\Dbg\Managed\Debugger
  * HKLM\SOFTWARE\Microsoft\Windows\NTCurrentVersion\AeDebug\Debugger

