**Linear Feedback Shift Register (LFSR)**
$$ k_{m+i}=\sum_{j=0}^{m-1}c_jk_{j+i}\operatorname{mod}2$$
can be used to generate a binary keystream

where $$ i\ge1\:,\:(c_0,c_1,...,c_{m-1})$$ are constant bits, and $$ (k_1,k_2,...,k_m)$$ are the initial bits

**Bit Stream**
![](Pasted%20image%2020240207101031.png)
`p = plaintext, k = key, c = ciphertext`
*Consequently:*
$$ \begin{aligned}\mathrm{p\oplus k=c,c\oplus k=p}\\\\\mathrm{p=(p\oplus k)\oplus k}\end{aligned}$$
**Simple Stream Cipher**
- Set up a known pattern (sequence) of 1's and 0's as a key
	- Aply the key to the plaintext bit stream using an XOR function
		- Recover the plaintext using the same key pattern on the ciphertext bit stream
![](Pasted%20image%2020240207101241.png)

**Pseudorandom Number Generators**
- A (*pseudo-*) *random number generator* (**PRNG**) is an algorithm which produces a long stream of seemingly random numbers in a prescribed range, from a specified initial state, the seed.
- A short sequence of key bits would be easy to remember but not very secure
- A long sequence of key bits would be secure but hard to remember

- Construct a LFSR to solve this issue

**Shift Register**
- A shift register is a hardware device which
	- saves bits
	- shifts bits
- For example, a 4-bit shift register looks like:
	![](Pasted%20image%2020240207101747.png)

This is LSFR. It takes in some of the bits in the shift register, then combines them with an XOR, and feedbacks the result as the input
![](Pasted%20image%2020240207101628.png)



**Example**
![](Pasted%20image%2020240207101824.png)


**RC4**
- RC4 was developed by Ron Rivet of MIT
	- Ron's Code 4
- RC4 generates a pseudorandom stream of bits (a keystream) which, for encryption, is combined with the plaintext using XOR; decryption is performed the same way.
![](Pasted%20image%2020240207104025.png)
- Uses an 8-bit keystream to encrypt each byte of plaintext
	- 3 loops with swaps, are able to produce a keystream with an estimated period of 10<sup>100</sup>
	- using n = 256, and some arbitrary length *"key"* would generate a valid 8-bit RC4 keystream