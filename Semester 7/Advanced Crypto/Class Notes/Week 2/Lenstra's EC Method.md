---
title: Lenkstra's EC Method
author:
  - Jon Marien
created: 2025-01-15
published: 2025-01-15
tags:
  - classes
---

| Title                | Author                       | Created          | Published        | Tags                   |
| -------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Lenkstra's EC Method | <ul><li>Jon Marien</li></ul> | January 15, 2025 | January 15, 2025 | [[#classes\|#classes]] |

# Lenstra EC Method (**Elliptic-Curve Factorization**)
Recall that for an integer a to have an inverse ${a^{−1} mod N}$ , a must be relatively prime to ${N}$. In other words, ${GCD(N, a) = 1}$. Lenstra’s method for factoring ${N = pq}$ looks for integers that do not have an inverse ${a^{−1} mod N}$ , and therefore are not relatively prime to ${N}$. If one of these integers is found we have that ${GCD(N, a) = p}$ or ${q}$.

## Mathematical "Dark Arts"
Their method searches for integers without an inverse, on randomly generated elliptic curves $\mathbb{Z}_N$:
$$ \begin{aligned}&y^2=x^3+ax+b\mod N\\&\lambda=\begin{cases}(y_2-y_1)(x_2-x_1)^{-1}\mod N&P\neq Q\\\\(3x_1^2+a)(2y_1)^{-1}\mod N&P=Q\end{cases}\\&x_3=\lambda^2-x_2-x_1\mod N\\&y_3=-\lambda(x_3-x_1)-y_1\mod N\end{aligned}$$

### Main Steps of the Method:
1. Randomly select parameters $a,x_0,y_0$ such that:
	- $2\leq a\leq N-1$
	- $2\leq y_0\leq N-1$
	- $2\leq x_0\leq N-1$
2. Compute $b=y_0^2-x_0^3-ax_0\mod N$. This establishes a random starting point $P=(x_0,y_0)\in E$, a random elliptic curve described by $y^2=x^3+ax+b\mod N$.
3. Compute ${(B!)P}$. If at any point during this computation, the slope, $\lambda$, requires an inverse that does not exist, then return the factor $GCD(N,2y_1)=p$ or $GCD(N,x_2-x_1)=p$.
4. If the computation of $(B!)P$ is completed without finding a factor, return to step 1 and search for the factor an another random elliptic curve.
## The Power of the Dark Side
Step 3 mirrors the Pollard $p-1$ method where we computed ${a=2^{B!} mod N}$ to obtain a factor of $GCD(N, a-1)=p$. A limitation of the ${p-1}$ method is that if a factor is not found with a small value of $B$, the only choice we have is to increase the size of $B$. Lenstra's method has no such limitation; small values of $B$ can be used, again and again, over different random elliptic curves, which tend to have different numbers of total points.

Step 3 can be modified in Lenstra's method by making substitutions for $B!$ such as the primorial $\#B$ for further efficiencies.

The primorial of a number is **the product of all the prime numbers less than or equal to that number**. For example, the primorial of 6 is 2×3×5=30.

### Practice Exercises
2.6) **GCD(9,15)=(3,5)**
2.7) **GCD(39,91)=(13, 7)**
2.8)
2.9)
2.10)