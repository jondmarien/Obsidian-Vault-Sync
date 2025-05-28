Here's a completely word-based breakdown of how to approach each quiz question type, focusing on strategic thinking and process:

---

## Quiz 1 - Elliptic Curves (Problem Solving Guide)
**Question Type 1: Point Addition**
1. **Check if points are vertical duplicates** - If x-coordinates match but y-coordinates are negatives modulo p, result is infinity point
2. **Calculate slope** - For distinct points: (Δy)/(Δx) mod p. For duplicate points: (3x² + curve_constant)/(2y) mod p
3. **Find new x-coordinate** - Slope² - x1 - x2 mod p
4. **Find new y-coordinate** - Slope*(original_x - new_x) - original_y mod p  
*Brain Tip: Always verify your inverses - if stuck, check GCD(denominator,p)=1*

**Question Type 2: ECDSA Signing**
1. **Compute temporary point** - Multiply random number k by public base point A using point doubling formula
2. **Extract r-value** - Take x-coordinate of result modulo q
3. **Calculate s-value** - Combine hash + private_key*r, then multiply by k's inverse modulo q  
*Brain Tip: Signature fails if k's inverse doesn't exist - always check GCD(k,q)=1 first*

---

## Quiz 2 - Factorization Methods (Decision Flow)
**Pollard p-1 Strategy:**
4. Choose smoothness bound B (start with 5)
5. Compute L = product of all primes ≤ B with exponents (B! factorization)
6. Calculate a = 2ᴸ mod N using successive squaring
7. Compute GCD(a-1, N) - if nontrivial, you found a factor  
*Brain Tip: Success hinges on p-1 having only small factors - try increasing B gradually*

**Lenstra ECM Approach:**
8. Choose random elliptic curve and point
9. Attempt point multiplication (like 2P)
10. During slope calculation, if denominator isn't invertible:
   - Compute GCD(denominator, N)
   - GCD result gives factor  
*Brain Tip: Curves are trial-and-error - expect multiple attempts before success*

---

## Quiz 3 - Shor's Algorithm (Critical Checks)
**Successful Factorization Path:**
11. Find smallest t where gᵗ ≡ 1 mod N (period)
12. **Must have even t** - If odd, abort
13. Compute a = g^(t/2)-1, b = g^(t/2)+1
14. Find factors via GCD(N,a) and GCD(N,b)  
*Brain Tip: Always verify t is actually the minimal period - check smaller exponents first*

**Failure Case Analysis:**
15. If period t is odd → No solution
16. If g shares factor with N → Trivial solution
17. If g^t ≠ 1 → Continue searching for t  
*Brain Tip: 169=13² requires different approach - Shor only works for distinct primes*

---

## Quiz 4 - Pratt Certificates (Verification Protocol)
**Stepwise Validation:**
18. **Prime decomposition** - Confirm N-1 factors into claimed primes
19. **Generator check** - Verify g^(N-1) ≡ 1 mod N using successive squaring
20. **Non-triviality test** - Ensure g^((N-1)/each_prime) ≠ 1 mod N  
*Brain Tip: Organization is key - make table of exponents and intermediate results*

**Efficiency Analysis:**
21. Count actual multiplication steps in your calculations
22. Compare to ⌊log₂N - 1⌋ (multiplication bound)
23. Track exponentiation stages vs 3log₂N - 3 theory  
*Brain Tip: Successive squaring cuts calculations exponentially - master this technique*

---

**Exam Strategy Toolkit:**
- **Modular Inverse First Aid**: When stuck, compute GCD(value, modulus) - if 1, inverse exists
- **Factorization Red Flags**: Even numbers → 2 is factor. Numbers ending with 5 → 5 is factor
- **Time Management**: Allocate 2 mins per mark (e.g., 4-mark question = 8 mins max)
- **Partial Credit Traps**: Always show inverse calculations and GCD steps - even if final answer wrong

Want me to focus deeper on any particular strategy?

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/edf3d024-ae3e-4cdd-8fa8-801e9f27f1d3/MATH36206-Quiz-1-4.pdf
[2] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/8d2c366e-2a25-4ee0-8a9e-fa0ac82eb357/Quiz-1-4-Solutions.pdf
[3] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_24431ac3-f920-4fb4-ab61-585bd0ff2547/5d193531-fa3b-4515-9650-60fc4704f6ef/MATH36206-Quiz-1-4.pdf
[4] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/5025329/edf3d024-ae3e-4cdd-8fa8-801e9f27f1d3/MATH36206-Quiz-1-4.pdf