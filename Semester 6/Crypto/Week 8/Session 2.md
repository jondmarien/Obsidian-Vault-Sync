# Elgamal Cryptosystem

## Facts:
- Public key system based on the discrete logarithm problem: $$ y=g^{x}\bmod p\:$$
- Used in the digital signature standard (DSS)
- Uses a random integer `k` in the creation of the cipher text so that a constant plaintext will result in a different ciphertext every time it's encrypted
- Has a ciphertext that is double the size of the plaintext

## Encryption
`"A"` has public key (p, g, y), where `p` is a large prime, `g` is a primitive root, and `y` is equal to `g^x modp`
The secret key `x` is difficult to compute for large values of `p`.

**To send a message `m` to "A", where:** $$ 0\leq m\leq p-1$$
- Get a random int `k`, where: $$ 1<k<p-1$$
- Compute c<sub>1</sub>: $$ c_1=g^k\bmod p$$
- Compute c<sub>2</sub>: $$ c_{2}=m\Bigl(y^{k}\Bigr)\mathrm{mod}\:p$$
- Send cipher text `c`: $$ c=(c_1,c_2)$$
## Decryption
`"A"` decrypts $$ c=(c_1,c_2)$$ by computing $$ c_2\bigg[c_1^{-x}\bigg]\mathrm{mod}p.$$
Evaluate: $$ \begin{aligned}c_2\Big[c_1^{-x}\Big]\mathrm{mod}p&=m\Big(y^k\Big)\Big[\left(g^k\right)^{-x}\Big]\\\\&=m\Big(y^k\Big)\Big[g^{-xk}\Big]\\\\&=m\Big(\left(g^x\right)^k\Big)\Big[g^{-xk}\Big]\\\\&=mg^{xk}\Big[g^{-xk}\Big]\\\\&=m\end{aligned}$$
## Examples
**Encryption**
`"A"` has public key (`p=19`,` g=10`, `y=3`), and secret key `x=5`

**To send a message `m=17` to "A":
- Get a random int `k`, let's say we get `k=6`
- Compute c<sub>1</sub>: $$ c_1=10^6\bmod{19}=11$$
- Compute c<sub>2</sub>: $$ c_{2}=17\Big(3^{6}\Big){\mathrm{mod}}19=5$$
- Send cipher text `c`: $$ c=(11,5)$$
**Decryption**
`"A"` decrypts $$ c=(11,5)$$ by computing $$ 5{\left[11^{-5}\right]}{\mathrm{mod}}19$$

First, get the inverse of 11mod19, which is 7. 
$$ \begin{aligned}5\Big[11^{-5}\Big]\mathrm{mod}19&=5\Big[\Big(11^{-1}\Big)^5\Big]\mathrm{mod}19\\\\&=5\Big[\Big(7\Big)^5\Big]\mathrm{mod}19\\\\&=17\end{aligned}$$
![](Pasted%20image%2020240306102646.png)

## Exercises
