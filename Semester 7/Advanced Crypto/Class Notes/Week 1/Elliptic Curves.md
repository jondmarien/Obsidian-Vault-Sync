---
title: Elliptic Curves
author:
  - Jon Marien
tags:
  - classes
created: 2025-01-06
published: 2025-01-10
---

| Title           | Author                       | Created          | Published        | Tags                   |
| --------------- | ---------------------------- | ---------------- | ---------------- | ---------------------- |
| Elliptic Curves | <ul><li>Jon Marien</li></ul> | January 06, 2025 | January 10, 2025 | [[#classes\|#classes]] |

# Elliptic Curves

## Basic Info
- Discovered in 1985, by Neal Koblitz and Victor Miller (8yrs after RSA)
- Entered wide use in '04-'05
	- Used in Bitcoin, TLS, etc.

## Why ECC?
- **RSA**
	- Secure is based on the hardness of the integer factorization, taking **subexponential time.***
- **ECC**
	- Security is based on the hardness of the ECDLP, taking **fully exponential time.**
- **Elliptic Curve** cryptosystems (**ECC**) can use *smaller parameters* than their counterparts, *while achieving the same security level.*

## Elliptic vs Elliptical
An elliptic curve, *E*, is the set of all points that are solutions to $y^2=x^3+ax+b$, including a point *O* at infinity.

![](Session%201%20-%20Elliptic%20Curves-20250106111141114.webp)

## Example of an Elliptic Curve

Let a = 1, and b = 6. Then the solutions for $y^2=x^3+x+6$ are illustrated as follows:
![](Session%201%20-%20Elliptic%20Curves-20250106111319286.webp)
We can see that $(-1,-2)\in E$ and that $(2,4)\in E$.

## Adding Points on the Curve
Let the addition of any two points, (x1, y1) and (x2, y2) in E be performed by drawing a line between
the points and determining the third point, (x3, y3), where the line intersects the curve... and
then signing the y-coordinate negative (or flip the point about the x-axis).
![](Session%201%20-%20Elliptic%20Curves-20250106112229865.webp)
When we add `(−1,−2)` to `(2, 4)` we get to the point `(3, 6)` which we flip to `(3,−6)`.
So for this particular curve we have that `(−1,−2) + (2, 4) = (3,−6)`.

The line shown is described by the equation $y\:=\:\lambda x+v$, with a slope of $\lambda\:=\:\frac{-2-4}{-1-2}\:=\:2$, and
a y-intercept of `v = 4 − 2(2) = 0`.

## Adding a Point to Itself on the Curve
Adding a point, $(x_1,y_1)$, to itself in `E` is be performed by drawing a tangent line and determining the other point where the tangent line intersects the curve... and then signing the y-coordinate negative (or flip the point about the x-axis).

![](Session%201%20-%20Elliptic%20Curves-20250106113218360.webp)
When we add `(2, 4)` to itself we get to the point `(−1.359,−1.459)` which we flip to `(−1.359, 1.459)`.

So for this particular curve we have that `(2, 4) + (2, 4)` ≈ `(−1.359, 1.459)`.
The line shown is described by the equation $y=\lambda x+v$, with a slope of `λ = 13/8` , and a y-intercept of $v=4-{\frac{13}{8}}(2)=0.75$. 

The slope is obtained by taking the derivative (wait what... calculus in crypto?) of $y^{2}=x^{3}+x+6$ at `x = 2` and `y = 4`:

$$ \begin{aligned}y^{2}&=x^{3}+x+6\\2y^{1}y^{\prime}&=3x^{2}+1+0\\y^{\prime}&=\frac{3x^{2}+1}{2y}\\y^{\prime}&=\frac{3(2)^{2}+1}{2(4)}\\y^{\prime}&=\frac{13}{8}\end{aligned}$$

## Elliptic Curve Equations
Let $P=(x_{1},y_{1})$ and $Q=(x_{2},y_{2})$ be points in *E*. Then $P+Q=R=(x_3,y_3)$ where:

$$\begin{align}
y^2 &= x^3 + ax + b & (1) \\
y &= \lambda x + v & (2) \\
\lambda &= \begin{cases}
    \frac{y_2 - y_1}{x_2 - x_1} & P \neq Q \\
    \frac{3x_1^2 + a}{2y_1} & P = Q
\end{cases} & (3) \\
x_3 &= \lambda^2 - x_2 - x_1 & (4) \\
y_3 &= -\lambda(x_3 - x_1) - y_1 & (5)
\end{align}
$$

### P+Q; P!=Q
$\text{Adding }P=(-1,-2)\text{ to }Q=(2,4)\text{:}$
$$ \begin{aligned}\lambda&=\frac{4-(-2)}{2-(-1)}=2\\x_{3}&=(2)^2-2-(-1)=3\\y_{3}&=-2(3-(-1))-(-2)=-6\end{aligned}$$
We get $R=(3,-6)$.
### P+Q; P=Q (or, P+P)
$\text{Adding }P=(2,4)\text{ to }Q=(2,4)$ {in other words, adding P = (2, 4) to itself}:
$$ \begin{aligned}&\lambda=\frac{3(2)^{2}+1}{2(4)}=\frac{13}{8}\\&x_{3}=(\frac{13}{8})^{2}-2-2=-1.359375\\&y_{3}=-\frac{13}{8}(-1.359375-(2))-(4)\approx1.458984375...\end{aligned}$$
We get $R=(\begin{matrix}-1.359375,1.458984375...\\\end{matrix})$.
### To Infinity!!
Adding $P=(2,4)\text{ to }Q=(2,-4)$:
$$ \lambda=\frac{-4-(4)}{2-(2)}\text{ is undefined}$$
We get `R = O` (the point at infinity).
Note that for any point `P` in `E` we define $P+O=P$, and $O+P=P$.

![](Session%201%20-%20Elliptic%20Curves-20250106124329680.webp)
## Elliptic Curves over $\mathbb{Z}_{p}$
An elliptic curve, `E`, over $\mathbb{Z}_{p}$ is the set of all integer solutions to $y^2\equiv x^3+ax+b\mod p,$, including a point `O` at infinity.

### Example of an Elliptic Curve over $\mathbb{Z}_{p}$
Let a = 1, b = 6, and p = 11. Then the solutions for $y^2=x^3+x+6\mod11$ are illustrated as follows:

![](Session%201%20-%20Elliptic%20Curves-20250106120902785.webp)
We can see that `(−1,−2) ≡ (10, 9) mod 11 ∈ E` and that `(2, 4) ∈ E`. We can’t see the point `O` (because it’s at infinity) but we still count it to determine the number of points in E:
$$ |E|=12+1=13$$
Before when we added these points on the real curve (by determining the line and finding the other point) we got `(−1,−2) + (2, 4) = (3,−6)`. We can still add these points but now we will get `(10, 9) + (2, 4) = (3, 5)`. This is done by ditching the geometrical interpretation (because there is no “line” anymore!) and using equations (3), (4), (5), all `mod p`:
$$ \lambda=\begin{cases}(y_2-y_1)(x_2-x_1)^{-1}\mod p&\quad P\neq Q\\\\(3x_1^2+a)(2y_1)^{-1}\mod p&\quad P=Q\\\\x_3=\lambda^2-x_2-x_1\mod p\\y_3=-\lambda(x_3-x_1)-y_1\mod p\end{cases}$$

#### Real World Example
Find P+Q, using $\begin{matrix}P\neq Q,\:y^2=x^3+x+6\mod11\end{matrix}$
$\mathrm{Adding }\:P=(10,9)\:\mathrm{ to }\:Q=(2,4)\:$:
$$ \begin{aligned}\lambda&=(4-9)(2-10)^{-1}\mod11\\&=(-5)(-8)^{-1}\mod11\\&=(6)(3)^{-1}\mod11\\&=(6)(4)\mod11\\&=24\mod11\\&=2\\x_{3}&=2^{2}-2-10\mod11\\&=-8\mod11\\&=3\\y_{3}&=-2(3-10)-9\mod11\\&=5\end{aligned}$$
We get $R=(3,5)$.

---
## Exercises -- See Paper Notes
1.1) $\text{For the elliptic curve, }E,\text{ described by }y^2=x^3+x+6:$
	a) Is $(-1, 2)\in E$? **Yes.**
	b) Is $(0,\sqrt{6})\in E$? **Yes.**
	c) Is $(4, 2)\in E$? **No.**
	d) Is $(5,\sqrt{136})\in E$? **Yes.**
	e) Evaluate P + Q if P = (3,−6) and Q = (−1, 2) by manually computing the slope, the equation of the line, and the result, R. **R = (2,4)**
	f) Evaluate P + Q if P = Q = (3,−6) by manually computing the slope, the equation of the line, and the result, R. **R = (-5/9, -62/27)**
1.2) $\text{For the elliptic curve, }E,\text{ described by }y^2=x^3-4x+2{:}$
	a) Is $(2, 0)\in E$? **No.**
	b) Is $(0,\sqrt{2})\in E$? **Yes.**
	c) Evaluate P + Q if P = (0, √2) and Q = (2, √2) by manually computing the slope, the equation of the line, and the result, R. **R = (-2, -√2)**
	d) Evaluate P + Q if P = Q = (−0.5, √3.875) by manually computing the slope, the equation of the line, and the result, R. **Need Help.**
1.3) $\mathrm{For~the~elliptic~curve,~}E,\mathrm{~over~}\mathbb{Z}_{11},\mathrm{~described~by~}y^{2}=x^{3}+x+6\mathrm{~mod~}11:$
	a) Evaluate P + Q if P = (8, 8) and Q = (2, 7) by manually computing the slope and the result.
	b) Evaluate 3P if P = (10, 9) by manually computing all slopes and results.
1.4) $\text{For the elliptic curve, }E,\text{ over }\mathbb{Z}_7,\text{ described by }y^2=x^3-4x+2\mod7\text{:}$
	a) Evaluate P + Q if P = (4, 1) and Q = (2, 3) by manually computing the slope and the result.
	b) Evaluate 8P if P = (0, 3) by manually computing all slopes and results.

> [!check]- Answers
> ![](Session%201%20-%20Elliptic%20Curves-20250106124350989.webp)

**Key Concepts:**
- **Elliptic Curve Definition:** An elliptic curve E is defined as the set of all points (x, y) that satisfy the equation y² = x³ + ax + b, including a special point O at infinity.
	- Example: The curve y² = x³ + x + 6 is illustrated with points like (-1, -2) and (2, 4).
- **Point Addition:** A geometric method is presented for adding points on elliptic curves. It involves drawing a line through two points and finding the third intersection point with the curve. The y-coordinate of this point is then negated.
	- Example: Adding (-1, -2) and (2, 4) yields (3, -6) on the curve y² = x³ + x + 6.
- **Elliptic Curves over $\mathbb{Z}_{p}$:** These curves are defined over a finite field $\mathbb{Z}_{p}$, where p is a prime number. The equation becomes y² ≡ x³ + ax + b (mod p). Point addition is performed using modular arithmetic instead of geometric interpretation.
	- Example: On the curve y² ≡ x³ + x + 6 (mod 11), adding (10, 9) and (2, 4) results in (3, 5).