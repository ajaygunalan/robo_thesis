---
tags: optimization
---

combining [[bfs_davidon_fletcher_powell_]] and [[bgfs_broyden_fletcher_goldfarb_shanno_]] we get Broyden Family:

 $$B^{k+1}(\varphi) = \varphi B_{BFGS}^{k+1} + (1-\varphi)B_{DFP}^{k+1}  \quad \varphi \in [0,1]$$

---

1. Initialize $x^0$ and  $\epsilon$ and symmetric positive definite $B^0$, $\varphi \in [0,1]$,  set $k=0$
2. while [[stopping_condition]]
	1. $d^k = -B^k(\varphi)g^k$
	2. find [[step_length]] $\alpha^k$ along $d^k$  s.t.
		1. $f(x^k + \alpha d^k) < f(x^k)$
		2. $\alpha^k$ satisfies [[armijo]]-[[wolfe]]
	3. $x^{k+1} = x^k + \alpha^kd^k$
	4. $B^{k+1}(\varphi) = \varphi B_{BFGS}^{k+1} + (1-\varphi)B_{DFP}^{k+1}$
	5. $k:=k+1$
3. End While

Output: $x^* = x^k$  is a stationary pt. of $f(x)$

