---
title: Complete Study Guide
author:
  - Jon Marien
created: 2025-04-17
published: 2025-04-17
tags:
  - classes
  - MATH36206
---

| Title                | Author                       | Created        | Published      | Tags                                               |
| -------------------- | ---------------------------- | -------------- | -------------- | -------------------------------------------------- |
| Complete Study Guide | <ul><li>Jon Marien</li></ul> | April 17, 2025 | April 17, 2025 | [[#classes\|#classes]], [[#MATH36206\|#MATH36206]] |

## Advanced Cryptology Final Exam Study Notes (Weeks 8-12)

### Week 8: NP-complete Problem Based Cryptosystems

#### 1. Subset-Sum Problem

- **Definition:** Given a set of numbers $S = {x_1, ..., x_k}$ and a target sum $t$, the Subset-Sum problem is to determine if there exists a subset of $S$ that sums to $t$. Mathematically, find $b_i \in {0, 1}$ such that $t = \sum_{i=1}^{k} b_i \cdot x_i$.
- **Complexity:** The general Subset-Sum problem is **NP-complete**. A brute-force approach to find a solution has a time complexity of $O(2^k)$.

#### 2. Subset-Sum Cryptography (Basic Idea)

- Use a set $S$ as the **public key**. Encrypt a binary message $b_1b_2...b_k$ as the sum $t = \sum_{i=1}^{k} b_i \cdot s_i$, where $s_i \in S$.
- **Problem:** Decrypting $t$ to find the original binary message is equivalent to solving the hard Subset-Sum problem, making it computationally infeasible. Also, solutions may not be unique.

#### 3. Superincreasing Sequences

- **Definition:** A sequence $S = {s_1, s_2, ..., s_n}$ is **superincreasing** if each element is greater than the sum of all preceding elements: $s_i > \sum_{j=1}^{i-1} s_j$ for all $i > 1$. Example: ${3, 5, 9, 18, 38, 75, 155, 310}$.
- **Solving Subset-Sum with Superincreasing Sequences:** This can be done in **polynomial time** using a greedy algorithm.
    - To find a subset of $S$ that sums to $t$: Start with the largest element $s_n$. If $t \ge s_n$, include $s_n$ in the subset and update $t = t - s_n$. Repeat this process for the remaining elements in decreasing order.
    - **Example:** $S = {3, 5, 9, 18, 38, 75, 155, 310}$, $t = 242$.
        - $242 \ge 310$? No.
        - $242 \ge 155$? Yes. $t = 242 - 155 = 87$. Subset includes 155.
        - $87 \ge 75$? Yes. $t = 87 - 75 = 12$. Subset includes 75.
        - $12 \ge 38$? No.
        - $12 \ge 18$? No.
        - $12 \ge 9$? Yes. $t = 12 - 9 = 3$. Subset includes 9.
        - $3 \ge 5$? No.
        - $3 \ge 3$? Yes. $t = 3 - 3 = 0$. Subset includes 3.
        - Solution: ${3, 9, 75, 155}$, corresponding to binary string $10100110$.

#### 4. Trapdoor Functions for Subset-Sum

- **Trapdoor:** A way to transform a hard problem into an easy one using secret information. In the context of Subset-Sum cryptography, the trapdoor involves transforming a superincreasing set $S$ (easy to solve Subset-Sum) into a seemingly random set $A$ (hard to solve Subset-Sum without the trapdoor) using two integers $u$ and $v$:
    - $\text{GCD}(u, v) = 1$
    - $u > \sum_{i=1}^{n} s_i$ (or $u > 2s_n$)
    - $a_i = v \cdot s_i \pmod{u}$ for $1 \le i \le n$. The set $A = {a_1, a_2, ..., a_n}$ is the **public key**.

#### 5. Merkle-Hellman Knapsack Cipher

- **Private Key:** A superincreasing set $S = {s_1, ..., s_n}$ and the integers $u$ and $v$ used to generate the public key $A$.
- **Public Key:** The set $A = {a_1, ..., a_n}$.
- **Encryption:** To encrypt an $n$-bit plaintext $b_1b_2...b_n$, compute the ciphertext $t' = \sum_{i=1}^{n} b_i \cdot a_i$.
- **Decryption:** To decrypt $t'$:
    1. Compute the modular inverse of $v$ modulo $u$: $v^{-1} \pmod{u}$. This can be done using the Extended Euclidean Algorithm since $\text{GCD}(u, v) = 1$.
    2. Compute the target sum $t$ with respect to the superincreasing set $S$: $t = t' \cdot v^{-1} \pmod{u}$.
    3. Solve the Subset-Sum problem for $\langle S, t \rangle$. Since $S$ is superincreasing, this can be done in polynomial time to recover the binary plaintext $b_1b_2...b_n$.
- **Example:** Encrypt "Bat" using 8-bit ASCII and $A = {39, 65, 117, 234, 494, 303, 671, 670}$, $u = 672, v = 13$.
    - B (01000010): $t' = 0(39) + 1(65) + 0(117) + 0(234) + 0(494) + 0(303) + 1(671) + 0(670) = 736$.
    - a (01100001): $t' = 0(39) + 1(65) + 1(117) + 0(234) + 0(494) + 0(303) + 0(671) + 1(670) = 852$.
    - t (01110100): $t' = 0(39) + 1(65) + 1(117) + 1(234) + 0(494) + 1(303) + 0(671) + 0(670) = 719$.
    - Decryption of 736: $v^{-1} \pmod{u} = 13^{-1} \pmod{672} = 517$. $t = 736 \cdot 517 \pmod{672} = 160$. Solving Subset-Sum for $S = {3, 5, 9, 18, 38, 75, 155, 310}$ and $t = 160$ gives $155 + 5$, so $01000010$ (B).
- **Security Basis:** Relies on the assumption that solving the general Subset-Sum problem is hard (NP-complete), while solving it for a superincreasing set is easy. The trapdoor $(u, v)$ allows the legitimate user to transform the hard problem back to the easy one.
- **Resistance to Quantum Attacks:** Not directly broken by known quantum algorithms like Shor's algorithm (which targets factoring and discrete logarithms). However, the security relies on the classical hardness of Subset-Sum. Future advancements in quantum algorithms could potentially impact its security.
- **Time Complexity:**
    - Key Generation: Generating a superincreasing sequence of length $n$ takes $O(n)$. Modular multiplications to get $A$ take $O(n)$. Finding $v^{-1}$ using EEA takes roughly $O(\log^2 u)$.
    - Encryption: Summation of $n$ terms, $O(n)$.
    - Decryption: Modular multiplication $O(\log^2 u)$. Solving superincreasing Subset-Sum takes $O(n)$.
- **Classical vs. Post-Quantum:** A classical public-key cryptosystem based on the hardness of an NP-complete problem.
- **Exam-style Exercises:** Determine if a set is superincreasing. Compute the public key $A$ from $S, u, v$. Encrypt and decrypt using Merkle-Hellman. Prove Subset-Sum is in P for superincreasing sets. Explain the condition $u > 2s_n$.
    - **Short Solutions/Outlines:**
        - 8.1 a) Check if each element is greater than the sum of the preceding ones. Then use the greedy algorithm for Subset-Sum.
        - 8.2 Use $s_i = v^{-1} a_i \pmod{u}$.
        - 8.3 Use $a_i = v s_i \pmod{u}$.
        - 8.4 Perform the summation $t' = \sum b_i a_i$.
        - 8.5 a) Use EEA. b) $s_i = v^{-1} a_i \pmod{u}$, $t = t' v^{-1} \pmod{u}$. c) Greedy algorithm on $S$ with target $t$. d) Verify the sum.
        - 8.6 Describe the greedy algorithm and its linear time complexity.
        - 8.7 To ensure that the result of $t' v^{-1} \pmod{u}$ corresponds to a unique sum of elements in $S$ with binary coefficients, avoiding wrap-around issues.

#### Flashcards (Week 8)

- **Subset-Sum Problem:** Finding a subset of a set that sums to a target.
- **NP-complete:** A class of problems believed to be computationally hard to solve in polynomial time.
- **Superincreasing Sequence:** Each element is greater than the sum of preceding elements.
- **Polynomial Time:** Computational time that grows polynomially with the input size (considered efficient).
- **Trapdoor Function:** A function easy to compute in one direction but hard to reverse without special information (the trapdoor).
- **Modular Inverse:** An element $v^{-1}$ such that $v \cdot v^{-1} \equiv 1 \pmod{u}$.
- **Merkle-Hellman Knapsack Cipher:** A public-key cryptosystem based on the Subset-Sum problem and superincreasing sequences.
- **Public Key (Merkle-Hellman):** The transformed set $A$.
- **Private Key (Merkle-Hellman):** The superincreasing set $S$ and the moduli $u, v$.
- **Encryption (Merkle-Hellman):** Sum of a subset of the public key elements.
- **Decryption (Merkle-Hellman):** Uses the trapdoor to solve an easy Subset-Sum problem.

#### Original Practice Problems (Week 8)

1. Determine if the set $S = {2, 3, 6, 13, 27}$ is superincreasing. If it is, find a subset that sums to $t = 32$.
    
    - **Solution:**
        - Is it superincreasing? $3 > 2$ (Yes), $6 > 2+3=5$ (Yes), $13 > 2+3+6=11$ (Yes), $27 > 2+3+6+13=24$ (Yes). So, $S$ is superincreasing.
        - Subset sum for $t=32$:
            - $32 \ge 27$? Yes. $t = 32 - 27 = 5$. Subset includes 27.
            - $5 \ge 13$? No.
            - $5 \ge 6$? No.
            - $5 \ge 3$? Yes. $t = 5 - 3 = 2$. Subset includes 3.
            - $2 \ge 2$? Yes. $t = 2 - 2 = 0$. Subset includes 2.
            - Subset: ${2, 3, 27}$, corresponding to binary $11001$.
2. Given the superincreasing set $S = {5, 8, 17, 35}$ and $u = 80, v = 21$. Compute the public key $A$ for the Merkle-Hellman knapsack cipher.
    
    - **Solution:**
        - $a_1 = 21 \cdot 5 \pmod{80} = 105 \pmod{80} = 25$.
        - $a_2 = 21 \cdot 8 \pmod{80} = 168 \pmod{80} = 8$.
        - $a_3 = 21 \cdot 17 \pmod{80} = 357 \pmod{80} = 37$.
        - $a_4 = 21 \cdot 35 \pmod{80} = 735 \pmod{80} = 15$.
        - Public key $A = {25, 8, 37, 15}$.
3. Encrypt the message "101" using the public key $A = {25, 8, 37, 15}$ from the previous problem.
    
    - **Solution:**
        - Plaintext "1010" (assuming 4-bit message).
        - $t' = 1(25) + 0(8) + 1(37) + 0(15) = 25 + 37 = 62$.
        - Ciphertext: $62$.
4. Given $u = 80, v = 21$, find $v^{-1} \pmod{u}$.
    
    - **Solution:** We need to find $x$ such that $21x \equiv 1 \pmod{80}$. Using the Extended Euclidean Algorithm:
        - $80 = 3 \cdot 21 + 17$
        - $21 = 1 \cdot 17 + 4$
        - $17 = 4 \cdot 4 + 1$
        - $1 = 17 - 4 \cdot 4 = 17 - 4 \cdot (21 - 1 \cdot 17) = 17 - 4 \cdot 21 + 4 \cdot 17 = 5 \cdot 17 - 4 \cdot 21 = 5 \cdot (80 - 3 \cdot 21) - 4 \cdot 21 = 5 \cdot 80 - 15 \cdot 21 - 4 \cdot 21 = 5 \cdot 80 - 19 \cdot 21$.
        - So, $-19 \cdot 21 \equiv 1 \pmod{80}$. $-19 \equiv -19 + 80 = 61 \pmod{80}$.
        - $v^{-1} \equiv 61 \pmod{80}$.
5. Consider a Merkle-Hellman cryptosystem with superincreasing set $S = {2, 7, 15}$ and $u = 32, v = 3$. The public key is $A = {6, 21, 13}$. You receive a ciphertext $t' = 27$. Decrypt the ciphertext.
    
    - **Solution:**
        - Find $v^{-1} \pmod{u}$: $3x \equiv 1 \pmod{32}$. Using EEA (or by inspection), $x = 11$ since $3 \cdot 11 = 33 \equiv 1 \pmod{32}$. So, $v^{-1} = 11$.
        - Compute $t = t' \cdot v^{-1} \pmod{u} = 27 \cdot 11 \pmod{32} = 297 \pmod{32} = 9$.
        - Solve Subset-Sum for $S = {2, 7, 15}$ and $t = 9$:
            - $9 \ge 15$? No.
            - $9 \ge 7$? Yes. $t = 9 - 7 = 2$. Subset includes 7.
            - $2 \ge 2$? Yes. $t = 2 - 2 = 0$. Subset includes 2.
            - Plaintext: $110$.

### Week 9: Hash-based Signature Schemes

#### 1. Lamport Signature Scheme

- **Key Generation:** For a $k$-bit message, generate $2k$ private keys $y_{i,j}$ (for $1 \le i \le k, j \in {0, 1}$). Compute the corresponding public keys $z_{i,j} = h(y_{i,j})$, where $h$ is a secure hash function. The public key is the set of all $z_{i,j}$'s.
- **Signing a $k$-bit message $m = m_1m_2...m_k$:** For each bit $m_i$:
    - If $m_i = 0$, reveal the private key $y_{i,0}$.
    - If $m_i = 1$, reveal the private key $y_{i,1}$.
    - The signature is the $k$-tuple of revealed private keys.
- **Verification of a signature $(s_1, s_2, ..., s_k)$ for a message $m = m_1m_2...m_k$:** For each part of the signature $s_i$:
    - If $m_i = 0$, check if $h(s_i) = z_{i,0}$.
    - If $m_i = 1$, check if $h(s_i) = z_{i,1}$.
    - The signature is valid if all checks pass.
- **One-time Signature:** The Lamport scheme is a **one-time signature** because each private key bit is used at most once per message. Using the same key pair to sign two different messages can compromise security.
- **Security Basis:** Relies on the **preimage resistance** of the hash function $h$. Given a hash value $z_{i,j}$, it should be computationally infeasible to find the corresponding private key $y_{i,j}$.
- **Resistance to Quantum Attacks:** Secure hash functions (like SHA-256) are believed to be resistant to practical quantum attacks, making Lamport signatures a candidate for **post-quantum cryptography**.
- **Time Complexity:** Key generation involves $2k$ hash computations. Signing involves revealing $k$ private keys (no computation). Verification involves $k$ hash computations.
- **Classical vs. Post-Quantum:** A post-quantum signature scheme.
- **Exam-style Exercises:** Find the Lamport public key and sign a given message. Determine which other messages can be signed if signatures for certain messages are observed.
    - **Short Solutions/Outlines:**
        - 9.1 Compute $z_{i,j} = h(y_{i,j})$. For the message "10", the signature is $(y_{1,1}, y_{2,0})$.
        - 9.2 Compute $z_{i,j} = h(y_{i,j})$. For "0111", signature is $(y_{1,0}, y_{2,1}, y_{3,1}, y_{4,1})$.
        - 9.3 If "011" reveals $y_{1,0}, y_{2,1}, y_{3,1}$ and "101" reveals $y_{1,1}, y_{2,0}, y_{3,1}$, then $y_{1,0}$ and $y_{1,1}$ are known, $y_{2,0}$ and $y_{2,1}$ are known, and $y_{3,1}$ is known. We can sign "111" (using $y_{1,1}, y_{2,1}, y_{3,1}$) and "001" (using $y_{1,0}, y_{2,0}, y_{3,1}$).
        - 9.4 Analyze which private keys are revealed by the given signatures and determine which new messages can be formed using these revealed keys.

#### 2. Merkle Signature Scheme

- **Merkle Tree:** A complete binary tree where each leaf node's value is the hash of a key, and each internal node's value is the hash of the concatenation of its children's values.
    - Depth $d$ has $2^d$ leaf nodes and a total of $2^{d+1} - 1$ nodes.
    - Leaf node $j$ (for $j = 2^d$ to $2^{d+1} - 1$) has value $V(j) = h(K_{j-2^d+1})$.
    - Internal node $j$ has value $V(j) = h(V(\text{left child}) || V(\text{right child}))$. The root node is $V(1)$.
- **Merkle Signature Generation for message $m_i$ using leaf key $K_i$:**
    1. Use the key $K_i$ to sign the message $m_i$ using a one-time signature scheme (like Lamport) to get signature $s_i$.
    2. Identify the path from the leaf node corresponding to $K_i$ back to the root of the Merkle tree.
    3. The Merkle signature consists of the key $K_i$, the one-time signature $s_i$, and the **sibling nodes** along the path to the root.
- **Merkle Signature Verification:**
    1. Compute the hash of the provided key $K_i$ to get the value of the leaf node.
    2. Using the provided sibling nodes, compute the value of the parent node by hashing the concatenation of the leaf node's value and the sibling's value (in the correct order).
    3. Repeat this process, moving up the tree, using the sibling nodes at each level until the root's value is computed.
    4. Compare the computed root value with the publicly known root value. If they match, the signature is valid.
- **Security Basis:** Relies on the security of the underlying one-time signature scheme and the **collision resistance** of the hash function used to build the Merkle tree. An attacker should not be able to create another valid path to the same root with a different leaf key.
- **Resistance to Quantum Attacks:** Since it relies on secure hash functions, Merkle signatures are considered **post-quantum**.
- **Time Complexity:** Building the Merkle tree takes time proportional to the number of nodes times the hash computation time. Signing and verifying involve a one-time signature operation and traversing the tree to the root, with hash computations at each level (logarithmic in the number of leaves). Signature size includes the one-time signature and a logarithmic number of hash values.
- **Classical vs. Post-Quantum:** A post-quantum signature scheme.
- **Exam-style Exercises:** Determine the root node value of a Merkle tree. Use a Merkle tree to sign a message. Determine the number of messages that can be signed.
    - **Short Solutions/Outlines:**
        - 9.5 a) Compute the hash of each key (leaf nodes). Then compute the hash of the concatenation of children's hashes, moving up to the root.
        - 9.5 b) Use $K_1$ to sign $m_1$, identify the path to the root, and include sibling nodes' values.
        - 9.5 c) Similar to b) using $K_4$.
        - 9.5 d) Similar to b) using $K_3$.
        - 9.6 a) Same as 9.5 a) for a depth 3 tree.
        - 9.6 b) Use $K_6$ to sign $m_6$, identify the path, and include siblings.
        - 9.6 c) Use $K_2$ to sign $m_2$, identify the path, and include siblings.
        - 9.6 d) The number of signable messages is equal to the number of leaf nodes ($2^d$).

#### Flashcards (Week 9)

- **Hash-based Signature:** A digital signature scheme that relies on the security of cryptographic hash functions.
- **Preimage Resistance:** A property of a hash function where it's hard to find an input that produces a specific output.
- **Collision Resistance:** A property of a hash function where it's hard to find two different inputs that produce the same output.
- **Lamport Signature Scheme:** A one-time signature scheme using pairs of private/public keys based on a hash function.
- **One-time Signature:** A signature scheme where each key pair can only be used to sign one message securely.
- **Merkle Tree:** A binary tree where leaves are hashes of data blocks, and internal nodes are hashes of their children.
- **Root Node (Merkle Tree):** The top node of the Merkle tree, representing the hash of all data blocks.
- **Sibling Node (Merkle Tree):** A node that shares the same parent as another node.
- **Merkle Signature Scheme:** A digital signature scheme that uses a Merkle tree to allow a single public key to be used for multiple signatures.
- **Path to the Root (Merkle Tree):** The sequence of nodes from a leaf to the root.

#### Original Practice Problems (Week 9)

1. Generate the Lamport public key for a 2-bit message using the hash function $h(x) = x^2 \pmod{17}$ and the private keys $y_{1,0} = 2, y_{1,1} = 3, y_{2,0} = 5, y_{2,1} = 7$. Then, sign the message "01".
    
    - **Solution:**
        - Public keys: $z_{1,0} = 2^2 \pmod{17} = 4$, $z_{1,1} = 3^2 \pmod{17} = 9$, $z_{2,0} = 5^2 \pmod{17} = 25 \pmod{17} = 8$, $z_{2,1} = 7^2 \pmod{17} = 49 \pmod{17} = 15$.
        - Public key: $(z_{1,0}=4, z_{1,1}=9, z_{2,0}=8, z_{2,1}=15)$.
        - Signing "01": Reveal $y_{1,0}$ (since the first bit is 0) and $y_{2,1}$ (since the second bit is 1).
        - Signature: $(2, 7)$.
2. Verify the Lamport signature $(2, 7)$ for the message "01" using the public key from the previous problem and the hash function $h(x) = x^2 \pmod{17}$.
    
    - **Solution:**
        - For the first bit (0), check if $h(2) = z_{1,0}$. $h(2) = 2^2 \pmod{17} = 4$, and $z_{1,0} = 4$. Match.
        - For the second bit (1), check if $h(7) = z_{2,1}$. $h(7) = 7^2 \pmod{17} = 49 \pmod{17} = 15$, and $z_{2,1} = 15$. Match.
        - Signature is valid.
3. Consider a Merkle tree of depth $d=1$ with keys $K_1 = 11, K_2 = 19$ and hash function $h(x) = x \pmod{5}$. Determine the root node value.
    
    - **Solution:**
        - Leaf nodes: $V(2) = h(K_1) = 11 \pmod{5} = 1$, $V(3) = h(K_2) = 19 \pmod{5} = 4$.
        - Root node: $V(1) = h(V(2) || V(3)) = h(1 || 4) = h(14) = 14 \pmod{5} = 4$.
4. Using the Merkle tree from the previous problem, sign the message $m_1$ (corresponding to $K_1$) assuming the one-time signature for $m_1$ using $K_1$ is $s_1$. Provide the Merkle signature.
    
    - **Solution:**
        - Leaf node for $K_1$ is node 2. Path to root is 2 -> 1. Sibling of node 2 is node 3 with value $V(3) = 4$.
        - Merkle signature: $(K_1=11, s_1, V(3)=4)$.
5. Verify the Merkle signature $(K_1=11, s_1, V(3)=4)$ for message $m_1$ using the hash function $h(x) = x \pmod{5}$ and the root value $V(1) = 4$.
    
    - **Solution:**
        - Compute leaf value: $V(2) = h(K_1) = 11 \pmod{5} = 1$.
        - Compute root value: $V(1) = h(V(2) || V(3)) = h(1 || 4) = h(14) = 14 \pmod{5} = 4$.
        - The computed root value (4) matches the public root value (4). The Merkle signature is valid (assuming the one-time signature $s_1$ is also valid for $m_1$ using $K_1$).

### Week 10: Learning With Errors (LWE) and Regev Cryptosystem

#### 1. Learning With Errors (LWE) Problem

- **Parameters:** Prime modulus $q$, dimension $n$, number of samples $m$. Secret $s \in (\mathbb{Z}_q)^n$. $m$ samples $((a_1, ..., a_n)_i, b_i)$ where $a_i \in (\mathbb{Z}_q)^n$ and $b_i \in \mathbb{Z}_q$. Error $e_i$ drawn from a probability distribution over $-\lfloor q/2 \rfloor$ to $+\lfloor q/2 \rfloor$.
- **Relationship:** $b_i = (\sum_{j=1}^{n} a_{ij} s_j + e_i) \pmod{q}$ for $1 \le i \le m$.
- **Problem Statement:** Given $m$ samples $((a_i, b_i))$, find the secret $s$. The errors $e_i$ make this problem hard to solve with certainty.
- **Basis for Post-Quantum Cryptography:** No efficient quantum algorithm is known to solve LWE when the errors are sufficiently large.

#### 2. Regev Public Key Cryptosystem

- **Parameters:** Integers $n, m$, prime $q$.
- **Private Key:** A secret vector $s = (s_1, ..., s_n) \in (\mathbb{Z}_q)^n$.
- **Public Key:** $m$ samples $((a_1, ..., a_n)_i, b_i) \in (\mathbb{Z}_q)^{n+1}$ where $b_i = (\sum_{j=1}^{n} a_{ij} s_j + e_i) \pmod{q}$, and $e_i$ are small random errors.
- **Encryption of a single bit $x \in {0, 1}$:**
    1. Select a random subset $S \subseteq {1, 2, ..., m}$.
    2. Ciphertext $y = ((a_1, ..., a_n), b)$ where:
        - If $x = 0$: $a = (\sum_{i \in S} a_i) \pmod{q}$, $b = (\sum_{i \in S} b_i) \pmod{q}$.
        - If $x = 1$: $a = (\sum_{i \in S} a_i) \pmod{q}$, $b = (\lfloor q/2 \rfloor + \sum_{i \in S} b_i) \pmod{q}$.
- **Decryption of ciphertext $y = (a, b)$:**
    1. Compute $x^* = (b - \sum_{j=1}^{n} a_j s_j) \pmod{q}$.
    2. If $x^_$ is closer to 0 than to $\lfloor q/2 \rfloor$, the decrypted bit is 0. Otherwise, it is 1. Closer means $|x^_| < |x^* - \lfloor q/2 \rfloor|$ (considering values in the range $-\lfloor q/2 \rfloor$ to $+\lfloor q/2 \rfloor$ or comparing distances on the modulo $q$ ring).
- **Possibility of Decryption Errors:** Can occur if the sum of the errors in the chosen subset $S$ is large enough to shift $x^*$ to the wrong side of $\lfloor q/2 \rfloor$.
- **Security Basis:** Provably secure based on the hardness of the LWE problem.
- **Resistance to Quantum Attacks:** Believed to be resistant to known quantum algorithms.
- **Time Complexity:** Encryption involves summing vectors and scalars, depending on the size of $S$. Decryption involves a dot product and a subtraction modulo $q$. Ciphertext size is $n+1$ elements of $\mathbb{Z}_q$ per bit of plaintext, leading to large overhead.
- **Classical vs. Post-Quantum:** A post-quantum public-key cryptosystem.
- **Exam-style Exercises:** Solve LWE problems (without errors to understand the underlying linear system). Encrypt and decrypt bits using Regev. Determine the number of private keys and subsets for encryption. Analyze ciphertext size.
    - **Short Solutions/Outlines:**
        - 10.1 Solve the system of linear equations modulo $q$.
        - 10.8 a) Choose $S={2, 3}$, compute sums of $a_i$ and $b_i$, add $\lfloor q/2 \rfloor$ to $b$ since $x=1$.
        - 10.8 e) For each ciphertext, compute $x^* = (b - a \cdot s) \pmod{q}$ and compare with $\lfloor q/2 \rfloor$.
        - 10.9 a) Number of choices for each $s_i$ is $q$, so $q^n$.
        - 10.9 b) Number of non-empty subsets of a set of size $m$ is $2^m - 1$.
        - 10.9 c) Ciphertext size is fixed, plaintext is 1 bit.

#### Flashcards (Week 10)

- **Learning With Errors (LWE):** A lattice-based problem involving solving noisy linear equations modulo $q$.
- **Secret (LWE):** The vector $s$ that is being sought.
- **Samples (LWE):** Pairs of vectors $a_i$ and scalars $b_i$.
- **Error (LWE):** The small random value $e_i$ added to the equation.
- **Regev Cryptosystem:** A public-key cryptosystem based on the LWE problem.
- **Private Key (Regev):** The secret vector $s$.
- **Public Key (Regev):** A set of LWE samples.
- **Encryption (Regev):** Encodes a bit by selecting a subset of public key samples and summing them (with an offset for bit 1).
- **Decryption (Regev):** Recovers the bit by computing a value and comparing it to $q/2$.
- **Post-Quantum Cryptography:** Cryptographic systems believed to be secure against attacks by quantum computers.
- **Lattice-based Cryptography:** Cryptographic systems whose security relies on the hardness of problems on mathematical lattices.

#### Original Practice Problems (Week 10)

1. Solve the LWE problem with $q = 5, e = (0, 0)$ and samples $((1, 2), 3), ((3, 1), 4)$. Find the secret $s = (s_1, s_2)$.
    
    - **Solution:**
        - $1s_1 + 2s_2 \equiv 3 \pmod{5}$
        - $3s_1 + 1s_2 \equiv 4 \pmod{5}$
        - Multiply the second equation by 2: $6s_1 + 2s_2 \equiv 8 \pmod{5} \Rightarrow s_1 + 2s_2 \equiv 3 \pmod{5}$. This is the same as the first equation, indicating dependence.
        - From the first equation, $s_1 = 3 - 2s_2 \pmod{5}$. Substitute into the second: $3(3 - 2s_2) + s_2 \equiv 4 \pmod{5} \Rightarrow 9 - 6s_2 + s_2 \equiv 4 \pmod{5} \Rightarrow 4 - s_2 \equiv 4 \pmod{5} \Rightarrow s_2 \equiv 0 \pmod{5}$.
        - If $s_2 = 0$, then $s_1 = 3 - 2(0) = 3 \pmod{5}$. Secret $s = (3, 0)$.
2. For the Regev cryptosystem with $q = 7$, public key $((1, 3), 2), ((2, 1), 5)$ and private key $s = (4, 1)$. Encrypt the bit "0" using the subset $S = {1}$.
    
    - **Solution:**
        - For $x = 0$, ciphertext $y = (a, b) = (a_1, b_1) = ((1, 3), 2)$.
3. Using the same parameters as the previous problem, encrypt the bit "1" using the subset $S = {2}$. $\lfloor q/2 \rfloor = \lfloor 3.5 \rfloor = 3$.
    
    - **Solution:**
        - For $x = 1$, ciphertext $y = (a_2, \lfloor q/2 \rfloor + b_2 \pmod{q}) = ((2, 1), 3 + 5 \pmod{7}) = ((2, 1), 8 \pmod{7}) = ((2, 1), 1)$.
4. Decrypt the ciphertext $y = ((3, 4), 6)$ in the Regev cryptosystem with $q = 11$ and private key $s = (2, 3)$.
    
    - **Solution:**
        - $x^* = (b - (a_1 s_1 + a_2 s_2)) \pmod{q} = (6 - (3 \cdot 2 + 4 \cdot 3)) \pmod{11} = (6 - (6 + 12)) \pmod{11} = (6 - 18) \pmod{11} = -12 \pmod{11} = -1 \pmod{11} = 10$.
        - $\lfloor q/2 \rfloor = \lfloor 5.5 \rfloor = 5$.
        - $|10 - 0| = 10$, $|10 - 5| = 5$. $x^*$ is closer to 5 than 0. Decrypted bit is 1.
5. How many different private keys are there for a Regev cryptosystem with $q = 19$ and $n = 2$?
    
    - **Solution:**
        - The private key $s = (s_1, s_2)$ where $s_1, s_2 \in \mathbb{Z}_{19}$.
        - There are 19 choices for $s_1$ and 19 choices for $s_2$.
        - Total number of private keys is $19 \cdot 19 = 361$.

### Week 11: Module Learning with Errors (MLWE) and Kyber Cryptosystem

#### 1. Module Learning with Errors (MLWE) Problem

- **Parameters:** Polynomial modulus $f(x)$ of degree $n$, prime modulus $q$. Number of polynomials per vector $k$. Secret vector of $k$ polynomials $s(x) = (s_1(x), ..., s_k(x))$ where coefficients are in $\mathbb{Z}_q$. $k \times k$ matrix of polynomials $A$ with coefficients in $\mathbb{Z}_q$. Error vector of $k$ polynomials $e(x) = (e_1(x), ..., e_k(x))$ with coefficients in $\mathbb{Z}_q$ and degrees $< n$.
- **Relationship:** $t(x) = As(x) + e(x) \pmod{f(x), q}$, where $t(x)$ is a vector of $k$ polynomials (the samples).
- **Problem Statement:** Given $A$ and $t(x)$, find the secret vector $s(x)$. The error $e(x)$ makes this hard.
- **Basis for Post-Quantum Cryptography:** MLWE is a lattice-based problem believed to be hard for quantum computers.

#### 2. Kyber Public Key Cryptosystem

- **Parameters:** Polynomial modulus $f(x)$ (e.g., $x^{256} + 1$), prime modulus $q = 3329$. Parameters $n$ (degree of polynomials) and $k$ (number of polynomials per vector) vary (e.g., $n=256, k=2$ for Kyber512).
- **Public Key:** $(A, t(x))$, where $A$ is a $k \times k$ matrix of polynomials and $t(x) = As(x) + e(x) \pmod{f(x), q}$.
- **Private Key:** A vector of $k$ polynomials $s(x)$.
- **Encryption of a message $m$ (often 256 bits):**
    1. Encode $m$ as a message polynomial $m(x)$ of degree $< n/8$ with coefficients in ${0, ..., 8}$ (after upscaling).
    2. Generate a random polynomial vector $r(x)$ and small error vectors $e_1(x), e_2(x)$.
    3. Compute $u(x) = A^T r(x) + e_1(x) \pmod{f(x), q}$ (a vector of $k$ polynomials).
    4. Compute $v(x) = t(x)^T r(x) + e_2(x) + m(x) \pmod{f(x), q}$ (a single polynomial).
    5. Ciphertext is $(u(x), v(x))$.
- **Decryption of ciphertext $(u(x), v(x))$:**
    1. Compute $m^*(x) = v(x) - s(x)^T u(x) \pmod{f(x), q}$.
    2. Convert the coefficients of $m^*(x)$ to binary. For each coefficient $c_i$, if it's closer to 0 than to $\lfloor q/2 \rfloor$, the corresponding bit is 0, otherwise 1.
- **Number Theoretic Transform (NTT):** Used for efficient multiplication of polynomials in Kyber implementations.
- **Security Basis:** Based on the hardness of the MLWE problem.
- **Resistance to Quantum Attacks:** A primary candidate for post-quantum cryptography, selected by NIST for standardization.
- **Time Complexity:** Encryption and decryption involve polynomial matrix/vector multiplications and additions, which are made efficient using NTT. Complexity depends on $n$ and $k$. Encryption of 256 bits per ciphertext is efficient.
- **Classical vs. Post-Quantum:** A post-quantum public-key cryptosystem.
- **Exam-style Exercises:** Find $t(x)$ for MLWE given $A, s(x), e(x)$. Encrypt and decrypt binary messages using a Kyber system with given parameters. Convert binary to message polynomials and vice versa for Kyber.
    - **Short Solutions/Outlines:**
        - 11.1 Perform the matrix-vector multiplication $As(x) \pmod{f(x), q}$ and add $e(x)$. Remember polynomial arithmetic modulo $f(x)$ and $q$.
        - 11.2 Follow the encryption steps: generate random $r, e_1, e_2$, compute $u$ and $v$.
        - 11.3 Follow decryption: compute $m^* = v - s^T u$, then convert coefficients to binary.
        - 11.4 Group binary bits into blocks, represent as coefficients of a polynomial, and upscale.
        - 11.5 For each coefficient, compare its distance to 0 and $\lfloor q/2 \rfloor$.

#### Flashcards (Week 11)

- **Module Learning With Errors (MLWE):** A generalization of LWE using polynomials and module structures.
- **Polynomial Modulus $f(x)$:** A polynomial used for reducing other polynomials.
- **Coefficient Modulus $q$:** A prime modulus for the coefficients of the polynomials.
- **Secret Polynomial Vector $s(x)$:** The secret in the MLWE problem.
- **Kyber Cryptosystem:** A post-quantum public-key cryptosystem based on the MLWE problem.
- **Number Theoretic Transform (NTT):** An efficient algorithm for polynomial multiplication (analogous to FFT).
- **Public Key (Kyber):** A pair $(A, t(x))$.
- **Private Key (Kyber):** The secret polynomial vector $s(x)$.
- **Encryption (Kyber):** Involves polynomial matrix/vector multiplications and additions with random elements and the message polynomial.
- **Decryption (Kyber):** Involves a similar computation using the private key and converting the result back to the message.
- **Message Polynomial:** A polynomial representation of the message to be encrypted.

#### Original Practice Problems (Week 11)

1. Find $t(x)$ for MLWE with $f(x) = x^2 + 1, q = 3, A = \begin{pmatrix} x & 1 \ 2 & x+1 \end{pmatrix}, s(x) = \begin{pmatrix} 1 \ x \end{pmatrix}, e(x) = \begin{pmatrix} 1 \ 0 \end{pmatrix}$.
    
    - **Solution:**
        - $As(x) = \begin{pmatrix} x & 1 \ 2 & x+1 \end{pmatrix} \begin{pmatrix} 1 \ x \end{pmatrix} = \begin{pmatrix} x(1) + 1(x) \ 2(1) + (x+1)(x) \end{pmatrix} = \begin{pmatrix} 2x \ 2 + x^2 + x \end{pmatrix} \pmod{x^2+1, 3} = \begin{pmatrix} 2x \ 2 - 1 + x \end{pmatrix} = \begin{pmatrix} 2x \ x+1 \end{pmatrix} \pmod{3}$.
        - $t(x) = As(x) + e(x) = \begin{pmatrix} 2x \ x+1 \end{pmatrix} + \begin{pmatrix} 1 \ 0 \end{pmatrix} = \begin{pmatrix} 2x+1 \ x+1 \end{pmatrix} \pmod{3}$.
2. Consider a Kyber system with $f(x) = x^2 + 1, q = 5, k = 2, n = 2$. Suppose the message is "10" (which becomes a message polynomial $m(x) = 2x$ after upscaling by $2^{n/8 - 1} = 2^{1-1} = 1$, assuming coefficients in ${0, 1}$ and then maybe multiplied by a factor). Let $r(x) = \begin{pmatrix} 1 \ 0 \end{pmatrix}$. (Simplified problem for illustration). Public key $(A, t(x))$, private key $s(x)$. For simplicity, assume $e_1(x) = \begin{pmatrix} 0 \ 0 \end{pmatrix}, e_2(x) = 0$. If $A = \begin{pmatrix} x & 1 \ 1 & x \end{pmatrix}$ and $s(x) = \begin{pmatrix} 1 \ x \end{pmatrix}$, find $t(x)$ and then compute $u(x)$ and $v(x)$ for encryption.
    
    - **Solution:**
        - $t(x) = As(x) = \begin{pmatrix} x & 1 \ 1 & x \end{pmatrix} \begin{pmatrix} 1 \ x \end{pmatrix} = \begin{pmatrix} 2x \ 1 + x^2 \end{pmatrix} = \begin{pmatrix} 2x \ 0 \end{pmatrix} \pmod{x^2+1, 5}$.
        - $u(x) = A^T r(x) + e_1(x) = \begin{pmatrix} x & 1 \ 1 & x \end{pmatrix} \begin{pmatrix} 1 \ 0 \end{pmatrix} + \begin{pmatrix} 0 \ 0 \end{pmatrix} = \begin{pmatrix} x \ 1 \end{pmatrix} \pmod{5}$.
        - $v(x) = t(x)^T r(x) + e_2(x) + m(x) = \begin{pmatrix} 2x & 0 \end{pmatrix} \begin{pmatrix} 1 \ 0 \end{pmatrix} + 0 + 2x = 2x + 2x = 4x \pmod{5}$.
        - Ciphertext $(u(x) = \begin{pmatrix} x \ 1 \end{pmatrix}, v(x) = 4x)$.
3. Using the same parameters as the previous problem, if you receive the ciphertext $(u(x) = \begin{pmatrix} 1 \ 0 \end{pmatrix}, v(x) = 2)$, decrypt it using the private key $s(x) = \begin{pmatrix} 1 \ x \end{pmatrix}$.
    
    - **Solution:**
        - $m^*(x) = v(x) - s(x)^T u(x) = 2 - \begin{pmatrix} 1 & x \end{pmatrix} \begin{pmatrix} 1 \ 0 \end{pmatrix} = 2 - (1 \cdot 1 + x \cdot 0) = 2 - 1 = 1 \pmod{x^2+1, 5}$.
        - The coefficients of $m^*(x) = 1$ are $(1)$. $\lfloor q/2 \rfloor = \lfloor 2.5 \rfloor = 2$. 1 is closer to 0 than 2 (considering modulo 5, distances are 1 and 1, need consistent rounding rule). Assuming closer to 0 means absolute difference is smaller, $|1-0|=1, |1-2|=1$. Let's use the rule from source: closer to 0 than $\lfloor q/2 \rfloor$. If $q=5, \lfloor q/2 \rfloor = 2$. 1 is closer to 0. So the bit is 0.
4. Convert the binary "110" into a message polynomial for Kyber with $f(x) = x^3 + 1, q = 7$. Upscale by $\lfloor q/8 \rfloor = \lfloor 0.875 \rfloor = 0$. Assume no upscaling for simplicity in this problem, and coefficients are the bits themselves.
    
    - **Solution:** $m(x) = 1x^2 + 1x^1 + 0x^0 = x^2 + x$.
5. Convert the modified message polynomial $m^*(x) = 3x^2 + 6x + 1$ into binary for Kyber decryption with $q = 7$. $\lfloor q/2 \rfloor = 3$.
    
    - **Solution:**
        - Coefficient of $x^2$ is 3, which is not closer to 0 than 3 (distance 3 vs 0). Bit 1.
        - Coefficient of $x^1$ is 6, which is closer to 0 than 3 (distance 1 vs 3). Bit 0.
        - Coefficient of $x^0$ is 1, which is closer to 0 than 3 (distance 1 vs 2). Bit 0.
        - Binary: "100".

### Week 12: McEliece Public Key Cryptosystem

#### 1. Error Correcting Codes

- **$[n, k, d]$ Code:** A linear code where $n$ is the codeword length, $k$ is the dimension (number of message bits), and $d$ is the minimum Hamming distance between any two codewords (minimum number of bits that differ).
- **Generator Matrix $G$ ($k \times n$):** Used to encode a $k$-bit message $x$ into an $n$-bit codeword $x_1 = xG$.
- **Minimum Distance $d$:** Determines the error-correcting capability $t = \lfloor (d-1)/2 \rfloor$.

#### 2. McEliece Public Key Cryptosystem (Using Goppa Codes)

- Uses a specific type of error-correcting code: **Goppa codes**, which have efficient decoding algorithms.
- **Parameters:** Integers $m, t$, with $n = 2^m, k = n - mt, d = 2t + 1$. Original parameters: $n=1024, k=512, t=50$.
- **Private Key:** A generator matrix $G$ of a Goppa code, an invertible $k \times k$ scrambling matrix $S$, and an $n \times n$ permutation matrix $P$.
- **Public Key:** The matrix $G' = SGP$ ($k \times n$).
- **Encryption of a $k$-bit plaintext $x$:**
    1. Generate a random error vector $e$ of length $n$ with weight $t$ (i.e., $t$ ones and $n-t$ zeros).
    2. Compute the $n$-bit ciphertext $y = xG' + e = xSGP + e$.
- **Decryption of an $n$-bit ciphertext $y$:**
    1. Compute $y_1 = yP^{-1} = xSGP P^{-1} + eP^{-1} = xSG + e'$ (where $e' = eP^{-1}$ also has weight $t$).
    2. Use the efficient decoding algorithm of the Goppa code (based on $G$) to decode $y_1$ and recover the closest codeword $x_1 = xS G$. This corrects the error $e'$.
    3. Compute $x_0$ such that $x_0 G = x_1 = xS G$. Since $G$ is a generator matrix, $x_0 = xS$.
    4. Compute the plaintext $x = x_0 S^{-1} = xS S^{-1}$.

#### 3. McEliece-like Cryptosystem (Using Hamming Codes)

- Uses a simpler error-correcting code, the **Hamming code** (e.g., `$$`) for illustration.
- The principles of key generation, encryption, and decryption are analogous to the Goppa code version, but using the generator matrix of the Hamming code and its decoding properties (correcting up to $t = \lfloor (3-1)/2 \rfloor = 1$ error).
- **Example:** Encryption of "1101" with error "0000100" and $G'$. Decryption of "0110110" using $P^{-1}$ and $S^{-1}$.

#### 4. Security Basis

- Relies on the difficulty of decoding a general linear code, which is believed to be a hard problem. The structure of the Goppa code allows the legitimate user (who knows $G, S, P$) to perform efficient decoding.

#### 5. Resistance to Quantum Attacks

- Considered secure by NIST and is a candidate for **post-quantum cryptography**. Decoding general linear codes is not known to be efficiently solvable by quantum computers.

#### 6. Time Complexity

- Key Generation: Matrix multiplications.
- Encryption: Matrix-vector multiplication and vector addition (with sparse error vector).
- Decryption: Matrix-vector multiplication, decoding of the error-correcting code (polynomial time for Goppa/Hamming codes), matrix inversion.
- Public key size (the $k \times n$ matrix $G'$) is relatively large.

#### 7. Classical vs. Post-Quantum

- A post-quantum public-key cryptosystem.

#### 8. Exam-style Exercises

- Encrypt and decrypt using a McEliece-like system with a given $G'$, $S^{-1}$, $P^{-1}$, and error vector. Write a permutation as a matrix. Find the inverse permutation and its matrix. Compute $G' = SGP$. Show that decryption works correctly for a certain error weight.
    - **Short Solutions/Outlines:**
        - 12.1 a) $y = xG' + e$.
        - 12.1 c) $y_1 = yP^{-1}$, decode $y_1$ to $x_1$, find $x_0$ such that $x_0 G = x_1$, $x = x_0 S^{-1}$.
        - 12.2 Create a matrix where the $i$-th column has a 1 in the $P7[i]$-th row and 0s elsewhere.
        - 12.3 Apply the inverse permutation and create the matrix similarly.
        - 12.4 Perform matrix multiplications.
        - 12.5 Follow the decryption steps and show that the error $eP^{-1}$ (with weight 1) will be corrected by the Hamming code decoding, leading to the recovery of $x$.

#### Flashcards (Week 12)

- **Error Correcting Code:** A method for encoding data to detect and correct errors.
- **$[n, k, d]$ Code:** Parameters of a linear block code (codeword length, message length, minimum distance).
- **Generator Matrix $G$:** Matrix used for encoding.
- **Minimum Hamming Distance $d$:** Minimum number of differing bits between codewords.
- **Error Correcting Capability $t$:** Maximum number of errors that can be corrected.
- **Goppa Code:** A type of error-correcting code with efficient decoding algorithms, used in McEliece.
- **Hamming Code:** A simpler error-correcting code used for illustration.
- **Scrambling Matrix $S$:** An invertible matrix used in key generation.
- **Permutation Matrix $P$:** A matrix representing a permutation of the bits.
- **McEliece Public Key Cryptosystem:** A post-quantum public-key cryptosystem based on the difficulty of decoding general linear codes.
- **Public Key (McEliece):** The matrix $G' = SGP$.
- **Private Key (McEliece):** $G, S, P$.
- **Encryption (McEliece):** Multiply plaintext by $G'$ and add a random error vector.
- **Decryption (McEliece):** Apply inverse permutation, decode the noisy codeword, and unscramble.

#### Original Practice Problems (Week 12)

1. Consider a `$$` repetition code with generator matrix $G = [1 \ 1 \ 1]$. Encode the message "1". What is the codeword? What is the minimum Hamming distance? How many errors can this code correct?
    
    - **Solution:**
        - Codeword: $1 \cdot [1 \ 1 \ 1] = [1 \ 1 \ 1]$.
        - Messages are "0" (codeword "000") and "1" (codeword "111").
        - Hamming distance between "000" and "111" is 3. Minimum distance $d = 3$.
        - Error correcting capability $t = \lfloor (d-1)/2 \rfloor = \lfloor 2/2 \rfloor = 1$. Can correct 1 error.
2. For a McEliece-like cryptosystem, you have a generator matrix $G = \begin{pmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \end{pmatrix}$, a scrambling matrix $S = \begin{pmatrix} 1 & 1 \ 0 & 1 \end{pmatrix}$, and a permutation $P = {2, 1, 3}$ (so $P^{-1} = {2, 1, 3}$). Compute the public key $G' = SGP$. (All operations in $\mathbb{Z}_2$).
    
    - **Solution:**
        - $SG = \begin{pmatrix} 1 & 1 \ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 1\cdot1 + 1\cdot0 & 1\cdot0 + 1\cdot1 & 1\cdot1 + 1\cdot1 \ 0\cdot1 + 1\cdot0 & 0\cdot0 + 1\cdot1 & 0\cdot1 + 1\cdot1 \end{pmatrix} = \begin{pmatrix} 1 & 1 & 0 \ 0 & 1 & 1 \end{pmatrix}$.
        - Permutation matrix $P$ corresponds to swapping the first two columns. So $G' = SGP$ is $SG$ with the first two columns swapped: $G' = \begin{pmatrix} 1 & 1 & 0 \ 1 & 0 & 1 \end{pmatrix}$.
3. Encrypt the 2-bit message "10" using the public key $G' = \begin{pmatrix} 1 & 1 & 0 \ 1 & 0 & 1 \end{pmatrix}$ (from the previous problem) with the error vector $e = (0, 1, 0)$.
    
    - **Solution:**
        - $x = (1, 0)$.
        - $xG' = (1, 0) \begin{pmatrix} 1 & 1 & 0 \ 1 & 0 & 1 \end{pmatrix} = (1\cdot1 + 0\cdot1, 1\cdot1 + 0\cdot0, 1\cdot0 + 0\cdot1) = (1, 1, 0)$.
        - Ciphertext $y = xG' + e = (1, 1, 0) + (0, 1, 0) = (1, 0, 0)$.
4. Decrypt the ciphertext $y = (1, 0, 0)$ using $P^{-1} = {2, 1, 3}$ and assuming a decoding algorithm that corrects single errors for the code generated by $G = \begin{pmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \end{pmatrix}$, and $S^{-1} = \begin{pmatrix} 1 & 1 \ 0 & 1 \end{pmatrix}$ (inverse of $S$ in $\mathbb{Z}_2$).
    
    - **Solution:**
        - $y_1 = yP^{-1} = (1, 0, 0)$ after permuting to ${2, 1, 3}$ indices becomes $(0, 1, 0)$.
        - We need to find a codeword close to $(0, 1, 0)$ in the code generated by $G$. Codewords are $(0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 0)$. The closest is $(0, 1, 1)$ (distance 1). So $x_1 = (0, 1, 1)$.
        - Find $x_0$ such that $x_0 G = x_1 = (0, 1, 1)$. If $x_0 = (0, 1)$, then $(0, 1) \begin{pmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \end{pmatrix} = (0, 1, 1)$. So $x_0 = (0, 1)$.
        - Plaintext $x = x_0 S^{-1} = (0, 1) \begin{pmatrix} 1 & 1 \ 0 & 1 \end{pmatrix} = (0\cdot1 + 1\cdot0, 0\cdot1 + 1\cdot1) = (0, 1)$.
5. Explain the role of the permutation matrix $P$ in the McEliece cryptosystem.
    
    - **Solution:** The permutation matrix $P$ (and its inverse $P^{-1}$ in decryption) is used to disguise the structure of the original Goppa code (or Hamming code). By permuting the columns of the generator matrix $G$, the public key $G'$ looks like the generator matrix of a general, unstructured linear code, which is hard to decode efficiently without knowing the private key components ($G, S, P$). The legitimate receiver uses $P^{-1}$ to reverse this permutation, allowing them to apply the efficient decoding algorithm of the original Goppa code.