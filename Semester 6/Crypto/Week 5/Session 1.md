| 0=0000 | 8=1000 |
| ---- | ---- |
| 1=0001 | 9=1001 |
| 2=0010 | A=1010 |
| 3=0011 | B=1011 |
| 4=0100 | C=1100 |
| 5=0101 | D=1101 |
| 6=0110 | E=1110 |
| 7=0111 | F=1111 |

| *Input Bit A* | *Input Bit B* | *Output Bit* |
| ---- | ---- | ---- |
| 0 | 0 | **0** |
| 0 | 1 | **1** |
| 1 | 0 | **1** |
| 1 | 1 | **0** |

**GF(2<sup>8</sup>)
$$ m(x)=x^{8}+x^{4}+x^{3}+x+1\:.$$
*Addition*
- Use bitwise operation

**Multiplication**
- 1-bit left shift
	$$ \left(b_{6}b_{5}b_{4}b_{3}b_{2}b_{1}b_{0}0\right)\mathrm{if}b_{7}=0$$
- 1-bit left shift
	$$ \left(b_{6}b_{5}b_{4}b_{3}b_{2}b_{1}b_{0}0\right)\oplus\left(00011011\right)\mathrm{if}b_{7}=1$$

**The XOR bit pattern (0001 1011) corresponds to**
$$ \begin{aligned}m(x)-x^8&=x^8+x^4+x^3+x+1-x^8\\&=x^4+x^3+x+1\end{aligned}$$
