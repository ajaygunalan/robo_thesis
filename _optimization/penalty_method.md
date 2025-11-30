---
tags: optimization
---

## Problem Formulation

$$ \begin{align} \min & \quad f(\mathbf{x}) \ \text{s.t.} & \quad h_j(\mathbf{x}) \leq 0, \quad j = 1, \ldots, l \ & \quad e_i(\mathbf{x}) = 0, \quad i = 1, \ldots, m \end{align} $$


### Algorithm

1. **Input**:
    
    - Sequence ${c^k}_{k=0}^{\infty}$
    - Tolerance $\epsilon$
2. **Initialization**:
    
    - Set $k := 0$
    - Initialize $\mathbf{x}^k$
3. **Main Loop**:
    
    - **while** $(q(\mathbf{x}^k, c^k) - f(\mathbf{x}^k)) > \epsilon$
        - (a) $\mathbf{x}^{k+1} = \text{argmin}_{\mathbf{x}} , q(\mathbf{x}, c^k)$
        - (b) $k := k + 1$
    - **endwhile**


This algorithm is a penalty method for solving constrained optimization problems. Instead of handling the constraints directly, it incorporates them into a new objective function $q(\mathbf{x}, c^k)$ that adds a penalty for any violation of the constraints. Here's the intuitive breakdown:

- **Penalty Function**: The function $q(\mathbf{x}, c^k)$ is designed so that when the constraints are violated, the function's value increases significantly. The penalty parameter $c^k$ controls how severe this increase is.
    
- **Iterative Minimization**: The algorithm starts with an initial guess $\mathbf{x}^0$ and iteratively minimizes the penalty function $q(\mathbf{x}, c^k)$. Each minimization step gives a new candidate solution $\mathbf{x}^{k+1}$
    
- **Convergence Check**: The algorithm checks the difference $q(\mathbf{x}^k, c^k) - f(\mathbf{x}^k)$. This difference reflects the amount of penalty being applied due to constraint violations. When this difference is below a small tolerance $\epsilon$, it means that the constraints are nearly satisfied, and the solution is close to being feasible for the original problem.
    
- **Parameter Update**: Although the exact update of $c^k$ isn’t detailed, the sequence is chosen to increasingly penalize constraint violations, guiding the solution toward feasibility.
    

In summary, by converting a constrained problem into a sequence of easier unconstrained problems and gradually enforcing the constraints through penalties, this method iteratively approaches a solution that minimizes the original objective while satisfying the constraints

