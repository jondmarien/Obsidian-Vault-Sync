## Elgamal Digital Signature
- Facts
	- Modified version used in the NIST Digital Signature Standard (DSS)
	- Uses a secure hash algorithm

## The Sender
The sender has the public key `(p, g, y)` where:
	p is a large prime
	g is a primitive root
	y = g<sup>x</sup> * mod p $$ y=g^x\operatorname{mod}p$$

The sender has the private key `(k, x)` to sign the message, where:
	k is a random integer such that `1<k<p-1` and `GCD(k, p-1)=1`
	x is difficult to compute for large values of `p`

| Sender                               | Reciever              | To Check                    |
| ------------------------------------ | --------------------- | --------------------------- |
| p, g, y                              | hash of m             | compute v<sub>1</sub>       |
| m -> h(m)                            | compute s<sub>1</sub>/s<sub>2</sub>         | compute v<sub>2</sub>       |
| m, (s<sub>1</sub>, s<sub>2</sub>) -> | message, (sig<sub>1</sub>, sig<sub>2</sub>) | v<sub>1</sub>=v<sub>2</sub> |

## To Sign
To sign a message `m`, where `0<=m<=p-1`:
	Get a random int `k`, where `1<k<p-1` and `GCD(k, p-1)=1`
	Get the hash of `m`, `h(m)`
	Compute s<sub>1</sub>= $$ s_1=g^k\bmod p$$
	Compute k<sup>-1</sup>= $$ k^{-1} mod( p - 1)$$
	Compute s<sub>2</sub>= $$ s_2=k^{-1}\left(h(m)-xs_1\right){\mathrm{mod}}\left(p-1\right)$$
	Send the message `m` and the signature `(s1, s2)` as: `m, (s1, s2)`


## The Receiver
The receiver verifies by computing `v1, v2`, and checking if `v1=v2` where:
	v<sub>1</sub>=$$ \nu_1=g^{h(m)}\operatorname{mod}p$$
	v<sub>2</sub>=$$ \nu_{2}=y^{s_{1}}s_{1}^{s_{2}}\bmod p$$

## Why this works
This works (unbelievably!) because:
$$ \begin{aligned}v_1&=v_2\\g^{^{h(m)}}\operatorname{mod}p&=y^{s_1}s_1^{^{s_1}}\operatorname{mod}p\\g^{^{h(m)}}\operatorname{mod}p&=\left(g^x\right)^{s_1}\left(g^k\right)^{k^{-1}(h(m)-xs_1)}\operatorname{mod}p\\g^{^{h(m)}}\operatorname{mod}p&=\left(g^{xs_1}\right)\left(g^{kk^{-1}(h(m)-xs_1)}\right)\operatorname{mod}p\\g^{^{h(m)-xs_1}}\operatorname{mod}p&=g^{^{kk^{-1}(h(m)-xs_1)}}\operatorname{mod}p\end{aligned}$$
$$ \begin{aligned}&h(m)-xs_1\bmod\left(p-1\right)=kk^{-1}\left(h(m)-xs_1\right)\bmod\left(p-1\right)\\&h(m)-xs_1\bmod\left(p-1\right)=h(m)-xs_1\bmod\left(p-1\right)\end{aligned}$$

We have used the fact that g<sub>i</sub> ≡ g<sub>j</sub> mod p **if and only if** `i ≡ j mod(p-1)`

## Example:
Sender has public key `(p=19, g=10, y=4)`, and private key `(k=5, x=16) `
(k is first component of private key, x is second component of private key)

## Sender 

| *Step*                                                                       | *Decision*                                    |
| ---------------------------------------------------------------------------- | --------------------------------------------- |
| **Choose a random int, k:**                                                  | 5, where 1<k<18, GCD(5,18)=1                  |
| **Get hash of m, h(m):**                                                     | 14                                            |
| **Compute s<sub>1</sub>:** g<sup>k</sup> mod p                               | 10<sup>5</sup>mod19=**3**                     |
| **Compute s<sub>2</sub>:** k<sup>-1</sup>(h(m) - x * s<sub>1</sub>) mod(p-1) | 5<sup>-1</sup>mod(19-1)=5<sup>-1</sup>(18)=11 |
| **Compute s<sub>2</sub>:** 5<sup>-1</sup>mod(19-1)=5<sup>-1</sup>(18)=11     | -374mod18=**4**                               |
| **Send the message and the signature:**                                      | m, (**3, 4**)                                 |

## Receiver 
Check if v<sub>1</sub> = v<sub>2</sub>

| *Step*                                                                                           | *Decision*                                         |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------- |
| **Compute v<sub>1</sub>:** g<sup>h(m)</sup> mod p                                                | 10<sup>14</sup>mod19=16                            |
| **Compute v<sub>2</sub>:** y<sup>s<sub>1</sub></sup> s<sub>1</sub><sup>s<sub>2</sub></sup> mod p | (4)<sup>3</sup> (3)<sup>4</sup> mod19=5184mod19=16 |
