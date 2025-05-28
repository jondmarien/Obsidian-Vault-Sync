---
title: Signature Schemes (Hash-Based)
author:
  - Jon Marien
created: 2025-03-10
published: 2025-03-10
tags:
  - classes
  - MATH36206
---

| Title                        | Author                       | Created        | Published      | Tags                                               |
| ---------------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Hash-Based Signature Schemes | <ul><li>Jon Marien</li></ul> | March 10, 2025 | March 10, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |

# Hash-Based Signature Schemes
Signature schemes that are based on cryptographically secure hash functions (like `SHA-256`) are of particular interest as there are, as far as we know, no practical quantum attacks for secure hashing functions. **Conventional** Signature schemes such as Elgamal or (EC)DSA rely on the DLP for their security and are vulnerable to quantum attacks. 

## Lamport Signature Scheme (Chp. 9.1)
The Lamport Signature Scheme involves signing a $k$-bit message using $2k$ private keys and another $2k$ public keys. The public keys are just the hash values of the private keys. The hash values related to the variable $y$: $y_{0,0}$, $y_{1,0}$ , etc..

**The first value** of the y subset is the 1st, 2nd, 3rd, or nth row or version of y coords. **The second value** of the y subset is corresponding to whether the given message has a value in that row. See [Generic Lamport Scheme Example](#Generic%20Lamport%20Scheme%20Example). 

If the hash function $h$ is cryptographically secure, then it is not feasible to determine the private keys given all the public keys:

- $k$-bit message
- $z_{i,j}$ are the $2k$ public keys
- $y_{i,j}$ are the $2k$ private keys.
- $1 \leq i \leq k$
- $0 \leq j \leq 1$
- $z_{i,j} = h(y_{i,j})$ where $h$ is the secure hash function.

### Generic Lamport Scheme Example
Sign the 3-bit message *"110"* using the (2(3) = **6**) private keys given by:
$$ [y_{1,0}$$
$$y_{1,1}$$
$$y_{2,0}$$
$$y_{2,1}$$
$$y_{3,0}$$
$$y_{3,1}]$$
First, publish the hash values of the private keys (i.e., make the 6 public keys):
$$[z_{1,0}=h(y_{1,0})$$
$$z_{1,1}=h(y_{1,1})$$$$z_{2,0}=h(y_{2,0})$$$$z_{2,1}=h(y_{2,1})$$$$z_{3,0}=h(y_{3,0})$$$$z_{3,1}=h(y_{3,1})]$$
Then sign "*110*" by revealing the secret keys corresponding to the $1$ bits. These are $y_{1,1}$, $y_{2,1}$, $y_{3,0}$. 

$$\boxed{\therefore \text{The signature is} (y_{1,1}, y_{2,1}, y_{3,0})}$$

To verify a signature using the public key, we check that:
$$h(y_{1,1})=z_{1,1}$$
$$h(y_{2,1})=z_{2,1}$$
$$h(y_{3,0})=z_{3,0}$$

#### Numeric Lamport Scheme Example
Usually, computing `SHA-256` hashes by hand is quite hard (next to impossible), we can substitute a really not secure hash function, such as $h(x)=g^x\cdot \pmod{p}$:

Sign the 3-bit message "*110*" using $h(x)=2^x \pmod{37}$ and private keys:
$$y_{1,0} = 23$$
$$y_{1,1} = 5$$
$$y_{2,0}=31$$
$$y_{2,1}=7$$
$$y_{3,0}=11$$
$$y_{3,1}=2$$
The public keys are:
$$z_{1,0}=h(y_{1,0}) = 5$$
$$z_{1,1}=h(y_{1,1}) = 32$$$$z_{2,0}=h(y_{2,0})=22$$$$z_{2,1}=h(y_{2,1})=17$$$$z_{3,0}=h(y_{3,0})=13$$$$z_{3,1}=h(y_{3,1})=26$$
Then, sign "*110*" by revealing the secret keys corresponding to the $1$ bits. These are $5,7, \text{\:and\:} 11$. The signature is ($5,7,11$).

To verify a signature using the public key, we compute:
$$h(5)=2^5\mod37=32$$$$h(7)=2^7\mod37=17$$$$h(11)=2^{11}\mod37=13$$
#### One-time Signature Schemes
The Lamport Signature Scheme is a one-time signature scheme because it only has **full** security on the **first** signature. Each signature for a $k$-bit message reveals $k$ of the $2k$ private keys, so it may be possible to construct valid signatures after observing just two signatures using the same public key.

For example, if a signature for `110` and `001` are observed then we can construct signatures for any other 3-bit message. This is because each pair has a missing entry where the other message bits fills it in. 
## Merkle Signature Scheme (Chp. 9.2)
The main downside of one-time signature scheme (i.e., Lamport) is that a new public key **must** be generated for each message to maintain full security. The Merkle Signature Scheme allows for a single overall public key to be used multiple times. The single overall public key is the value of the root node of a "Merkle Tree".

### Merkle Trees
Merkle Trees are complete (full) binary trees of depth $d$. Each of the $j$ lead nodes has a value equal to the hash of some key $K_{j-2^{d}+1}$. Each of the internal nodes has a value equal to the ***hash of it's children***. A Merkle tree with depth $d$ has:
- A total of $2^{d+1}-1$ nodes wit labels $j=1,2,3,\dots,2^{d+1}-1$.
- $2^d$ leaf nodes with Values $V(j)=h(K_{j-2^{d}+1})$.
- Remaining internal nodes with values $V(j)=h(V(\text{left child})\;\;\;||\;\;\; V(\text{right child}))$.
Where $h$ is a **secure hash function**, and "||" denotes the concatenation of any two values. Left side first, followed by right side. ***Order is important.***

#### Merkle Tree Example
Determine the value of the root node of a Merkle Tree with depth $d = 2$ with keys $K_1 = 10,\;K_2 = 20,\;K_3 = 30,\;K_4 = 40$, and hash function $h(x) = x \pmod{7}$:

The tree has a total of $2^{2+1}-1=7$ nodes, and $2^n = 4$ leaf nodes.

The values of each of the leaf nodes are:
$$V(4)=h(K_{4-2^{2}+1}) = h(K_{1}) = 10 \pmod{7} = 3$$
$$V(5)=h(K_{5-2^{2}+1}) = h(K_{2}) = 20 \pmod{7} = 6$$$$V(6)=h(K_{6-2^{2}+1}) = h(K_{3}) = 30 \pmod{7} = 3$$$$V(7)=h(K_{7-2^{2}+1}) = h(K_{7}) = 40 \pmod{7} = 5$$
The values of each of the internal nodes are:
$$V(3)=h(V(6)\;\;\;||\;\;\; V(7)) = h(2\;\;\;||\;\;\;5) = h(25) = 25 \pmod{7} = 4$$
$$V(2)=h(V(4)\;\;\;||\;\;\; V(5)) = h(3\;\;\;||\;\;\;6) = h(36) = 36 \pmod{7} = 1$$
$$V(1)=h(V(2)\;\;\;||\;\;\; V(3)) = h(1\;\;\;||\;\;\;4) = h(14) = 14 \pmod{7} = 0$$
Note that the values of the internal vertices can only be computed from "largest to smallest" with the value of the root note, $V(1)$, computed at end. Also, the hash function $h(x)$ used in this case is not secure... A real Merkle tree would use a hash function similar to $SHA-256(x)$ (instead of $h(x))$.

### Merkle Signature
In the previous example it was shown that to compute the value of the root node, $V(1)$, you need to know the value of all the other nodes in the Merkle tree. 

The Merkle signature for a message $m_i$ involves revealing the key, $K_i$, of a leaf node in the tree and using it as a public key to sign a message. This key, $K_i$, and signature, $s_i$, are sent with the values of any sibling nodes along the path back to the root. The entire signature has the form $(K_i, s_i, V(\text{sibling a}), V(\text{sibling b}), ...)$.

The receiver would use this information to compute the value of the root, $V(1)$, and compare it with the published value of $V(1)$, which is the overall public key for this scheme. 

**The maximum number of messages** that can be signed using the same overall public key **is equal to the number of leaf nodes** in the Merkle Tree.
#### Merkle Signature Example
Use the Merkle Tree from the previous 