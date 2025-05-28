---
title: Complete Study Guide - PPLX
author:
  - Jon Marien
created: 2025-04-17
published: 2025-04-17
tags:
  - classes
  - MATH36206
---

| Title                       | Author                       | Created        | Published      | Tags                                               |
| --------------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Complete Study Guide - PPLX | <ul><li>Jon Marien</li></ul> | April 17, 2025 | April 17, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |

---

### Comprehensive Study Notes for Advanced Cryptology (Weeks 8–12)

## **1. NP-Complete Problem-Based Cryptosystems**

### **Key Concepts**
- **Subset-Sum Problem**: Given a set $S = \{s_1, s_2, ..., s_n\}$ and target $t$, determine if a subset of $S$ sums to $t$. NP-complete, so worst-case complexity is $O(2^n)$.
- **Superincreasing Sequence**: Each term exceeds the sum of all previous terms. Subset-sum is solvable in $O(n)$ for these sequences using a greedy algorithm.
- **Trapdoor Function**: Transforms a superincreasing sequence into a "hard" public key using modular arithmetic. Example: $a_i = v \cdot s_i \mod u$, where $\gcd(u, v) = 1$.
- **Merkle-Hellman Knapsack Cipher**:
  - **Public Key**: Trapdoor set $A = \{a_1, a_2, ..., a_n\}$.
  - **Private Key**: Superincreasing sequence $S$, $u$, $v$.
  - **Encryption**: $t' = \sum b_i a_i$, where $b_i \in \{0,1\}$.
  - **Decryption**: Compute $t = t' \cdot v^{-1} \mod u$, then solve the easy subset-sum for $S$.

### **Example: Merkle-Hellman Encryption/Decryption**
- Let $S = \{3, 5, 9, 18\}$, $u = 672$, $v = 13$. Public key: $A = \{39, 65, 117, 234\}$.
- Encrypt $1101$: $t' = 39 + 65 + 234 = 338$.
- Decrypt $t' = 338$: Compute $t = 338 \cdot 517 \mod 672 = 242$. Solve $3 + 9 + 75 + 155 = 242$.

### **Security & Weaknesses**
- **Security Basis**: Relies on subset-sum’s NP-hardness without the trapdoor.
- **Quantum Resistance**: **No**—broken by lattice reduction attacks (e.g., Lenstra-Lenstra-Lovász algorithm).
- **Weaknesses**: Key size, non-unique decryption, and vulnerability to lattice attacks.

---

## **2. Hash-Based Signature Schemes**

### **Lamport Signatures**
- **Key Generation**: Generate $2k$ private keys $y_{i,j}$ and compute public keys $z_{i,j} = h(y_{i,j})$.
- **Signing**: For message $b_1b_2...b_k$, reveal $y_{i,b_i}$.
- **Verification**: Check $h(y_{i,b_i}) = z_{i,b_i}$.

### **Merkle Signatures**
- **Merkle Tree**: Binary tree where leaf nodes are hashes of keys, and internal nodes are hashes of children.
- **Signing**: Reveal the key, signature, and sibling hashes along the path to the root.
- **Verification**: Recompute the root hash from the provided path.

### **Example: Lamport with $h(x) = 7^x \mod 11$**
- Private keys: $y_{1,0} = 3$, $y_{1,1} = 7$.
- Public keys: $z_{1,0} = 2$, $z_{1,1} = 6$.
- Sign "1": Reveal $y_{1,1} = 7$. Verify $7^7 \mod 11 = 6$.

### **Security & Weaknesses**
- **Security Basis**: Collision-resistant hash functions.
- **Quantum Resistance**: **Yes**—no known quantum attacks on hashes.
- **Weaknesses**: One-time use (Lamport), large key sizes.

---

## **3. Learning With Errors (LWE) & Regev Cryptosystem**

### **LWE Problem**
- Given $(a_i, b_i = \langle a_i, s \rangle + e_i \mod q)$, find secret $s$. Errors $e_i$ are small and random.
- **Hardness**: Reduces to worst-case lattice problems; resistant to quantum attacks.

### **Regev Cryptosystem**
- **Encryption**: For bit $x$, ciphertext $(a, b) = (\sum a_i, \sum b_i + \lfloor q/2 \rfloor x)$.
- **Decryption**: Compute $x^* = b - \langle a, s \rangle \mod q$. If $x^*$ is closer to $\lfloor q/2 \rfloor$, output 1.

### **Example: Regev Encryption**
- Let $q = 11$, $s = (1, 2)$, public key samples: $((5, 8), 7)$, $((3, 6), 3)$.
- Encrypt "1" with $S = \{1, 2\}$: $a = (5+3, 8+6) = (8, 3)$, $b = 7 + 3 + 6 = 16 \mod 11 = 5$.
- Decrypt $(8, 3, 5)$: $x^* = 5 - (8 \cdot 1 + 3 \cdot 2) = -9 \mod 11 = 2$. Closer to 0, so $x = 0$.

### **Security & Weaknesses**
- **Quantum Resistance**: **Yes**—based on LWE hardness.
- **Weaknesses**: Large ciphertexts, sensitivity to error distribution.

---

## **4. Module-LWE (MLWE) & Kyber**

### **Kyber Cryptosystem**
- **MLWE**: Uses polynomial rings $R_q = \mathbb{Z}_q[x]/(x^n + 1)$. Secrets are vectors of polynomials.
- **Encryption**: $(u, v) = (A^T r + e_1, t^T r + e_2 + m)$, where $m$ is scaled by $\lfloor q/2 \rfloor$.
- **Decryption**: $m^* = v - s^T u$, then thresholding.

### **Example: Kyber Encryption**
- Let $f(x) = x^3 + 1$, $q = 7$, $A = \begin{bmatrix} 6x^2 + x & 4x + 3 \end{bmatrix}$, $t = [3x^2 + 5x]$.
- Encrypt "101" ($m = 3x^2 + 3$): 
  - $u = A^T r = 6x^2 + x$, $v = t^T r + 6x + 3x^2 + 3$.
  - Ciphertext: $(6x^2 + x, 6x^2 + 4x + 3)$.

### **Security & Weaknesses**
- **Quantum Resistance**: **Yes**—MLWE is lattice-based.
- **Weaknesses**: Complex polynomial arithmetic, side-channel attacks.

---

## **5. McEliece Cryptosystem**

### **Error-Correcting Codes**
- **Goppa Codes**: $[n, k, d]$-code with efficient decoding. Example: `$$` Hamming code.
- **McEliece**:
  - **Public Key**: Scrambled generator matrix $G' = SGP$.
  - **Encryption**: $y = xG' + e$, where $e$ has weight $t$.
  - **Decryption**: Decode $yP^{-1}$ to correct errors, then compute $x = x_0S^{-1}$.

### **Example: McEliece with Hamming Code**
- Let $G = \begin{bmatrix} 1 & 1 & 1 & 1 & 0 & 0 & 0 \end{bmatrix}$, error $e = 0000100$.
- Encrypt "1101": $y = 1101 \cdot G + e = 0110110$.
- Decrypt: Correct error to $0110010$, decode to $x_0 = 1101$.

### **Security & Weaknesses**
- **Quantum Resistance**: **Yes**—based on decoding hardness.
- **Weaknesses**: Large keys (megabytes), performance overhead.

---

## **6. Summary Tables**

### **Classical vs. Post-Quantum Schemes**
| **Scheme**         | **Security Basis** | **Quantum Resistance** | **Key Size**      |
|---------------------|--------------------|------------------------|--------------------|
| RSA                 | Factoring          | No                     | Moderate           |
| Merkle-Hellman      | Subset-Sum         | No                     | Small              |
| Kyber (MLWE)        | Lattice            | Yes                    | Small              |
| McEliece            | Code Decoding      | Yes                    | Very Large         |
| Lamport             | Hash Functions     | Yes                    | Large              |

### **Algorithm Complexity**
| **Scheme**         | **Encryption** | **Decryption** | **Attack Complexity** |
|---------------------|----------------|----------------|------------------------|
| Merkle-Hellman      | $O(n)$     | $O(n)$     | $O(2^{n/2})$       |
| Regev (LWE)         | $O(n)$     | $O(n)$     | $O(2^n)$           |
| Kyber               | $O(n \log n)$| $O(n \log n)$| $O(2^n)$         |
| McEliece            | $O(n^2)$   | $O(n)$     | $O(2^{n})$         |

---

## **7. Exam-Style Exercises**

### **Exercise 1: Merkle-Hellman Decryption**
- Given $t' = 386$, $u = 215$, $v = 137$, find $v^{-1} \mod u$ and decrypt.
  - **Solution**: $v^{-1} = 113$, $t = 386 \cdot 113 \mod 215 = 188$. Subset-sum: $188 = 107 + 52 + 25 + 4 \rightarrow 10100110$.

### **Exercise 2: LWE Decryption**
- Solve $(12x + 5y \equiv 5 \mod 19)$, $(9x + 16y \equiv 11 \mod 19)$.
  - **Solution**: $x = 14$, $y = 13$.

### **Exercise 3: Kyber Polynomial Operations**
- Multiply $(3x^2 + x)$ and $(x + 1)$ modulo $x^3 + 1$.
  - **Result**: $3x^3 + 4x^2 + x \equiv 4x^2 + x - 3 \mod 7$.

---

**Weaknesses & Attacks**: Highlight lattice attacks on Merkle-Hellman, side-channel vulnerabilities in Kyber, and McEliece’s key size inefficiency. Use examples from provided quizzes for step-by-step clarity
