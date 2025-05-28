# Session 1 - AES S-Box
## S-Box
![](Pasted%20image%2020240318100437.png)


## Inverse S-Box
![](Pasted%20image%2020240318100454.png)

## Multiplicative Inverses in GF(2<sup>n</sup>) & AES S-Box
GF(2<sup>8</sup>) = $m(x)=x^8+x^4+x^3+x+1$ 
{11B} = 100011011

The substitution values found in the AES S-box are found by computing the multiplicative inverse of the initial 8-bit value, and then computing each bit of the substitution value according to: 
$$ b_i=\begin{pmatrix}a_i+a_{i+4}+a_{i+5}+a_{i+6}+a_{i+7}+c_i\end{pmatrix}\mathrm{mod}2$$
where $c_{7}c_{6}c_{5}c_{4}c_{3}c_{2}c_{1}c_{0}=01100011$
**NOTE**: Coefficients are reduced mod2 and subscripts (x<sub>2</sub>) are reduced mod8

## Example
Compute the AES S-box value for {53}
![](Pasted%20image%2020240318103229.png)

![](Pasted%20image%2020240415104128.png)
