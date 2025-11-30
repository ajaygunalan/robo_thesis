---
tags: optimization
---

If [[armijo]]-[[wolfe]] are difficult to ensure then do [[backtracking]]

1. Choose $\hat{\alpha} > 0$, $\rho \in (0,1)$, $c_1 \in (0, 1)$, Set $\alpha = \hat{\alpha}$
2. while $f(x^k + \alpha d^k) > f(x^k) +c_1 \alpha g^{kT} d^k$ [[armijo]] condition is not satisfied
	1. $\alpha := \rho \alpha$
3. end while
4. output: $\alpha^k =\alpha$

we start with big $\alpha$ and keep decreasing until we are staisified.

[backtracking_lec_12](https://youtu.be/0UIt48Dt-5c?list=PL6EA0722B99332589&t=2102)


