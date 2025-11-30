---
tags: optimization
---

- **Objective**: $\min f(x)$
- **Subject to**:
    - $h_j(x) \leq 0, \quad j = 1,\ldots,l$ (inequality constraints)
    - $e_i(x) = 0, \quad i = 1,\ldots,m$ (equality constraints)
- **Feasible set**: $X = {x : h_j(x) \leq 0, e_i(x) = 0, j = 1,\ldots,l; i = 1,\ldots,m}$

## Active Set

- Active constraints at $x^*$:
    - $\mathcal{I} = {j : h_j(x^*) = 0}$ (active inequality constraints)
    - $\mathcal{E} = {1,\ldots,m}$ (equality constraints, always active)
    - $\mathcal{A}(x^*) = \mathcal{I} \cup \mathcal{E}$

## Regular Point

- A point $x^* \in X$ is a **regular point** if the gradient vectors ${\nabla h_j(x^*) : j \in \mathcal{I}} \cup {\nabla e_i(x^*) : i \in \mathcal{E}}$ are linearly independent. "The combined set of vectors formed by taking the gradients of all the active inequality constraints AND the gradients of all the equality constraints, evaluated at the point $x^*$

## KKT Necessary Conditions

- **Theorem**: If $x^* \in X$ is a local minimum and a regular point, then there exist unique vectors $\lambda^* \in \mathbb{R}^l_+$ and $\mu^* \in \mathbb{R}^m$ such that:
    
    1. $\nabla f(x^*) + \sum_{j=1}^{l} \lambda_j^* \nabla h_j(x^*) + \sum_{i=1}^{m} \mu_i^* \nabla e_i(x^*) = \mathbf{0}$ (stationarity) $\implies$  (You're minimizing on a hillside (objective) bounded by fences (constraints). The optimal point occurs where the downhill pull equals the fence pushback)
        
    2. $\lambda_j^* h_j(x^*) = 0 \quad \forall j = 1,\ldots,l$ (complementary slackness) $\implies$   Either the constraint is active, or its influence is zero
        
    3. $\lambda_j^* \geq 0 \quad \forall j = 1,\ldots,l$ (dual feasibility) $\implies$  This condition ensures that the "force" from an active inequality constraint always pushes you away from the forbidden region, never pulls you towards it.
        

## Related Concepts

- **KKT Point**: $(x^*, \lambda^*, \mu^*)$ satisfying the above conditions
- **Lagrangian function**: $\mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{j=1}^{l} \lambda_j h_j(x) + \sum_{i=1}^{m} \mu_i e_i(x)$
- **Stationarity condition**: $\nabla_x \mathcal{L}(x^*, \lambda^*, \mu^*) = \mathbf{0}$
- **Inactive constraints**: For $j \notin \mathcal{I}$, we have $\lambda_j^* = 0$


If a convex optimization problem satisfies [[slater_s_constraint_qualification]]. Then,  First Order KKT conditions are necessary and sufficient fort global minimum. 




[Lec 24](https://www.youtube.com/watch?v=qALRTlKJheQ&list=PL6EA0722B99332589&index=25)