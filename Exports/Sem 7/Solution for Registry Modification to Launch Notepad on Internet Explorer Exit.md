---
title: Solution for Registry Modification to Launch Notepad on Internet Explorer Exit
author: Jon Marien
created: 2025-03-04
published: 2025-03-04
tags: 
NotionID-OBS-NOTION-DB: 1ac6431b-f9a1-81fa-adc8-f204c8073437
link-OBS-NOTION-DB: https://www.notion.so/Solution-for-Registry-Modification-to-Launch-Notepad-on-Internet-Explorer-Exit-1ac6431bf9a181faadc8f204c8073437
---

**Issue:**
Attempted to modify the Windows registry to launch Notepad.exe when Internet Explorer (iexplore.exe) exits. However, the expected behavior is not occurring, and research indicates that adding registry keys alone may not be sufficient.

**Solution:**
Follow the steps below to troubleshoot and ensure Notepad launches correctly after closing Internet Explorer.
1. Verify the Registry Entries
Ensure the correct registry keys and values are set:
1. Open Registry Editor (regedit):
   - Press **Win + R**, type `regedit`, and press **Enter**.
2. Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\iexplore.exe`
3. Ensure the following values are correctly set:
   - **ReportingMode** (REG_DWORD) = `1`
   - **MonitorProcess** (REG_SZ) = `C:\windows\system32\notepad.exe`
4. Run Commands with Administrator Privileges

If you have not already done so, ensure you execute the commands with administrative privileges:
1. Close any open **Command Prompt** windows.
2. Open **Command Prompt** as Administrator:
   - Click on the **Start Menu**, type `cmd`, right-click on **Command Prompt**, and select **Run as Administrator**.
3. Re-enter the registry commands:
   reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\iexplore.exe" /v ReportingMode /t REG_DWORD /d 1
   reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit\iexplore.exe" /v MonitorProcess /d "C:\windows\system32\notepad.exe"
4. Verify SilentProcessExit Polic

Ensure no policies are preventing Notepad from launching:
1. Navigate to:
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\SilentProcessExit
2. Verify that no additional restrictions are set under this key.
3. Confirm Image File Execution Options Are Not Interfering
If Image File Execution Options have been modified, they might prevent Internet Explorer from executing properly.
1. Navigate to:
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\iexplore.exe
2. If there are any **Debugger** or other unexpected entries, remove them using:
   reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\iexplore.exe" /f
3. Restart your system after making these changes.
4. Test with Process Monitor Tool
If the above steps do not resolve the issue, use **Process Monitor** from Sysinternals to track process execution:
1. Download **Process Monitor** from the official Microsoft Sysinternals website.
2. Run **Process Monitor** as Administrator.
3. Set a filter for `iexplore.exe` and observe if it attempts to execute `notepad.exe`.
4. If Notepad is not executed, check for any blocking policies or security software interference.
5. Restart and Test Again
After verifying and reconfiguring the registry settings:
- **Restart your computer** to apply changes.
- Open and close **Internet Explorer (iexplore.exe)**.
- If properly configured, Notepad should launch automatically.
Final Notes:
If the issue persists, consider:
- Checking for Windows Group Policy restrictions.
- Reviewing **Event Viewer** logs for errors related to `SilentProcessExit`.
- Testing on a different Windows 7 machine to confirm behavior.
Let me know if any further assistance is required.

Mohammed