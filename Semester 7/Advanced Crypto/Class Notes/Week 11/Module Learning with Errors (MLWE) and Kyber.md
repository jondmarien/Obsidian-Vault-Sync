---
title: Module Learning with Errors (MLWE) and Kyber
author:
  - Jon Marien
created: 2025-03-24
published: 2025-03-24
tags:
  - classes
  - MATH36206
---

| Title                                        | Author                       | Created        | Published      | Tags                                               |
| -------------------------------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Module Learning with Errors (MLWE) and Kyber | <ul><li>Jon Marien</li></ul> | March 24, 2025 | March 24, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |
# Mathematical Knowledge Prerequisites
## Polynomial Rings

## Representing Polynomials as Vectors

## The module $R_q^k$

# MLWE & Kyber Cryptosystem
The Kyber public key cryptosystem was recently selected by NIST for standardization in their Post-Quantum Cryptography (PQC) standardization process. It’s based on the Module Learning with Errors (MLWE) problem, which allows for more efficient encryption of 256 bits per ciphertext. The catch? It involves vectors and matrices of integer polynomials, and implementations require the use of a Number Theoretic Transform (NTT) to handle all the multiplications.

## Recall: LWE Problem
Given $m$ samples, determine all $n$ secrets where:
- the secrets are an $n$-tuple, $s\in(\mathbb{Z}_q)^n\colon\:s=(s_1,s_2,...,s_n).$
- the $m$ samples are of the form: $((a_1,a_2,...,a_n)^i,b^i)\text{, for }1\leq i\leq m.$
- the "right hand side values" are: $b^i=e^i+\sum_{j=1}^na_j^is_j\mathrm{~mod~}q,\mathrm{~for~}1\leq i\leq m.$
- $e^i$ are $m$ random "errors" over the range $-\lfloor q/2\rfloor\text{ to }+\lfloor q/2\rfloor\text{, for }1\leq i\leq m.$
- $q$ is a prime modulus.

### MLWE Problem
Instead of integers in $\mathbb{Z}_q,$ we use polynomials with a polynomial modulus $f(x)$ and coefficients modulus $q$. Also, we use $n$ to denote the maximum degree of the polynomials, and $k$ for the number of polynomials in each vector.

Given matrix $A$ and vector $\vec{t}$  (the samples), determine all $k$ secrets where:
- the **secrets** are a vector of $k$ polynomials: $\vec{s}=(s_1(x),s_2(x),...,s_k(x)).$
- the "**samples**" are a $k\;\cdot\;k$ of polynomials $A$, and a vector of $k$ polynomials $\vec{t}$.
- the "**right hand size values**" are: $\vec{t}=A\vec{s}+\vec{e}.$
- $\vec{e}$ is a vector of $k$ **random polynomial** "errors": $\vec{e}=(e_1(x),e_2(x),...,e_k(x)).$
- $f(x)$ is the **polynomial modulus**.
- $q$ is a **prime modulus** for all polynomial coefficients.

**In other words**, MLWE involves vectors and matrices of elements in the ring of integer polynomials $R_q=\mathbb{Z}_q[x]/\langle f(x)\rangle.$

#### MLWE Example
Find $\vec{t}$ for MLWE with:
$\mathrm f(x)=x^3+1,q=7,A=\begin{bmatrix}6x^2+x,&4x+3\\x^2+5x,&2x\end{bmatrix},\vec{s}=\begin{bmatrix}x^2+1\\x\end{bmatrix},\mathrm{~and~}\vec{e}=\begin{bmatrix}1\\6x^2\end{bmatrix}.$

$$ \begin{aligned}&\vec{t}=A\vec{s}+\vec{e}\\&=\begin{bmatrix}6x^2+x,&4x+3\\x^2+5x,&2x\end{bmatrix}\begin{bmatrix}x^2+1\\x\end{bmatrix}+\begin{bmatrix}1\\6x^2\end{bmatrix}\\&=\begin{bmatrix}(6x^2+x)(x^2+1)+(4x+3)(x)\\(x^2+5x)(x^2+1)+(2x)(x)\end{bmatrix}+\begin{bmatrix}1\\6x^2\end{bmatrix}\\\\&=\begin{bmatrix}3x^2+5x+6\\3x^2+4x+2\end{bmatrix}+\begin{bmatrix}1\\6x^2\end{bmatrix}\\\\&=\begin{bmatrix}3x^2+5x\\2x^2+4x+2\end{bmatrix}\end{aligned}$$
**Note**: All polynomial multiplications and additions are mod $f(x)=x^3+1$ and coefficients are $mod\;q = 7$

## Kyber Public Key Cryptosystem
The kyber public key cryptosystem has:
- the **public** key: $(A,\vec{t}),\mathrm{~where~}\vec{t}=A\vec{s}+\vec{e}.$
- the **private** key: $\vec{s},\text{ where }\vec{s}=(s_1(x),s_2(x),...,s_k(x)).$
- **polynomial modulus** $f(x)$ and **prime modulus** $q$ for all polynomial coefficients.
- **maximum degree** of the polynomials $n$.
- $k$ **polynomials** in each vector.

### Kyber Encryption Example
Encrypt binary "$101$" using a Kyber $n=k=2$ cryptosystem with $f(x)=x^3+1,\;q=7,$ public key $(A,\vec{t})=\left(\begin{bmatrix}6x^2+x,&4x+3\\x^2+5x,&2x\end{bmatrix},\begin{bmatrix}3x^2+5x\\2x^2+4x+2\end{bmatrix}\right)$ and "errors" $\vec{r}=\begin{bmatrix}1\\0\end{bmatrix},\vec{e_1}=\begin{bmatrix}0\\x^2\end{bmatrix},$ and $e_2=6x.$

***Convert Binary to Polynomial and "Upscale":***
Convert "$101$" $\to1x^2+0x+1$.

We "**upscale**" by multiplying $\lfloor q/2\rfloor=\lfloor7/2\rfloor=3{:}\quad3(1x^2+0x+1)=3x^2+0x+3=3x^2+3.$

The message polynomial is $m=3x^2+3$.

#### Kyber Encryption Compute
***compute $\vec{u}$***
$$ \begin{aligned}\vec{\boldsymbol{u}}&=A^\mathrm{T}\vec{r}+\vec{e_1}\\&=\begin{bmatrix}6x^2+x,&4x+3\\x^2+5x,&2x\end{bmatrix}^\mathrm{T}\begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}0\\x^2\end{bmatrix}\\&=\begin{bmatrix}6x^2+x,&x^2+5x\\4x+3,&2x\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}0\\x^2\end{bmatrix}\\&=\begin{bmatrix}6x^2+x\\4x+3\end{bmatrix}+\begin{bmatrix}0\\x^2\end{bmatrix}\\&=\begin{bmatrix}6x^2+x\\x^2+4x+3\end{bmatrix}\end{aligned}$$
***compute $v$***
$$ \begin{aligned}&v=t^\mathrm{T}\vec{r}+e_2+m\\&=\begin{bmatrix}3x^2+5x\\2x^2+4x+2\end{bmatrix}^\mathrm{T}\begin{bmatrix}1\\0\end{bmatrix}+(6x)+(3x^2+3)\\&=\begin{bmatrix}3x^2+5x,&2x^2+4x+2\end{bmatrix}\begin{bmatrix}1\\0\end{bmatrix}+(6x)+(3x^2+3)\\&=(3x^2+5x)1+(2x^2+4x+2)0+(6x)+(3x^2+3)\\&=6x^2+11x+3\\&=6x^2+4x+3\end{aligned}$$

**The ciphertext is** $(\vec{u},v)=\left(\begin{bmatrix}6x^2+x\\x^2+4x+3\end{bmatrix},6x^2+4x+3\right).$

### Kyber Decryption Example
Decrypt $\mathfrak{t}\left(\vec{u},v\right)=\left(\begin{bmatrix}6x^2+x\\x^2+4x+3\end{bmatrix},6x^2+4x+3\right)$ using the private key $\vec{s}=\begin{bmatrix}x^2+1\\x\end{bmatrix}$ with $f(x)=x^3+1\mathrm{~and~}q=7.$

#### Kyber Encryption Compute
***compute $m^*$***
$$ \begin{aligned}m^{*}&=v-\vec{s}^\mathrm{T}\vec{u}\\&=(6x^2+4x+3)-\begin{bmatrix}x^2+1\\x\end{bmatrix}^\mathrm{T}\begin{bmatrix}6x^2+x\\x^2+4x+3\end{bmatrix}\\&=(6x^2+4x+3)-\begin{bmatrix}x^2+1,&x\end{bmatrix}\begin{bmatrix}6x^2+x\\x^2+4x+3\end{bmatrix}\\&=(6x^2+4x+3)-(3x^2+5x+5)\\&=3x^2-1x-2\\&=3x^2+6x+5\end{aligned}$$
So the modified message polynomial (because of the errors) is: $m^* = 3x^2+6x+5$.

***Convert $m^*$ to Binary***
The original 3-bit message in binary was $b_{3}b_{2}b_{1}$. So for each coefficient $c_{i}$ in $m^*$:

$b_i=\begin{cases}0&\text{if }c_i\text{ is closer to }0\text{ than }\lfloor q/2\rfloor\\1&\text{otherwise}\end{cases}\quad\text{for }i\in\{3,2,1\}.$

*We have that:*
$\begin{array}{l}b_3=1\mathrm{~(}c_3=3\text{ is }\underline{\mathrm{not}}\text{ closer to 0 than 3)}\\b_2=0\mathrm{~(}c_2=6\text{ is closer to 0 than 3)}\\b_1=1\mathrm{~(}c_1=5\text{ is }\underline{\mathrm{not}}\text{ closer to 0 than 3)}\end{array}$

The original binary was $b_{3}b_{2}b_{1} \to$ "$101$".

## Standard Kyber Parameters
The three main implementations of Kyber all use a common prime modulus $q = 3329$ and differ mainly in the number of polynomials per vector $k$. Using a polynomial modulus $f(x)$ with degree $n = 256$ allows for $256$ bits of data to be encrypted at a time, which is a huge improvement over Regev(LWE) single bit encryption.

$$ \begin{array}{|c|c|c|c|c|}\hline&n&k&q&\text{security level}\\\hline\text{Kyber}512&256&2&3329&\text{AES}128\\\hline\text{Kyber}768&256&3&3329&\text{AES}192\\\hline\text{Kyber}1024&256&4&3329&\text{AES}256\\\hline\end{array}$$
The actual Kyber implementations use compression parameters for the ciphertexts, $(\vec{u}, v)$, and also have error parameters to control the size of the coefficients of the polynomials in $\vec{s},\vec{e}$ (when making the public/private keys), and in $\vec{r},\vec{e_{1}}, e_{2}$ (when encrypting). In general the coefficients must be much smaller than $q$ for decryption to function reliably.

Finally, due to the nature of MLWE it is possible for Kyber decryption to produce an incorrect result even when only small coefficients are used. The NIST submission for Kyber gives $2^{-139}$ as one of the largest probabilities of this occurring.