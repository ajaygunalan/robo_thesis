---
tags: optimization
---

### Slater's Constraint Qualification

A regularity condition in convex optimization requiring the existence of a point where all inequality constraints hold strictly (and equality constraints hold exactly).

There exists a point $x_{slater}$ such that:

- $h_j(x_{slater}) < 0$ for all non-linear inequality constraints
- $Ax_{slater} = b$ for equality constraints

This point typically lies in the relative interior of the feasible set, ensuring the region has actual interior volume rather than being edge-only.

Significance for KKT Conditions: When Slater's condition holds, the Karush-Kuhn-Tucker conditions become both:

- Necessary: Any global minimum must satisfy KKT
- Sufficient: Any KKT point is guaranteed to be the global minimum

Key Implications:

- Guarantees strong duality holds
- Ensures Lagrange multipliers exist
- Provides foundation for duality theory in convex programs