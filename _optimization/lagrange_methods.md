---
tags: optimization
---

### Problem Formulation

We're trying to minimize a quadratic function $$\frac{1}{2}x^T H x + c^T x,$$ subject to the linear equality constraint $$Ax = b.$$

### Lagrangian Method

Using the Lagrange multiplier method, we "absorb" the constraint into the objective by introducing a multiplier vector $\lambda$. We define the Lagrangian as $$L(x,\lambda)= \frac{1}{2} x^T H x + c^T x + \lambda^T (Ax - b).$$

Then we set the gradients with respect to $x$ and $\lambda$ equal to zero (the KKT conditions):

1. **Stationarity (with respect to $x$)**: $$\nabla_x L(x,\lambda)= Hx + c + A^T\lambda = 0.$$
    
2. **Feasibility (with respect to $\lambda$)**: $$\nabla_\lambda L(x,\lambda)= Ax - b = 0.$$
    

### Solution Process

From the first equation, we solve for $x$: $$x = -H^{-1}(c + A^T\lambda).$$

Next, we substitute this expression for $x$ into the constraint $Ax = b$: $$A\Bigl[-H^{-1}(c + A^T\lambda)\Bigr]= b.$$

This gives us a linear system for $\lambda$: $$-AH^{-1}A^T\lambda - AH^{-1}c = b,$$

or rearranged, $$\lambda = -\bigl(AH^{-1}A^T\bigr)^{-1}\Bigl(AH^{-1}c + b\Bigr).$$

Finally, substitute $\lambda$ back into $$x = -H^{-1}(c + A^T\lambda)$$ to get the solution $x$.

### Summary

In summary, by forming the Lagrangian, taking derivatives with respect to both $x$ and $\lambda$, and solving the resulting system, we obtain the explicit solution for $x$ that minimizes the quadratic function while satisfying $Ax = b$.