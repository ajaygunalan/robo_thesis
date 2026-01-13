---
title: "Outer Product (Wedge)"
tags: [outer-product, blades, determinants]
---

You want an element that *is* "the oriented subspace spanned by these vectors". The outer product $\wedge$ is defined almost entirely by that demand.

## The defining behaviors
- Antisymmetry (vectors): $a \wedge b = -b \wedge a$ (so $a \wedge a = 0$).
- Bilinearity: distribute over $+$, pull out scalars.
- Associativity: no parentheses needed in $a \wedge b \wedge c$.

Those rules make $a \wedge b$ an oriented area element (a 2-blade) and $a \wedge b \wedge c$ an oriented volume element (a 3-blade).

## Determinants are the coefficient story
Expand $a \wedge b$ in a basis and the coefficients are $2 \times 2$ determinants; expand $a \wedge b \wedge c$ in $\mathbb{R}^3$ and you get the $3 \times 3$ determinant. The wedge keeps the *geometric unit* (like $e_1 \wedge e_2$) attached instead of collapsing everything to a scalar.

## Zero is an incidence test
- $a \wedge b = 0$ $\Leftrightarrow$ dependence / parallelness.

## Swapping higher grades
For a $k$-blade $A_k$ and $l$-blade $B_l$:
- $A_k \wedge B_l = (-1)^{kl} B_l \wedge A_k$.

Only odd-with-odd swaps negate. That's why scalar wedge multiplication behaves like ordinary multiplication without contradicting antisymmetry.
