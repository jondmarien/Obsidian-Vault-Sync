---
title: Debuggers and Disassembly
author:
  - Jon Marien
created: 2025-03-19
published: 2025-03-19
tags:
  - classes
  - INFO43921
---

| Title                     | Author                       | Created        | Published      | Tags                                               |
| ------------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Debuggers and Disassembly | <ul><li>Jon Marien</li></ul> | March 19, 2025 | March 19, 2025 | [[#classes\|#classes]], [[#INFO43921\|#INFO43921]] |
# __Debuggers and Disassembly__

Disassembly is a process of converting the machine code into the more human-readable assembly language format, a lot of which we have seen in the previous section. To disassemble a program, you can use software (also known as disassemblers) that does nothing but disassemble a program (that’s right, it doesn’t debug a program, but only disassembles it). Alternatively, you can also use a debugger for the disassembly process, where a debugger apart from its ability to debug a program can also double up as a disassembler.

A debugger is software that troubleshoots other applications. Debuggers help programmers to execute programs in a controlled manner, not presenting to you the current state of the program, its memory, its register state, and so forth, but also allowing you to modify this state of the program while it is dynamically executing.

There are two types of debuggers based on the code that needs to be debugged: __source-level debuggers and machine-language debuggers__. Source-level debuggers debug programs at a high-level language level and are popularly used by software developers to debug their applications. But unlike programs that have their high-level source code available for reference, we do not have the source code of malware when we debug them. Instead, what we have are compiled binary executables at our disposal. To debug them, we use machine language binary debuggers like __OllyDbg and IDA,__ which is the subject of our discussion here and which is what we mean here on when we refer to debuggers.

These debuggers allow us to debug the machine code by disassembling and presenting to us the machine code in assembly language format and allowing us to step and run through this code in a controlled manner. Using a debugger, we can also change the execution flow of the malware as per our needs.

![](M10-2-Debugging%20Intro1_0.png)

Set OllyDbg to start debugging a new program and stops/breaks at the entry point of the PE file, it is debugging.
You should disable in OllyDbg is the SFX option. You should uncheck all the options in the SFX tab.

![](M10-2-Debugging%20Intro1_1.png)

![](M10-2-Debugging%20Intro1_2.png)

![](M10-2-Debugging%20Intro1_3.png)

## __Disassembly window of OllyDbg__
![](M10-2-Debugging%20Intro1_4.png)

![](M10-2-Debugging%20Intro1_5.png)

![](M10-2-Debugging%20Intro1_6.png)

Do note that Run to Cursor does not work for a location that is not in the execution path. It similarly won’t work for a previously executed instruction that no longer fall in the execution path of the program if it continues execution. For example, for our hello world program Sample-16-1.exe, after you have executed till 0x40109E, you cannot Run to Cursor at 0x40901D; that is, the previous instruction unless you restart the debugger.

__Run__ executes the debugger till it encounters a breakpoint (covered later), or the program exits or an exception is encountered.

__Execute Till Return__ executes all instructions up and until it encounters a RET instruction.

**Execute Till User Code**: You need this feature when you are inside a DLL module and want to get out of the DLL into the user compiled code, which is the main module of the program you are debugging.

You can go/jump to a specified address in the program that is being debugged in OllyDbg using Ctrl+G. The address to which you want to jump into can be either an address in the Disassembly window or the Memory window.

- Breakpoints are features provided by debuggers that allow you to specify pausing/stopping points in the program and allow us to inspect the state of the process at these points.
	- A breakpoint can be used on instructions or memory locations.
- A breakpoint against an instruction tells the debugger to pause/stop/break the execution of the process when control reaches that instruction.
	- You can also place a breakpoint on a memory location/address, which instructs the debugger to pause/stop/break the execution of the process when data (instruction or non-instruction) at that memory location is accessed. Accessed here can be split into either read, written into, or executed operations.

![](M10-2-Debugging%20Intro1_7.png)

## __Software Breakpoints__
Software breakpoints implement the breakpoint without the help of any special hardware but instead relies on modifying the underlying data or the properties of the data on which it wants to apply a breakpoint.

Drawbacks of software breakpoints: implementing software breakpoint functionality  __modifies the value and properties of the instruction or data location __ that it intends to break on. This can open these breakpoints to easy scanning-based detection by malware that checks if any of the underlying data has been modified. This makes for  __easy debugging armoring checks by malware.__

Place a software breakpoint at a instruction by using the F2 key or double-clicking this instruction or right-clicking and selecting Breakpoints ➤ Toggle

## __Hardware Breakpoint__
Hardware breakpoints counter the drawback by using dedicated hardware registers to implement the breakpoint. They don’t modify either the state, value, or properties of the instruction/data that we want to set a breakpoint on.

From a debugger perspective setting a hardware breakpoint compared to a software breakpoint differs in the method/UI used to set the breakpoint; otherwise, you won’t notice any difference internally on how the breakpoint functionality operates.

software breakpoints can be slower than hardware breakpoints.

Drawback: you can only set a limited number of hardware breakpoints because the dedicated hardware registers to implement them are small.

To set a hardware breakpoint on an instruction in the Disassembly window or any raw data in the Data window, you can right-click it select Breakpoint ➤ Hardware, which should open a window like Figure 16-26

![](M10-2-Debugging%20Intro1_8.png)

## __Memory Breakpoint__
You can also set a  __breakpoint on a data at a memory location__ , where the data may or may not be an instruction. These breakpoints are called memory breakpoints , and they instruct the debugger to break the execution of the process when the data that we set a memory breakpoint has been accessed or executed (depending on the options you set for the memory breakpoint).

From a malware reversing perspective, memory breakpoints can be  __useful to pinpoint decryption loops __ that pick up data from an address and write the unpacked/uncompressed data to a location. There are other similarly useful use-cases as well.

## __Undoing Debugger Analysis__
To undo the assembly analysis in OllyDbg you can right on any instruction in the Disassembly window and select Analysis ➤ Remove analysis, where if you select Remove analysis from selection, it only undo the analysis on the instruction on which you right-clicked on the cursor, while Remove analysis from module undoes it for the entire module.

![](M10-2-Debugging%20Intro1_9.png)

## __Identifying The Stack Frame__
Every function has its own block of space on the stack called the stack frame that is used by the function to hold the parameters passed to the function, its local variables. The frame also holds other book-keeping data that allows it to clean itself up after the function has finished execution and returns, and set the various registers to point to the earlier stack frame.

Now a program is usually made up of multiple functions, with functions calling other functions, resulting in huge chains of stack frames stacked on top of each other in the stack. The topmost stack frame in the stack is the one that belongs to the currently executing function in the process. For your understanding, we have taken a simple two function C program seen in Listing 16-15.

![](10-0/images/M10-2-Debugging%20Intro1_10.png)

![](M10-2-Debugging%20Intro1_11.png)

## __Identifying a Function Epilogue__
- Most of the time, at function start, you encounter the following set of instructions that carries out this setup, which is called the function prologue, as seen in Listing 16-16.
- The first instruction saves the current/caller_function’s EBP to the stack. At this instruction location, the EBP still points to the stack frame of this function’s caller function. Pushing the EBP of the caller function, lets this function reset the EBP back to the caller’s EBP, when this function returns and transfers control to its caller.
	- The second instruction sets up the EBP for the current function making it point to the current function’s stack frame.
		- The third instruction allocates space for local variables needed by the current function.

![](M10-2-Debugging%20Intro1_12.png)

__Identifying a Function Prologue__

* when the function has finished execution, and it needs to return control to its caller, it needs to do cleanup, frees the allocated space for the local variables in its stack frame, and reset various pointers. To do this, it uses the set of these three instructions usually, called the function epilogue, as seen in Listing 16-17.
  * The first instruction resets the ESP back to EBP. This address in EBP to which the ESP is assigned points to the address in the stack frame to which the ESP pointed just after the first instruction in the function epilogue, which is the caller function’s EBP.
  * Running the second instruction pops the top of the stack into the EBP, restoring the EBP to point to the caller function’s stack frame.
  * The third instruction pops the saved return address from the stack to the EIP register, so the caller function starts executing from the point after which it had called the current function.

![](M10-2-Debugging%20Intro1_13.png)

__Identifying Local Variables__

![](M10-2-Debugging%20Intro1_14.png)

![](M10-2-Debugging%20Intro1_15.png)

![](M10-2-Debugging%20Intro1_16.png)

![](M10-2-Debugging%20Intro1_17.png)

__Identifying Pointers__

Block 1: These two instructions translate to LOCAL.1 = 1, which in C code maps to a = 1.

Block 2: The instruction loads the address of LOCAL.1 into EAX.

Block 3: This translates to LOCAL.2 = EAX, where EAX contains the address of LOCAL.1.

![](M10-2-Debugging%20Intro1_18.png)

![](M10-2-Debugging%20Intro1_19.png)

__Identifying Global variables__

- OllyDbg names all local variables using the LOCAL. naming scheme. But it didn’t name DS:[402000] with a LOCAL. prefix naming scheme, which means it is not a local variable.

- local variables are located on the stack, which means DS:[402000] isn’t located on the stack. Anything that is not on the stack is global.

![](M10-2-Debugging%20Intro1_20.png)

![](M10-2-Debugging%20Intro1_21.png)

__Identifying Array on Stack__

![](M10-2-Debugging%20Intro1_22.png)

![](M10-2-Debugging%20Intro1_23.png)

![](M10-2-Debugging%20Intro1_24.png)

__Identifying Branch Conditions__

![](M10-2-Debugging%20Intro1_25.png)

![](M10-2-Debugging%20Intro1_26.png)

__Identifying Loops__

![](M10-2-Debugging%20Intro1_27.png)

![](M10-2-Debugging%20Intro1_28.png)