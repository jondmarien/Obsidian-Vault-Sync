---
title: S2 - Time Complexity
author:
  - Jon Marien
created: 2025-01-22
published: 2025-01-22
tags:
  - classes
---
# Shor's Algorithm Part 2
## Time Complexity
Step 2 in the algorithm is the bottleneck. We may have to exponentiate $g^x\mod N$ up to $ϕ(N)$ times to be able to find the period. If we let $n$ be the number of bits required to encode $N$ then $n = log2(N)$ and step 2 will take $O(2n)$ steps, which is exponential time (and not polynomial time).

Compare this to trial division where up to $√N$ divisions may be required to find a factor. This requires $O(2^n/2)$ steps, which is also exponential time. So using Shor’s classical algorithm on a standard computer is no better than trial division. 

The trick is to implement step 2 on a quantum computer that can exponentiate $g^x mod N$ using a superposition of all values of $x$ all at once, and then measure the computation for some random remainder $r$. Then what will be left (apparently!) is an array of exponents, $x$, that yield the same remainder $(r)mod N$ which can be used to find the period $t$. Step 5 is the only other computationally significant step, but it can be accomplished in polynomial time using the Euclidean Algorithm.

## Problem Reductions
Shor’s algorithm takes advantage of the fact that the problem of factoring can be reduced to the problem of order finding using a reduction.

$FACTOR=\{N|N=pq,\text{ for integers }p,q>1\}$

$ORDER=\{\langle N,g,t\rangle|t$ is the smallest positive integer such that $g^t\equiv1\mod N\}$

Order finding is the problem of finding the smallest $t\ge1$ such that $g^t\equiv{1}mod N$. (We have called $t$ the period but it is also called the order of $g$.
## Quantum Computing and Information Security
Under the assumption that quantum computers are feasible (for computations involving more than a few bits...):
- The problems of factoring and order finding will no longer require exponential time to solve.
- Cryptosystems that are based on integer factorization (like RSA) will no longer be secure.
- New cryptosystems based on “more computationally difficult” problems will be required in the short term.

### Exercises
3.3. Let $FACTOR=\{N|N=pq,\text{ for integers }p,q>1\}$
	a) $\text{Is }N=23\in FACTOR?$
	b) $\text{Is }N=337\in FACTOR?$
	c) $\text{Is }N=101\in FACTOR?$
3.4 Let $ORDER=\{\langle N,g,t\rangle|t$ is the smallest positive integer such that $g^t\equiv1\mod N\}$
	a) $\mathrm{Is}\:\langle13,6,12\rangle\in ORDER?$
	b) $\mathrm{Is}\:\langle13,3,6\rangle\in ORDER?$
	c) $\mathrm{Is}\:\langle13,3,3\rangle\in ORDER?$
	d) $\mathrm{Is}\:\langle11,8,9\rangle\in ORDER?$
	e) $\mathrm{Is}\:\langle33,5,10\rangle\in ORDER?$
	f) $\mathrm{Is}\:\langle33,5,32\rangle\in ORDER?$