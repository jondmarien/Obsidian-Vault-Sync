# Conditional Entropy

## What is It?
Let `x` and `y`be discrete random variables. 
Then the conditional entropy, $\mathrm{H(x\mid y)}$, is the weighted average of the entropies of x given a possible value of `y`, over all the different possible values of `y`.

The weights of each entropy of `x` are with respect to the probability of the possible value of `y`, $\mathbb{P}(\mathbf{y})$.

If $\mathrm{x\in X}$ and $\mathrm{y\in Y}$ then H(x | y) may be computed directly using:
$$ H(x\mid y)=\sum_{y\in Y}P(y)\cdot\left[-\sum_{x\in X}P(x\mid y)\cdot\log_2\Big[P(x\mid y)\Big]\right]$$

## Example
Let $x\in\{000,010,100,110,001,011,101,111\}$ represent the result of flipping a coin three times.
Let $y\in\{0,1\}$ represent the result of the last flip.

Find $\mathcal{H}(\mathrm{x}\mid\mathrm{y})$, the conditional entropy of `x` given that the result of the last flip is known.

There are two possible values of `y `to consider: `y = 0` and `y = 1`.
When `y = 0` , then `x` can only be `{000,010,100,110}` with  $P(x)=\frac{1}{4}$ for each of these. 

Then:
$$ \begin{aligned}H(x\mid y=0)&=-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]\\&=-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)\\&=2\end{aligned}$$


When `y = 1` , then `x` can only be `{001,011,101,111}` with  $P(x)=\frac{1}{4}$ for each of these. 
Then:
$$ \begin{aligned}H(x\mid y=1)&=-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]-\frac{1}{4}\log_2\biggl[\frac{1}{4}\biggr]\\&=-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)-\frac{1}{4}(-2)\\&=2\end{aligned}$$The conditional entropy of `x` given that the result of the last flip is known is:
$$ \begin{aligned}H(x\mid y)&=\sum_{y\in Y}P(y)\cdot\left[-\sum_{x\in X}P(x\mid y)\cdot\log_2\left[P(x\mid y)\right]\right]\\&=P(y=0)\cdot\left[-\sum_{x\in X}P(x\mid y=0)\cdot\log_2\left[P(x\mid y=0)\right]\right]+P(y=1)\cdot\left[-\sum_{x\in X}P(x\mid y=1)\cdot\log_2\left[P(x\mid y=1)\right]\right]\\&=P(y=0)\cdot\left[H(x\mid y=0)\right]+P(y)=1\cdot\left[H(x\mid y=1)\right]\\&=\frac12\left[H(x\mid y=0)\right]+\frac12\cdot\left[H(x\mid y=1)\right]\\&=\frac12\cdot\left[2\right]+\frac12\cdot\left[2\right]\\&=2\end{aligned}$$


# Key Equivocation
## What is It?
Consider a cryptosystem with 
`plaintexts`: $\mathrm{x\in M}$ , 
`ciphertexts`: $\mathrm{y\in C}$ , and 
`keys`: $\mathrm{k\in K}$  .

The amount of remaining uncertainty in the key **given that** the ciphertext is known, $H(k\mid y)$, is called the **key equivocation**. It may be computed directly using:
$$ H(k\mid y)=\sum_{y\in C}P(y)\cdot\left[-\sum_{k\in K}P(k\mid y)\cdot\log_2\Bigl[P(k\mid y)\Bigr]\Biggr]\right. $$
The **key equivocation** may also be computed indirectly by the following theorem:
$$ H(k\mid y)=H(k)+H(x)-H(y)$$ 
## Example
A cryptosystem with 
`plaintexts`: $x\in M=\left\{a,b\right\}$, 
`ciphertexts`: $y\in\mathbb{C}=\{1,2,3,4\}$, and
`keys`: $k\in K=\{k_{1},k_{2},k_{3}\}$ has encryption matrix:

|               | a   | b   |
| ------------- | --- | --- |
| k<sub>1</sub> | 1   | 2   |
| k<sub>2</sub> | 2   | 3   |
| k<sub>3</sub> | 3   | 4   |
And **probability distributions**: $P(a)=\frac{1}{4},P(b)=\frac{3}{4}\quad\text{and}\quad P(k_{1})=\frac{1}{2},P(k_{2})=\frac{1}{4},P(k_{3})=\frac{1}{4}$

If the `ciphertext` is `y=2` then:
$$ \begin{aligned}P(k=k_1\mid y=2)&=\frac{P(k=k_1)\cdot P(y=2\mid k=k_1)}{P(y=2)}=\frac{\frac12\cdot\frac34}{\frac7{16}}=\frac67\\\\P(k=k_2\mid y=2)&=\frac{P(k=k_2)\cdot P(y=2\mid k=k_2)}{P(y=2)}=\frac{\frac14\cdot\frac34}{\frac7{16}}=\frac17\\\\\\P(k=k_3\mid y=2)&=\frac{P(k=k_3)\cdot P(y=2\mid k=k_3)}{P(y=2)}=\frac{\frac14\cdot0}{\frac7{16}}=0\end{aligned}$$
Then the **amount of remaining uncertainty** in the key given that the ciphertext is `y = 2 `is:
$$ \begin{aligned}-\sum_{k\in\mathcal{K}}P(k\mid y=2)\cdot\log_2\Big[\:P(k\mid y=2)\Big]&=-\frac{6}{7}\log_2\Big[\frac{6}{7}\Big]-\frac{1}{7}\log_2\Big[\frac{1}{7}\Big]-0\\&=-\frac{6}{7}(-0.22239…)-\frac{1}{7}(-2.80735…)-0\\&\cong0.59167…\end{aligned}$$
To obtain the **key equivocation** we would compute the amount of remaining uncertainty in the key for other three cases where the ciphertext is `y = 1` or `y = 3 `or `y = 4` , and then sum all the cases according their probabilities:
$$ \begin{aligned}H(k\mid y)&=\sum_{\mathrm{y\in C}}P(y)\cdot\left[-\sum_{k\in K}P(k\mid y)\cdot\log_2\!\left[P(k\mid y)\right]\right]\\&=P(y=1)\times H(k\mid y=1)+P(y=2)\times H(k\mid y=2)+P(y=3)\times H(k\mid y=3)+P(y=4)\times H(k\mid y=4)\\&=P(y=1)\times H(k\mid y=1)+\quad\frac{7}{16}\times(0.59167…)uad+P(y=3)\times H(k\mid y=3)+P(y=4)\times H(k\mid y=4)\end{aligned}$$

# Perfect Secrecy and Conditional Entropy

Recall that a cryptosystem has **perfect secrecy** if $\mathsf{P}(\mathbf{x}\mid\mathbf{y})=\mathsf{P}(\mathbf{x})$ for all $\mathrm{x\in M}$ and $\mathrm{y\in C}$ .

Another way to determine perfect secrecy is to measure the uncertainty in the plaintext, $\mathcal{H}(\mathrm{x})$, and
compare this to the remaining uncertainty in the plaintext given that the ciphertext is known, $\mathbb{H}(\mathrm{x}|\mathrm{y})$.

If they are equal, then knowing the ciphertext does not change the amount of information that we know
about the plaintext.

Therefore, a cryptosystem has perfect secrecy if $\mathrm{H(x\mid y)=H(x)}$.

$\mathcal{H}(x|y)$ may be computed directly using the general formula for  conditional entropy with $\mathrm{x\in M}$ and $\mathrm{y\in C}$:

$$ H(x\mid y)=\sum_{y\in\mathcal{C}}P(y)\cdot\left[-\sum_{x\in\mathcal{M}}P(x\mid y)\cdot\log_{2}\Big[P(x\mid y)\Big]\right]$$