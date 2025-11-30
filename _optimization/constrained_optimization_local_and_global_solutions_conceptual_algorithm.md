---
tags: optimization
---

## Constrained Optimization

$$ \begin{align} \min & \quad f(\mathbf{x}) \ \text{s.t.} & \quad h_j(\mathbf{x}) \leq 0, \quad j=1,\ldots,l \ & \quad e_i(\mathbf{x}) = 0, \quad i=1,\ldots,m \ & \quad \mathbf{x} \in S \end{align} $$

- **Inequality constraint functions**: $h_j: \mathbb{R}^n \rightarrow \mathbb{R}$
- **Equality constraint functions**: $e_i: \mathbb{R}^n \rightarrow \mathbb{R}$
- **Assume** all functions ($f$, $h_j$'s and $e_i$'s) are sufficiently smooth
-  Assume $X$ to be nonempty set in $\mathbb{R^n}$
- In concise way, Minimize $f(\mathbf{x})$ subject to $\mathbf{x} \in X$ 

### Feasible Set

$$X = {\mathbf{x} \in S : h_j(\mathbf{x}) \leq 0, e_i(\mathbf{x}) = 0, j=1,\ldots,l, i=1,\ldots,m}$$


## Convex Programming Problem

$$ \begin{align} \min & \quad f(\mathbf{x}) \ \text{s.t.} & \quad h_j(\mathbf{x}) \leq 0, \quad j=1,\ldots,l \ & \quad e_i(\mathbf{x}) = 0, \quad i=1,\ldots,m \ & \quad \mathbf{x} \in S \end{align} $$

### Properties:

- $f(\mathbf{x})$ is a convex function
- $e_i(\mathbf{x})$ is affine ($e_i(\mathbf{x}) = a_i^T\mathbf{x} + b_i$, $i = 1,\ldots,m$)
- $h_j(\mathbf{x})$ is a convex function for $j = 1,\ldots,l$
- $S$ is a convex set

### Key Characteristics:

- Any local minimum is a global minimum
- The set of global minima form a convex set


## How to solve it?
- Reformulation to an unconstrained problem needs to be done with care
- Solve the constrained problem directly.

[Lec20](https://www.youtube.com/watch?v=Cn6nicxxOhY&list=PLEAYkSg4uSQ3Hi2kc4n4bqJvxrtyaQa3P&index=20)
