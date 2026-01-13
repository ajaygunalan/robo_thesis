---
title: "Contraction (⌋)"
tags: [geometric-algebra, inner-product, blades]
---

The scalar product answers "how aligned are two same-grade subspaces?" Contraction exists because geometry also asks: What remains of $B$ once we enforce orthogonality to $A$? That question only makes sense when grades can differ, so the product must reduce grade.

## Intuition
Think "take from $B$ the biggest subspace that lives in $B$ but is most unlike $A$."
In 3-D, if $B$ is a plane (a bivector) and $x$ is a vector, $x \lrcorner B$ is a vector in the plane and perpendicular to $x$ (Figure 3.3 idea).

So the output is still a blade (an oriented subspace), not just a number.

## The implicit definition
If $Y = X \wedge A$ shares a factor $A$ with $B$, we demand that removing $A$ from $Y$ inside a scalar product is equivalent to removing $A$ from $B$:
$$
(X \wedge A) * B = X * (A \lrcorner B)
$$
That pins down $A \lrcorner B$ (fully in nondegenerate metrics), so contraction is a real product, not notation.

The grade must satisfy
$$
\operatorname{grade}(A \lrcorner B) = \operatorname{grade}(B) - \operatorname{grade}(A)
$$
(negative grades collapse to 0).

When grades match, $A \lrcorner B$ is just the scalar product: contraction is the "one inner product to rule them all."

## Computation rules
You can compute everything from a small rule set:
- Scalars: $\alpha \lrcorner B = \alpha B$; but $B \lrcorner \alpha = 0$ if $\operatorname{grade}(B) > 0$
- Vectors: $a \lrcorner b = a \cdot b$
- Leibniz-style rule over wedges:
  $$
  a \lrcorner (B \wedge C) = (a \lrcorner B) \wedge C + (-1)^{\operatorname{grade}(B)} B \wedge (a \lrcorner C)
  $$
- Key associativity-like identity:
  $$
  (A \wedge B) \lrcorner C = A \lrcorner (B \lrcorner C)
  $$

A workhorse expansion for a vector $x$ on a factored blade:
$$
x \lrcorner (a_1 \wedge \dots \wedge a_k) = \sum_{i=1}^k (-1)^{i-1}(x \cdot a_i) \; a_1 \wedge \dots \wedge \widehat{a_i} \wedge \dots \wedge a_k
$$
For a bivector:
$$
x \lrcorner (a_1 \wedge a_2) = (x \cdot a_1)a_2 - (x \cdot a_2)a_1
$$

## Geometric facts
For blades $A, B$:
- $A \lrcorner B$ is contained in $B$.
- $A \lrcorner B$ is perpendicular to $A$.
- If $x \lrcorner A = 0$, then $x$ is perpendicular to every vector in the subspace of $A$.

