---
title: Pollards Theorem (Factoring)
author:
  - Jon Marien
created: 2025-01-13
published: 2025-01-13
tags:
  - classes
---

| Title                        | Author                       | Created          | Published        | Tags                   |
| ---------------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Pollards Theorem (Factoring) | <ul><li>Jon Marien</li></ul> | January 13, 2025 | January 13, 2025 | [[#classes\|#classes]] |

# Factoring
The security of many cryptosystems is based on the integer factorization problem;
	Given a composite integer ${N}$ find any factor (${p}$ or ${q}$) such that ${N} ={pq}$.

For example, we know that *33*, *24*, and *1309* can all be factored because *33 = 3 x 11*, *24 = 2 x 12*, and *1309 = 7 x 187*. The integers *13*, *101*, and *1049* cannot be factored because they are all primes. So, the integer factorization problem consists of determining if a given integer is in the following set:
$$ FACTOR=\{N|N=pq,\text{ for integers }p,q>1\}$$
We have that *33*, *24*, and *1039* $\in FACTOR$.
We have that *13*, *101*, and *1049* $\notin FACTOR$.

## Factoring Algorithms
A factoring algorithm for a given integer ${N}$ determines if $N\in FACTOR$, and provides proof of membership (also called certificate) by returning any factor (${p}$ or ${q}$) of ${N}$.

## Trial Division up to $\sqrt{N}$ method
It is simple and effective (for small values of ${N}$):
![](Pasted%20image%2020250113134343.png)
This algorithm takes a maximum of $\sqrt{N}$ steps to complete the for loop, so it’s $O(\sqrt{N})$ Although this might seem fast it’s actually horrible when we evaluate the number of steps in terms of the size of ${N}$ in binary. For example, the input ${N}$ = 221 is an 8-bit number. So the maximum number of steps to complete the for loop is about $\sqrt{2^8}=2^{8/2}=2^4$.

In general, if the input ${N}$ is an n-bit number, the maximum number of steps to complete the for loop is about $\sqrt{2^n}=2^{n/2}$. So trial division is actually a $O(2^n)$ (or exponential time) algorithm where n is the size of the input in binary. 
# Pollards Theorem

## Pollard's ${p-1}$ Method
Let ${N = pq}$ and ${p-1=}$ $\begin{aligned}S_1S_2...S_i\end{aligned}$ be the prime factorization of ${p-1}$.

Let $B\in\mathbb{Z}^+$ such that $\begin{aligned}B!~=~B(B~-~1)(B~-~2)...(s_i)...(s_2)...(s_1)...(3)(2)(1)\end{aligned}$ contains all factors of ${p-1}$ or ${q-1}$ (**BUT NOT BOTH!!!**).

Then, $\big(p-1\big)\big|B!$

Compute $a=2^{B!}\mod N$. We have that:
$$ \begin{aligned}a&=2^{B!}\mod N\\a&\equiv2^{B!}\mod p\\&=2^{(p-1)\frac{B!}{p-1}}\mod p\\&=(1)^{\frac{B!}{p-1}}\mod p\\&=1\mod p\end{aligned}$$
Then $\begin{aligned}a-1&\equiv0\mod p\end{aligned}$, and we have that $p\big|\big(a-1\big)$ ***and*** $p|N$, so therefore $p=GCD(N,a-1)$.

## Pollard's ${p-1}$ Method Examples
2.4) Factor ${N=407}$ using ${B=5}$.

$$ \begin{aligned}a&=2^{B!}\mod N\\&=2^{5!}\mod407\\&=2^{120}\mod407\\&=2^{64}2^{32}2^{16}2^8\mod407\\&=(49)(81)(9)(256)\mod407\\&=100\end{aligned}$$
$\begin{aligned}p=GCD(407,100-1)=GCD(407,99)\vdots\end{aligned}$
$$ \begin{aligned}407&\mod99&=11\\99&\mod11&=0\end{aligned}$$
$\begin{aligned}p=GCD(407,99)=11\text{ and }N=407=11\times37\end{aligned}$.

**Note:** using ${B=6}$ would not work as ${6! = 720}$ contains the factors of both 11-1 and 37-1:
$$ \begin{aligned}a&=2^{B!}\mod N\\&=2^{6!}\mod407\\&=2^{720}\mod407\\&=2^{512}2^{128}2^{64}2^{16}\mod407\\&=(367)(366)(49)(9)\mod407\\&=1\end{aligned}$$

### Exercises -- See Paper Notes
2.1) Factor ${N = 77}$ using the Pollard ${p − 1}$ method with:
	a) ${B=3}$
	b) ${B=4}$
	c) ${B=5}$
	Show the computation of ${a}$ and $GCD(N,a-1)$.
2.2) Factor ${N = 299}$ using the Pollard ${p − 1}$ method with ${B=4}$, and determine the largest value of ${B}$ that can be used.
2.3) Factor ${N = 517}$ using the Pollard ${p − 1}$ method with ${B=5}$, and determine the largest value of ${B}$ that can be used.
2.4) Determine the range for ${B}$ that can be used when factoring ${N}$ using the Pollard ${p-1}$ method.
	a) $N=899=29\times31$
	b) $N=11413=101\times113$
	c) $N=8881=83\times107$
2.5) Let $\#B$ be the primordial of ${B}$. $\#B=\prod\limits_{n=1}^Bp_n$ where $p_{n}$ is the $n^{th}$ prime number.
	For example $\#3=\prod\limits_{n=1}^3p_n=2\times3\times5=30$.
	a) Factor N = 407, B = 3, a = (2^#B) mod N
	b) Factor N = 4853, B = 4, a = (2^#B) mod N