---
tags: optimization
---

$$\min f(x)$$
$$x \in \mathbb{R^n} \quad f \in C^1$$

1. Initialize $x^0$ and  $\epsilon$, set $k=0$
2. while [[stopping_condition]]
	1. find descent direction $d^k$ for $f$ at $x^k$
	2. find [[step_length]] $\alpha^k$ along $d^k$  s.t.
		1. $f(x^k + \alpha d^k) < f(x^k)$
		2. $\alpha^k$ satisfies [[armijo]]-[[wolfe]]
	3. $x^{k+1} = x^k + \alpha^kd^k$ 
	4. $k:=k+1$
3. End While

Output: $x^* = x^k$  is a stationary pt. of $f(x)$