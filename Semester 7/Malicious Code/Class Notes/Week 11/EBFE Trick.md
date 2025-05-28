 ## __The EBFE Trick__

In the examples shown earlier, we stopped debugging in the injector process at the `CreateRemoteThread` API in `Sample-18-1.exe` and at `ResumeThread` in `Sample-18-2.exe`, after which we attached a new instance of the debugger to the target process. 

Sometimes it can happen that the debugger is not able to attach to the target process mostly for cases where the target process is in a suspended state. How do we get around this problem where we can’t attach to the target process, but we need to still attach to it somehow and debug it using the debugger?

Let’s explore a technique called the `EBFE` technique that can help us to take control of the situation. The technique patches bytes in memory of the target process by using a tool like Process Hacker. We can patch the bytes at the calculated IEP to the hex machine code value `EBFE`. You will soon see the meaning of these bytes and how they are useful in debugging the target process and its injected code.

To explore the technique, let’s use `Sample-18-1.exe` and debug it up to the instruction that CALLs `CreateRemoteThread` API. It is after this point where we had earlier attached the target process to a new instance of OllyDbg debugger in our earlier analysis.

But let’s assume that OllyDbg cannot attach to the target process at this point. We now turn to Process Hacker for help. We can use the same technique to view the memory contents of injected code in Process Hacker as we did earlier in Figure 18-6. Make a note of the first two instruction bytes at the IEP address `0x340000`, which is `FC 33` in this case and replace it with the bytes EB FE, as shown in Figure 18-22.

![](M12-2-EBFE%20trick_0.png)

After editing these instruction code bytes in the process, we need to press the Write button that writes the edited contents back to the process’s memory.

Now come back to the OllyDbg/debugger instance for the injector process, and you can continue debugging it and execute/run over the CALL instruction to `CreateRemoteThread` API or even run/execute the complete injector process. If the injector process has a handle to the target process, it releases the handle. If the target process was earlier in a suspended state like in Sample-18-2.exe, it is now an active process.

Now let’s spawn a new instance of OllyDbg and attach it to the target process. Since we have completely executed the code in the injector process, we can expect that the injected code is now executing in the target process’s thread. In OllyDbg that we have now opened for the target process, let’s see the threads in the target process by using a key combination of Alt+T. As seen in Figure 18-23, a thread that shows its Entry value of `0x340000` which is the location of the injected code and was the argument to the `CreateRemoteThread` API in the injector process.

![](M12-2-EBFE%20trick_1.png)

You can double-click this entry to take you to the code in the disassembler window, as seen in Figure 18-24.

![](M12-2-EBFE%20trick_2.png)

If you look at the bytes of the first instruction, it is `EBFE`, which is the one we inserted and patched earlier. You see these instruction bytes `EBFE` in assembly means `JMP 0x340000`, which is its own address, or in other words, `JMP <to_itself>`. The jump instruction is a loop to itself and continues executing itself without moving forward to the next instruction. If this instruction was not there, the complete injected code would have been executed from the IEP, and we could not have got a chance to debug the injected code in the target process from the IEP. But since the first instruction `EBFE`, which we patched at the IEP, is busy looping over itself, we get a chance to attach to the target process and still debug from the IEP. Now we can patch the original bytes FC 33 in place of EB FE and then continue executing step by step from here.

