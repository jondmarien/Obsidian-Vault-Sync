# Types of Cryptosystem Security
## Computational Security
A cryptosystem is considered to be computationally secure if the best algorithm that can be used for breaking it requires at least N steps/operations, where N is a very, very, ridiculously large positive integer. 

We can't prove that any cryptosystem is computationally secure because we can never assert
that we know what the "best" algorithm is; for example some evil attacker may have cooked up an algorithm that the security industry doesn't know about.

We can however use the N value a benchmark for brute force attacks such as an exhaustive key search.

## Provable Security
Cryptosystems whose security is based on solving a known problem are provably secure; any evil attacker who can efficiently break the cryptosystem must be able to efficiently solve the known problem.

For example, the RSA cryptosystem is based on the integer factorization problem. If an evil attacker can
efficiently break RSA, then as a consequence they must be able to also efficiently factor an integer. 

Note that the proof of security for a provably secure cryptosystem is relative to the known problem and
not absolute an absolute proof of security.

## Unconditional Security
The holy grail of security. A cryptosystem that is unconditionally secure cannot be broken, even with infinite computing power. But the cost of eternal security comes at a price; the length of any key used must be at least as long as the plaintext message, and keys can only be used once.

This creates key management issues that tend to make these types of cryptosystems impractical for
general use.

## One-time Pad
An n-bit One-time Pad cryptosystem $(M,C,K,E,D)$ has $M=C=K=(\mathbb{Z}_2)^n\:,$ the set of all binary
strings of length n.

$$ x\in(\mathbb{Z}_2)^n,y\in(\mathbb{Z}_2)^n,k\in(\mathbb{Z}_2)^n$$
in other words, the plaintext, ciphertext, and keys are all from the set of all plaintext binary strings of length n. This implies that the length of the key (n-bits) is equal to the length of the plaintext (n-bits) and the length of the ciphertext (n-bits).


## Proof of Perfect Secrecy of the One-time Pad
Recall that a cryptosystem has perfect secrecy if P(x | y) = P(x) for all  $x\in M$ and $y\in C$  One-time Pad cryptosystem we have that keys are randomly generated and used one only once. This means that each time we encrypt, the probability of using a given n-bit key is $P(k_{i})=\frac{1}{2^{n}}$ for 1 ≤ i ≤ n. The probability of getting a given ciphertext y<sub>0</sub> is:
$$ \begin{aligned}P(y=y_0)&=P(k_1)\cdot P(y=y_0\mid k_1)+P(k_2)\cdot P(y=y_0\mid k_2)+_…+P(k_n)\cdot P(y=y_0\mid k_n)\\&=\frac{1}{2^n}\cdot P(y=y_0\mid k_1)+\frac{1}{2^n}\cdot P(y=y_0\mid k_2)+_…+\frac{1}{2^n}\cdot P(y=y_0\mid k_n)\\&=\frac{1}{2^n}\bigg[\sum_{i=1}^nP(y=y_0\mid k_i)\bigg]\end{aligned}$$
We also have that P( y = y<sub>0</sub> | k<sub>i</sub> ) = P(x<sub>i</sub>) , where xi is the plaintext such that $y_{0}=e_{k_{i}}(x_{i})$ (in other words, encrypting x<sub>i</sub> with key k<sub>i</sub> gives the ciphertext y<sub>0</sub>). In general we don't know the individual probabilities P(x<sub>i</sub>) (because that would mean knowing which plaintext binary strings are more frequent that others), but we do know that they all sum to 1. Therefore:
$$ P(y=y_{0})=\frac{1}{2^{n}}\biggl[\sum_{i=1}^{n}P(y=y_{0}\mid k_{i})\biggr]=\frac{1}{2^{n}}\biggl[\sum_{i=1}^{n}P(x_{i})\biggr]=\frac{1}{2^{n}}\biggl[1\biggr]$$

The probability of getting a given ciphertext y<sub>0</sub> given a plaintext x<sub>0</sub> is $$ P(y=y_0\mid x=x_0)=P(k_i)=\frac{1}{2^n}$$
This is because there only exists one unique key, k<sub>i</sub>, that encrypts x<sub>0</sub> as y<sub>0</sub>.
Using Baye's theorem we have that:
Loading latex…$$ \begin{aligned}P(x=x_0\mid y=y_0)&=\frac{P(x=x_0)\cdot P(y=y_0\mid x=x_0)}{P(y=y_0)}\\&=\frac{P(x=x_0)\cdot\frac{1}{2^n}}{\frac{1}{2^n}\Big[1\Big]}\\&=P(x=x_0)\end{aligned}$$Which proves the condition for perfect secrecy. Therefore, the n-bit One-time Pad is <u>unconditionally secure</u> against a ciphertext only attack.