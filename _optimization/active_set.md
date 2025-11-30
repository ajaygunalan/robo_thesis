---
tags: optimization
---

## 1. The Main Problem

We want to solve:
$$
\begin{aligned}
\min_{x}\quad & \tfrac12\,x^T\,H\,x \;+\; c^T\,x\\
\text{subject to}\quad 
& a_i^T\,x \;=\; b_i,\quad i\in \mathcal{E} \quad (\text{equality constraints}),\\
& a_i^T\,x \;\le\; b_i,\quad i\in \mathcal{I} \quad (\text{inequality constraints}),
\end{aligned}
$$
where $H$ is symmetric positive definite.

---

## 2. What "Active Set" Means

- **Active constraints** are those that hold with equality at the current point $x$.  
  - All equality constraints are always active.  
  - Inequality constraints are active if $a_i^T x = b_i$.  

- The **working set**, $W^k$, is the set of currently active constraints at iteration $k$.  

---

## 3. Basic Idea of the Active Set Method

1. **Start** with a feasible point $x^0$ and an initial guess of which constraints are active, $W^0$.  
2. **Solve a reduced QP subproblem** that treats active constraints as equalities. This gives a direction $d^k$.  
3. **Check direction** $d^k$:  
   - If $d^k = 0$, we cannot move within the current active set to reduce the objective. Then we check multipliers to see if we should remove any constraint from the active set.  
   - If $d^k \neq 0$, we compute how far we can move along $d^k$ before we violate any non‐active constraint. That distance is $\alpha^k$. We update $x^{k+1} = x^k + \alpha^k d^k$. Any constraint that becomes tight is then added to the working set.  
4. **Repeat** until no further improvement is possible or all multipliers indicate optimality.

---

## 4. The Reduced QP Subproblem

At iteration $k$, define $g^k = H\,x^k + c$. We solve:
$$
\min_{d}\quad \tfrac12\,d^T\,H\,d \;+\; (g^k)^T\,d
\quad\text{subject to}\quad 
a_i^T\,d \;=\; 0 \;\;\forall\,i\in W^k.
$$
- This says: "Find a direction $d$ that remains in the subspace defined by the active constraints, and that reduces the quadratic objective as much as possible."

---

## 5. If $d^k = 0$: Checking Multipliers

- When the best descent direction in the current active subspace is $0$, we look at the Lagrange multipliers $\lambda$ for each active constraint.  
- If **all** multipliers for active inequality constraints are $\lambda_i \ge 0$, it means we are at a (local) minimum that respects the constraints—i.e., we're done.  
- If **any** multiplier for an inequality constraint is negative, that constraint is "too restrictive." We remove it from $W^k$ and resolve.

---

## 6. If $d^k \neq 0$: Moving Along $d^k$

- We find the **maximum step** $\alpha^k$ we can take along $d^k$ without violating any inactive inequality constraints:
  $$
  \alpha^k \;=\;\min\Bigl\{\,1,\;\min_{i\notin W^k:\;a_i^T\,d^k>0}\,\frac{b_i - a_i^T\,x^k}{\,a_i^T\,d^k\,}\Bigr\}.
  $$
  - If no inequality blocks the way, $\alpha^k=1$. Otherwise, we stop just at the next constraint boundary.  
- Update $x^{k+1} = x^k + \alpha^k d^k$.  
- If $\alpha^k < 1$, it means a new constraint has become active at the boundary, so add that constraint to $W^k$.

---

## 7. Iterate Until Convergence

Keep repeating the process:
1. Solve the reduced QP (using the current active set).  
2. Check the resulting direction and update $x^k$.  
3. Add or remove constraints from $W^k$ based on multipliers or newly active constraints.  
4. Stop when you can't improve further and all multipliers are nonnegative.

Because $H$ is positive definite, the subproblems are well‐defined and the method converges to the global minimizer.

---

### Intuitive Summary

Think of the method as "guessing" which inequalities are tight (active) at the optimal solution, solving a simpler QP with those constraints treated as equalities, then adjusting the guess whenever you discover that:
- A constraint assumed active shouldn't be (it has a negative multiplier).
- A constraint you assumed inactive has just become tight and needs to be added.

This guess‐adjust‐solve loop continues until the optimal solution is found.