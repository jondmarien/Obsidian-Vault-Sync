---
title: S1 - Time Complexity and Big-O Notation
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
---

| Title                                   | Author                       | Created           | Published         | Tags                   |
| --------------------------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| S1 - Time Complexity and Big-O Notation | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |

# Time Complexity and Big-O Notation

## Big-O Notation
Let $f$, $g$ be functions from the set of non-negative integers to non-negative real numbers. We have that $f(n)$ is $O(g(n))$ if integers $c$ and $k$ exist such that for every $n ≥ k$:
$$ f(n)\leq c\:g(n)$$
## Linear Functions
Show that $2n + 3$ is $O(n)$.

Let $k = 1$. Then find $c$ such that for every $n ≥ k$:
$$ \begin{aligned}f(n)&\leq c\:g(n)\\2n+3&\leq c\:n\\2(1)+3&\leq c\:(1)\\5&\leq c\end{aligned}$$
With $c = 5$ and $k = 1$ we have that $2n + 3 ≤ c\;\;n$ for every $n ≥ k$. Therefore $2n + 3$ is $O(n)$.
![](S1%20-%20Time%20Complexity%20and%20Big-O%20Notation-February-3rd-2025-11-44-44.webp)

## Polynomial Functions
Show that $2n^4 + 3n^2 + 1$ is $O(n^4)$.

Let $k = 2$. Then find $c$ such that for every $n ≥ k$:
$$ \begin{aligned}f(n)&\leq c\:g(n)\\2n^{4}+3n^{2}+1&\leq c\:n^{4}\\2(2)^{4}+3(2)^{2}+1&\leq c\:(2)^{4}\\45&\leq c\:16\\\frac{45}{16}&\leq c\\2.8125&\leq c\end{aligned}$$
With $c = 3$ (because $3 ≥ 2.8125$) and $k = 2$ we have that $2n^4 + 3n^2 + 1 ≤ c\;\;n^4$ for every $n ≥ k$. Therefore $2n^4 + 3n^2 + 1$ is $O(n^4)$.
![](S1%20-%20Time%20Complexity%20and%20Big-O%20Notation-February-3rd-2025-11-47-07.webp)

## Logarithmic Functions
Show that $log_{2}(n) + 8$ is $O(log_{2}n)$.

Let $k = 10$. Then find $c$ such that for every $n ≥ k$.
$$ f(n)\leq c\:g(n)$$
$$ \begin{aligned}&\log_2(n)+8\leq c\:\log(n)\\&\log_2(10)+8\leq c\:\log(10)\\&\log_2(10)+8\leq c\:1\\&\log_2(10)+8\leq c\end{aligned}$$
$$ \begin{aligned}3.32...+8&\le c\\11.32...&\le c\end{aligned}$$
With $c = 12$ (because $12 ≥ 11.32...$) and $k = 10$ we have that $log_{2}(n) + 8 ≤ c\;\;log_{2}\;n$ for every $n ≥ k$. Therefore $log_{2}(n) + 8$ is $O(log_{2}\;n)$.
![](S1%20-%20Time%20Complexity%20and%20Big-O%20Notation-February-3rd-2025-11-53-35.webp)

### Practice Exercises
5.1) 
	Show that $3n + 1$ is $O(n)$. 
5.2) 
	Show that $5n + log2(n)$ is $O(n)$. 
5.3) 
	Show that $2n^5 + 3n^4 + 42$ is $O(n^5)$. 
5.4) 
	Show that $(n^2 + 5)(n + 2)$ is $O(n^3)$. 
5.5) 
	Show that $n\;log_{2}\;n$ is $O(n\;log_{2}\;n)$. 
5.6) 
	Show that $n log_{2} n$ is $O(n^2)$. 
5.7) 
	Show that $3n$ is $O(4n)$.
5.8) 
	Show that $3n$ is not $O(2n$). 
5.9) 
	Show that $n! is O(n^n)$. $( n! = n × (n − 1) × ... × 2 × 1 )$.
5.10)  
	Show that $\frac{n^2 + 4n + 3}{n+1}$ is $O(n)$.

## Time Complexity of Algorithms
Consider an algorithm that reads an input string $w$ of length $n$ bits. The time complexity, $f(n)$, of the algorithm is the maximum number of steps that the algorithm will use on any input $w$ of length $n$. We typically use big-O notation to estimate $f(n)$.
### Notation
- $w$: the input 
- $n$: the length of the input in binary. 
- $f(n)$: the maximum number of steps required for an input of n bits. 
- $O(g(n))$: the estimate of the time complexity of the algorithm where $f(n)$ is $O(g(n))$.
#### Example: Time Complexity of a "Search" Algorithm
```python
def search(w):
	i=0
	while w[i]=='0':
		i+1
	return(i)
```
```python
search('000000010000')
```
```
# Output
7
```

This algorithm takes a binary input $w$ of $n$ bits and searches, starting from the first bit, for a “$1$”. The algorithm returns the position of the first “$1$” found and then stops.

So for example, if $w$ = $(000000010000)_{2}$ then $n = 12$ bits. The number of steps required will be $8$ in total ($7$ to check the first “$0$” bits and then one more to find the “$1$”). So in this case when $n = 12$, only $8$ steps are required.

The maximum number of steps required could be $f(n) = n$ steps: when there is a “$1$” in the very last bit, or there are only “$0$”s. So the time complexity of this search algorithm is $O(n)$.

#### Example: Time Complexity of a "Loop" Algorithm
```python
def loop(w):
	for i in range(int(w,2)):
		print(i)
```
```python
loop('1111')
```
```
# Output
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```

This algorithm takes a binary input w and prints every integer (in decimal form) from $0$ to $w − 1$.

So for example, if $w = (1111)_{2}$ then $n = 4$ bits. The number of steps required will be $15$ in total ($print: 0,1,2,...,13,14$ and then stop). So when $n = 4$, $15 ≈ 2^n = 2^4$ steps are required.

#### Example: Time complexity of algorithms that don’t have binary inputs
```python
def loop(N):
	for i in range(N):
		print(i)
```
```python
loop(15)
```
```
# Output
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```
This algorithm takes a decimal input w and prints every integer (in decimal form) from $0$ to $w − 1$. 

So for example, if $N = 15$ then the number of steps required will be $15$ in total ($print: 0,1,2,...,13, 14$ and then stop). 

So the maximum number of steps required for an input $N$ is simply $N$ steps. Using big-O notation we can state (correctly) that this algorithm is $O(N)$. 

But it’s not a linear time algorithm. 

This is because the length of $N$, if it was written in binary, would be $n ≈ log_{2}(N)$ bits, meaning that $N ≈ 2^n$. So we still have a time complexity of $O(2^n)$.