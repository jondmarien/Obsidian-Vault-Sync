---
title: Assignment 1
author: Jon Marien
created: 2025-01-20
tags: ---

---

**Question 1: Finding Strings in `assignment1.exe`**
- *Press `ALT + R` to get the search for referenced strings window*![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240119172649.png]]

**Question 2: Setting a Breakpoint**
- *Setting the breakpoint* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240119174417.png]]
- *Entering my name* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240119174049.png]]

**Question 3: Reaching the Function Call** 
- *The entire function call* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120143415.png]]
- *The Prolog* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120143506.png]]
- *The Epilog* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120143439.png]]

**Question 4: Modifying The Condition**
- *The Jump To Modify* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120144410.png]]
	- *Current Behaviour*
		- The program checks if the user's input contains the word "password" using the `str` function
		- If "password" is **not** found, it jumps to a specific point (assignme.0040154A), which skips a function execution
- *Conditional Jump with Modification* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120144749.png]]
	- *Modification*
		- To ensure the function always executes, regardless of the presence of "password":
			- Change the conditional jump instruction from `jnz` (jump if not zero) to `je` (jump if equal)
			- This creates an unconditional jump, always executing the function

**Question 6: Snapshot of the Stack**
- *Stack During Execution* ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120151358.png]]
	- The stack shows many procedures being called by system and a few by user. Below is another example of the stack ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120153449.png]]

**Question 7: Showing the secret**
- *With my name*
	- ![[Semester 6/Software Dev/Assigments/Pics/Secret Name.png]]
- *With `password`* 
	- ![[Semester 6/Software Dev/Assigments/Pics/Secret Password.png]]

**Question 8: Finding Syscalls**
- *stdcall*
	- ![[Semester 6/Software Dev/Assigments/Pics/Pasted image 20240120152334.png]]
- *fastcall*
	- ![[Semester 6/Software Dev/Assigments/Pics/fastcall.png]]

**Question 9:  Analysis Bonus**
-  *Basic Operations of the Program*
	- The program first prompts the user to enter their name and stores it in a buffer. After that, it then greets the user and checks if the entered name contains the string "password". If the name includes "password", the program proceeds to reveal the secret.
- *To Reveal the Secret*
	- To start, it prints the string "Your secret is ". Following that, it takes two arguments: One likely pointing to a string containing the secret (which I could not find) or data used to generate it (most likely this), and the other being a numerical value that modifies the secret characters. I think the value could be 8, or 12 (C in hex). After all of that, it iterates through each character of the secret string. *For each character, it adds a value based on the character's position and the numerical argument, and then prints the modified character*.