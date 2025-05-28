---
title: NP-Complete Problem Based Cryptosystems
author:
  - Jon Marien
created: 2025-03-03
published: 2025-03-03
tags:
  - classes
---

| Title                                   | Author                       | Created        | Published      | Tags                   |
| --------------------------------------- | ---------------------------- | -------------- | -------------- | ---------------------- |
| NP-Complete Problem Based Cryptosystems | <ul><li>Jon Marien</li></ul> | March 03, 2025 | March 03, 2025 | [[#classes\|#classes]] |

# NP-Complete Problem Based Cryptosystems

Recall that a language $B$ is $NP-Complete$ if:
1. $B$ is in $NP$, and
2.  every other language $A$ in $NP$ can be reduced to $B$/

$\therefore \text{it\:can\:be\:shown\:that\:SUBSET-SUM\:is\:} NP-complete.$

$SUBSET\text{-}SUM=\{\langle S,t\rangle|S=\{x_1,...,x_k\}\text{ and the sum of some subset of }S\mathrm{~is~}t\}$

To determine if $\langle S,t\rangle=\{\{5,14,9,23,16,7,31,27\},50\}\in SUBSET-SUM$, we have to find some subset of the $n = 8$ numbers, $S = \{5, 14, 9, 23, 16, 7, 31, 27\}$, that add up to $t = 50$. We prohibit using the same number more than once (although some interpretations of $SUBSET-SUM$ allow for this and treat $S$ as a multi-set...) and define the problem mathematically as:
$$\boxed{\begin{aligned}t=\sum_{i=1}^nb_i\cdot s_i\end{aligned}}$$
Where $b_{i}\in\{0,1\},\:s_{i}\in S,\mathrm{~and~}n=|S|$.

Solving (by brute force) we might find a solution and represent it as a string:
$$ b_1b_2b_3b_4b_5b_6b_7b_8=01100001$$

In other words the sum of the numbers corresponding to the 1 bits, $\{5,14,9,23,16,7,31,27\}$, is $14+9+27=50=t$.

Note that to find a solution (by brute force) for any $SUBSET-SUM$ problem requires at most $2^n$ steps so the time complexity is clearly $O(2^n)$ or $EXPTIME$.
### SUBSET-SUM Crypto
If we use the set $S$ as the public key then we can encrypt binary data using the sum $t$. For example, with $S = \{5, 14, 9, 23, 16, 7, 31, 27\}$, then "$01100001$" would be encrypted as "$50$", because:
$$ \boxed{\begin{aligned}t&=\sum_{i=1}^nb_i\cdot s_i\\&=0(5)+1(14)+1(9)+0(23)+0(16)+0(7)+0(31)+1(27)\\&=14+9+27\\&=50\end{aligned}}$$
An immediate problem with this method is that it is **too hard** to decrypt "$50$" (we are still solving an $EXPTIME$ problem). Also the decrypted strings **may not be *unique***. For example "$50$" decrypts as "$01100001$", but also "$11000010$".

#### Superincreasing Sequences
A sequence is “**superincreasing**” if each number in the sequence is greater than the sum of all the previous numbers in the sequence. For example $3, 5, 9, 18, 38, 75, 155, 310$ is **a superincreasing sequence**. When $S$ can be written as a superincreasing sequence, solving this special case of $SUBSET-SUM$ can be done in polynomial time.

To determine if $⟨S, t⟩ = \{\{3, 5, 9, 18, 38, 75, 155, 310\}, 242\} ∈ SUBSET-SUM$, we can quickly compute:
$$ \begin{aligned}242-155&=87\\87-75&=12\\12-9&=3\\3-3&=0\end{aligned}$$
To obtain the unique solution $3+9+75+155=242=t\mathrm{~or~}b_1b_2b_3b_4b_5b_6b_7b_8=10100110$.
#### Superincreasing SUBSET-SUM Crypto
If we use the superincreasing set $S=\{3,5,9,18,38,75,155,310\}$, then "$10100110$" would be encrypted as "$242$" because:
$$ \boxed{\begin{aligned}t&=\sum_{i=1}^nb_i\cdot s_i\\&=1(3)+0(5)+1(9)+0(18)+0(38)+1(75)+1(155)+0(310)\\&=3+9+75+155\\&=242\end{aligned}}$$
Now, it's way too **easy** to decrypt "$242$". We can use the "***greedy***" algorithm described above as the set $S$ is **superincreasing**.
### The Trapdoor
A solution to this $SUBSET-SUM$ crypto dilemma is to transform the superincreasing set $S = \{s_{1}, s_{2}, ..., s_{n}\}$ into a **trapdoor set**, $A = \{a_{1}, a_{2}, ..., a_{n}\}$, using the integers $u$ and $v$ such that:
- $GCD(u,v)=1$
- $u >2_{s_{n}} (s_{n} \text{\:is\:the\:largest\:element\:in\:} S)$
- $a_i=vs_i\mod u,1\leq i\leq n$

Using the superincreasing set $S = \{3, 5, 9, 18, 38, 75, 155, 310\}$ with $u = 672$ and $v = 13$ we compute the trapdoor set $A = \{39, 65, 117, 234, 494, 303, 671, 670\}$. Then "$10100110$" would be encrypted as the **trapdoor target** $t$ ="$1130$" because:

$$ \boxed{\begin{aligned}t^{\prime}&=\sum_{i=1}^nb_i\cdot a_i\\&=1(39)+0(65)+1(117)+0(234)+0(494)+1(303)+1(671)+0(670)\\&=39+117+303+671\\&=1130\end{aligned}}$$

Note that decrypting the **trapdoor target** "$1130$" using only the **trapdoor set** $A$ (i.e. without knowing $(u, v)$) is hard.

But if we know $(u = 672, v = 13)$ we can:
- Compute the inverse of $v$: $v^−1\:mod\;u\: = 517$.

- compute the original superincreasing set elements $s_i = v^−1 \cdot ai$ to get: $S = \{3, 5, 9, 18, 38, 75, 155, 310\}$.

- Compute the original target: $t = t^′(v^−1) = 1130(517)\:mod\;u\: = 242$.

- Solve this special case of $SUBSET-SUM$ for $⟨S, t⟩$ in polynomial time to easily decrypt the original target “$242$” as ‘$10100110$”.
### The Merkle-Hellman Knapsack Cipher
The $n$-bit Merkle-Hellman Knapsack cipher has:
- Public key $A=\{a_1,a_2,...,a_n\}$
- Private key $(u,v)$ such that:
	- $GCD(u,v)=1$
	- $S=\{s_1,s_2,....,s_n\} \text{\:is\:a\:superincreasing\:set}$.
	- $u >2_{s_{n}} \text{where\:}s_{n} \text{\:is\:the\:largest\:element\:in\:} S$
	- $a_i=vs_i\mod u,1\leq i\leq n$
- $n$-bit plaintext blocks, $b_1b_2...b_n;\text{ encrypted as }t^{\prime}=\sum_{i=1}^nb_i\cdot a_i$.
- integer ciphertext blocks, $t^′$, decrypted by solving the special case of $SUBSET-SUM$ for $\langle S,t=t'(v^{-1})\mod u\rangle$.
#### Merkle-Hellman Example
Encrypt and then decrypt "$Bat$" using 8-bit ASCII encoding and the Merkle-Hellman knapsack cipher with public key $A = \{39, 65, 117, 234, 494, 303, 671, 670\}$, and private key $(u = 672, v = 13)$.

**Encrypting the plaintext “Bat”:**
$$ \boxed{\begin{array}{ll}\mathrm{B}\to01000010,&t'=65+671=736\\\mathrm{a}\to01100001,&t'=65+117+670=852\\\mathrm{t}\to01110100,&t'=65+117+234+303=719\end{array}}$$
**Decrypting the ciphertext “736 852 719”:**
- $13^−1\:\:mod\:\:672 = 517$ (which is computed using EEA)
- $s_i=517a_i\mod672,\mathrm{~for~}1\leq i\leq8{:}S=\{3,5,9,18,38,75,155,310\}$

$$ \boxed{\begin{aligned}&t=736(517)\mod672=160=155+5\to01000010\to\mathrm{B}\\&t=852(517)\mod672=324=310+9+5\to01100001\to\mathrm{a}\\&t=719(517)\mod672=107=75+18+9+5\to01110100\to\mathrm{t}\end{aligned}}$$

##### Lesson Exercises
> [!todo]
 ![](image-94.png)
>> [!help]-
	>> ![](image-91.png)
