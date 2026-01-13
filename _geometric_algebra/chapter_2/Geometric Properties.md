---
title: "Geometric Properties"
tags: [subspaces, orientation, weight]
---

A subspace as a mere set forgets what geometry keeps asking for. The chapter names the extra structure and then builds a single algebraic container for it.

## The triad
### Attitude
Which carrier subspace you mean. $a$ and $\mu a$ determine the same line attitude.

### Orientation
The "handed choice" that flips when you swap spanning order. A plane spanned by $(a,b)$ should be opposite to one spanned by $(b,a)$.

### Weight
"How much" of the subspace element you have, relative within the same attitude. Scaling a spanning vector scales weight; collapsing spanning directions kills it.

These three are the reason a plane needs more than "the set of all $\lambda a + \mu b$".

## Reshapeability (no privileged anchor)
A bivector isn't a fixed parallelogram tied to a corner; it's "some amount of oriented area in a plane". You can slide/shear the picture without changing the element, as long as attitude/orientation/weight are preserved.

## Membership and containment become wedge tests
A $k$-blade $A$ directly represents a homogeneous $k$-subspace by:

- $x$ lies in the subspace of $A$ $\Leftrightarrow$ $x \wedge A = 0$.

Containment lifts: $A \subseteq B$ means each spanning vector of $A$ wedges to zero with $B$. Incidence stops being a coordinate exercise and becomes a one-line computation.
