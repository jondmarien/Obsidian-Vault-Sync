Here's a simplified breakdown of each quiz question with key concepts and solution strategies:

---

## Quiz 1 - Elliptic Curves

### 1. Point Addition on Elliptic Curve $y^2 = x^3 -7x +10 \mod 7$

**Goal**: Find $P + Q$ where  P=(1,2) , $ Q=(3,4).
- **Formula**: Use slope $$ \lambda = \frac{y_Q - y_P}{x_Q - x_P} \mod 7 $$
- **Steps**:
  1. Calculate slope: $$ \lambda = (4-2)(3-1)^{-1} \mod 7 = 2 \cdot 4 \mod 7 = 1 $$
  2. Compute $$ x_3 = \lambda^2 - x_P - x_Q \mod 7 = 1 - 1 - 3 = -3 \equiv 4 \mod 7 $$
  3. Compute $$ y_3 = \lambda(x_P - x_3) - y_P \mod 7 = 1(1-4) - 2 = -5 \equiv 2 \mod 7 $$
- **Result**: $$ P + Q = (4, 2) $$
  🧠 *Key concept: Modular inverses and slope formulas for non-vertical points.*

---

### 2. ECC Digital Signature (ECDSA)
**Goal**: Sign message $x$ with hash $h(x)=2$, $k=2$, $m=7$

- **Steps**:
  1. **Compute $$ kA = 2(7,2) $$
     - Use point doubling formula $$ \lambda = \frac{3x_A^2 + a}{2y_A} \mod 11 = \frac{3(7)^2 + 1}{4} \mod 11 = 4 $$
     - $$ x_3 = \lambda^2 - 2x_A \mod 11 = 4^2 - 14 = 2 $$
     - $$ y_3 = \lambda(x_A - x_3) - y_A \mod 11 = 4(7-2) - 2 = 18 \equiv 7 \mod 11 $$
     - $$ kA = (2,7) $$$$ r = 2 \mod 13 = 2 $$
  2. **Compute $s$**
  $$ s = (h(x) + m \cdot r) \cdot k^{-1} \mod 13 = (2 + 7 \cdot 2) \cdot 2^{-1} \mod 13 = 16 \cdot 7 \mod 13 = 8 $$
- **Signature**: $$ (r, s) = (2, 8) $$
  🧠 *Key concept: Point doubling for key generation and modular inverses for signature calculation.*

---

## Quiz 2 - Pollard $$ p-1 $$ and Lenstra
### 1. Pollard $$ p-1 $$ Factorization of $$ N = 1403 $$
**Goal**: Factor $$ N $$ using $$ B=5 $$.
- **Steps**:
  1. Compute $$ a = 2^{5!} \mod 1403 $$:
     - Use successive squaring: $$ 2^{120} \mod 1403 = 793 $$.
  2. Compute $$ \gcd(793 - 1, 1403) = \gcd(792, 1403) = 61 $$.
  3. Factor: $$ 1403 = 61 \times 23 $$.  
  🧠 *Key concept: Smoothness of $$ p-1 $$ (here, $$ 60 = 61-1 $$ divides $$ 5! $$).*

---

### 2. Lenstra EC Factorization of $$ N = 221 $$
**Goal**: Compute $$ 2P $$ on $$ y^2 = x^3 + 3x + 72 \mod 221 $$, $$ P=(101,85) $$.
- **Steps**:
  1. Calculate slope $$ \lambda = \frac{3x_P^2 + 3}{2y_P} \mod 221 $$:
     - $$ \lambda = \frac{3(101)^2 + 3}{170} \mod 221 $$.
  2. Find $$ 170^{-1} \mod 221 $$:
     - $$ \gcd(170, 221) = 17 \neq 1 $$, so $$ N $$ splits as $$ 17 \times 13 $$.  
  🧠 *Key concept: Non-invertible denominators during point operations reveal factors.*

---

## Quiz 3 - Shor's Algorithm
### 1. Factor $$ N = 893 $$ with $$ g = 657 $$
**Goal**: Find period $$ t $$, then factors.
- **Steps**:
  1. Compute $$ g^t \mod 893 = 1 $$. Find $$ t=6 $$.
  2. $$ a = 657^{6/2} - 1 = 703 $$, $$ b = 657^{6/2} + 1 = 705 $$.
  3. $$ \gcd(893, 703) = 19 $$, $$ \gcd(893, 705) = 47 $$.  
  🧠 *Key concept: Period-finding via modular exponentiation and even $$ t $$.*

---

### 2. Why $$ N = 169 $$ Fails with $$ g = 22 $$
- **Reason**: $$ g^t \mod 169 $$ yields $$ t=3 $$ (odd), making $$ g^{t/2} $$ non-integer.  
  🧠 *Key concept: Shor's requires even $$ t $$.*

---

## Quiz 4 - Pratt Certificates
### 1. Pratt Certificate for $$ N = 43 $$
**Verification Steps**:
1. **Prime decomposition**: $$ 43-1 = 42 = 7 \times 3 \times 2 $$.
2. **Check $$ 30^{42} \mod 43 = 1 $$** using successive squaring.
3. Verify $$ 30^{42/p_i} \mod 43 \neq 1 $$ for $$ p_i = 7, 3, 2 $$.  
🧠 *Key concept: Pratt certificates require a primitive root and prime witnesses.*

---

### General Exam Tips:
4. **Elliptic Curves**:
   - Memorize point addition/doubling formulas.
   - Practice modular inverses (e.g., $$ 2^{-1} \mod 7 = 4 $$).
5. **Factorization**:
   - Pollard $$ p-1 $$: Look for $$ B $$ where $$ p-1 $$ is $$ B $$-smooth.
   - Lenstra: Compute until a GCD ≠ 1 appears.
6. **Shor’s Algorithm**:
   - Always check if $$ t $$ is even.
7. **Pratt Certificates**:
   - Verify $$ g^{N-1} \equiv 1 \mod N $$ and $$ g^{(N-1)/p_i} \neq 1 \mod N $$.

Let me know if you’d like a deeper dive into any specific method!

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/edf3d024-ae3e-4cdd-8fa8-801e9f27f1d3/MATH36206-Quiz-1-4.pdf
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/8d2c366e-2a25-4ee0-8a9e-fa0ac82eb357/Quiz-1-4-Solutions.pdf
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_24431ac3-f920-4fb4-ab61-585bd0ff2547/5d193531-fa3b-4515-9650-60fc4704f6ef/MATH36206-Quiz-1-4.pdf
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/edf3d024-ae3e-4cdd-8fa8-801e9f27f1d3/MATH36206-Quiz-1-4.pdf