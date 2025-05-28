## Advanced Encryption Standard (AES)
- Some facts:
	- Initiated in 1999 by NIST and published by NIST in 2001
		- Rinjdael was the winner in a long list of ciphers
	- AES-128 is a 128-bit block cipher with variable length key (we'll use a 128-bit key)
	- More secure than triple-DES; designed to replace DES
- 10 rounds of:
	- Substitution, row shifting, column mixing, key adding
	- Uses 8-bit binary in GF(2<sup>8</sup>)

## 4 Steps
1. S-Box Substitution
2. Row Shifting
3. Column Mixing
4. Key Adding

## Initialization
>Each 128-bit string of data (block) is formatted into a 4x4 array of 2-hexit numbers:

```
111010101000 ........................... 000011000101
EA835CF00445332D655D98AD8596BOC5
```

$\begin{array}{|c|c|c|c|}\hline87&\text{F}2&4\text{D}&97\\\hline6\text{E}&4\text{C}&90&\text{EC}\\\hline46&\text{E}7&4\text{A}&\text{C}3\\\hline\text{A}6&8\text{C}&\text{D}8&95\\\hline\end{array}$
## S-box substitution (SubBytes)
The s-box table is used to map each 2-hexit element {x, y} in the 4x4 array to another one located at `row x` and `column y` in the S-box:

$\begin{array}{|c|c|c|c|}\hline87&\text{F}2&4\text{D}&97\\\hline6\text{E}&4\text{C}&90&\text{EC}\\\hline46&\text{E}7&4\text{A}&\text{C}3\\\hline\text{A}6&8\text{C}&\text{D}8&95\\\hline\end{array}$

The mapped (output) elements Of the S-box are not a linear mathematical function pf the input
elements; they are derived using the multiplicative inverse of the input elements.


## Row Permutation
Row 1: {1,2,3,4}
Row 2: {2,3,4,1}
Row 3: {3,4,1,2}
Row 4: {4,1,2,3}

$\begin{array}{|c|c|c|c|c|c|c|}\hline87&\text{F2}&4\text{D}&97\\\hline\text{EC}&6\text{E}&4\text{C}&90\\\hline\text{4A}&\text{C3}&46&\text{E7}\\\hline\text{8C}&\text{D8}&95&\text{A6}\\\hline\end{array}\quad\to\begin{array}{|c|c|c|c|c|}\hline\text{87}&\text{F2}&4\text{D}&97\\\hline\text{6E}&4\text{C}&90&\text{EC}\\\hline\text{46}&\text{E7}&4\text{A}&\text{C3}\\\hline\text{A6}&\text{8C}&\text{D8}&95\\\hline\end{array}$


## Column Mixing (Additions and Multiplications in GF(2<sup>8</sup>))

Apply these matrices and binary bitwise XORs and left bit shifts:
$\begin{bmatrix}02&03&01&01\\01&02&03&01\\01&01&02&03\\03&01&01&02\end{bmatrix}$ $\begin{array}{|c|c|c|c|c|c|c|}\hline87&\text{F2}&4\text{D}&97\\\hline6\text{E}&4\text{C}&90&\text{EC}\\\hline46&\text{E7}&4\text{A}&\text{C3}\\\hline\text{A6}&8\text{C}&\text{D8}&95\\\hline\end{array}=\begin{array}{|c|c|c|c|c|}\hline47&40&\text{A3}&4\text{C}\\\hline37&\text{D4}&70&\text{9F}\\\hline94&\text{E4}&3\text{A}&42\\\hline\text{ED}&\text{A5}&\text{A6}&\text{BC}\\\hline\end{array}$

Verify the first result: 
```
{02}×{87} + {03}×{6E} + {01}×{46} + {01}×{A6} = {47}
```

$$ \begin{aligned}&(02)\times(67)=(0000710)+(0007100101)=(0001010101011)\\\\&(03)\times(65)=(11011100)\oplus(01101110)=(10110010)\\\\&(010)\times(46)=(01000110)\\\\&(010)\times(48)=(10100110)\\\\&(00010010100100100110)(10100110)\\\\&=(1010011)+(01000110)(10100110)\\\\&=(11100001)+(10100110)\\\\&=(01000110)\\\\&=(47)\end{aligned}$$

## Key Addition (AddRoundKey)
A new key is computed for EACH ROUND, based on the initial 128-bit key 

If the first round key is: 
```
AC7766F319FADC2128D12941575C006A
```

Then it is added by XOR to the 4x4 array from `MixColumns`

$\begin{array}{|c|c|c|c|c|c|c|c|c|c|}\hline47&40&\text{A3}&4\text{C}\\\hline37&\text{D4}&70&\text{9F}\\\hline94&\text{E4}&3\text{A}&42\\\hline\text{ED}&\text{A5}&\text{A6}&\text{BC}\\\hline\end{array}\oplus\begin{array}{|c|c|c|c|c|c|c|c|c|c|}\hline\text{AC}&19&28&57\\\hline77&\text{FA}&\text{D1}&5\text{C}\\\hline66&\text{DC}&29&00\\\hline\text{F3}&21&41&\text{6A}\\\hline\end{array}=\begin{array}{|c|c|c|c|c|c|}\hline\text{EB}&59&8\text{B}&1\text{B}\\\hline40&2\text{E}&\text{A1}&\text{C3}\\\hline\text{F2}&38&13&42\\\hline1\text{E}&84&\text{E7}&\text{D6}\\\hline\end{array}$
 
Verify the first addition: $\{47\}+\{\mathrm{AC}\}=(01000111)\oplus(10101100)=(11101011)=\{\mathrm{EB}\}$

Therefore, the output ciphertext, after a single round is: 
```
EB40F21E592E38848BA113E71BC342D6
```

Compare this to the initial input plaintext: 
```
EA835CF00445332D655D98AD8596B0C5
```


## AES Decryption
Each step in a single round of AES is <u>invertible</u>
1. <u>SubBytes is invertible</u> by the **Inverse S-Box** table.
2. <u>ShiftRows is invertible</u> by applying the inverse permutation for each row.
3. <u>MixColumns is invertible</u> by applying by the inverse of the encryption matrix:
	 inverse              x        encryption matrix  =       identity
	$\begin{bmatrix}0\mathrm{E}&0\mathrm{B}&0\mathrm{D}&09\\09&0\mathrm{E}&0\mathrm{B}&0\mathrm{D}\\0\mathrm{D}&09&0\mathrm{E}&0\mathrm{B}\\0\mathrm{B}&0\mathrm{D}&09&0\mathrm{E}\end{bmatrix}\begin{bmatrix}02&03&01&01\\01&02&03&01\\01&01&02&03\\03&01&01&02\end{bmatrix}=\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}$
4. <u>AddRoundKey is invertible</u> by adding the round key again.