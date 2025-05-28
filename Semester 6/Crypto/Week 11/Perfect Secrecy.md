# Perfect Secrecy

## What is It?
For a cryptosystem $(M,C,K,E,D)$ where:

$x\in M$, the set of all plaintext strings
$y\in C$, the set of all ciphertext strings
$k\in K$, the set of all encryption keys
$e_k\in E$, the set of all encryption rules for a key `k` (every rule can be the same encryption function)
$d_{k}\in D$, the set of all decryption rules for a key `k` (every rule can be the same decryption function)

This cryptosystem has perfect secrecy if $\mathbf{P}(\mathbf{x}\mid\mathbf{y})=\mathbf{P}(\mathbf{x})$ for all $\mathrm{x\in\mathcal{M}}$ and $y\in Q$.

## Example