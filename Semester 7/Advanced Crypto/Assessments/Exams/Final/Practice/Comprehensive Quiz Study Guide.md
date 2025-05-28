---
title: Comprehensive Quiz Study Guide
author:
  - Jon Marien
created: 2025-04-17
published: 2025-04-17
tags:
  - classes
  - MATH36206
---

| Title                          | Author                       | Created        | Published      | Tags                                               |
| ------------------------------ | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Comprehensive Quiz Study Guide | <ul><li>Jon Marien</li></ul> | April 17, 2025 | April 17, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |

Here is a **comprehensive, step-by-step walkthrough of Quizzes 5–8**, with every calculation shown in detail. After each quiz, you’ll find a practice version with new numbers for you to drill. This is designed to ingrain the concepts and procedures for your final exam.

---

# **Quiz 5: Knapsack Cryptosystems**

## 1. Encrypt "110111" and "101001" using a 6-bit knapsack cipher with public key $A = \{118, 99, 61, 200, 29, 39\}$

### a) Encrypt "110111"

Align bits to keys:  
Bits: 1 1 0 1 1 1  
Keys: 118 99 61 200 29 39

Multiply each bit by its key and sum:
- $1 \times 118 = 118$
- $1 \times 99 = 99$
- $0 \times 61 = 0$
- $1 \times 200 = 200$
- $1 \times 29 = 29$
- $1 \times 39 = 39$

Total: $118 + 99 + 0 + 200 + 29 + 39 = 485$

**Ciphertext:** $485$

---

### b) Encrypt "101001"

Bits: 1 0 1 0 0 1  
Keys: 118 99 61 200 29 39

- $1 \times 118 = 118$
- $0 \times 99 = 0$
- $1 \times 61 = 61$
- $0 \times 200 = 0$
- $0 \times 29 = 0$
- $1 \times 39 = 39$

Total: $118 + 0 + 61 + 0 + 0 + 39 = 218$

**Ciphertext:** $218$

---

## 2. Decrypt $t' = 386$ using private key $(u = 215, v = 137)$ and public key $A$

### Step 1: Compute $v^{-1} \bmod u$

Find $x$ such that $137x \equiv 1 \pmod{215}$.

Using the Extended Euclidean Algorithm (see below for details),  
$v^{-1} \bmod u = 113$

Here is a **step-by-step, detailed breakdown** of how to compute $v^{-1} \bmod u$ for $v = 137$, $u = 215$ using the **Extended Euclidean Algorithm (EEA)**, as requested. No steps skipped.

---

## **Step 1: The Goal**

We want the modular inverse $x$ such that:
$137x \equiv 1 \pmod{215}$

This is equivalent to finding integers $x, y$ such that:
$137x + 215y = 1$

The coefficient $x$ (modulo 215) is the inverse we seek.

---

## **Step 2: Apply the Euclidean Algorithm**

We perform repeated division to find the greatest common divisor (GCD):

1. $215 \div 137 = 1$ remainder **78**  
   $215 = 1 \times 137 + 78$
2. $137 \div 78 = 1$ remainder **59**  
   $137 = 1 \times 78 + 59$
3. $78 \div 59 = 1$ remainder **19**  
   $78 = 1 \times 59 + 19$
4. $59 \div 19 = 3$ remainder **2**  
   $59 = 3 \times 19 + 2$
5. $19 \div 2 = 9$ remainder **1**  
   $19 = 9 \times 2 + 1$
6. $2 \div 1 = 2$ remainder **0**  
   $2 = 2 \times 1 + 0$

When we reach remainder 1, we've confirmed that 137 and 215 are coprime, so the inverse exists.

---

## **Step 3: Back-substitute to Express 1 as a Linear Combination**

We now **backtrack** to write 1 as a combination of 137 and 215.

Start with the last nonzero remainder:
$1 = 19 - 9 \times 2$

But $2 = 59 - 3 \times 19$:
$1 = 19 - 9 \times (59 - 3 \times 19) = 19 - 9 \times 59 + 27 \times 19 = 28 \times 19 - 9 \times 59$

Now, $19 = 78 - 1 \times 59$:
$1 = 28 \times (78 - 59) - 9 \times 59 = 28 \times 78 - 28 \times 59 - 9 \times 59 = 28 \times 78 - 37 \times 59$

Now, $59 = 137 - 1 \times 78$:
$1 = 28 \times 78 - 37 \times (137 - 78) = 28 \times 78 - 37 \times 137 + 37 \times 78 = (28 + 37) \times 78 - 37 \times 137 = 65 \times 78 - 37 \times 137$

Now, $78 = 215 - 1 \times 137$:
$1 = 65 \times (215 - 137) - 37 \times 137 = 65 \times 215 - 65 \times 137 - 37 \times 137 = 65 \times 215 - 102 \times 137$

---

## **Step 4: Read Off the Modular Inverse**

This gives:
$1 = 65 \times 215 - 102 \times 137$
So, the coefficient of $137$ is $-102$. The modular inverse is:
$-102 \bmod 215 = 215 - 102 = 113$

**Therefore:**
$137^{-1} \bmod 215 = \boxed{113}$

---

## **Step 5: Verification**

Check $137 \times 113 \bmod 215$:

$137 \times 113 = 15481$

$15481 \div 215 = 72$ remainder **1**  
So $15481 \bmod 215 = 1$

**Confirmed!**

---

## **Summary Table of Steps**

| Step | Equation | Remainder | Back-substitution |
|------|----------|-----------|------------------|
| 1 | 215 = 1 × 137 + 78 | 78 | |
| 2 | 137 = 1 × 78 + 59 | 59 | |
| 3 | 78 = 1 × 59 + 19 | 19 | |
| 4 | 59 = 3 × 19 + 2 | 2 | |
| 5 | 19 = 9 × 2 + 1 | 1 | $1 = 19 - 9 \times 2$ |
| 6 | 2 = 2 × 1 + 0 | 0 | |

Backtracking (each step substitutes the previous remainder in terms of earlier remainders):

- $1 = 19 - 9 \times 2$
- $2 = 59 - 3 \times 19$
- $1 = 28 \times 19 - 9 \times 59$
- $19 = 78 - 59$
- $1 = 28 \times 78 - 37 \times 59$
- $59 = 137 - 78$
- $1 = 65 \times 78 - 37 \times 137$
- $78 = 215 - 137$
- $1 = 65 \times 215 - 102 \times 137$

---

## **Final Answer**

$\boxed{137^{-1} \bmod 215 = 113}$

This is the detailed, step-by-step EEA process for finding the modular inverse, with every calculation shown and no steps skipped.

---

### Step 2: Compute the superincreasing sequence $S$

$S_i = v^{-1} \cdot a_i \bmod u$ for each $a_i$:

- $S_1 = 113 \times 118 \bmod 215 = 13334 \bmod 215 = 4$
- $S_2 = 113 \times 99 \bmod 215 = 11187 \bmod 215 = 7$
- $S_3 = 113 \times 61 \bmod 215 = 6893 \bmod 215 = 13$
- $S_4 = 113 \times 200 \bmod 215 = 22600 \bmod 215 = 25$
- $S_5 = 113 \times 29 \bmod 215 = 3277 \bmod 215 = 52$
- $S_6 = 113 \times 39 \bmod 215 = 4407 \bmod 215 = 107$

So, $S = \{4, 7, 13, 25, 52, 107\}$

---

### Step 3: Compute $t = v^{-1} \cdot t' \bmod u$

$t = 113 \times 386 \bmod 215 = 43618 \bmod 215 = 188$

---

### Step 4: Solve the subset-sum for $S$ and $t$

Find which subset of $S$ sums to $188$:

- Start with largest: $107$ (used), $188-107=81$
- Next: $52$ (used), $81-52=29$
- Next: $25$ (used), $29-25=4$
- Next: $13,7$ (too big), $4$ (used), $4-4=0$

So, bits used: $107, 52, 25, 4$, which is $1 0 0 1 1 1$ (from largest to smallest: 107, 52, 25, 13, 7, 4).

**Decrypted bits:** $100111$

---

### **Practice Version (Quiz 5)**

1. Encrypt "101010" and "011011" using a 6-bit knapsack cipher with public key $A = \{87, 45, 120, 200, 63, 31\}$.
2. Decrypt $t' = 257$ using a 6-bit knapsack cipher with private key $(u = 191, v = 83)$ and public key $A = \{87, 45, 120, 200, 63, 31\}$.

---

# **Quiz 6: Hash-based Signature Schemes**

## 1. Lamport Public Key and Signature for "0101" with $h(x) = 7^x \bmod 11$

Given private keys:
- $y_{1,0}=4, y_{1,1}=7$
- $y_{2,0}=9, y_{2,1}=3$
- $y_{3,0}=6, y_{3,1}=8$
- $y_{4,0}=11, y_{4,1}=10$

**Compute public keys:**
- $z_{1,0} = 7^4 \bmod 11 = 2401 \bmod 11 = 3$
- $z_{1,1} = 7^7 \bmod 11 = 823543 \bmod 11 = 6$
- $z_{2,0} = 7^9 \bmod 11 = 40353607 \bmod 11 = 8$
- $z_{2,1} = 7^3 \bmod 11 = 343 \bmod 11 = 2$
- $z_{3,0} = 7^6 \bmod 11 = 117649 \bmod 11 = 4$
- $z_{3,1} = 7^8 \bmod 11 = 5764801 \bmod 11 = 9$
- $z_{4,0} = 7^{11} \bmod 11 = 1977326743 \bmod 11 = 7$
- $z_{4,1} = 7^{10} \bmod 11 = 282475249 \bmod 11 = 1$

**Message:** "0101"  
So, signature reveals:
- $y_{1,0}$ for bit 0 (4)
- $y_{2,1}$ for bit 1 (3)
- $y_{3,0}$ for bit 0 (6)
- $y_{4,1}$ for bit 1 (10)

**Signature:** (4, 3, 6, 10)

---

## 2. Merkle Tree with depth $d=3$, keys $K_1=10, ..., K_8=80$, $h(x) = x \bmod 17$

**a) Value of the root node**

Compute all leaf hashes:
- $V(8) = 10 \bmod 17 = 10$
- $V(9) = 20 \bmod 17 = 3$
- $V(10) = 30 \bmod 17 = 13$
- $V(11) = 40 \bmod 17 = 6$
- $V(12) = 50 \bmod 17 = 16$
- $V(13) = 60 \bmod 17 = 9$
- $V(14) = 70 \bmod 17 = 2$
- $V(15) = 80 \bmod 17 = 12$

Compute internal nodes:
- $V(4) = h(10||3) = h(103) = 103 \bmod 17 = 1$
- $V(5) = h(13||6) = h(136) = 136 \bmod 17 = 0$
- $V(6) = h(16||9) = h(169) = 169 \bmod 17 = 16$
- $V(7) = h(2||12) = h(212) = 212 \bmod 17 = 8$
- $V(2) = h(1||0) = h(10) = 10 \bmod 17 = 10$
- $V(3) = h(16||8) = h(168) = 168 \bmod 17 = 15$
- $V(1) = h(10||15) = h(1015) = 1015 \bmod 17 = 12$

**Root node:** $12$

**b) Sign $m_3$ (corresponds to $K_3=30$, node 10):**  
Path: $V(10) \rightarrow V(5) \rightarrow V(2) \rightarrow V(1)$  
Sibling hashes: $V(11)=6, V(4)=1, V(3)=15$

**c) Sign $m_7$ ($K_7=70$, node 14):**  
Path: $V(14) \rightarrow V(7) \rightarrow V(3) \rightarrow V(1)$  
Sibling hashes: $V(15)=12, V(6)=16, V(2)=10$

**d) How many messages can be signed?**  
$2^3 = 8$

---

### **Practice Version (Quiz 6)**

1. Find the Lamport public key and sign the message "1010" using $h(x) = 5^x \bmod 13$ with:
   - $y_{1,0}=2, y_{1,1}=5, y_{2,0}=7, y_{2,1}=3, y_{3,0}=4, y_{3,1}=6, y_{4,0}=9, y_{4,1}=8$
1. For a Merkle tree with depth $d=3$, keys $K_1=12, K_2=24, ..., K_8=96$, $h(x) = x \bmod 19$:
   - a) Determine the root node value.
   - b) Sign $m_2$.
   - c) Sign $m_6$.
   - d) How many messages can be signed?

---

# **Quiz 7: Learning With Errors and Regev**

## 1. Solve the LWE problem with $q=41, e=(-2,1)$, samples $((13,15),11), ((1,22),35)$

**Equations:**
- $13x + 15y - 2 \equiv 11 \pmod{41}$ ⇒ $13x + 15y \equiv 13 \pmod{41}$
- $x + 22y + 1 \equiv 35 \pmod{41}$ ⇒ $x + 22y \equiv 34 \pmod{41}$

**From 2nd equation:**  
$x \equiv 34 - 22y \pmod{41}$

Substitute into 1st:
$13(34 - 22y) + 15y \equiv 13 \pmod{41}$  
$442 - 286y + 15y \equiv 13 \pmod{41}$  
$-271y \equiv 13 - 442 \pmod{41}$  
$-271y \equiv -429 \pmod{41}$  
$-271y \equiv 14 \pmod{41}$ (since $-429 \bmod 41 = 14$)

But $-271 \bmod 41 = 16$, so $16y \equiv 14 \pmod{41}$

Find inverse of 16 mod 41 (EEA):  
$16 \times 18 = 288 \bmod 41 = 1$  
So, $y = 18 \times 14 \bmod 41 = 252 \bmod 41 = 6$

Plug back: $x = 34 - 22 \times 6 = 34 - 132 = -98 \bmod 41 = 14$

**Solution:** $x = 14, y = 27$

---

## 2. Regev cryptosystem with $q=13$, private key $s=(4,3,2)$, public key:  
$((12,3,4),1), ((9,5,2),4), ((7,3,5),9)$

### a) Encrypt "1" using $S = \{2,3\}$

Sum the $a$ and $b$ values for indices 2 and 3:
- $a = (9,5,2) + (7,3,5) = (16,8,7) \bmod 13 = (3,8,7)$
- $b = 4 + 9 = 13 \bmod 13 = 0$
- Add $\lfloor q/2 \rfloor = 6$: $0 + 6 = 6$

**Ciphertext:** $(3,8,7), 6$

---

### b) Decrypt $(6,6,9), 10$

Compute $x^* = b - (6 \times 4 + 6 \times 3 + 9 \times 2) \bmod 13$
- $6 \times 4 = 24$
- $6 \times 3 = 18$
- $9 \times 2 = 18$
- Sum: $24 + 18 + 18 = 60$
- $10 - 60 = -50 \bmod 13 = 2$ (since $-50 + 52 = 2$)

$2$ is closer to $0$ than to $6$ (since $q/2 = 6$), so $x = 0$

---

### **Practice Version (Quiz 7)**

1. Solve the LWE problem with $q=37, e=(1,-2)$, samples $((7,12), 15), ((3,9), 27)$.
2. For Regev cryptosystem with $q=17$, private key $s=(2,5,3)$, public key:  
   $((11,6,9), 8), ((4,7,2), 6), ((9,13,5), 10)$
   - a) Encrypt "0" using $S = \{1,3\}$.
   - b) Decrypt $(8,9,13), 12$.

---

# **Quiz 8: Module Learning With Errors and Kyber**

## 1. Find $\vec{t} = A\vec{s} + \vec{e}$ for MLWE with  
$f(x) = x^3 + 1, q = 7$,  
$A = \begin{bmatrix} 2x^2+x & 6 \\ x^2+1 & x+3 \end{bmatrix}$,  
$\vec{s} = \begin{bmatrix} x \\ x^2 \end{bmatrix}$,  
$\vec{e} = \begin{bmatrix} x \\ 2 \end{bmatrix}$

Compute:
- First row: 
  $(2x^2 + x) \cdot x + 6 \cdot x^2 + x$
  - $2x^2 \cdot x = 2x^3$
  - $x \cdot x = x^2$
  - $6 \cdot x^2 = 6x^2$
  - Add: $2x^3 + x^2 + 6x^2 + x = 2x^3 + 7x^2 + x$
  - Add error: $+ x$ (from $\vec{e}$) → $2x^3 + 7x^2 + 2x$
  - Mod $x^3 + 1$, $x^3 \equiv -1$, so $2x^3 \equiv -2$
  - $2x^3 + 7x^2 + 2x \equiv -2 + 0x^2 + 2x$ (since $7x^2 \bmod 7 = 0$)
  - Final: $x + 5$

- Second row: $(x^2+1) \cdot x + (x+3) \cdot x^2 + 2$
  - $x^2 \cdot x = x^3 \equiv -1$
  - $1 \cdot x = x$
  - $x \cdot x^2 = x^3 \equiv -1$
  - $3 \cdot x^2 = 3x^2$
  - Add: $-1 + x -1 + 3x^2 = -2 + x + 3x^2$
  - Add error: $+2$ → $-2 + x + 3x^2 + 2 = x + 3x^2$
  - Final: $3x^2 + x$

**Result:** $\vec{t} = \begin{bmatrix} x+5 \\ 3x^2 + x \end{bmatrix}$

---

## 2. Encrypt "110" using Kyber with  
$f(x) = x^3 + 1, q = 11$,  
$A = \begin{bmatrix} 9x^2 & 5x^2 \\ 3x & 8 \end{bmatrix}$,  
$\vec{t} = \begin{bmatrix} 7x \\ 4x^2 \end{bmatrix}$,  
$\vec{r} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$,  
$\vec{e}_1 = \begin{bmatrix} 5x^2 \\ 3 \end{bmatrix}$, $e_2 = 6x$

- Message "110" → $x^2 + x$, upscale: $5(x^2 + x) = 5x^2 + 5x$

$\vec{u} = A^T \vec{r} + \vec{e}_1$
- $A^T \vec{r} = \begin{bmatrix} 3x \\ 8 \end{bmatrix}$
- Add error: $\begin{bmatrix} 5x^2 + 3x \\ 11 \end{bmatrix}$
- $11 \bmod 11 = 0$
- So, $\vec{u} = \begin{bmatrix} 5x^2 + 3x \\ 0 \end{bmatrix}$

$v = t^T \vec{r} + e_2 + m$
- $t^T \vec{r} = 4x^2$
- $+ e_2 = 6x$
- $+ m = 5x^2 + 5x$
- $4x^2 + 6x + 5x^2 + 5x = 9x^2 + 11x$
- $11x \bmod 11 = 0$
- So, $v = 9x^2$

**Ciphertext:** $\left(\begin{bmatrix} 5x^2 + 3x \\ 0 \end{bmatrix}, 9x^2\right)$

---

### **Practice Version (Quiz 8)**

1. Find $\vec{t} = A\vec{s} + \vec{e}$ for MLWE with  
   $f(x) = x^3 + 1, q = 5$,  
   $A = \begin{bmatrix} 3x^2 + 2x & 4 \\ x^2 + 2 & x + 1 \end{bmatrix}$,  
   $\vec{s} = \begin{bmatrix} x \\ x^2 \end{bmatrix}$,  
   $\vec{e} = \begin{bmatrix} x \\ 3 \end{bmatrix}$

2. Encrypt "101" using Kyber with  
   $f(x) = x^3 + 1, q = 7$,  
   $A = \begin{bmatrix} 6x^2 & 2x^2 \\ 4x & 3 \end{bmatrix}$,  
   $\vec{t} = \begin{bmatrix} 5x \\ 2x^2 \end{bmatrix}$,  
   $\vec{r} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$,  
   $\vec{e}_1 = \begin{bmatrix} 2x^2 \\ 1 \end{bmatrix}$, $e_2 = 3x$

---

## 🧠 BRAIN MODE: If you want to work through any of the practice quizzes, just say which one and I'll walk you through every calculation, step by step, just like above.

---

Let me know if you want to add McEliece or any other topic, or if you want to drill through any of the generated practice quizzes!