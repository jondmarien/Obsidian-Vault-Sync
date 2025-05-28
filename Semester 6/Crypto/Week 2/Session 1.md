**Euclidean Algorithm
- The oldest algorithm known to man for finding GCD(a,b)
	- It is much faster and optimized than prime factorization
	- ![[EA.png]]
	- The answer of the first part is in the position succeeding the modulo operation. The number preceding the modulo is the same as the one following the modulo in the first answer.
**Extended Euclidean Algorithm
- the purpose of this is to find the GCD of a, b; and solving $$sa + tb = GCD(a, b)$$
	- Works the same way EA does, but also includes extended calculations of the quotients, the remainders, and the coefficients `s` and `t` that give a linear combination of `a` and `b` for each remainder
**Example
- **EEA
	- Find an inverse to 71mod481, where a = 13, b = 37 {(13)(17)=481}![[EEA.png]]$$1 = 31 * 481 - 210 * 71$$
	- -210 is congruent to 271mod481, because -210+481=271
	- Final answer is 271, because it is an inverse of 71mod481
	-  *EEA_Fast![[EEA_Fast.png]]