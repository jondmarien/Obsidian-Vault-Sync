---
title: Midterm Prep
author:
  - Jon Marien
created: 2025-02-15
published: 2025-02-15
tags:
  - classes
---

| Title        | Author                       | Created           | Published         | Tags                   |
| ------------ | ---------------------------- | ----------------- | ----------------- | ---------------------- |
| Midterm Prep | <ul><li>Jon Marien</li></ul> | February 15, 2025 | February 15, 2025 | [[#classes\|#classes]] |
<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Comprehensive Walkthrough of Cryptology Problems for Midterm Preparation

---

This report provides a detailed, step-by-step explanation of the attached cryptology problems, covering elliptic curve operations, Pollard p-1 factorization, Lenstra's elliptic curve method (ECM), Shor's algorithm, and Pratt primality certificates. Each solution is analyzed with mathematical rigor and implementation-level details to ensure full understanding of the underlying principles and computational techniques.

---

## Elliptic Curve Arithmetic and Digital Signatures

### Problem 1: Elliptic Curve Point Addition

**Task**: Compute $$
P + Q
$$ on the curve $$
E: y^2 = x^3 - 7x + 10 \mod 7
$$, where $$
P = (1, 2)
$$ and $$
Q = (3, 4)
$$.

**Solution**:

1. **Calculate the slope $$
\lambda
$$**:

$$
\lambda = \frac{y_2 - y_1}{x_2 - x_1} \mod 7 = \frac{4 - 2}{3 - 1} \mod 7 = \frac{2}{2} \mod 7
$$

The inverse of $$
2 \mod 7
$$ is $$
4
$$ (since $$
2 \cdot 4 = 8 \equiv 1 \mod 7
$$), so:

$$
\lambda = 2 \cdot 4 \mod 7 = 8 \mod 7 = 1
$$
2. **Compute $$
x_3
$$**:

$$
x_3 = \lambda^2 - x_1 - x_2 \mod 7 = 1^2 - 1 - 3 \mod 7 = -3 \mod 7 = 4
$$
1. **Compute $$
y_3
$$**:

$$
y_3 = \lambda(x_1 - x_3) - y_1 \mod 7 = 1(1 - 4) - 2 \mod 7 = -3 - 2 \mod 7 = -5 \mod 7 = 2
$$

**Result**: $$
P + Q = (4, 2)
$$.

**Key Insight**: Point addition on elliptic curves uses the chord-tangent method, where the line connecting $$
P
$$ and $$
Q
$$ intersects the curve at a third point, which is reflected to obtain the sum[^1][^2].

---

### Problem 2: ECDSA Signature Generation

**Task**: Sign a message with hash $$
h(x) = 2
$$ using the elliptic curve $$
E: y^2 = x^3 + x + 6 \mod 11
$$, public key $$
A = (7, 2)
$$, private key $$
m = 7
$$, and random $$
k = 2
$$.

**Solution**:

2. **Compute $$
kA = 2A
$$**:
    - **Slope $$
\lambda
$$**:

$$
\lambda = \frac{3x_1^2 + a}{2y_1} \mod 11 = \frac{3(7^2) + 1}{2 \cdot 2} \mod 11 = \frac{148}{4} \mod 11
$$

Simplify numerator: $$
148 \mod 11 = 4
$$. Inverse of $$
4 \mod 11
$$ is $$
3
$$:

$$
\lambda = 4 \cdot 3 \mod 11 = 12 \mod 11 = 1
$$
    - **New coordinates**:

$$
x_3 = \lambda^2 - 2x_1 \mod 11 = 1 - 14 \mod 11 = -13 \mod 11 = 9
$$

$$
y_3 = \lambda(x_1 - x_3) - y_1 \mod 11 = 1(7 - 9) - 2 \mod 11 = -4 \mod 11 = 7
$$

**Result**: $$
kA = (9, 7)
$$.
3. **Signature components**:
    - $$
r = x_3 \mod q = 9 \mod 13 = 9
$$
    - $$
s = (h(x) + m \cdot r) \cdot k^{-1} \mod q
$$:

$$
s = (2 + 7 \cdot 9) \cdot 2^{-1} \mod 13 = (65) \cdot 7 \mod 13 = 455 \mod 13 = 8
$$

**Result**: Signature $$
(r, s) = (9, 8)
$$.

**Verification**: The verifier computes $$
i = h(x) \cdot s^{-1} \mod q
$$ and $$
j = r \cdot s^{-1} \mod q
$$, then checks if $$
iA + jB = kA
$$[^1][^2].

---

## Integer Factorization Techniques

### Problem 1: Pollard p-1 Factorization of $$
N = 1403
$$

**Task**: Factor $$
N
$$ using $$
B = 5
$$ and determine the maximum usable $$
B
$$.

**Solution**:

4. **Compute $$
2^{5!} \mod 1403
$$** using successive squaring:
    - $$
2^2 \mod 1403 = 4
$$
    - $$
2^4 \mod 1403 = 16
$$
    - $$
2^8 \mod 1403 = 256
$$
    - $$
2^{16} \mod 1403 = 998
$$
    - $$
2^{32} \mod 1403 = 1277
$$
    - $$
2^{64} \mod 1403 = 443
$$
    - Combine: $$
2^{120} = 2^{64+32+16+8} = 443 \cdot 1277 \cdot 998 \cdot 256 \mod 1403 = 793 \mod 1403
$$.
5. **GCD computation**:

$$
\gcd(793 - 1, 1403) = \gcd(792, 1403) = 61
$$

Thus, $$
1403 = 61 \times 23
$$.
6. **Largest $$
B
$$**:
    - Factors of $$
p-1 = 60
$$: $$
2^2 \cdot 3 \cdot 5
$$.
    - Factors of $$
q-1 = 22
$$: $$
2 \cdot 11
$$.
    - $$
B
$$ must include $$
5
$$ but exclude $$
11
$$, so $$
B_{\text{max}} = 10
$$[^1][^2].

---

### Problem 2: Lenstra's ECM for $$
N = 221
$$

**Task**: Factor $$
N
$$ by computing $$
2P
$$ on $$
E: y^2 = x^3 + 3x + 72 \mod 221
$$, where $$
P = (101, 85)
$$.

**Solution**:

7. **Compute slope $$
\lambda
$$**:

$$
\lambda = \frac{3x_1^2 + a}{2y_1} \mod 221 = \frac{3(101^2) + 3}{2 \cdot 85} \mod 221
$$

Simplify numerator: $$
3 \cdot 10201 + 3 = 30606
$$.

Denominator: $$
170
$$.
8. **GCD check**:

$$
\gcd(170, 221) = 17 \quad (\text{via Euclidean algorithm})
$$

Since $$
\gcd \neq 1
$$, $$
N
$$ is factored as $$
221 = 17 \times 13
$$[^1][^2].

---

## Quantum Factorization and Primality Verification

### Problem 1: Shor's Algorithm for $$
N = 893
$$

**Task**: Factor $$
N
$$ using base $$
g = 657
$$.

**Solution**:

9. **Find period $$
t
$$**:

Compute $$
g^t \mod 893
$$:
    - $$
657^6 \mod 893 = 1
$$, so $$
t = 6
$$.
10. **Compute factors**:
    - $$
a = 657^{3} - 1 \mod 893 = 703 \mod 893
$$.
    - $$
b = 657^{3} + 1 \mod 893 = 705 \mod 893
$$.
    - $$
\gcd(893, 703) = 19
$$, $$
\gcd(893, 705) = 47
$$.

**Result**: $$
893 = 19 \times 47
$$[^1][^2].

---

### Problem 2: Pratt Certificate Verification for $$
N = 43
$$

**Task**: Verify the Pratt certificate using successive squaring.

**Solution**:

11. **Check $$
30^{42} \mod 43 = 1
$$** via binary exponentiation:
    - $$
30^2 \mod 43 = 40
$$, $$
30^4 \mod 43 = 9
$$, $$
30^8 \mod 43 = 38
$$, $$
30^{16} \mod 43 = 25
$$, $$
30^{32} \mod 43 = 23
$$.
    - Combine: $$
30^{42} = 30^{32+8+2} = 23 \cdot 38 \cdot 40 \mod 43 = 1
$$.
12. **Verify $$
g^{(N-1)/p_i} \neq 1 \mod N
$$** for primes $$
p_i = 7, 3, 2
$$:
    - $$
30^{6} \mod 43 = 16 \neq 1
$$.
    - $$
30^{14} \mod 43 = 6 \neq 1
$$.
    - $$
30^{21} \mod 43 = 42 \neq 1
$$.

**Conclusion**: $$
N = 43
$$ is prime[^1][^2].

---

## Conclusion

These problems illustrate core cryptology concepts, emphasizing the interplay between algebraic structures, modular arithmetic, and computational algorithms. Mastery of these techniques requires attention to detail in inverse calculations, GCD optimizations, and period-finding in cyclic groups. The solutions provided align with theoretical expectations and validate the correctness of each step through systematic verification.

<div style="text-align: center">⁂</div>

# Comprehensive Explanation of Weeks 5 and 6 Cryptology Content

---

This report provides a granular, line-by-line analysis of time complexity concepts (Week 5) and complexity class relationships (Week 6), following the attached problem solutions. Each mathematical operation and algorithmic step is dissected to ensure foundational understanding.

---

## Week 5: Time Complexity Analysis

### Problem 5.1: Prove $$
3n + 1
$$ is $$
O(n)
$$

**Step 1: Definition Application**

Big-O requires finding constants $$
c > 0
$$ and $$
k \geq 1
$$ such that:

$$
3n + 1 \leq c \cdot n \quad \forall n \geq k
$$

**Step 2: Inequality Simplification**

Divide both sides by $$
n
$$ (valid for $$
n > 0
$$):

$$
3 + \frac{1}{n} \leq c
$$

**Step 3: Constant Selection**

- Let $$
k = 1
$$:

At $$
n = 1
$$:

$$
3(1) + 1 = 4 \leq c \cdot 1 \implies c \geq 4
$$
- For $$
n > 1
$$:

$$
\frac{1}{n} < 1
$$, so $$
3 + \frac{1}{n} < 4
$$. Thus, $$
c = 4
$$ satisfies all $$
n \geq 1
$$.

**Conclusion**: $$
3n + 1 \leq 4n
$$ for $$
n \geq 1
$$, proving $$
3n + 1 \in O(n)
$$.

---

### Problem 5.12: Time Complexity of "answer" Algorithm

**Algorithm Code**:

```python  
def answer(w):
    x = int(w[^1], 2) * 42
    print(x)
```

**Step-by-Step Analysis**:

1. **Input Handling**:
    - $$
w
$$ is a binary string of length $$
n
$$.
    - Extracting $$
w[^1]
$$ (second character) is $$
O(1)
$$ via index access.
2. **Conversion Operation**:
    - `int(w[^1], 2)` converts a single binary digit to decimal:
        - Only 2 possible values (0/1), so $$
O(1)
$$.
1. **Multiplication**:
    - Multiplying by 42: $$
O(1)
$$ arithmetic operation.
2. **Printing**:
    - Outputting an integer: $$
O(1)
$$ (fixed-size value).

**Total Complexity**: $$
O(1) + O(1) + O(1) = O(1)
$$.

---

## Week 6: Complexity Classes and NP-Completeness

### Problem 6.1a: Show $$
FACTOR \in NP
$$

**Definition**:

$$
FACTOR = \{N \mid N = pq \text{ for integers } p, q > 1\}
$$.

**Verifier Construction**:

3. **Certificate**: A factor $$
c
$$ of $$
N
$$ (either $$
p
$$ or $$
q
$$).
4. **Verification Steps**:
- Check $$
1 < c < N
$$: $$
O(1)
$$ via comparison.
    - Verify $$
N \mod c = 0
$$:
        - Division operation: $$
O(\log^2 N)
$$ using schoolbook division[^1][^5].

**Polynomial Runtime**:

- Total steps: $$
O(\log^2 N)
$$, polynomial in $$
N
$$'s bit-length.

**Conclusion**: $$
FACTOR \in NP
$$ since factors serve as polynomial-time verifiable certificates.

---

### Problem 6.3b: Verify $$
\langle 89, 5, 106 \rangle \in DLP
$$ with $$
c=24
$$

**Task**: Confirm $$
5^{24} \equiv 89 \mod 106
$$.

**Step 1: Successive Squaring**

Compute $$
5^{24} \mod 106
$$ efficiently:

5. **Exponent Breakdown**:

$$
24 = 16 + 8
$$, so compute $$
5^{16}
$$ and $$
5^8
$$:
6. **Intermediate Calculations**:
    - $$
5^1 = 5 \mod 106
$$
    - $$
5^2 = 25 \mod 106
$$
    - $$
5^4 = 25^2 = 625 \mod 106 = 625 - 5 \cdot 106 = 625 - 530 = 95
$$
    - $$
5^8 = 95^2 = 9025 \mod 106
$$:

$$
9025 \div 106 = 85 \times 106 = 9010
$$, so $$
9025 - 9010 = 15
$$
    - $$
5^{16} = 15^2 = 225 \mod 106 = 225 - 2 \times 106 = 13
$$
7. **Combine Results**:

$$
5^{24} = 5^{16} \times 5^8 = 13 \times 15 = 195 \mod 106 = 195 - 106 = 89
$$.

**Verification**: $$
195 \equiv 89 \mod 106
$$, confirming the certificate $$
c=24
$$ is valid[^1][^5].

---

### Problem 6.9: $$
SUBSET-SUM \in P \implies P = NP
$$

**Proof Structure**:

8. **NP-Completeness**:

$$
SUBSET-SUM
$$ is NP-complete (shown via reduction from 3-SAT)[^1][^5].
9. **Assumption**:

If $$
SUBSET-SUM \in P
$$, a polynomial-time algorithm exists for it.
10. **Implications**:
    - All NP problems reduce to $$
SUBSET-SUM
$$ in polynomial time (by NP-completeness).
    - Solving $$
SUBSET-SUM
$$ in P-time would allow solving any NP problem in P-time.
11. **Conclusion**:

This would collapse the polynomial hierarchy: $$
P = NP
$$.

---

## Critical Analysis of Problem Reductions

### Example: $$
VERTEX-COVER \leq SET-COVER
$$

**Problem Definitions**:

- $$
VERTEX-COVER
$$: Find $$
k
$$ nodes covering all edges.
- $$
SET-COVER
$$: Find $$
k
$$ subsets covering the universe $$
U
$$.

**Reduction Process**:

12. **Mapping Components**:
    - Let $$
U = E
$$ (edges of the graph).
    - For each vertex $$
v
$$, create subset $$
S_v
$$ containing edges incident to $$
v
$$.
13. **Equivalence Proof**:
    - **Forward**: A vertex cover $$
\{v_1, ..., v_k\}
$$ implies $$
\{S_{v_1}, ..., S_{v_k}\}
$$ covers all edges.
    - **Reverse**: A set cover $$
\{S_{v_1}, ..., S_{v_k}\}
$$ implies $$
\{v_1, ..., v_k\}
$$ is a vertex cover.
14. **Complexity**:
    - Reduction runs in $$
O(|V| + |E|)
$$, polynomial in graph size[^1][^5].

**Significance**:
This reduction preserves problem structure, enabling NP-completeness proofs via existing NP-hard problems.

---

## Conclusion

These analyses demonstrate:

15. **Big-O Mastery**: Selecting optimal constants $$
c, k
$$ requires testing boundary conditions and understanding asymptotic dominance.
16. **NP Verification**: Certificates must enable polynomial-time validation through algorithmic steps like modular arithmetic or subset checks.
17. **Reduction Logic**: Mapping components between problems preserves computational hardness, forming the basis of NP-completeness theory.

The exercises emphasize the practical implications of complexity class separations for cryptography, where problems like $$
FACTOR
$$ and $$
DLP
$$ remain computationally hard under classical computing models.

<div style="text-align: center">⁂</div>

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/1c667a0a-3bea-48a7-9386-fbf571b9eed5/Week_6.pdf

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/ca10fce8-f151-4d11-b0bb-d61b61dc8268/Week_5.pdf

[^3]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/9f38a850-8399-42e8-a239-f12ec49d1a90/How-to-Count-O-n-in-Code.md

[^4]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/ca10fce8-f151-4d11-b0bb-d61b61dc8268/Week_5.pdf

[^5]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/1c667a0a-3bea-48a7-9386-fbf571b9eed5/Week_6.pdf


