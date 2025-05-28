# Conditional Probability
## Bayes' Theorem
$$ P(x\mid y)=\frac{P(x)\cdot P(y\mid x)}{P(y)}$$

## Example
A pair of 6-sided dice is rolled. 
	Let `x` represent if the roll is doubles. 
	Let `y` represent the sum on both dice. 
Then:
`x ∈{0,1} `
	(where 0 corresponds to a non-doubles roll, and 1 corresponds to a doubles roll)
`y ∈{2,3,4,5,6,7,8,9,10,11,12} `
	(the possible sums)

Find the probability of rolling doubles given that the roll was a sum of 4.

First of all, we note that we can easily solve this directly by considering the event space given that a sum of 4 was rolled; 
	it consists of the following three rolls: 
	{(1,3),(2,2),(3,1)}. 
	Only one of these, (2,2), is doubles, so we have that $P(\text{doubles}\mid\text{sum of}4)=P(x=1\mid y=4)=\frac13\:.$

Alternatively, could be solved by using Bayes' Theorem:
$$ \begin{aligned}P(x=1\mid y=4)&=\frac{P(x=1)\cdot P(y=4\mid x=1)}{P(y=4)}\\\\&=\frac{6\cdot\frac{1}{36}\cdot\frac{6}{6}}{\frac{3}{36}}\\\\&=\frac{1}{3}\end{aligned}$$
(The 36 in here is the number of sides raised to the number of dice)

So, the probability of rolling doubles given that the roll was a sum of 4 is about `0.3333`.



## Conditional Probability in Cryptosystems
For a cryptosystem (M,C,K,E,D) where:

$x\in M$, the set of all plaintext strings
$y\in C$, the set of all ciphertext strings
$k\in K$, the set of all encryption keys
$e_k\in E$, the set of all encryption rules for a key k (every rule can be the same encryption function)
$d_k\in D$, the set of all decryption rules for a key k (every rule can be the same decryption function)

Consider the problem of finding the probability that the plaintext was "`info`" given that the ciphertext is "`33921`".

To solve this problem using Bayes' theorem we need to know:
$P(x=\text{info})$, the probability of this particular plaintext being encrypted; for example we would expect that the plaintext string "`info`" would be more probable than say "`zxhq`".

$\mathbb{P}(y=33921 | x=\mathrm{info})$, the probability of the cipher text being `33921` given that the plaintext is "`info`"; this depends on knowing all the possible ways of obtaining a ciphertext of `33921` using the all the keys` k` in `K`, and if some keys are more likely to be used than others.

$P(y=33921)$, the overall probability of the cipher text being `33921`; again this depends on knowing all the possible ways of obtaining a ciphertext of `33921` using the all the keys `k` in `K,` and if some keys are more likely to be used than others.

Anyone who has an encryption matrix for the cryptosystem and the probability distributions for both `x` and `k` can solve this using Bayes' theorem:

$$ P(x=\text{info}\mid y=33921)=\frac{P(x=\text{info})\cdot P(y=33921\mid x=\text{info})}{P(y=33921)}$$

## Example
A cryptosystem consists of the following plaintext, ciphertext, and key sets:

$\mathrm{x\in M=\{a,b\}}$, the set of all plaintext strings
$y\in\mathbb{C}=\{1,2,3,4\}$, the set of all ciphertext strings
$k\in K=\{k_1,k_2,k_3\}$, the set of all encryption keys

The probability distributions for x and k are: $P(a)=\frac{1}{4},P(b)=\frac{3}{4}\mathrm{~and~}P(k_{1})=\frac{1}{2},P(k_{2})=\frac{1}{4},P(k_{3})=\frac{1}{4}$

The encryption matrix is:

|               | _a_ | _b_ |
| ------------- | --- | --- |
| _k<sub>1</sub>_ | 1   | 2   |
| _k<sub>2</sub>_ | 2   | 3   |
| _k<sub>3</sub>_ | 3   | 4   |
plaintext = x
ciphertext = y

Find the probability that the plaintext was "`b`" given that the ciphertext is "`2`".
$$ \begin{aligned}P(x=b)&=\frac34\\\\P(y=2\mid x=b)&=P(k_1)=\frac12\\\\P(y=2)&=P(k_1)\times P(y=2\mid k_1)+P(k_2)\times P(y=2\mid k_2)\\\\&=\frac12\times\frac34+\frac14\times\frac14\\&=\frac38+\frac1{16}\\&=\frac7{16}\end{aligned}$$
$$ P(x=b\mid y=2)=\frac{P(x=b)\cdot P(y=2\mid x=b)}{P(y=2)}=\frac{\frac{3}{4}\cdot\frac{1}{2}}{\frac{7}{16}}=\frac{\frac{3}{8}}{\frac{7}{16}}=\frac{3}{8}\times\frac{16}{7}=\frac{6}{7}$$
So the probability that the plaintext was "`b`" given that the ciphertext is "`2`" is about `0.8571`.