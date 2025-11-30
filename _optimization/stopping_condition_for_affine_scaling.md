---
tags: optimization
---

## Primal Problem (P)

min     $c^T x$
s.t.    $Ax = b$
        $x \geq 0$

## Dual Problem (D)

max     $b^T \mu$
s.t.    $A^T \mu \leq c$

For any primal and dual feasible $x$ and $\mu$,

$c^T x \geq b^T \mu$    (Weak Duality)

At optimality,

$c^T x - b^T \mu = 0$    (Strong Duality)

**Idea**: Use the duality gap, $c^T x - b^T \mu$, to check optimality

[[how_you_get_μ]] 