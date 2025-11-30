---
tags: optimization
---

[[extreme_points]]



## Standard Form

$$\min \quad  c^T x$$
$$\text{s.t.} \quad  a_i^T x (\leq, =, \geq) b_i, \quad i = 1,\ldots,m \  $$
$$x \geq 0$$

## Feasible Region

$$X = \{x : a_i^T x (\leq, =, \geq) b_i, \quad i = 1,\ldots,m, : x \geq 0\}$$

![[unbounded_feasible_region.png]]

## Key Properties

- X is a closed convex set
- The set of optimal solutions is a convex set
- The linear program may have:
    - no solution, or
    - a unique solution, or
    - infinitely many solutions
- If $x^*$ is an optimal solution to LP, then $x^*$ must be a boundary point of X. If $z = c^T x^*$, then ${x : c^T x = z}$ is a supporting hyperplane to X
- If X is compact and if there is an optimal solution to LP, then at least **one [[extreme_points]] of X is an optimal solution to the linear programming problem**
- You can convert any LP into the std. LP form 


[lec_31](https://youtu.be/SU8Hk79d4VI?list=PL6EA0722B99332589&t=788)