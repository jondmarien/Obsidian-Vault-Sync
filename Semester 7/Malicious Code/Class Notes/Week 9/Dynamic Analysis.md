---
title: Dynamic Analysis
author:
  - Jon Marien
created: 2025-03-12
published: 2025-03-12
tags:
  - classes
  - INFO43921
---

| Title            | Author                       | Created        | Published      | Tags                                               |
| ---------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Dynamic Analysis | <ul><li>Jon Marien</li></ul> | March 12, 2025 | March 12, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |

# Chapter 13
Dynamic analysis involves executing a sample using the aid of various tools and recording not only the behavior but also observing the various artifacts generated by the executed malware. Combined, it can help us analyze and make conclusions about the sample more accurately.

## **Keep Your Base Snapshot Handy**
You learned that we need a base snapshot of our analysis VM with all the system tweaks setup and the analysis tools installed. Every new sample that we obtain should start the analysis from the base snapshot. When analyzing a sample, you might have to re-run the sample and re-analyzed it again and again. Some of these re-runs you might want to start from scratch by going back to the base snapshot. The reasons why using the pristine state of a base snapshot is important are,
	During the execution of the sample, the sample might make some changes to the system, dropping some hints for itself in case it is re-run later. If you re-run the same sample later again in the same environment without resetting your VM, the malware might start up, check for the existence of hints that indicate that it has already run in that environment, and if so, behave differently or exit. Some hints/artifacts from malware are registry entries, config files, or dummy files on the disk, mutexes, and so forth

Sometimes malware you analyzed earlier in the analysis VM might still be running even though you think you killed it. When you re-run the sample, it might clash with the existing process, or it might check for the hints/artifacts it left inside the analysis VM, so it now behaves differently or exits. As a result, you may not get the malware’s true behavior and events.
	If you reuse a VM environment that you used to analyze a different sample, then there might be artifacts and events from that earlier malware that you might mix up and confuse as those generated and belonging to any new malware you analyze. Resting the VM ensures that you have a clean environment to analyze a new sample, with no stray events and artifacts from any older analyzed sample that you could get confused with.

## **First Run: A Bird’s-Eye View**
The best first step in the analysis process is to casually run the sample and notice at a very high level its behavior. This is important for two reasons.

- A lot of samples, like ransomware, have very public or explicit behavior. Running the sample and observing the effects that the malware had on the system, and the files on disk might be enough to conclude that the sample is malware and figure out the type and intent of the malware.
- Casually observing the behavior of the malware under execution, helps us set a tone, and our expectations, and prepare ourselves for the next set of tools needed to continue with its analysis in depth.

We might have to repeat this process and casually re-run the same sample multiple times, since a single execution may not help us observe enough about its behavior. Every time we casually re-run the sample, it is highly recommended that we reset the VM to the pristine base snapshot. While we carry out this process, we also want to take the aid of a few simple tools like Process Hacker and the file browser, that help us observe the sample’s behavior passively.

## **Whoa! The Sample Refuses to Run!**
Not every malware sample you obtain might run when you try to execute it for the first time. Some of the reasons for this can be,
	Sometimes the samples might need a certain environment or a certain SDK/framework installed, which might be missing in your analysis VM. For example, the sample you are analyzing might be a .NET sample that requires a particular version of the .NET Framework, which may not be installed on your system. Or the sample might be Java malware that requires the Java Runtime Engine (JRE), which is not installed on the system.
		The malware might have certain dependencies on DLLs and config files that it needs to run, which might be missing from your analysis VM.

A lot of these dependencies, frameworks, environments needed by a sample to run can be figured out from the  **static**   **analysis**  phase. Once we figure out these missing dependencies and install and set them up, the sample runs as expected.

Keep in mind is that when PE Executable samples fail to run, the easiest way to figure out the issue is to run the sample using a  **debugger**  like `OllyDbg`. Using a debugger helps you figure out the issue very quickly and efficiently, saving your precious time. You don’t have to be a super reverse engineer to use OllyDbg or any other debugger.

## **Run as Administrator or Not**
By default, if you double-click any sample on the system, it runs as a non-administrator, with fewer privileges, functionalities, features available for the running process. Some malware requires administrator privileges to perform certain operations that require special privileges. For example, if malware wants to copy a file into the protected OS system folder C:\Windows\System32, it needs administrator privileges.

While running any malware sample, you want to test it by running both with and without administrator privileges. Start by running it without administrator privileges, which is easy to do, since all you need to do is double click.

Reset your VM and run the sample as an administrator, which you can by right-clicking the sample and selecting Run as an Administrator.

Each of the scenarios might provide different sets of events and behaviors for the running malware process, which you may not see with the other, and the difference might be crucial in your figuring out if the sample is malicious or not.

Let’s now play with Sample-13-3, to which you can add the .exe file extension. In the samples repository, it is named Sample-13-3.txt because it is a text file that holds the instructions that you need to follow to download the real malware sample. Start Process Hacker and open the folder that holds the sample file, which should look similar to the left side of Figure 13-5. Notice that we have some dummy PDF (.pdf) and Excel (.xlsx) files in that folder. This is part of the process where we want our analysis VM setup to look and mimic a regular victim’s machine, also explained in Chapter 2.

![](images/M8-2-Dynamic%20Analysis_0.png)

![](images/M8-2-Dynamic%20Analysis_1.png)

Now that you have that in place, run the sample. What do you see? From the right side of Figure 13-5, we see that suddenly all the files have been modified and a .doc file extension added to them. We also see a new file created in the same folder called Read**_ME.html. Both indicators point to the Sample-13-3 being ransomware.

The newly created Read**_ME.html is an HTML file. Opening it confirms that we have ransomware, as seen in Figure 13-6.

Let’s now play with Sample-13-2, to which you can add the .exe file extension. In the samples repo, it is named Sample-13-2.txt because it is a text file that holds instructions that you need to download the real malware sample. Don’t run the sample yet. Start Process Hacker and open the folder that holds the sample file, which should look similar to the left side of Figure 13-2.

Now that you have that in place, run the sample as an administrator by right-clicking it and selecting Run as an Administrator. A new process called SVOHOST.EXE pops up, as seen on the right side of Figure 13-3. Sample-13-2.exe is deleted from the disk.

Both symptoms are suspicious. The name of the new process SVOHOST.EXE is suspiciously similar to the OS process svchost.exe, which is like the psycholinguistic technique, a stealth technique explained in Chapter 11. The deletion of the executable file on the disk is also a classic technique used by a lot of malware, which we explain later in the chapter.

Now let’s check the properties and see if we notice anything. In the properties seen in Figure 13-4, we notice that the executable file from which the new process SVOHOST.EXE is created is located at C:\Windows\System32\SVOHOST.EXE. You can go back to a pristine system, or use your own experience, but there is no system program located in C:\Windows\System32 that is called SVOHOST.EXE.

![](images/M8-2-Dynamic%20Analysis_2.png)

![](images/M8-2-Dynamic%20Analysis_3.png)

## **ProcMon: Behavior Events Analysis**
Let’s analyze Sample-13-2 in the context of ProcMon. Make sure to add the .exe file extension to this sample.

1. Start Process Hacker so that you have an eye on the process(es) that are started when you run your sample.
2. Start ProcMon and hit Ctrl+E to stop capturing events. By default, ProcMon captures all events on the system, and sometimes you have too many events.
3. Hit Ctrl+X so that you can clear the existing events displayed by it.
4. Hit Ctrl+E so that you can start the capture of events.
5. Run Sample-13-2.exe, while making sure via Process Hacker that it is running or at least it has created other child processes.
6. Let the sample run for a while, and then hit Ctrl+E in ProcMon. You don’t want to run it too long, however; otherwise, you are inundated with too many events to analyze.

Let’s go through the events and see if we can notice any malicious events/indicators from events related directly or indirectly to our sample process. Note that you want to look for events from the main malware process, Sample-13-2.exe, and from all the child processes created by this sample process and from other processes that our sample or its children possibly code inject into. You can filter events first to start with only Sample-13-2.exe.

In Figure 13-18, Sample-13-2.exe creates a file called SVOHOST.EXE in C:\Windows\System32\ and writes into it using the contents from Sample-13-2.exe. How do we know that the contents of Sample-13-2.exe are being copied over into this new file C:\Windows\System32\SVOHOST.exe? Because we can see a ReadFile event for Sample-13-2.exe file and then a WriteFile for SVOHOST.exe file.

![](images/M8-2-Dynamic%20Analysis_4.png)

## **Malicious Events**
**All the events so far indicate maliciousness:**
1.	Creating a new file called SVOHOST.EXE, which is named very similar to the system program svchost.exe, which from our experience indicates the psycholinguistic technique
2.	Creating a new file from step 1 in the protected system folder C:\Windows\System32. Third-party applications don’t make modifications to any content in the OS system folder.
3.	Copying and pasting its contents into this new file, which is a commonly used malware technique, where malware copy themselves into a new file in another folder on the system so that they can run as a new process from this new file located in this new folder.

Let’s search for any registry events and see if the sample creates some Run entries for persistence. In Figure 13-19, it creates a new persistence entry in the registry by registering a new Run key, `SoundMam`, at `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\SoundMam`, whose value is the path to newly created malware file `C:\Windows\Systeme32\SVOHOST.EXE`. This is another perfect indicator of maliciousness in combination with the events we saw earlier.

![](images/M8-2-Dynamic%20Analysis_5.png)

Since the malware sample creates a RUN persistence entry, let’s verify with the AutoRuns tool if this persistence RUN entry still exists. As you can see in Figure 13-20, it does pick it up—double confirmation. Yay!

![](images/M8-2-Dynamic%20Analysis_6.png)

Continuing with our analysis process, now let’s search for some process events. Figure 13-21 shows that Sample-13-2.exe creates a new process for the file it created earlier, `C:\Windows\System32\SVOHOST.EXE`.

![](images/M8-2-Dynamic%20Analysis_7.png)

The following is the full chain of malicious events for `Sample-13-2.exe`:
1.	Creates a new file `C:\Windows\System32\SVOHOST.exe` in the system folder, using a file name similar to the system program `svchost.exe`.
2.	Copies itself into this new file from step 1, `SVOHOST.exe`.
3.	Creates a persistence RUN entry in the registry for this new file from step 1.
4.	Starts a new process out of this new file from step 1, `SVOHOST.exe`.

## **Detecting Code Injection**
Code injection is caught using various techniques. One method detects the use of certain Win32 APIs. We listed the various APIs used by different code injection techniques in Chapter 10. Keeping these APIs in mind, and by using a tool like APIMiner, you can easily detect code injection.

Similarly, we can also detect code injection by using ProcMon. Certain code injection techniques involve creating a remote thread in another process, which pops up as an event in ProcMon. Usually, remote thread injection doesn’t always mean it is malware, since even clean software like debuggers can create a remote thread in another process. But if seen, you can treat it as suspicious and possibly code injection in progress and investigate it further. On seeing such an event, you should investigate both the process that created the remote thread and the remote process in which the new thread was created. Another effective method to detect certain code injection techniques is by searching for page properties where injected code pages most often have RWX permission and are private pages. Also, a good means of analysis at this point is to inspect the strings in the remote process memory searching for any malicious memory artifacts.

## **GMER and Ring3 API Hook Scanner**

At this stage, let’s assume you have figured that the malware sample carries out code injection. Not every code injection technique indicates that the malware intends to do API hooking or is trying to use rootkit functionality. But it is a high possibility at this point that one of the intentions of the malware might be API hooking or rootkits. At this stage, it is best to run tools like GMER and Ring3 API Hook Scanner, both of which can easily tell you if any APIs have been hooked and if a rootkit has been detected. For more on this, you can refer to Chapter 10 and Chapter 11 for rootkits.

## **Yara on Live Processes**

In Chapter 12, we explored how you can write YARA rules and run them on files on disk. You can also use the YARA tool. Run it with YARA rules against live running processes, which then use the process’s memory as a buffer to run the rules against. Try the YARA exercises in Chapter 12, but run the exercise samples against the live process by using the command line yara32.exe <yara_rules_file_path> <PID_OF_PROCESS>. The third parameter (<PID_OF_PROCESS>) is the PID of the process whose memory you want to scan with the YARA rules.

## **Other Malicious Behavior**

Throughout Part 3 of this book, hands-on exercises demonstrated the various features and behaviors displayed by malware. We used various tools, both static and dynamic, for detecting malware features and events and not only concluded that a sample was malware but also determined its intent.

In this section, we rehash some of these notable malware features and how to identify them. To catch these malware features, we need static and dynamic analysis tools. It is important to know how to use these tools and all the malware features and events. Please refer to prior chapters when asked and play with the hands-on exercises. The more these concepts are ingrained in your mind, the more they become second-nature.

### **1-Stealing System File Names for Stealth**

We covered stealing system file names for stealth in Chapter 11. In this technique, the malware uses the names of various OS system programs to name their malware files and processes in a bid to fool users into thinking they are clean OS programs and processes.

This mechanism of the malware can easily be noted by casually observing its behavior, the path of the process’s program file on disk, and other process properties by using tools like Process Hacker and Process Explorer.

### **2-Weird File and Process Names**

We covered weird file names and process names in Chapter 11. With these techniques, malware uses enticing and misleading names to fool the user into clicking its files or ignoring process names in Task Manager.

This mechanism of the malware can easily be noted—first, by a good dose of common sense, and second, by having good knowledge of what normal programs and processes are named on your clean system. If you know how most OS system programs and processes are actually named, this will help you catch anomalous files and process names that look similar to the real ones.

ProcMon, APIMiner, Process Hacker, and casual observing file and process properties using a file browser are easy ways to obtain malware-event information, on top of which you can apply your common sense to catch anomalous behavior.

### **3-Disappearing Executable**

A very common mechanism used by most malware is to copy itself to another location and then delete its program file on disk. You saw an example of this in Figure 13-3.

This malware technique easily pops up in the file browser if you casually observe its behavior when you run it. Similarly, ProcMon catches the event when the file is deleted. APIMiner catches the same events through CopyFile() and DeleteFile()Win32 API calls.

### **4-Number of Process Instances**

Malware has a habit of using OS program/process names for its programs/processes. But we can catch this malware technique by exploiting the fact that there are only a certain fixed number of OS system processes that run at an instance of time. We see more processes than the fixed number for that OS system process name, and we can conclude we have something malicious going on.

We talked about this in Chapter 5. This technique can be easily caught by a tool like Process Hacker by casually observing the name of every process created when you run your analysis sample. If the newly created processes have a system program/process name, manually counting the number of instances with that process name.

### **5-Process Session IDs**

Malware often names its programs/processes after OS system programs/processes. But most OS system programs run under session 0.

We can easily catch this malware behavior using Process Hacker by casually observing the name of every process created when you run your analysis sample. If it has a system program/process name, and verify if its session ID is 0 or not.