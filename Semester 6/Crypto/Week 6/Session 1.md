**Matrices**
- A matric is a rectangular array of numbers
$$ \begin{bmatrix}1&0&2\\1&3&0\\0&0&1\end{bmatrix}$$
$$ \begin{bmatrix}0&1&1&0\\1&0&0&4\end{bmatrix}$$
$$ \begin{bmatrix}1&2&3&4&5\end{bmatrix}$$

- A matrix with `m` rows and `n` columns is said to be an ***m x n matrix***
- A ***square matrix*** is a matrix with the same number of rows and columns
- Two matrices are ***equal*** if both matrices have the same number of rows and columns and the corresponding entries in every position are equal

---------------------------------

**Matrix Multiplication**
- A product of two matrices is only defined when the number of columns in the first matrix is equal to the number of rows of the second matrix.
$$ \text{If AB=}\left[c_{ij}\right]\text{then}\:c_{ij}=a_{i1}b_{1j}+a_{i2}b_{2j}+...+a_{ik}b_{kj}$$
*Example 1*
$$ \mathrm A=\begin{bmatrix}2&9&0&5\end{bmatrix}\text{ and}\:\mathrm B=\begin{bmatrix}3\\1\\-8\\2\end{bmatrix}$$
`A` is a 1 x 4 matrix. `B` is a 4 x 1 matrix.
Since the # of columns of `A` is equal to the # of rows of B, `AB` is defined.
`AB` is the following 1 x 1 matrix:

$$ \color{red}{\mathbf{AB}=\begin{bmatrix}2&9&0&5\end{bmatrix}}\color{red}{\begin{bmatrix}3\\1\\-8\\2\end{bmatrix}}=$$
=` [(2)(3)+(9)(1)+(0)(-8)+(5)(2)]=[25]`

*Example 2*
$$ \mathbf{A}=\begin{bmatrix}1&2&0\\5&4&2\end{bmatrix}\text{ and }\mathbf{B}=\begin{bmatrix}7&3&9\\2&0&4\end{bmatrix}$$
`A` is a 2 x 3 matrix. `B` is a 2 x 3 matrix.
Since the # of columns of` A` is not equal to the # of rows of`B`,`AB` is not defined.

*Example 3*
$$ \mathbf{A}=\begin{bmatrix}1&0&4\\2&1&1\\3&1&0\\0&2&2\end{bmatrix}\text{ and }\mathbf{B}=\begin{bmatrix}2&4\\1&1\\3&0\end{bmatrix}$$
- A is a 4 x 3 matrix, B is a 3 x 2 matrix.
Since the # of columns of A is equal to the # of rows of B, AB is defined.

$$ \mathbf{AB}=\color{red}{\begin{bmatrix}1&0&4\\2&1&1\\3&1&0\\0&2&2\end{bmatrix}}\color{blue}{\begin{bmatrix}2&4\\1&1\\3&0\end{bmatrix}}=\color{blue}{\begin{bmatrix}(1)(2)+(0)(1)+(4)(3)&(1)(4)+(0)(1)+(4)(0)\\(2)(2)+(1)(1)+(1)(3)&(2)(4)+(1)(1)+(1)(0)\\(3)(2)+(1)(1)+(0)(3)&(3)(4)+(1)(1)+(0)(0)\\(0)(2)+(2)(1)+(2)(3)&(0)(4)+(2)(1)+(2)(0)\end{bmatrix}}=\color{blue}{\begin{bmatrix}14&4\\8&9\\7&13\\8&2\end{bmatrix}}$$

------------------------------------

**Matrix Inverses**
Given an `n x n` matrix **A**, the inverse **A<sup>-1</sup>** is an `n x n` such that **AA**<sup>-1</sup> = **A<sup>-1</sup> . A** = I<sub>n</sub>
![](Pasted%20image%2020240212101808%201.png)
$$ \mathbf{AB}=\begin{bmatrix}2&5\\1&3\end{bmatrix}\begin{bmatrix}3&-5\\-1&2\end{bmatrix}=\begin{bmatrix}(2)(3)+(5)(-1)&(2)(-5)+(5)(2)\\(1)(3)+(3)(-1)&(1)(-5)+(3)(2)\end{bmatrix}=\begin{bmatrix}1&0\\0&1\end{bmatrix}$$

Since **AB = I<sub>2</sub>**, **B** is the inverse of **A**

In general, for any 2x2 $$ \mathbf{A}=\left\lfloor\begin{array}{cc}a&b\\c&d\end{array}\right\rfloor $$
, the determinant of **A** is: `det(A) = (ad) - (bc)`
The inverse **A<sup>-1</sup>** can be computed using the determinant of **A**: $$ \mathbf{A}^{-1}=\frac{1}{\det(\mathbf{A})}\cdot\left[\begin{matrix}d&-b\\-c&a\end{matrix}\right]$$
*Example 1*
$$ \text{If }\mathbf{A}=\begin{bmatrix}2&5\\1&3\end{bmatrix},\text{ find }\mathbf{A}^{-1}:$$

$$ \mathbf{A}^{-1}=\begin{bmatrix}\frac{3}{(2)(3)-(1)(5)}&\frac{-5}{(2)(3)-(1)(5)}\\\frac{-1}{(2)(3)-(1)(5)}&\frac{2}{(2)(3)-(1)(5)}\end{bmatrix}=\begin{bmatrix}\frac{3}{1}&\frac{-5}{1}\\\frac{-1}{1}&\frac{2}{1}\end{bmatrix}=\begin{bmatrix}3&-5\\-1&2\end{bmatrix}$$

The value of `ad - bc`= (2)(3)-(1)(5)=1 is called the <u>determinant</u> of the matrix **A**

*More Examples*
$$ \mathbf{A}=\begin{bmatrix}1&2\\3&4\end{bmatrix}$$
**det(A)=4-6=-2**
$$ \color{red}{A^{-1}=\frac{1}{-2}\cdot\begin{bmatrix}4&-2\\-3&1\end{bmatrix}=\begin{bmatrix}-2&1\\3/2&-1/2\end{bmatrix}}$$
$$ \mathbf{B}=\left[\begin{array}{cc}3&1\\7&2\end{array}\right]$$
**det(B)=6-7=-1**
$$ \color{red}{\mathrm{B}^{-1}=\frac{1}{-1}\cdot\begin{bmatrix}2&-1\\-7&3\end{bmatrix}=\begin{bmatrix}-2&1\\7&-3\end{bmatrix}}$$
$$ \mathbf{C}=\begin{bmatrix}-1&6\\1&2\end{bmatrix}$$
**det(C)=-2-6=-8**
$$ \color{red}{C^{-1}=\frac1{-8}\cdot\begin{bmatrix}2&-6\\-1&-1\end{bmatrix}=\begin{bmatrix}-2/8&6/8\\1/8&1/8\end{bmatrix}}$$

Switch the left term in the matrix (using above examples) and apply a negative sign in the right terms
- swap 1 and 4, and make 2 and 3 negative (A)
- swap 3 and 2, and make 1 and 7 negative (B)
- swap 2 and -1, and make 1 and 6 negative (C)

---------------------------
**Hill Cipher**
Encrypt (9, 20, 11, 18) using K = $$ \left[\begin{array}{cc}11&8\\3&7\end{array}\right]$$
*K* is a 2 by 2 matrix, so we encrypt `m=2` elements at a time
$$ \begin{aligned}&\left[\begin{array}{cc}9&20\\\end{array}\right]\left[\begin{array}{cc}11&8\\3&7\\\end{array}\right]=\left[\begin{array}{cc}159&212\\\end{array}\right]\mathrm{mod}26=\left[\begin{array}{cc}3&4\\\end{array}\right]\\\\&\left[\begin{array}{cc}11&18\\\end{array}\right]\left[\begin{array}{cc}11&8\\3&7\\\end{array}\right]=\left[\begin{array}{cc}175&214\\\end{array}\right]\mathrm{mod}26=\left[\begin{array}{cc}19&6\\\end{array}\right]\end{aligned}$$
The cipher text is (3, 4, 19, 6)



-----------------------
**Fiestel Cipher**
![](Pasted%20image%2020240212104418%201.png)
One round of a Feistel cipher:
- Split the previous state into two sides L<sup>i-1</sup> and R<sup>i-1</sup>
- set L<sup>i</sup>= R<sup>i-1</sup>
- Set R<sup>i</sup> = L<sup>i-1</sup> Of (R<sup>i-1</sup>,K<sup>i</sup>) where K<sup>i</sup> is the round key
- Return (L<sup>i</sup> R<sup>i</sup>)

**DES**
In DES R<sup>i-1</sup> would be 32-bits and the encryption function f (R<sup>i-1</sup>, K<sup>i</sup>) would:
- Expand R<sup>i-1</sup> from 32-bits to 48-bits.
- XOR the expanded R<sup>i-1</sup> with the 48-bit round key K<sup>i-1</sup> and write the result as eight 6-bit strings.
- Map each 6-bit string to 4-bits using 8 different S-boxes (yes... 8 of them in total!)
- Permute the resulting 32-bit string using a defined permutation P.

**Encryption Function**
$$ f(R^{i-1},K^i)=P(R^{i-1}\oplus K^i)$$
*Example 1*
![](Pasted%20image%2020240212105120%201.png)