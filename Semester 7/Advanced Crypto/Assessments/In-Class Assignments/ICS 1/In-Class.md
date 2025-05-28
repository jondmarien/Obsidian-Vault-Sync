
Only **TWO** questions have to be completed, we chose #3 and #2.
# Question 2 
## Listing All Points on E and Finding |E|

We now search for all solutions (x, y) ∈ 𝔽₇ × 𝔽₇ to

y² ≡ x³ + 2x + 4 (mod 7).

Because our field 𝔽₇ is small, we can check x = 0, 1, 2, 3, 4, 5, 6, and for each x compute the right-hand side and see if it is a quadratic residue in 𝔽₇. We remember the squares (quadratic residues) mod 7 are {0, 1, 2, 4}.

1. **x = 0**
    - RHS = 0³ + 2·0 + 4 = 4.
    - We need y² ≡ 4. Then y ≡ ±2 = 2, 5 (mod 7).
    - Points: (0, 2), (0, 5).
2. **x = 1**
    - RHS = 1³ + 2 + 4 = 7 ≡ 0.
    - We need y² ≡ 0 → y = 0.
    - Point: (1, 0).
3. **x = 2**
    - RHS = 2³ + 2·2 + 4 = 8 + 4 + 4 = 16 ≡ 2.
    - We need y² ≡ 2, so y ≡ ±3 = 3, 4 (mod 7).
    - Points: (2, 3), (2, 4).
4. **x = 3**
    - RHS = 3³ + 6 + 4 = 37 ≡ 37 − 35 = 2 (mod 7).
    - Again y² ≡ 2 → y = 3, 4.
    - Points: (3, 3), (3, 4).
5. **x = 4**
    - RHS = 4³ + 8 + 4 = 76 ≡ 76 − 70 = 6 (mod 7).
    - We need y² ≡ 6, but 6 is not in {0,1,2,4}.
    - No solutions.
6. **x = 5**
    - 5³ = 125 ≡ 125 − 119 = 6 (mod 7).
    - RHS = 6 + 2·5 + 4 = 6 + 10 + 4 = 20 ≡ 6 (mod 7).
    - We need y² ≡ 6, which fails again.
    - No solutions.
7. **x = 6**
    - 6³ = 216 ≡ 6 (mod 7).
    - RHS = 6 + 2·6 + 4 = 6 + 12 + 4 = 22 ≡ 1 (mod 7).
    - We need y² ≡ 1, so y ≡ ±1 = 1, 6 (mod 7).
    - Points: (6, 1), (6, 6).

Therefore, the affine points on E are:

(0, 2), (0, 5),  
(1, 0),  
(2, 3), (2, 4),  
(3, 3), (3, 4),  
(6, 1), (6, 6).

In total, there are **9** affine points. But in elliptic-curve notation, we always include the point at infinity (the identity) as well. Thus:

|E| = 9 + 1 = 10.

Therefore, **the total number of points on E is 10**.