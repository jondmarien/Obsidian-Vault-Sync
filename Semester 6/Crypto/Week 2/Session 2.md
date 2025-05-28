**RSA**
$$ \begin{aligned}&\mathsf{GCD}(e,\phi(n))=1\\&\mathsf{GCD}(e,\phi(pq))=1\\&\mathsf{GCD}(e,(p-1)(q-1))=1\end{aligned}$$

**To Encrypt**
$$ C=M^{e}{\mathrm{mod}}n$$                                              where `c` is the ciphertext and `m` is the plaintext
**To Decrypt**
$$ M=C^{d}\operatorname{mod}n$$where `d` is the private decryption exponent

To obtain `d`, the factorization of `n` must be known (GCD)
$$ d=e^{-1}mod\Phi(n)$$
**To Sign**
C^d = 
$$ \begin{aligned}\left(m^e\right)^d&=m^{ed}\operatorname{mod}n\\&=m^{1+r(p-1)(q-1)}\operatorname{mod}n\\&=m^1m^{r(p-1)(q-1)}\operatorname{mod}n\\&=m^1m^{r\phi(n)}\operatorname{mod}n\\&=m^1\Big(m^{\phi(n)}\Big)^r\operatorname{mod}n\\&=m^1\left(1\right)^r\operatorname{mod}n\\&=m\operatorname{mod}n\end{aligned}$$
**Examples


C<sup>d </sup>modn
$$ C^d modn$$