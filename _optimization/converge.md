---
tags: optimization
---

#idk

## Global Convergence Theorem [Zoutendijk]

Consider the problem to $\min f(x)$ over $\mathbb{R^n}$. 

Suppose $f$ is bounded below in $\mathbb{R^n}$, $f \in C^1$ and the $\nabla f(=g$) is [[lipchitz_continuous]].

If at every iteration $k$ of an optimization algorithm, a descent direction $d^k$ is chosen s.t.

1. $\cos^2{\theta_k} >  \delta(>0)$ where $\theta_k$ is the angle between $d^k$  and $g^k$
2. $\alpha^k$ satisfies [[armijo]]-[[wolfe]] conditions.

Then, optimization algorithm either terminates in a finite no. of iteration's or $\lim_{k \to \infty} \left\| g^k\right\| = 0$

