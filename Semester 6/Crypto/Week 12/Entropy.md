# Entropy of a Discrete Random Variable

## What is Entropy?
The entropy of a discrete random variable `x` is a measure of the amount of information gained by the outcome of an experiment where we find the value of` x`.

The number of bits required for the expected outcome 

## Entropy Definition
Let `x` be a discrete random variable. The entropy of `x` is: 
$$ H(x)=-\sum P(x)\cdot\log_{2}\bigl[P(x)\bigr]$$
## Information
Let $x\in\{0,1\}$ represent a coin flip `(heads=1, tails=0)`. To record the information about this coin flip we need 1-bit.

Now let $x\in\{0,1\}^{n}$ represent the results of n coin flips `(with heads=1, tails=0 for each flip)`. To record the information about all n coin flips we need n-bits (i.e. a bit string of length n).

The **entropy** of x is a measure of the amount of information produced by flipping the coin. Or if the coin has not yet been flipped, it's a measure of the remaining uncertainty.

### Examples
Let $x\in\{00,01,10,11\}$ represent the results of 2 coin flips. Determine the entropy of `x`. Each of these values has $P(x)=\frac{1}{4}$.

$$ \begin{aligned}H(x)&=-\sum P(x)\cdot\log_2\Big[\:P(x)\Big]\\&=-\frac{1}{4}\log_2\Big[-\frac{1}{4}\Big]-\frac{1}{4}\log_2\Big[\frac{1}{4}\Big]-\frac{1}{4}\log_2\Big[\frac{1}{4}\Big]\\&=-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)\\&=\frac{1}{2}+\frac{1}{2}+\frac{1}{2}+\frac{1}{2}\\&=2\end{aligned}$$

--------

A cryptosystem consists of the following plaintext, ciphertext, and key sets:

$\mathrm{x\in M=\{a,b\}}$, the set of all plaintext strings
$y\in\mathbb{C}=\{1,2,3,4\}$, the set of all ciphertext strings
$k\in K=\{k_1,k_2,k_3\}$, the set of all encryption keys

The probability distributions for `x` and `k` are:  $$P(a)=\frac14,P(b)=\frac34\text{ and }P(k_1)=\frac12,P(k_2)=\frac14,P(k_3)=\frac14$$ 
The encryption matrix is: 

|               | a   | b   |
| ------------- | --- | --- |
| k<sub>1</sub> | 1   | 2   |
| k<sub>2</sub> | 2   | 3   |
| k<sub>3</sub> | 3   | 4   |

Determine the **amount of uncertainty in the key**. (Which is **Entropy**!!!!)

The random variable associated with the key is `k` so we find the entropy of `k`:
$$ \begin{aligned}H(k)&=-\sum P(k)\cdot\log_2\Big[P(k)\Big]\\&=-P(k_1)\cdot\log_2\Big[P(k_1)\Big]-P(k_2)\cdot\log_2\Big[P(k_2)\Big]-P(k_3)\cdot\log_2\Big[P(k_3)\Big]\\&=-\frac12\log_2\Big[\frac12\Big]\quad-\frac14\log_2\Big[\frac14\Big]\quad-\frac14\log_2\Big[\frac14\Big]\\&=-\frac12(-1)-\frac14(-2)-\frac14(-2)\\&=\frac12+\frac12+\frac12\\&=1.5\end{aligned}$$

## Exercises
#1-4

