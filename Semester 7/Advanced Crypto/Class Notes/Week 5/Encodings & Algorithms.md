---
title: S2 - Encodings & Algorithms
author:
  - Jon Marien
created: 2025-02-05
published: 2025-02-05
tags:
  - classes
---

| Title                       | Author                       | Created           | Published         | Tags                   |
| --------------------------- | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| S2 - Encodings & Algorithms | <ul><li>Jon Marien</li></ul> | February 05, 2025 | February 05, 2025 | [[#classes\|#classes]] |

# Session 2
## Encodings
Let the **encoding** of an object into it's representation as a string be $\langle\:object\:\rangle$ 

### Examples of Encodings
If $\langle\:card\:\rangle$ = $[suit,\:value]$, then ![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-08-51-28.webp) = $[♣,\:5]$

If $G$ is a graph and $⟨\:G\:⟩$ = $[V,\:E]$, then ![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-08-52-38.webp) = $[{A,\:B,\:C,D},\;{(A,\:B),(A,\:C),(B,\:D)}]$

## Languages
Let a set of encodings be a **language**.

### Examples of Languages
Let $CARDS = \{⟨card⟩|card$ is in a standard deck of 52 cards$\}$ be the language of a deck of cards.

Let $CONNECTED = \{⟨G⟩|G$ is a connected undirected graph$\}$ be the language of all connected undirected graphs.

Let $FACTOR = $\{N |N = pq$, for integers $p, q > 1\}$ be the language of all composite positive integers.

Let $ORDER = $\{⟨N, g, t⟩|t$ is the smallest positive integer such that $g^t ≡ 1\;mod\;N\;\}$ be the language of all positive integers $N,\:g,\:t$ where $t$ is the smallest positive integer such that $g^t ≡ 1\:mod\:N$.

#### Describing Languages
$CARDS$ is the language of a standard deck of 52 cards, so we can describe it trivially by listing all the encodings of the 52 cards: $A = {[♣, 1], [♣, 2], ..., [♢, 4], [♢, 5], ..., [♡, 8], [♡, 9], ..., [♠, 12], [♠, 13]}$.

#### Describing Languages Using Algorithms
The languages $CONNECTED$, $FACTOR$, and $ORDER$ all contain an infinite number of encodings, so we cannot list all the encodings to describe these languages. Instead we use an **algorithm to determine membership** in the language. Such an algorithm is called a **decider** for the language.

## Algorithms
Let an **algorithm** for a language be a set of instructions that determine membership in the language.

### Examples of Algorithms
```python
def Trial_Division(N):
	import math
	for p in range(2,int(math.sqrt(N))):
		if N%p == 0:
			return(p)
		return('prime' )

print(Trial_Division(1049))
print(Trial_Division(1309))
```
Output:
`prime`
`7`

"`Trial Division(N)`" is an exponential time algorithm that decides $FACT OR$.

The number of steps required for this algorithm **depends** on the size of the input integer $N$ because the full range of $2$ to $\sqrt{N}$ may be searched for a factor $p$.

For an input of say $N = 1049$ (an 11-bit integer), the algorithm takes **31** steps to determine that $N$ is prime (and therefore $N\not\in FACTOR$). But $31 ≈ \sqrt211 = \frac{211}{2}$ which is $O(2^n)$ where $n$ is the input size in bits. 

Because the only know algorithms for $FACTOR$ are exponential time or $O(2^n)$, it is **not possible** to decide $FACTOR$ efficiently in polynomial time.

##### Exercises
![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-09-08-44.webp)

> [!check]- Answers
> ![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-09-09-32.webp)
> ![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-09-09-44.webp)
> ![](S2%20-%20Encodings%20&%20Algorithms-February-5th-2025-09-09-53.webp)