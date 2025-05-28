# Week 1 - Session 1
Three main types of encryption  
## Transposition  
- Rearranging the order of the letters. The key is the permutation applied to the positions  

## Substitution  
- Individual letters are replaced in a systematic way by *different letters*. (i.e., every 'e' swapped with a 't')  
  
## Codebook  
- Complete words are replaced by different words  
## Definitions  
- Cryptology  
- Cryptanalysis  
- Encryption  
	- The process of disguising a message in such a way as to hide its substance  
- Decryption  
	- The process of turning ciphertext back into a plaintext

## Key  
- Secret-Key Cryptography  
	- The secret key is known only to both parties involved  
  
## Public-Key Crypto  
- Introduced in the 1970s by Diffie and Hellman  
- Public key to encrypt, private key to decrypt  
- RSA  
	- Much slower than secret-key  
  
  
## Z26 Encoding  
![Image-1](Week1-S1_1.png)  

## Polyalphabetic  
- The same character is encrypted by various characters depending on its position in the plaintext  
  
## Monoalphabetic  
- Each character is mapped to a unique alphabetic character  
## Symmetrical Encryption   
- Using the same key to encrypt AND decrypt  
  
## Asymmetrical Encryption  
- Using two different keys to encrypt and decrypt (k1 and k2)  
  
## Block Ciphers  
- Block of plaintext; block of ciphertext  
  
## Stream Ciphers  
- Encrypt one (bit) character at a time  
	- First uses a key to construct a keystream, then each bit is encrypted    
  
## Classical Methods (Private Key)  
### Affine ciphers  
$$ C=f\left(M\right)=(aM+b)mod26$$                                                                  where {a, b} is the private key  
### Inverse function 
 $$ M=a^{-1}(C-b)mod26$$ 
### Totient Function  
$$ \phi(m)=\prod_{i=1}^n(p_i^{e_i}-p_i^{e_i-1})$$
$$ \phi(m)=(2^2-2^1)(3^1-3^0)(5^1-5^0)=2\times2\times4=16$$

  ### Shift ciphers  
  - Shifts the letters a fixed amount (all 'a' changed to 'f', all 'b' changed to 'g')  

$$ \mathrm{C}=\mathrm{f}(M)=(M+k)mod26$$
$$ \mathrm{M}=(C-k)mod26$$                                                                    where {k} is the private key  
  
  
### Transposition ciphers  
- The order of the characters is changed to obscure the message  
	 - Split into blocks size *n*  
		 - Find the inverse permutation to decrypt  
  
  
## Vigenère ciphers  
- Relatively large key space  
- Symmetric cipher  
- Polyalphabetic  
- Requires a key (a word), split the message into blocks of m, where m is the amount of letters in the key. Then convert the key and the message into an integer string. Combine the two integer strings, run mod26, for each character, and then you have the secret message