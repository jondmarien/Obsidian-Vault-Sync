**Return to Libc Attacks**
![[Pasted image 20240129131145.png]]

- With the ability to execute shellcode on the stack, an attacker can try to call one of the dynamically loaded libc functions
- As before, a stack is "smashed" by overfilling a buffer and the return address is replaced with a crafted memory address
	- The new crafted memory address will  be the address of the libc function to execute

**Getting Addresses**
- Assuming ASLR is off, you can determine the address of a C function at runtime with GDB, and print the function address
	- ![[Pasted image 20240129132325.png]]


