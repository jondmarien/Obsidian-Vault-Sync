---
author:
- Jon Marien
created: 2025-03-17
published: 2025-03-17
tags:
- classes
- MATH36206
title: Learning With Errors and Regev Cryptosystem
---

| Title | Author | Created | Published | Tags |
|----|----|----|----|----|
| Learning With Errors and Regev Cryptosystem |  | March 17, 2025 | March 17, 2025 |  |

# LWE & Regev

- ☐ INSERT CHAPTER 10.1 ➕ 2025-03-19 ⏫
- ☐ INSERT CHAPTER 10.2 ➕ 2025-03-19 ⏫
- ☐ INSERT CHAPTER 10.3 ➕ 2025-03-19 ⏫
  - ☒ INSERT CHAPTER 10.3.1 and 10.3.2 ✅ 2025-03-19

## Regev Public Cryptosystem (10.3)

### Regev Encrypt Example (10.3.1)

Encrypt the single bit $1$, (i.e., $x=1$) using the Regev cryptosystem with $q=11, S=\{1,3\}$, and the public key: $((5,8,10),7), \;\; ((4,9,1),4),\;\;((3,6,0),3)$.

From the public key we can see that $m=3$, and $n=3$, and also $\left\lfloor  \frac{q}{2}  \right\rfloor=\lfloor 5.5 \rfloor=5$.

We have that:
$$ \begin{aligned}\sum_{i\in S}(a_1,a_2,...a_n)^i&=(5+3,8+6,10+0)\\&=(8,14,10)\\&=(8,3,10)\mod11\\\lfloor q/2\rfloor+\sum_{i\in S}b^i&=5+(7+3)\\&=5+(10)\\&=15\\&=4\mod11\end{aligned}$$
$$\boxed{\therefore \text{the ciphertext is }y=((8,3,10),4)}$$
\### Regev Decrypt Example (10.3.2)
Decrypt the ciphertext $y=((8,3,10),4)$ using the private key: $s=(1,2,3)$:
$$ \begin{aligned}x^{*}&=b-\sum_{j=1}^na_js_j\\&=4-(8(1)+3(2)+10(3))\\&=4-(8+6+30)\\&=4-44\\&=-40\\&=4\mod11\end{aligned}$$

We have that $x^*=4$ is closer to $\left\lfloor  \frac{q}{2}  \right\rfloor = 5$ than $0$ is.

$$\boxed{\therefore \text{the decrypted single bit is ``1'' (i.e., x =1)}}$$

#### Exercises

> \[!todo\]
> \![\[image-139.png\]\]

> \[!check\]-
> \![\[image-140.png\]\]
