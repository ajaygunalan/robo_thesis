---
tags: optimization
---

Lagrange multipliers provide a way to solve constrained optimization problems by transforming them into an unconstrained one. The key insight is that at an optimum (maximum or minimum) subject to a constraint, any small change that remains within the constraint does not lead to a first‐order change in the objective function. Geometrically, this means that the gradient of the objective function f is parallel to the gradient of the constraint function h—that is,

$$\nabla f(x_0) = \lambda \nabla h(x_0)$$

Here, the multiplier $\lambda$ (or the set of multipliers for multiple constraints) measures how sensitive the optimal value of $f$ is to a change in the constraint. In economics, $\lambda$ is often called the **shadow price** because it tells you how much the optimal profit (or utility) would increase if the constraint were relaxed by one unit. In physics, particularly in Lagrangian mechanics, $\lambda$ can be interpreted as the force needed to maintain the constraint.

This interpretation—that $\lambda$ quantifies the rate of change of the optimum value with respect to the constraint—arises from the envelope theorem and shows up in many fields where optimization under constraints is essential.
