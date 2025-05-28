**Process Memory Organization**
![[Pasted image 20240122131027.png]]
- *Prolog pushes to the stack*
- *Epilog pops off the stack*

- Stack={bottom of the stack: 0xFFF, top of the stack: 0x000}
- Stack={BP (base pointer), local main variable, SP (top of stack), IP (instruction pointer), BP (base pointer), then run whatever is in the code (function, etc)}

**Modifying the Execution Flow**
![[Pasted image 20240122151716.png]]
- *Step 1* 
	- ![[Pasted image 20240122151742.png]]
- *Step 2*
	- ![[Pasted image 20240122151757.png]]
- *Step 3*
	- ![[Pasted image 20240122151810.png]]
- *Step 4*
	- ![[Pasted image 20240122151819.png]]


**Exploiting Overflows (Smashing the Stack)**
- Modify the flow of execution by spawning a shell and issuing commands from it
	- ![[Pasted image 20240122151938.png]]
	- ![[Pasted image 20240122151952.png]]

- If there is no code to spawn a shell, then place the code in the buffer we are overflowing, and set the return address to point back to the buffer:
	- ![[Pasted image 20240122152046.png]]
	- ![[Pasted image 20240122152054.png]]


**Spawning a Shell**

**Testing the Shellcode**

**How to find the Shellcode**
