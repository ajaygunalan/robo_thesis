---
tags: optimization
---

$$ \begin{align} \min & \quad f(\mathbf{x}) \ \text{s.t.} & \quad \mathbf{x} \in X \end{align} $$


$x^* \in X$ is a local minimum $\Rightarrow \tilde{F}(x^*) \cap \tilde{D}(x^*) = \phi$


1.  $\tilde{D}(x)$ contains directions along which the objective function decreases:
	-  $\tilde{D}(x) = {d : \nabla f(x)^T d < 0} \subseteq D(x)$ (obtuse angle)
2. $\tilde{F}(x)$ contains directions that maintain feasibility with respect to active constraints
	- $x \in X$: $\tilde{F}(x) \triangleq {d : \nabla h_j(x)^T d < 0 ; j \in \mathcal{A}(x)} \subseteq F(x)$ (inner product or dot product)
3. Active Constraints that are satisfied with equality at point $x^*$
	- $\mathcal{A}(x) = {j : h_j(x) = 0}$


**Why not use $D(x)$ and $F(x)$?** 
Cuz $\tilde{D}(x)$ and $\tilde{F}(x)$ They can expressed as gradient of $f(x)$ and  $\mathcal{A}(x)$ that can be used to derive algebraic condition.

- This is only a necessary condition for a local minimum
- Utility of this condition depends on the constraint representation
- Cannot be directly used for equality constrained problems

### Feasible Direction

> A vector $\mathbf{d} \in \mathbb{R}^n, \mathbf{d} \neq \mathbf{0}$ is said to be a **feasible direction** at $\mathbf{x} \in X$ if there exists $\delta_1 > 0$ such that $\mathbf{x} + \alpha\mathbf{d} \in X$ for all $\alpha \in (0, \delta_1)$.

- Let $\mathcal{F}(\mathbf{x}) =$ Set of feasible directions at $\mathbf{x} \in X$ (w.r.t. $X$) [[constrained_optimization_local_and_global_solutions_conceptual_algorithm#Feasible Set]]

### Descent Direction

> A vector $\mathbf{d} \in \mathbb{R}^n, \mathbf{d} \neq \mathbf{0}$ is said to be a **descent direction** at $\mathbf{x} \in X$ if there exists $\delta_2 > 0$ such that $f(\mathbf{x} + \alpha\mathbf{d}) < f(\mathbf{x})$ for all $\alpha \in (0, \delta_2)$.

- Let $\mathcal{D}(\mathbf{x}) =$ Set of descent directions at $\mathbf{x} \in X$ (w.r.t. $f$)










[Lec 21](https://www.youtube.com/watch?v=niohGO560Zw&list=PLEAYkSg4uSQ3Hi2kc4n4bqJvxrtyaQa3P&t=2731s)