---
tags: optimization
---

## Primal Problem

$$\min_x \quad  f(x)$$
$$\text{s.t.} \quad  h_j(x) \leq 0, \quad j = 1,\ldots,l$$
$$e_i(x) = 0, \quad i = 1,\ldots,m $$
$$x \in X$$

## Dual Problem

$$ \max_{\lambda,\mu} \quad  \theta(\lambda, \mu) $$
$$\text{s.t.} \quad  \lambda \geq 0$$

where $\theta(\lambda, \mu) = \min_{x \in X} \mathcal{L}(x, \lambda, \mu)$

## Optimal Solutions and Duality Gap
Let $x^*$ and $(\lambda^*, \mu^*)$ be optimal solutions to the primal and dual problems respectively. Let $p^*$ and $d^*$ be optimal primal and dual objective function values respectively. $p^* = d^* \Rightarrow$ There is no duality gap.

## Conditions for Zero Duality Gap

Under what conditions is $p^* = d^*$?

Optimal primal and dual objective function values are same ($p^* = d^*$) if and only if $(x^*, \lambda^*, \mu^*)$ is a Lagrangian saddle point, that is, for $x,x^* \in X$ and $\lambda,\lambda^* \geq \mathbf{0}$:

$$\mathcal{L}(x^*, \lambda, \mu) \leq \mathcal{L}(x^*, \lambda^*, \mu^*) \leq \mathcal{L}(x, \lambda^*, \mu^*)$$



# How to find a saddle point if it exists?

## Nonlinear Programming Problem (NLP)

$$ \begin{align} \min \quad & f(x) \ \text{s.t.} \quad & h_j(x) \leq 0, \quad j = 1,\ldots,l \ & e_i(x) = 0, \quad i = 1,\ldots,m \ & x \in X \end{align} $$

## Theorem: KKT Points and Lagrangian Saddle Points

Let $f$ and $h_j$'s be continuously differentiable convex functions, $e_i(x) = a_i^T x - b_i, \forall i$ and $X$ be a convex set. Assume that Slater's condition holds. Then:

$$(x^*, \lambda^*, \mu^*) \text{ is a KKT point} \Rightarrow (x^*, \lambda^*, \mu^*) \text{ is a Lagrangian saddle point.}$$

If $x^*$ is primal feasible, $x^* \in \text{int}(X)$, $\lambda^*$ is dual feasible and $(x^*, \lambda^*, \mu^*)$ is a Lagrangian saddle point, then $(x^*, \lambda^*, \mu^*)$ is a KKT point.

