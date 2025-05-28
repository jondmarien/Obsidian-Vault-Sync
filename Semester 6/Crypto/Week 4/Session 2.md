**Galois Fields**
$$ GF(p^{n})$$
- For encryption algorithms that operate on 2, 3, 4, ..., `n` bits of data at a time, we require finite fields of 2<sup>2</sup>, 2<sup>3</sup>, 2<sup>4</sup>, 2<sup>n</sup>
- The encryption algorithms used in the Advanced Encryption Standard (AES) operate on 8-bits of data at a time and require a finite field of order `256`. 
	- This is accomplished with `256` polynomial elements that are multiplied and added modulo `m(x)`, an irreducible polynomial of degree `8`.

*Example*
- Fill this out from slides

**Addition GF(2<sup>3</sup>)
![[Pasted image 20240131105955.png]]

**Multiplication GF(2<sup>3</sup>)
![[Pasted image 20240131110012.png]]
