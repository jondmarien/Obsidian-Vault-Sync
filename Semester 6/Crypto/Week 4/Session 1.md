**Algebraic Structures

**Finite Fields**
$$ \begin{aligned}&a+b\in F\\&a+\left(b+c\right)\equiv\left(a+b\right)+c\\&a+0=0+a=a\\&a+(-a)=(-a)+a=0\quad\\&a+b=b+a\\&ab+b=a\\&ab\in F\\&(ab)c=(ab)c\\&a(b+c)=ab+ac\quad\\&ab+ab+ac\quad\\&ab=ba\\&a1=a\quad\\&ab=0\mathrm{~iff~}a=0\mathrm{~or~}b=0\\&aa^{-1}=a^{-1}a=1,\quad a\neq0\quad\end{aligned}$$
- A field is a set of numbers in which you can add, subtract, multiply and divide (R, C... are fields)
- In crypto we need finite fields
	- finite fields are the same as Galois Fields

- A finite field only exists if it has pm elements, where p is prime and m is a positive integer.
	- Examples:
		- There is a finite field with:
		- 11 elements GF(11)
		- 81 elements GF (81)=GF (34)
		- 256 elements GF (256)=GF (28)
	- There is no finite field with 12 elements (12 = 22x3)
![[Pasted image 20240129101719.png]]
**Prime Fields**
- For a prime number `p`, the set of non-negative integers $$ \mathbb{Z}_p$$ with addition and multiplication modulo `p` form a finite field. Since this FF has `p` elements, we denote it as *GF(p)*. The "GF" is short for Galois field; a finite field with order `p`.
	- Show that `Z`3 with addition and multiplication modulo 3 is a finite field
	- Show that `Z`4 with addition and multiplication modulo 3 is NOT a finite field

**Finite Fields with order 2^n**
