# intersection and union of subspaces

In 3D you already know what “intersection” and “span” mean: two planes through the origin usually intersect in a line, but if the planes coincide the intersection should be the plane itself. This chapter is about making that kind of [[incidence (geometry)|incidence]] computation algebraic, without hard-coding a list of special cases. The tools are the **meet** ($\cap$) and **join** ($\cup$): incidence products on blades that represent the subspaces.

The price of that geometric faithfulness is that meet/join cannot behave like the products we used earlier. Unlike the outer product and [[Contraction (⌋)|contraction]], meet/join are **not bilinear**: an arbitrarily small perturbation can push a configuration across a degeneracy (containment, coincidence, rank loss), and the correct output grade can jump. That is why meet/join are restricted to blades (subspaces) rather than extended to arbitrary multivectors.

There is a second “this feels different” warning: the **intersection subspace is well defined, but its weight and orientation are not**. For incidence questions, only the attitude (which subspace) is intrinsic; a scalar can slide between factors without changing the represented geometry. Keep that explicit via [[scalar ambiguity and attitude]].

The algebraic structure rests on outer-product factorization. For blades $A$ and $B$, the meet $M = A \cap B$ is the largest common factor, and the join $J = A \cup B$ is the smallest blade containing both:
$$
A = A' \wedge M, \quad B = M \wedge B', \quad J = A' \wedge M \wedge B'.
$$
Grade bookkeeping: $j = a + b - m$, where lowercase letters denote grades. See [[meet and join]] for the full derivation.

The factorization leaves an unavoidable scalar ambiguity in $M$ and $J$; only the represented subspaces (attitudes) are intrinsic. See [[scalar ambiguity and attitude]].

Once a join $J$ is fixed, the meet becomes a [[Contraction (⌋)|contraction]] computation:
$$
M = (B \rfloor J^{-1}) \rfloor A.
$$
This is linear in $A$ and $B$ as long as the correct join stays fixed. See [[meet from join]] for the join-relative dual form, and [[computing complementary factors]] for extracting $A'$ and $B'$.

The nonlinearity is localized: cross into a degenerate configuration and the correct join abruptly changes. That piecewise-linear structure and the "zero meet = degeneracy alarm" diagnostic live in [[piecewise linearity and degeneracy]], with numerical consequences in [[computational stability]].

When the join is normalized, meet magnitude carries quantitative information—a sine measure of relative attitude between subspaces. See [[angle from meet magnitude]]. Sign conventions under argument swapping follow a grade-dependent parity rule in [[ordering and orientation sign]].

Meet and join are nonmetric incidence constructions that transform cleanly under invertible linear maps (provided you dualize relative to the transformed join). See [[linear transformation invariance]].

All of this assumes subspaces through the origin. Offset objects (parallel planes, circles, spheres) require embedding in homogeneous or conformal models where meet/join apply operationally. See [[offset models]].
