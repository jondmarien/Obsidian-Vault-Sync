---
title: EC Digital Signature
author:
  - Jon Marien
created: 2025-01-08
published: 2025-01-08
tags:
  - classes
---

| Title                | Author                       | Created          | Published        | Tags                   |
| -------------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| EC Digital Signature | <ul><li>Jon Marien</li></ul> | January 08, 2025 | January 08, 2025 | [[#classes\|#classes]] |

# EC DS

## Basic Info

- A point *P* is selected on an elliptic curve
- That point is multiplied by a number, thus creating a new point on the curve *aP*.
- The new point on the curve is very difficult to find, even with the original point at your disposal. Brute force search requires exponential time.
## Theorem
![](Pasted%20image%2020250108082017.png)
- Suppose $n=\#E(\mathbb{Z}_p)$ is prime, and let $P\in E(\mathbb{Z}_p)$ with $P\neq\overset{}{\infty}$. Then:
	i) $nP=\infty\:$
	ii) The points $\infty,P,2P,3P,...,(n-1)P$ are distinct, and so $E(\mathbb{Z}_p)=\{\infty,P,2P,3P,\ldots,(n-1)P\}$
- *P* is called a generator of $E(\mathbb{Z}_p)$.
- *Note:* $kP=(k\bmod n)P$ for all $k\in\mathbb{Z}$.

- Consider the elliptic curve $E/\mathbb{Z}_{23}:Y^2=X^3+X+4$
- We have $\#E(\mathbb{Z}_{23})=29$. The 29 points in $E(\mathbb{Z}_{23})$ are: (0,2), (0,21), (1,11), (1,12),
(4,7), (4,16), (7,3), (7,20), (8,8), (8, 15), (9,11), (9,12), (10,5), (10,18), (11,9), (11,14),
(13,11), (13,12), (14,5), (14, 18), (15,6), (15,17), (17,9), (18,14), (18,9), (18,14), (22,5),
(22,18), $\infty\:$.
- ![](Pasted%20image%2020250108082652.png)
## Definition
- The **elliptic curve discrete logarithm problem** (ECDLP) is the following:
- The integer `l` is called the **discrete logarithm** of `Q` to the base `P`, written $\ell=\log_PQ$.
# Multiplicative Order
The order of an integer *α mod n* is the smallest positive integer *k* such that *αk ≡ 1 mod n*. For example the order of *3 mod 11* is 5, because *35 ≡ 1 mod 11*.
## DSA

## DSA Signature

## DSA Verification

## Order of a Point
The order of a point *P* on an elliptic curve *E* is the smallest positive integer *k* such that *kP = O* (where *O* is the point at infinity). For example the order of the point **A = (8, 8)** on the elliptic curve, *E*, over $\mathbb{Z}_{11}$ described by $y^2=x^3+x+6\mod11$ is 13, because *13A = O.*

## ECDSA (Elliptic Curve Digital Signature Algorithm)
Let *A* and *B* be points on an elliptic curve where *E* and *A* has prime order *q* and:
$$ B=mA$$
- $\begin{matrix}0\leq m\leq q-1\\\end{matrix}$
- $(A,B,E,q)$ is the public key
- *m* is the private key

## ECDSA Signature
Sign the message *x* using random integer *k* where $1\leq k\leq q-1$, and hash function *h*:
$$ \operatorname{sig}(x,k)=(r,s)$$
- $kA=(u,v)$
- $r=u\mod q$
- $s=(h(x)+mr)k^{-1}\mod q$
## ECDSA Verification
Verify by computing *i* and *j* and checking if *u* $\mathrm{mod}\:q=r$:
$$ \mathrm{ver}(x,(r,s))=\mathrm{true}\quad\Longleftrightarrow\quad u\mod q=r$$
- $i=h(x)s^{-1\mod q}$
- $j=r\cdot s^{-1\mod q}$
- $(u,v)=iA+jB$
### ECDSA Example
Use the elliptic curve, *E*, over $\mathbb{Z}_{11}$ described by $\begin{matrix}y^2=x^3+x+6\mod11\end{matrix}$ to sign a message *x* with hash *h(x) = 2* using the public key ( *A = (8, 8)*, *B = (3, 6)*, *E*, *q = 13*), random *k = 5*, and private key *m = 7*:
$$ kA=5(8,8)=2(8,8)+2(8,8)+1(8,8)$$
$$ \begin{aligned}(8,8)+(8,8):\quad\lambda&=(3(8)^2+1)(2(8))^{-1}\mod11\\&=(193)(5)^{-1}\mod11\\&=(193)(9)\mod11\\&=10\\x_3&=(10^2-8-8)\mod11=7\\y_3&=-10(7-8)-8\mod11=2\end{aligned}$$
$$ \begin{aligned}(7,2)+(7,2):\quad\lambda&=(3(7)^2+1)(2(2))^{-1}\mod11\\&=(148)(4)^{-1}\mod11\\&=(148)(3)\mod11\\&=4\\x_3&=(4^2-7-7)\mod1=2\\y_3&=-4(2-7)-2\mod11=7\end{aligned}$$
$$ \begin{aligned}(2,7)+(8,8):\quad\lambda&=(8-7)(8-2)^{-1}\mod11\\&=(1)(6)^{-1}\mod11\\&=(1)(2)\mod11\\&=2\\x_3&=(2^2-8-2)\mod11=5\\y_3&=-2(5-2)-7\mod11=9\end{aligned}$$
$kA=5(8,8)=(5,9)$
$$ \begin{array}{rl}r=5&\mod13\\=5\end{array}$$
$$ \begin{aligned}s&=(2+7(5))(5)^{-1}\mod13\\&=(37)8\mod13\\&=10\end{aligned}$$
$\mathrm{sig}(x,k)=(r,s)=(5,10)$

Verify $\mathrm{sig}(x,k)=(r,s)=(5,10)$:
$$ \begin{aligned}i&=2(10^{-1})\mod13\\&=2(4)\mod13\\&=8\end{aligned}$$
$$ \begin{aligned}j&=5\cdot10^{-1}\mod13\\&=5\cdot4\mod13\\&=20\mod13\\&=7\end{aligned}$$
$$ \begin{aligned}(u,v)&=8(8,8)+7(3,6)\\&=(5,2)+(10,9)\\&=(5,9)\end{aligned}$$
$\mathrm{ver}(x,(5,10))=\mathrm{true}$ because $\begin{matrix}5&\mathrm{mod}&13=5\end{matrix}$. :LiCheckCheck:

---
## Exercises
1.5) Use the elliptic curve, *E*, over $\mathbb{Z}_{11}$ described by $\begin{matrix}y^2=x^3+x+6\mod11\end{matrix}$ to sign a message *x* with hash $h(x)=4$ using the public key $(A=(2,7), B=(7,2),E  ,q=13)$, random *k = 3*, and private key *m = 7*.
1.6) Determine the values for i and j needed to verify the signature from the previous question.
1.7) Let $\alpha$ be an integer in $\mathbb{Z}_{7}$:
	a) What is the order of $\alpha$ = 2?
	b) What is the order of $\alpha$ = 5?
	c) What is the order of $\alpha$ = 6?
1.8) Let *A* be a point in the elliptic curve, *E*, over $\mathbb{Z}_{7}$ described by $\begin{matrix}y^2=x^3-x+3\mod7\end{matrix}$:
	a) What is the order of A = (4, 0)?
	b) What is the order of A = (5, 2)?
	c) Show that the order of A = (2, 4) is 6.
1.9) Prove that for the DSA:
$$ (\alpha^{e_1}\beta^{e_2}\mod p)\mod q=(\alpha^k\mod p)\mod q$$
1.10) Prove that for the ECDSA:
$$ iA+jB\mod q=kA\mod q$$

> [!check]- Answers
> ![](Exercises%201.2%20Answers.png)

