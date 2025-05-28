## Hash Functions
A hash function $$ h:X\rightarrow Y$$assigns a has value `h(x)` to some data `x`. The hash values have a fixed size, but the data can have any size.

Let `X` be the set of all possible input data (messages).
Let `y` be the set of all possible hash values (message digests).

A pair $$ (x,y)\in X\times Y$$ is a <u>valid pair</u> under a hash function `h` if `h(x)=y`

## Secure Hash Functions
For a hash function to be considered secure, it must solve the following 3 problems:
1. **Preimage**: Given $$ y\in Y$$ find $$ x\in X$$ such that `h(x)=y`.
2. **Second Preimage**: Given $$ x\in X$$, find $$ x^{\prime}\in X$$ such that `h(x')=(h(x)` and `x' != x`.
4. **Collision**: Find $$ x,x^{\prime}\in X$$ such that `h(x')=h(x)` and `x' != x`.

- **Example**:
	-  The hash function `h(x) = xmodn`, where `n = 128`, from the set of all possible binary input strings to the set of all 7-bit message digests is <u>not secure</u>.

## Random Oracle
The ideal case for a hash function is a "Random Oracle" where the only way to compute `h(x)` is to query the oracle.

Let $$ F^{X,Y}$$ denote the set of functions from $$ X\to Y$$
Let $$ \begin{vmatrix}X\end{vmatrix}=N\quad\text{and }\begin{vmatrix}Y\end{vmatrix}=M$$ Then, $$ \left|F^{X,Y}\right|=M^{N}$$
If a hash function "behaves" like a random oracle then the probability of solving the preimage problem is $$ P(h(x)=y)=\frac{1}{M}$$
## Preimage Security
Preimage security is `t`.
	2<sup>t</sup> is the the total number of trials in the brute force
	2<sup>t</sup> = 3
	t = log<sub>2<sup>3</sup></sub> = (log 3 / log 2)

## Secure Hash Algorithm (SHA)
Secure hash algorithms use sets of cryptographic hash functions; **one-way functions that map input data of variable size to bit strings of fixed size**. These functions are **not invertible** so the only way to attempt to obtain the input data from the output bit string is to **brute force** search all possible input data. Cryptographic hash functions also have a **very low probability of collision**.

The NSA's "SHA-256" is a popular algorithm currently in use. The input data is broken up into **512-bit chunks** and put through a "modular 2<sup>32</sup> mathematical meat grinder" involving the fractional part of the square and cube roots of primes, mixing bits, and compressions. At the end, a **256-bit string is output** (which is usually displayed in hex using 64 hexits).

- Examples:
![](Pasted%20image%2020240304104829.png)

The only known way of obtaining the input data string `(x)` for any of these SHA-256 hash values `(y)` is to run the algorithm. In this way the SHA-256 "behaves" like a random oracle. 

Therefore, the probability of solving the preimage problem is $$ P(h(x)=y)=\frac{1}{2^{256}}$$This is often stated as a preimage security of `t=256`, because it would take about $$ 2^{t}=2^{256}$$ steps to brute force a search for a preimage.

## Examples for Hash Functions
The hash function `h(x) = xmodn`, where `n = 128`, from the set of all possible binary input strings to the set of all 7-bit message digests.
- The pair (111100001100, 0001100) is valid because `3852mod128=12`.
- The pair (010101010101, 1111111) is not valid because `1365mod128=85 != 127`.