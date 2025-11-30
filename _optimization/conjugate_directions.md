---
tags: optimization
---

if $f(x)$ is like  $4x^2_1 +x^2_2 - 2x_1x_2$. Then , we need to transform into **conjugate basis** $d^0, d^1, \dots,d^{n-1}$ which are linearly independent. Consider:

$$ \min f(x) \stackrel{\text{def}}{=} \frac{1}{2}x^THx - c^Tx $$

where $H \in \mathbb{R^{n \times n}}$ is symmetric positive definite matrix and $x^0 \in \mathbb{R^n}$. Then any $x \in \mathbb{R^n}$ :

$$x = x^0 + \sum_{i=0}^{n-1} \alpha^i d^i$$

---

Conjugate Gradient Algorithm (Fletcher–Reeves) for Quadratic function, $\frac{1}{2} x^T H x + c^T x$, where $H$ is symmetric positive definite:
1. Initialize $x^0,  \epsilon,  d^0 = -g^0$, set $k := 0$
2. while} $\left\|g^k\right\| \le \epsilon$
	1. $\alpha^k = - \frac{(g^k)^T d^k}{(d^k)^T H d^k}$ (for [[exact_line_search]])
	2. $x^{k+1} = x^k + \alpha^k d^k$
	3. $g^{k+1} = H x^{k+1} + c$
	4. $\beta^k = \frac{(g^{k+1})^T g^{k+1}}{(g^k)^T g^k}$
	5. $d^{k+1} = -g^{k+1} + \beta^k d^k$
	6. $k:=k+1$
3. endwhile
Output: $x^* = x^k$, global minimum of $f(x)$


Conjugate Gradient Algorithm (Fletcher–Reeves) for Non-quadratic function, $f(x)$:
1. Initialize $x^0,  \epsilon,  d^0 = -g^0$, set $k := 0$
2. while} $\left\|g^k\right\| \le \epsilon$
	1. $\alpha^k = \arg \min_{\alpha>0} f(x^k + \alpha d^k)$ (might not be [[exact_line_search]])
	2. $x^{k+1} = x^k + \alpha^k d^k$
	3. compute $g^{k+1}
	4. if $k<n-1$
		1. $\beta^k = \frac{(g^{k+1})^T g^{k+1}}{(g^k)^T g^k}$
		2. $d^{k+1} = -g^{k+1} + \beta^k d^k$ (may not be descnet)
		3. $k:=k+1$
	5. else (thus, we restart after $n$ iterations)
		1. $x^0 = x^{k+1}$
		2. $d^0 = -g^{k+1}$
		3. $k := 0$
3. endwhile
Output: $x^* = x^k$, global minimum of $f(x)$


Other methods to calculate $\beta^k$ are: (1) Polak-Ribiere $\beta^k = \frac{(g^{k+1})^T (g^{k+1}-g^k)}{(g^k)^T g^k}$ method converges to Fletcher Reeves method in quadratic case. For non-quadratic this is better. (2) Hestenes-Steifel method  $\beta^k = \frac{(g^{k+1})^T (g^{k+1}-g^k)}{(g^{k+1}-g^k)^T d^k}$ is related to version of [[bgfs_broyden_fletcher_goldfarb_shanno_]]. Hence [[bgfs_broyden_fletcher_goldfarb_shanno_]] can be thought of way to generate [[conjugate_directions]].




[video](https://www.youtube.com/watch?v=pjcq2y1cA-4&list=PL6EA0722B99332589&index=20)