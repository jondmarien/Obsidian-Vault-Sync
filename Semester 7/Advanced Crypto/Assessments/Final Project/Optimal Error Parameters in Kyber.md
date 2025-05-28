---
title: Optimal Error Parameters in Kyber
author:
  - Jon Marien
  - Jillian Moorcroft
created: 2025-04-05
published: 2025-04-05
tags:
  - classes
  - MATH36206
---

| Title                             | Author                                                 | Created        | Published      | Tags                                               |
| --------------------------------- | ------------------------------------------------------ | -------------- | -------------- | -------------------------------------------------- |
| Optimal Error Parameters in Kyber | <ul><li>Jon Marien</li><li>Jillian Moorcroft</li></ul> | April 05, 2025 | April 05, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |

# **Comprehensive Analysis of Optimal Error Parameters in Kyber/Regev Cryptosystems**

---

## **1. Mathematical Foundations \& Parameter Design**

### **1.1 LWE/MLWE Problem Formulation**
Kyber’s security relies on the **Module-LWE (MLWE)** problem over polynomial rings
$$R_q = \mathbb{Z}_q[x]/(f(x))$$where:

- $f(x) = x^{256} + 1$ (cyclotomic polynomial)
- $q = 3329$ (prime modulus)
- Secret vector$\mathbf{s} \in R_q^k$, error vectors $\mathbf{e}, \mathbf{e}_1, \mathbf{e}_2$

The public key is $(\mathbf{A}, \mathbf{t} = \mathbf{A}\mathbf{s} + \mathbf{e})$, where $\mathbf{A}$ is a random matrix in $R_q^{k×k}$. Decryption fails when accumulated errors exceed $\lfloor q/4 \rfloor$.

### **1.2 Error Distribution Mechanics**
Kyber uses **centered binomial distributions** with parameters $\eta_1, \eta_2$:

- Probability mass function:
$$P(X=k) = \binom{\eta + k}{2\eta} 2^{-2\eta}$$
- Key generation uses $\eta_1$, encryption uses$\eta_2$
- Variance $\sigma^2 = \eta/2$, critical for security proofs

**Example**: For `Kyber512` ($\eta_1=3$):

- Max error coefficient magnitude: $3$
- 68% of coefficients fall in $[-2, 2]$

---

## **2. Parameter Optimization: Security vs. Correctness**

### **2.1 Security Analysis**

#### **Lattice Attack Resistance**

Security estimates use **BKZ 2.0** lattice reduction complexity:
$Cost \approx 2^{0.0091 \cdot \beta \log \beta - 0.104 \cdot \beta}$
where$\beta$is the block size. For `Kyber512`:

- Core-SVP hardness: 138.2 bits (MATZOV model) [7]
- Dual attack complexity: $2^{137.5}$(G6K model)[7]

#### **Quantum Resistance**
`Kyber1024` achieves **256-bit quantum security** via:

- MLWE dimension $n=256$
- Module rank $k=4$
- Error width $\eta_2=2$

### **2.2 Decryption Failure Probability ($\delta$)**
Derived via tail bounds of error distributions:
$\delta = \Pr\left[\left|\left|\mathbf{e}^T\mathbf{r} + e_2 - \mathbf{s}^T\mathbf{e}_1\right|\right|_\infty \geq \lfloor q/4 \rfloor\right]$

**Theoretical vs. Real-World Discrepancies**:

- Assumed independence of errors overestimates security
- Fixed public keys increase failure rates by $2^{20} \times$(Prest et al.)[7]
- Formal verification in Isabelle found:
    - Original bounds: $\delta < 2^{-139}$
    - Verified bounds: $\delta < 2^{-137.8}$(0.2% deviation)

---

## **3. Parameter Sets \& Performance Trade-offs**

### **3.1 Kyber Standard Parameters**

| **Parameter**           | **Kyber512**      | **Kyber768**        | **Kyber1024**       |
| :------------------ | :------------ | :-------------- | :-------------- |
| Security Level      | 128-bit       | 192-bit         | 256-bit         |
| $n$                 | 256           | 256             | 256             |
| $k$                 | 2             | 3               | 4               |
| $\eta_1$            | 3             | 2               | 2               |
| $\eta_2$            | 2             | 2               | 2               |
| $(d_u, d_v)$        | (10,4)        | (10,4)          | (11,5)          |
| $\delta$            | $2^{-139}$    | $2^{-164}$      | $2^{-174}$      |
| **Ciphertext Size** | **768 bytes** | **1,088 bytes** | **1,536 bytes** |

### **3.2 Efficiency Improvements**
**Lattice Quantizers** (Zhang et al.[4]):

- Reduce ciphertext size by **36.47%**
- Lower $\delta$ by **299×** via Voronoi cell optimization
- Maintain same $(q, k, \eta_1, \eta_2)$ as standard Kyber

---

## **4. Attack Surface \& Mitigations**

### **4.1 Key Recovery Attacks**

#### **Primal Attack (uSVP)**
- Converts MLWE to unique shortest vector problem
- `Kyber512` security margin: **9.2 bits** (below NIST’s 143-bit threshold[7])
- Countermeasure: Increase $\eta_1$ to 3 (as in `Kyber512`)

#### **Weak Ciphertext Attacks**
- Requires $2^{64}$ decryption queries to achieve 50% success rate
- NIST limits queries to $2^{48}$, making attacks impractical[7]

### **4.2 Side-Channel Vulnerabilities**

**Single-Trace Attacks** (Guo et al.[7]):
- Target polynomial multiplication in` masked_poly_frommsg()`
- 95% recovery accuracy using 86% fewer traces than majority voting
- Mitigation: Constant-time NTT implementations

**Fault Injection (Roulette Attack)**:
- Glitch clock to skip instructions during decapsulation
- Full key recovery in 5 days on ARM Cortex-M4[7]
- Defense: Hardware redundancy checks

---

## **5. Implementation Considerations**

### **5.1 NTT Optimization**

Kyber uses **Number Theoretic Transform** for polynomial multiplication:

- $\mathcal{O}(n \log n)$ vs. naive $\mathcal{O}(n^2)$
- 256-point NTT reduces encryption time by 63%

### **5.2 Code Requirements**

While Python isn’t preferred, exemplary code would:

- Precompute error distributions using$`numpy.random.binomial`$
- Implement decryption failure simulation:

```python
def decrypt_failure_prob(eta1, eta2, q):
    errors = binomial(2*eta1, 0.5) - eta1 
    + binomial(2*eta2, 0.5) - eta2
    return np.mean(np.abs(errors) &gt;= q//4)
```

---

## **6. Open Problems \& Future Work**

1. **Tighter Failure Bounds**: Address independence assumptions in $\delta$ calculations
2. **Parameter Agility**: Develop dynamic $\eta$ adjustment for quantum supremacy transitions
3. **HW-SW Co-design**: Optimize lattice quantizers for FPGA/ASIC implementations

---

# **Presentation-Ready Slides**:
- **Slide 1**: Kyber parameter comparison table + error distribution visual
- **Slide 2**: Decryption failure equation + real-world vs theoretical δ
- **Slide 3**: Lattice quantizer performance gains (Zhang’s data)
- **Slide 4**: Attack surface diagram + mitigation strategies

[^1]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/a762ab6c-9bf3-402f-998f-0d480908ca5c/MATH36206-Project.pdf

[^2]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/d23747c7-3a8f-4730-b501-6809baed290f/message.txt

[^3]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_24431ac3-f920-4fb4-ab61-585bd0ff2547/30e6cbd9-88e7-468a-b568-a934898dd95e/Week_11.pdf

[^4]: https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_24431ac3-f920-4fb4-ab61-585bd0ff2547/2e4582e6-a852-4f8f-bca4-fc3a8074511a/Week_10.pdf

[^5]: https://pq-crystals.org/kyber/data/kyber-specification-round3-20210131.pdf

[^6]: https://cryptojedi.org/papers/kybernistr1-20171130.pdf

[^7]: https://eprint.iacr.org/2023/1952.pdf

