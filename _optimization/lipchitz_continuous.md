---
tags: optimization
---

How do we control decay of $(g^{k+1} - g^k)^T  \ge (C_2-1)g^{kT}d^k$


**Intuitive Explanation of Lipschitz Continuity**

A function (or its gradient) is Lipschitz continuous if its change is uniformly bounded by a constant times the change in input. In simpler terms, there’s a constant LL (the Lipschitz constant) such that for any two points, the difference in the function’s (or gradient’s) value doesn’t exceed LL times the distance between those points. This property ensures “smooth” behavior, preventing sudden, unpredictable jumps.

**Controlling the Decay in the Inequality**

In the inequality

 $(g^{k+1} - g^k)^T  \ge (C_2-1)g^{kT}d^k$

the left-hand side represents the change in the gradient over successive iterations. Thanks to Lipschitz continuity, we know that

 $\left\| g^{k+1} - g^k \right\|  \le L \left\| x^{k+1} - x^k \right\|$

so the change in the gradient is controlled by how far we move between iterations. When moving in a descent direction $d^k$, this bound ensures that the change in the gradient does not disrupt the progress toward a minimum. The term $(C_2-1)$ quantifies a controlled fraction of the gradient’s contribution along the descent direction, ensuring that the improvement (or decay) in the gradient is proportional to the step taken. This balance is key in iterative optimization methods to maintain convergence and stability.