---
title: S1 - P, NP, NP-Complete
author:
  - Jon Marien
created: 2025-02-10
published: 2025-02-10
tags:
  - classes
---

| Title                   | Author                       | Created           | Published         | Tags                   |
| ----------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| S1 - P, NP, NP-Complete | <ul><li>Jon Marien</li></ul> | February 10, 2025 | February 10, 2025 | [[#classes\|#classes]] |

# P, NP, & NP-Complete Languages

## The Class $P$
$P$ is the class of languages that are decidable in polynomial time. Some examples can be the following:
- $RELPRIME = \{\langle{a,b}\rangle|\:GCD(a,b) = 1,\: a,b\in\mathbb{Z}^+\}$
- $CONNECTED=\{\langle G\rangle|G\:\text{is a connected undirected graph}\}$
- $PATH=\{\langle G,s,t\rangle|G\text{ is a directed graph that has a path from vertex s to vertex }t\}$
### Proof that $PATH\:\in\:P$
Let the graph $G$ have $m$ vertices given by: $$ v_1,v_2,...,v_{m-1},v_m.$$
In order to prove that $PATH\:\in\:P$, we describe a polynomial time algorithm to solve $PATH$:
- On input $\langle G,s,t\rangle$:
	1. Mark vertex $s$.
	   
	2. Repeat until no new vertices are marked: Scan all edges in $G$. If an edge (${v_a, v_b})$ is found where $v_a$ is marked and $v_b$ is not marked, mark $v_b$.
	   
	3. If $t$ is marked, accept. Otherwise, reject.

If we let $e$ be the number of edges in $G$, we have part 2. We must scan through $e$ edges at most $m$ times. So, $M_{PATH}$ uses at most $1+m\times e+1=2+m\times e$ steps, which is polynomial. $\therefore$ $PATH\:\in\:P$.

## The Class $NP$
$NP$ is the class of languages that have **polynomial time verifiers**.

A verifier for a language $L$ is an algorithm $V$, where: 
- $L =  \{w|V\:\text{accepts}\:\langle{w,c}\rangle\:\text{for some string}\:c\}$
- The string $c$ is the **certificate** (or proof) that $w\in L$.

Some examples of languages that have polynomial time verifies are:
- $FACTOR=\{N|N=pq,\text{ for integers }p,q>1\}$
- $ORDER=\{\langle N,g,t\rangle|t\text{ is the smallest positive integer such that }g^t\equiv1\mod N\}$
- $DLP=\{\langle y,g,N\rangle|\:y\equiv g^x\mod N,\text{ for some }x\in\mathbb{Z}^+\}$
- $\begin{aligned}&HAMPATH=\{\langle G,s,t\rangle|G\mathrm{~is~a~diroctod~graph~that~has~a~Hamiltonian^*~path~from~vertex~}s\\&\mathrm{to~vertex~}t\}\end{aligned}$
*\* A Path that goes through every vertex in the graph **exactly once**.*

### $PATH\:vs.\:HAMPATH$

The languages $PATH$ and $HAMPATH$ are similar problems in that they both involve finding paths in a directed graph. Algorithms exist that solve $PATH$ in polynomial time... but no such algorithms are known to exist that solve $HAMPATH$ in polynomial time.

## $P=NP\:?$
**$P$ languages can be *decided* in polynomial time**.
For example:
- Given two positive integers, we can efficiently decide if they are relatively prime using the Euclidean algorithm.

$NP$ **languages can be *verified* in polynomial time.**
For example: 
- Given a positive integer and a factor of that integer, we can efficiently verify that the integer contains the factor using a verifier. But directly finding the factor efficiently, without using a quantum computer, is not possible (as far as we know).

In general if $L ∈ NP$, it (by definition) has a polynomial time verifier, but we cannot assume that $L$ is also $∈ P$. To establish that $L ∈ P$, a polynomial time algorithm that decides the language must be found.

On one hand, if $P=NP$ then all problems that can be verified in polynomial time can also be decided in polynomial time. Because there are so many problems that can be verified efficiently but require brute force methods to solve, $P=NP$ is generally believed to be false. But it could be that we have yet to discover novel efficient algorithms that can replace brute force search...maybe one day 😉.

On the other hand, if $P \neq NP$, then there must be a problem that can be verified efficiently and a proof that it cannot be decided in polynomial time (in other words, a proof that it can only be solved using brute force search). No such proof is known to exist for any $NP$ problem.

#### Exercises
[Week_6, page 3](Week_6.pdf#page=3&selection=6,0,6,9)

## $NP-Complete$ Problems
A language $B$ is $NP-Complete$ if:
1. $B$ is in $NP$, and
2. Every other language $A$ in $NP$ can be reduced** to $B$.
*\*\* Math details: Language $A$ is **polynomial time mapping** reducible to language $B,\:A\leq_{p}B$, if there is a polynomial time computable function $f:{\Sigma^*}\longrightarrow{\Sigma^*}$, where for every $w\in\Sigma^{*}$,*
$$ w\in A\Longleftrightarrow f(w)\in B$$
The function $f$ is called the polynomial time reduction from $A$ to $B$.
${\Sigma^*}$ is the set of all possible input strings.

## Problem Reductions
In cryptographic applications we are interested in knowing if a “hard problem” (like factoring) can be reduced to a related problem (like order-finding). If algorithms have been developed that can solve the related problem (like Shor’s) then we may have security issues with any cryptosystems that are based on the “hard problem”.

For the purposes of approaching this from an applied point of view (and to simplify the math) we will only show, but not prove, how a problem $A$ can be reduced to problem $B$ using the notation:$$ A\leq B$$To do this we show that any problem in $A$ can be solved by mapping it to a related problem in $B$ without introducing any more “computational difficulty”. Then $A$’s “computational difficulty” must be contained within $B$’s “computational difficulty”.

## Showing that a Language is $NP-Complete$
Suppose we want to show that some new and exiting language, $C$, is $NP-Complete$. 

The conventional (easy) way of doing this is to carefully select another language, $B$, which has been previously proven to be $NP-Complete$. 

The selection of $B$ should be done in a way that makes it possible to reduce $B$ to $C$ (so that $B ≤ C$). 
- Then, if $C$ is in NP, it must be NP-Complete because another NP-Complete language, B, was reduced to it.

The following is a (very short!) list of some languages that have been proven to be $NP-Complete$:
$$SAT=\{\langle\phi\rangle|\phi\mathrm{~is~a~satisfiable~Boolean~formula}\}$$
$$VERTEX-COVER=\{\langle G,k\rangle|G\mathrm{~is~an~undirected~graph~with~a~}k\mathrm{-node~vertex~cover}\}$$
$$HAMPATH=\{\langle G,s,t\rangle|G\text{ is a directod graph that has a Hamiltonian path from }s\text{ to }t\}$$$$SUBSET-SUM=\{\langle S,t\rangle|S=\{x_{1},...,x_{k}\}\mathrm{~and~the~sum~of~some~subset~of~}S\mathrm{~is~}t\}$$

Note that $FACTOR$ and $DLP$ are **not** $NP-Complete$ (**as far as we know**).

## Showing that $SET-COVER\;\in\;\mathrm{NP}$

$$ SET\text{-}COVER=\{\langle U,S,k\rangle|S\text{ is a collection of subsets of }U\text{, and the union of }k\text{ subsets in }S\text{ equals }U\}$$

For example:
$$ \langle\{c,r,y,p,t,o\},\{S_1=\{t,o\},S_2=\{c,r,y\},S_3=\{r,o,y\},S_4=\{c,o,p\}\},3\rangle\in SET\text{-}COVER.$$
This can be verified using the certificate $c = \{S_{1}, S_{2}, S_{4}\}$.

We have that $|c|=3$, and that $S_1\cup S_2\cup S_4=\{t,o\}\cup\{c,r,y\}\cup\{c,o,p\}=\{c,r,y,p,t,o\}$.

A **polynomial time verifier** for $SET-COVER$ is:

On input $\langle$$U,S,k,c\rangle$:
1. Check that the certificate, $c$, consists of exactly $k$ subsets from $S$. If it does not, then reject it.
2. Compute the union of all elements in $c$. If this equals $U$, accept it. Otherwise, reject it.

If $S$ contains $m$ subsets, then part 1. requires at most $m × k$ steps. Part 2. is done once. So this verifier involves at most $mk + 1$ steps which is polynomial, and therefore $SET-COVER ∈ NP$.

## Choosing an $NP-Complete$ Language, $B$, for the Reduction
If we want to show that show $SET-COVER$ is $NP-Complete$, we have to show that every other language $A$ in $NP$ can be reduced to $SET-COVER$.

The easiest way to do this is to find another $NP-Complete$ language, $B$, that is similar to $SET-COVER$, or that has characteristics that allow us to easily show that $B ≤ SET-COVER$. Because $B$ is $NP-Complete$, every other language $A$ in $NP$ can be reduced to $B$, and if $B ≤ SET-COVER$, then every other language $A$ in $NP$ can be reduced to $SET-COVER$. In other words:
$$ A\leq B\leq SET-COVER$$
In this case we’ll choose $B = VERTEX-COVER$ as our $NP-Complete$ language, and reduce it to $SET-COVER$.

## Showing $VERTEX-COVER \leq SET-COVER$
$VERTEX\text{-}COVER=\{\langle G,k\rangle|G\text{ is an undirected graph with a }k\text{-node vertex cover}\}$
$SET\text{-}COVER=\{\langle U,S,k\rangle|S\text{ is a collection of subsets of }U\text{, and the union of }k\text{ subsets in }S\text{ equals }U\}$
A specific problem reduction can be shown with the following graph $G = {V, E}$:
![[image.png]]

A 2-node ($k = 2$) vertex cover for $G$ is $\{d, b\}$.

Let the set $U$ be the edge set, $E$, of the graph: $U=\{(a,b),(b,c),(c,d),(d,a),(d,e)\}$.

For every $v \in V$, let $S_{v}$ contain all edges adjacent to $v$:
- $S_a=\{(d,a),(a,b)\}$
- $S_b=\{(a,b),(b,c)\}$
- $S_c=\{(b,c),(c,d)\}$
- $S_d=\{(c,d),(d,e),(d,a)\}$
- $S_e=\{(d,e)\}$

We then have that $S$ is a collection of subsets of the edges in the graph, $S=\{S_a,S_b,S_c,S_d,S_e\}$, such that the union of the 2 subsets $\{S_{d},S_{b}\}$ equals $U$. 

Then:
$$ \text{A 2-node }(k=2)\text{ vertex cover for }G\text{ is }\{d,b\}\Longleftrightarrow\text{the union of the 2 subsets }\{S_d,S_b\}\text{ equals }U.$$

We have shown a specific problem reduction (only for this specific graph $G$) from $VERTEX-COVER$ to $SET-COVER$.

The general problem reduction from $VERTEX-COVER$ to $SET-COVER$ (which is not limited to any specific graph) is simply:
- Let the set $U$ be the edge set, $E$, of the graph $G = \{V,E\}$.
- For every $v \in V$, let $S_{v}$ contain all edges adjacent to $v$, where $S_{\boldsymbol{v}}\subseteq U$.

Then, $S$ is a collection of subsets of the edges in the graph, $S = \{S_{v1},S_{v2},...\}$ such that:
$$ G\text{ has a k-node vertex cover}\Longleftrightarrow\text{the union of }k\text{ subsets in }S\text{ equals }U$$
$$\therefore VERTEX-COVER \leq SET-COVER$$
## Show $SET-COVER$ is $NP-Complete$
$SET-COVER$ is $NP-Complete$ if:
1. $SET-COVER is in $NP$, and
2. Every other language $A$ in $NP$ can be reduced to $SET-COVER$

In [6.7](#Showing%20that%20$SET-COVER%20;%20in%20;%20mathrm{NP}$) we showed that $SET-COVER$ is in $NP$.

In [6.9](#Showing%20$VERTEX-COVER%20leq%20SET-COVER$) we showed that every other language $A$ in $NP$ can be reduced to $SET-COVER$, by reducing $VERTEX-COVER$ to $SET-COVER$, where $VERTEX-COVER$ is $NP-Complete$.

$$\therefore SET-COVER \text{\;is\;NP-Complete}.$$

### Exercises
[Week_6, page 8](Week_6.pdf#page=8&selection=6,0,6,9)
