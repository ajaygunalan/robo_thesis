---
tags: optimization
---

# Convex Programming Problem (CP)

## Primal Problem

$$\min_{x} f(x) $$
$$\text{s.t.} \quad  h_j(x) \leq 0 j = 1,\ldots,l $$ 
$$e_i(x) = 0, \quad e_i(x) = a_i^T x - b_i, \quad i = 1,\ldots,m$$
$$x \in \mathbb{R}^n$$

where $f$ and $h_j$'s are continuously differentiable convex functions. Assume that Slater's condition holds.

## Lagrangian

$$ \mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{j=1}^{l} \lambda_j h_j(x) + \sum_{i=1}^{m} \mu_i e_i(x) $$

## Dual Problem

$$ \max_{\underset{\mu}{\lambda \geq 0}} \quad \min_{x \in \mathbb{R}^n} \mathcal{L}(x, \lambda, \mu) $$

## Wolfe Dual of CP

$$ \max_{x,\lambda,\mu} \quad  \mathcal{L}(x, \lambda, \mu)$$
$$\text{s.t.} \quad \nabla_x \mathcal{L}(x, \lambda, \mu) = 0$$
$$\lambda \geq 0$$

The dual of Dual-LP is LP!
In case of QP, dual is not useful is $H$ is semi-definite but useful if $H$ is positive definite. 
The dual problem is a convex even if the primal problem is not! for general NLP

[lec 29](https://www.youtube.com/watch?v=-Ow9_rFcGv8&list=PL6EA0722B99332589&index=30)




