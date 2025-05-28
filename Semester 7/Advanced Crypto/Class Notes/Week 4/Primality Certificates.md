---
title: S1 - Primality Certificates
author:
  - Jon Marien
created: 2025-01-27
published: 2025-01-27
tags:
  - classes
---

| Title                       | Author                       | Created          | Published        | Tags                   |
| --------------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| S1 - Primality Certificates | <ul><li>Jon Marien</li></ul> | January 27, 2025 | January 27, 2025 | [[#classes\|#classes]] |

# Primality Certificates (#4)
Recall the sets for $FACTOR$ and $ORDER$.
$$ FACTOR=\{N|N=pq,\text{ for integers }p,q>1\}$$
$$ORDER=\{\langle N,g,t\rangle|t\text{ is the smallest positive integer such that }g^t\equiv1\mod N\}$$
We can determine if some integer N is in $FACTOR$ using a factoring algorithm. If however we are given a factor of N , say p, we do not need to use a factoring algorithm to determine if $N\in FACTOR$, we can simply compute N mod p. If the result is 0 then we have verified that $N\in FACTOR$.
## Certificates (#4.1)
Any factor of N is a certificate to verify that $N\in FACTOR$. For example, if N = 221 then c = 17 is a certificate for $N\in FACTOR$. We can verify that $N\in FACTOR$ by computing 221 mod 17 = 0 which clearly does not involve exponential time. 

But what if we want to show that $N\not\in FACTOR?$ In other words, what if we want to prove that N is prime? 

One possible certificate would be a list of all the possible prime factors of N ; given this list we could check that each possible factor does not divide N (in other words, check that N mod ${c_i}$ = 0 for all possible factors $c_{i}$). But this verification process would be computationally equivalent to running a brute force factoring algorithm which would require exponential time.

## Pratt Primality Certificates (#4.2)
A Pratt Primality Certificate for some integer $N$ is a method of verifying (without using exponential time) that $N$ is prime. It’s based on the converse of Fermat’s Little Theorem; if $\langle N,g,N-1\rangle\in ORDER$ for some witness $g$, then $N$ must be $prime$.

The method starts by providing a certificate, $c\:=\:[g,(p_1,p_2,...,p_{k-1},p_k)],$, for $\langle N,g,N-1\rangle$ and then provides additional certificates for all prime factors $p_i$ > 2. 

A convenient way of representing a Pratt Certificate for $N$ is using a tree, $T$, rooted at $N$ such that the children of vertex $N$ are the prime factors of $N − 1$, and (in general) the children of any internal vertex with label $V$ are the prime factors of $V − 1$. Because a certificate is not required for any prime factor $p_{i}=2$, all external vertices in $T$ have a label of 2 (and do not have any children).
### Example with Theory (#4.3)
Here is a rooted tree T that represents a Pratt Primality Certificate for the prime N = 173.

![](S1-January-27th-2025-11-45-57.webp)

#### Verifying a Pratt Certificate (#4.4)
Let $T$ represent a Pratt Certificate for an integer $N$. Let $V$ be any internal vertex in $T$ with children $(p_{1}, p_{2}, ..., p_{k-1}, p_{k})$ and witness $g$. We verify $T$ by checking if for every internal vertex $V$:

$$\prod_{i=1}^kp_i=V-1$$
$$ g^{V-1}\equiv1\mod V$$
$$g^{\frac{V-1}{p_i}}\neq1\bmod V\text{ for }1\leq i\leq k$$
Note that the witness $g$ is specific to each internal vertex $V$ (in other words $g$ can vary from vertex to vertex) so the value of $g$ is appended the the label of the internal vertex $V$. External vertices do not require a witness $g$ (because they are all 2s). 

During the verification process, the method of successive squaring must be used for all exponentiations (otherwise Pratt would not approve because the process would require exponential time)!

#### Example with Numbers (#4.5)
Manually verify the following Pratt Certificate for $N = 173 \not\in FACTOR$, using the method of successive squaring for all exponentiations.
![](S1-January-27th-2025-11-50-18.webp)

$V = 173, g = 2$:
$$ \prod\limits_{i=1}^kp_i=43\times2\times2=172=V-1$$
$$ g^{V-1}=2^{172}=2^{128}2^{32}2^82^4=(133)(96)(83)(16)=16955904\equiv1\mod173$$
$$ g^{\frac{V-1}{p_1}}=2^{\frac{172}{43}}=2^4=16\neq1\bmod173$$
$$ \ddot{g^{\frac{V-1}{p_2}}}=2^{\frac{172}{2}}=2^{86}=2^{64}2^{16}2^{4}2^{2}=(47)(142)(16)(4)=427136=172\neq1\bmod173$$

$V = 43, g = 2$:
$$ \prod\limits_{i=1}^kp_i=7\times3\times2=42=V-1$$
$$ g^{V-1}=3^{42}=3^{32}3^83^2=(13)(25)(9)=2925\equiv1\bmod43$$
$$ g^{\frac{V-1}{p_1}}=3^{\frac{42}{7}}=3^6=3^43^2=(38)(9)=342=41\neq1\bmod43$$
$$ g^{\frac{V-1}{p_2}}=3^{\frac{42}{3}}=3^{14}=3^83^43^2=(25)(38)(9)=8550=36\neq1\bmod43$$
$$ g^{\frac{V-1}{p_3}}=3^{\frac{42}{2}}=3^{21}=3^{16}3^43^1=(23)(38)(3)=2622=42\neq1\bmod43$$
$V = 7, g = 3$:
$$ \prod\limits_{i=1}^kp_i=3\times2=6=V-1$$
$$ g^{V-1}=3^6=3^43^2=(4)(2)=8\equiv1\mod7$$
$$ g^{\frac{V-1}{p_1}}=3^{\frac{6}{3}}=3^2=2\neq1\bmod7$$
$$ g^{\frac{V-1}{p_2}}=3^{\frac{6}{2}}=3^3=3^23^1=(2)(3)=6\neq1\bmod7$$
$V = 3, g = 2$:
$$ \prod\limits_{i=1}^kp_i=2=V-1$$
$$ g^{V-1}=2^2=4\equiv1\mod3$$
$$ g^{\frac{V-1}{p_1}}=2^{\frac{2}{2}}=2^1=2\neq1\bmod3$$
We have verified $T$ by checking that for every internal vertex $V$:

$$\prod_{i=1}^kp_i=V-1$$
$$ g^{V-1}\equiv1\mod V$$
$$g^{\frac{V-1}{p_i}}\neq1\bmod V\text{ for }1\leq i\leq k$$
Therefore, $N = 173 \not\in FACTOR$ and is $prime$.

##### Theoretical Upper Bound for Exponentiation and Multiplication Steps (#4.6)
In Pratt’s original paper the following upper bounds are proven:
- Any $T$ for $N > 3$ can be verified using at most $(\lfloor3\log_2(N)\rfloor-3)$ steps, involving an exponentiation.
- At most $(\lfloor\log_2(N)\rfloor-1)$ multiplications are required to check that $\prod_{i=1}^kp_i=V-1$ for every $V$ in $T$. Note that this does not include all the multiplications required to verify $T$, only those that are needed to check the prime factorizations.

So theoretically, in the previous example, we expect at most $(\lfloor3\log_2(173)\rfloor-3)=19$ exponentiation steps, and at most $(\lfloor\log_2(173)\rfloor-1)\overset{\cdot}{\operatorname*{=}}6$ multiplications.

Counting the actual number of multiplications and exponentiations used:

$V = 173, g = 2$: ***2 multiplications, 3 exponentiation* steps** 
$V = 43, g = 3$: ***2 multiplications, 4 exponentiation* steps** 
$V = 7, g = 3$: ***1 multiplication, 3 exponentiation* steps** 
$V = 3, g = 2$: ***0 multiplications, 2 exponentiation* steps**

**Total:** ***5 multiplications, 12 exponentiation* steps** (which is within the theoretical upper bounds).

## Practice Questions (#4.7)

