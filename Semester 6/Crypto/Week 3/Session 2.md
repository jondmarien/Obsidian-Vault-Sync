**Diffie Hellman Exchange
- Establishes a secret key between 2 parties and involves the exchange of public information
- Involves a prime modulus `p` and a base `g`, where `g` is a primitive root of `p` (`g^k*modp` can be used to generate all `p-1` integers relatively prime to `p`)
	- `g` is a primitive root of `p`.
		- For all numbers relatively prime to `p` there is a key (?)
			- `g^k is congruent a(modp)`

**Showing Primitive Rule**

| 3^1mod7=3 | 4^1mod7=4 |
| ---- | ---- |
| 3^2mod7=2 | 4^2mod7=2 |
| 3^3mod7=6 | 4^3mod7=1 |
| 3^4mod7=4 | 4^4mod7=4 |
| 3^5mod7=5 |  |
| 3^6mod7=1 |  |
4 <u>is not</u> a primitive rule of 7


- *Example*
	- Both p and g are published.
		Person A chooses a secret power `a` and sends `g^a mod p` to person B.
		Person B chooses a secret power `b` and sends `g^b mod p` to person A.
			Person A computes `s = (g^b mod)^a mod p`
			Person B computes `s = (g^a mod)^b mod p`
		Person A and B both share a secret encryption key `s = g^ab mod p`
		![[Pasted image 20240124102031.png]]
- *Example 2*
	- `p=991` and `g=6`
		- A chooses a secret power `a=123` and sends `6^123 mod 991 = 541` to B.
			B chooses a secret power `b=456` and sends `6^456 mod 991 = 644` to A.
			- A computes: `s = (644)123 mod 991=265`.
				B computes: `s = (541)456 mod 991=265`.
			- Person A and B both share a secret encryption key `s = 265 = 6^(123)(456)mod 991`
		
| A | B |
| ---- | ---- |
| 6^123mod991=541 | 6^456mod991=644 |
| 644^123mod991=265 | 541^456mod991=265 |


