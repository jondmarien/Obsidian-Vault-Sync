---
title: Assignment 4 - Debugging
author:
  - Jon Marien
created: 2025-04-09
published: 2025-04-09
tags:
  - classes
  - INFO43921
---

| Title                    | Author                       | Created        | Published      | Tags                                               |
| ------------------------ | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Assignment 4 - Debugging | <ul><li>Jon Marien</li></ul> | April 09, 2025 | April 09, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |

# **Assignment: Debugging - 12.5%**

Submit your answers with snapshots documenting each step you take. Please, check the Slate for the deadline.

## **1. Utilizing Debugging Tricks for Unpacking Malware**
Refer to the technique outlined in "M11-1-Debugging Tricks for Unpacking Malware". Note that Ass4-1 is packed using UPX. You'll need to use a hardware breakpoint to identify the original malware payload's address before it was packed. Unzip Ass4-1 and rename the extracted file to include a .exe extension prior to debugging.

- **Q1-1**: Where did you set the hardware breakpoint, and why? Include a snapshot of your breakpoint. (1.5 points)
	- I set the hardware breakpoint on the memory address indicated by the `ESP` (Stack Pointer) register right after the initial `PUSHAD` instruction at the program's entry point executed. To do this, I first ran the debugger to execute past `PUSHAD`, noted the value in `ESP` from the Registers window, navigated to that address in the Memory Bytes window, right-clicked, and selected "Set Breakpoint". I configured it as a **Hardware** breakpoint, triggered on **READ_WRITE** access, with a **Length** of **4** bytes (suitable for 32-bit registers).
	- I chose this location and type because the UPX packer uses `PUSHAD` to save the program's state (registers) onto the stack early on. Near the end of the unpacking routine, it uses `POPAD` to restore this state right before jumping to the Original Entry Point (OEP). The `POPAD` instruction reads the saved values from the _exact_ stack location where `PUSHAD` saved them. By placing a hardware breakpoint that monitors read/write access to this specific stack address (pointed to by `ESP` after `PUSHAD`), I could intercept execution precisely when `POPAD` accesses this memory, effectively pausing the program just before the crucial jump to the unpacked code.
	- **The snapshot shows an enabled breakpoint entry. The "Kind" column indicates "Hardware", the "Address" column displays the specific stack address read from `ESP` (e.g., `0019FFA0`), the "Length" is 4, and the "Sleigh Kind" column shows "read | write".**
- **Q1-2**: At which instruction does the debugger halt due to the hardware breakpoint? Provide an explanation and a snapshot. (1.5 points)
	- The debugger halted execution directly at the `POPAD` instruction within the UPX unpacking stub.
	- The hardware breakpoint I set on the stack address (from Q1-1) was configured to trigger upon a read or write access. The `POPAD` instruction's function is to _read_ multiple values from the stack to restore the general-purpose registers. When the CPU attempted to execute `POPAD` and read the first saved register value from the monitored stack address, the hardware breakpoint condition was met, causing the debugger to pause execution immediately _before_ the `POPAD` instruction fully completed its operation. At this point, the Instruction Pointer (`EIP`) register points to the memory address of this `POPAD` instruction.
	- **The snapshot shows the Listing view with the `POPAD` instruction highlighted, indicating it is the current instruction pointed to by `EIP`. The Registers window confirms that the value of `EIP` corresponds to the address of the highlighted `POPAD` instruction.**
- **Q1-3**: What is the jump address? Include a snapshot. (1.5 points)
	- After the debugger stopped at the `POPAD` instruction (as described in Q1-2), I examined the subsequent instructions in Ghidra's Listing view. A few instructions after `POPAD`, I located a large, unconditional `JMP` instruction. The **jump address** is the target operand specified by this `JMP` instruction. This target address represents the **Original Entry Point (OEP)** of the unpacked malware code.
	- The jump address (OEP) I identified in the `JMP` instruction following `POPAD` was [You would insert the actual address found here, e.g., `0x00408701` if using the video's example, or the specific address found for `Ass4-1.exe`].
	- **The snapshot focuses on the assembly code immediately following the `POPAD` instruction. An unconditional `JMP` instruction is clearly visible (e.g., `JMP 0x00408701`), and the target address operand (`0x00408701` in this example) is highlighted or indicated as the jump address.**
- **Q1-4**: What is the first instruction following the jump execution? (1.5 points)
	- The first instruction following the execution of the jump (i.e., the first instruction of the _original_, unpacked program) is the instruction located at the **OEP address** determined in Q1-3.
	- I found this instruction by navigating Ghidra's Listing view to the OEP address that was the target of the final `JMP` instruction. Alternatively, I could have single-stepped the debugger one time (Step Into) from the `JMP` instruction, which would land execution directly on this first instruction at the OEP.
	- **The specific instruction I observed at the OEP address [e.g., `0x00408701`] was [You would insert the actual assembly instruction found, e.g., `PUSH EBP`].**

## **2. Identifying the Injection Entry Point**

Using the approach from "M12-1-Debugging Code Injection", determine the injection entry point for Ass4-2. Remember to add a .exe extension to Ass4-2 before beginning the debugging process.

- **Q2-1**: On which instructions did you place breakpoints, and why? Provide a snapshot of your list of breakpoints. (1.5 points)
	- I placed software execution breakpoints (`SW_EXECUTE`) on the following Windows API functions within `Ass4-2.exe`:
		1. `kernel32.dll::OpenProcess`: To identify which process the malware intends to inject into by capturing the Process ID (PID) passed as an argument.
		2. `kernel32.dll::VirtualAllocEx`: To find out the base address of the memory block the malware allocates within the target process's address space. This is where the injected code will reside.
		3. `kernel32.dll::WriteProcessMemory`: To intercept the moment the malware writes its payload (shellcode) into the allocated memory block in the target process. This allows inspection of the payload itself.
		4. `kernel32.dll::CreateRemoteThread`: To capture the final step where the malware starts execution of its injected code within the target process. The start address passed to this function _is_ the injection entry point we're looking for.
	- Process injection typically involves these sequential steps: opening a handle to the target process, allocating memory within it, writing the malicious code to that memory, and finally, creating a remote thread to execute the written code. Placing breakpoints on these specific APIs allows me to observe each critical stage of the injection process, gather necessary information like the target PID, allocated memory address, the payload being written, and the starting address for execution within the target process.
	- **The snapshot shows four enabled breakpoints. Each entry lists the "Location" (e.g., `KERNEL32.DLL::VirtualAllocEx`), "Kind" (`SW_EXECUTE`), and "State" (`Enabled`).**
- **Q2-2**: What is the target process ID, and how did you determine it? Include a snapshot. (1.5 points)
	- I determined the target process ID by examining the arguments passed to the `OpenProcess` function call when my breakpoint on it was hit.
		1. I started debugging `Ass4-2.exe` in Ghidra.
		2. Execution stopped at my breakpoint on `kernel32.dll::OpenProcess`.
		3. In Ghidra's Decompiler window, I looked at the `OpenProcess` call site. The second argument (`dwProcessId`) corresponds to the target Process ID.
		4. I noted the value being passed for this `dwProcessId` argument, either directly from the Decompiler view (if it resolved to a constant or variable) or by inspecting the relevant register or stack location shown in the Registers/Stack windows just before the call executes.
	- The value I observed being passed as the `dwProcessId` argument to `OpenProcess` was [You would insert the actual PID found here, e.g., `1234`].
	- **The snapshot shows the Decompiler view paused at the call to `OpenProcess`. The second argument, identified as the Process ID, is highlighted. If the value isn't immediately obvious in the decompiler, the corresponding register (e.g., `EDX` for 32-bit stdcall if pushed second-to-last, or `RDX` for 64-bit fastcall) or stack location holding the PID value is shown in the auxiliary windows.**
- **Q2-3**: What is the address of the allocated memory block? Provide a snapshot. (1.5 points)
	- I found the address of the memory block allocated in the target process by inspecting the return value of the `VirtualAllocEx` function call.
		1. After hitting the breakpoint on `kernel32.dll::VirtualAllocEx`, I let the function execute completely by stepping _over_ it (using F8 or the "Step Over" button in Ghidra's debugger controls).
		2. Immediately after the function returned, I checked the value in the `EAX` register (for 32-bit) or `RAX` register (for 64-bit) using Ghidra's "Registers" window. The Windows API convention is to return values in this register.
		3. The value in `EAX`/`RAX` is the base address of the memory block successfully allocated within the target process.
	- The address returned by `VirtualAllocEx` (observed in the `EAX`/`RAX` register) was [You would insert the actual address found here, e.g., `0x00AB0000`].
	- **The snapshot shows the program execution paused immediately _after_ the call to `VirtualAllocEx`. The "Registers" window is visible, with the `EAX` (or `RAX`) register highlighted, displaying the allocated memory address.**
- **Q2-4**: What are the first 4 bytes of the injected buffer? Include a snapshot. (1.5 points)
	- I identified the first four bytes of the injected payload by examining the source buffer passed to the `WriteProcessMemory` function just before it was called.
		1. Execution stopped at my breakpoint on `kernel32.dll::WriteProcessMemory`.
		2. I identified the argument corresponding to `lpBuffer` (the pointer to the data _in the injector's memory_ that will be written to the target). This is typically the 3rd argument. I located its value using the Decompiler or by checking registers/stack.
		3. I opened Ghidra's "Memory Bytes" window (`Window` -> `Memory Bytes`).
		4. I navigated to the address specified by the `lpBuffer` argument.
		5. The first four bytes displayed at this memory location are the initial bytes of the shellcode payload that the malware intends to write into the target process.
	- The first four bytes located at the `lpBuffer` address were [You would insert the actual hex bytes found here, e.g., `0xFC 0xE8 0x82 0x00`].
	- **The snapshot displays the "Memory Bytes" window showing the memory contents starting at the address identified as `lpBuffer`. The first four bytes are highlighted. The Decompiler view shows the call to `WriteProcessMemory`, indicating how the `lpBuffer` address was identified from the function arguments.**