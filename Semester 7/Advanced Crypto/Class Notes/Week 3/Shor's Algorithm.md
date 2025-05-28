---
title: S1 - Shor's Algorithm
author:
  - Jon Marien
created: 2025-01-20
published: 2025-01-20
tags:
  - classes
---

| Title                 | Author                       | Created          | Published        | Tags                   |
| --------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| S1 - Shor's Algorithm | <ul><li>Jon Marien</li></ul> | January 20, 2025 | January 20, 2025 | [[#classes\|#classes]] |

# Shor's Algorithm

This relatively simple factoring algorithm provides a great starting point for exploring the impacts of quantum computing and importance of time complexity theory. Assume that we want to factor a modulus, `N = p · q`, for the usual reasons. Here is a classical version of Shor’s algorithm (modified to be functional and easy to implement):

## How it works
1. Randomly select a base `1 < g < N`.
2. Compute powers of $g\mod N\colon g^2,g^3,...,g^{9001},...$.
3. Find the period `t` such that $g^x\equiv g^{x+t}\mod N$.
4. If $t$ is even, compute $a=g^{t/2}-1$ and $b=g^{t/2}+1$.
5. Compute the $\mathrm{GCD}(a,N)$ and $\mathrm{GCD}(b,N)$... to get the factors $p$ and $q$.

### Examples:
Factoring `N = 221`. With base `g = 38` we find a period of `t = 4`, `p = 13` and `q = 17`:
1. $g=38$
2. powers of `g mod n` are:
$[38,\:118,\:64,\:1,\:38,\:118,\:64,\:1,\:38,\:118,\:64,\:1,\:38,\:118,\:64,\:1,\:38,\:118,\:64,\:1]\:\dots$
3. $t = 4$
4. $a = 117$
   $b = 119$
5. $p = 13$
   $q = 17$

With base `g = 5` we find a period `t = 16`, `p = 13`, and `q = 17`:
1. $g = 5$
2. powers of `g mod n` are:
$[5,25,125,183,31,155,112,118,148,77,164,157,122,168,177,1,5,25,125,183]\:\dots$
3. $t = 16$
4. $a = 177$
   $b = 119$
5. $p = 13$
   $q = 17$

## Examples of Factoring `N = 221`; Limits 
If $\mathrm{GCD}(g,N)\neq1$ , then the algorithm has trivially found a factor without completing steps 2,3,4,5. Shor's algorithm **WILL FAIL** if $t$ is odd, or if $g^{\frac{t}{2}}\equiv-1\mod N$.

### $\mathrm{GCD}(g,N)\neq1$
With base $g = 26$ we find a period of $t = 8$, but can only get the factor $q$ directly because $\mathrm{GCD}(g,N)=1$:
1. $g = 26$
2. powers of `g mod n` are:
$[26,\:13,\:117,\:169,\:195,\:208,\:104,\:52,\:26,\:13,\:117,\:169,\:1]\\\dots$
3. $t = 8$
4. $a = 168$
   $b = 170$
This case results in the successful factorization of `N` but in many implementations these types of cases are screened out by computing `GCD(g, N)` before computing steps 2,3,4,5. If $\mathrm{GCD}(g,N)\neq1$ then the algorithm stops (because it has already found the factor).

