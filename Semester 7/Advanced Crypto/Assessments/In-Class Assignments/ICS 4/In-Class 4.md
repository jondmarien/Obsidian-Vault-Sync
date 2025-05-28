---
title: In-Class 4
author:
  - Jon Marien
  - Lucas Oppedisano
  - Mohammed Elsayed
created: 2025-01-29
published: 2025-01-29
tags:
  - classes
---

| Title      | Author                                                                                                        | Created          | Published        | Tags                   |
| ---------- | ------------------------------------------------------------------------------------------------------------- | ---------------- | ---------------- | ---------------------- |
| In-Class 4 | <ul><li>Jon Marien (marien)</li><li>Lucas Oppedisano (oppedilu)</li><li>Mohammed Elsayed (elsayemu)</li></ul> | January 29, 2025 | January 29, 2025 | [[#classes\|#classes]] |
|            |                                                                                                               |                  |                  |                        |

 ![](In-Class%204-January-29th-2025-09-34-31.webp)
Prime number picked was 241. 

![|380](In-Class%204-January-29th-2025-09-35-30.webp)

For part d), we decided to use python to verify that 7 (`a`) is a primitive root modulo 241 (`p`).
Below is the code and the respective output.
```python
def is_primitive_root(a: int, p: int) -> bool:
    """
    Verifies if 'a' is a primitive root modulo prime 'p'
    using Fermat's Little Theorem and order verification
    """
    print(f"\n=== Verifying if {a} is a primitive root modulo {p} ===")
    
    # 1. Verify Fermat's Little Theorem (base requirement)
    print(f"\n[1/3] Checking Fermat's Little Theorem: {a}^{p-1} ≡ 1 mod {p}")
    fermat_result = pow(a, p-1, p)
    if fermat_result != 1:
        print(f"✗ Failed: {a}^{p-1} ≡ {fermat_result} mod {p}")
        return False
    print(f"✓ Passed: {a}^{p-1} ≡ 1 mod {p}")

    # 2. Check order by testing prime factors of φ(p) = p-1
    print("\n[2/3] Checking order by testing divisors of φ(p):")
    factors = [2, 3, 5]  # Prime factors of 240 (since p-1 = 240)
    order = p-1
    
    for factor in factors:
        exponent = order // factor
        result = pow(a, exponent, p)
        print(f" - Testing {a}^{exponent} mod {p}:")
        print(f"   → {a}^{exponent} ≡ {result} mod {p}")
        if result == 1:
            print(f"✗ Failed: Order divides {exponent} (factor {factor})")
            return False
        print(f"   ✓ Confirmed: Not congruent to 1 (factor {factor} check passed)")

    # 3. Final verification
    print("\n[3/3] All checks passed!")
    print(f"✓ {a} has order {order} modulo {p}")
    print(f"✓ {a} is a primitive root modulo {p}")
    return True

# Example verification for 7 mod 241
if __name__ == "__main__":
    print("STARTING VERIFICATION".center(50, "="))
    is_primitive_root(7, 241)
    print("".center(50, "="))
```

Output:
```Sample Output:
---------------STARTING VERIFICATION---------------

=== Verifying if 7 is a primitive root modulo 241 ===

[1/3] Checking Fermat's Little Theorem: 7^240 ≡ 1 mod 241
✓ Passed: 7^240 ≡ 1 mod 241

[2/3] Checking order by testing divisors of φ(p):
 - Testing 7^120 mod 241:
   → 7^120 ≡ 240 mod 241
   ✓ Confirmed: Not congruent to 1 (factor 2 check passed)
 - Testing 7^80 mod 241:
   → 7^80 ≡ 15 mod 241
   ✓ Confirmed: Not congruent to 1 (factor 3 check passed)
 - Testing 7^48 mod 241:
   → 7^48 ≡ 91 mod 241
   ✓ Confirmed: Not congruent to 1 (factor 5 check passed)

[3/3] All checks passed!
✓ 7 has order 240 modulo 241
✓ 7 is a primitive root modulo 241
---------------------------------------------------
```