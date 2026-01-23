# scalar ambiguity and attitude

Meet and join return blades representing subspaces, but they do not canonically fix an absolute weight or sign for those blades. The defining factorization
$$
A = A' \wedge M,\qquad B = M \wedge B'
$$
permits a scalar to move freely between the meet and the complementary factors: replacing $M$ by $\gamma M$ forces $A'$ and $B'$ to rescale by $1/\gamma$ to keep $A$ and $B$ unchanged, and it rescales the join $J=A'\wedge M \wedge B'$ by $1/\gamma$ as well.

Geometrically, this reflects that a blade’s *attitude* (the subspace it represents) is intrinsic, while its absolute magnitude and orientation sign are partly conventional for incidence constructions like intersection/union.

Formulas that depend only on the represented subspace should be invariant to this freedom. For example, projection onto the meet subspace uses both $M$ and $M^{-1}$,
$$
(x \rfloor M^{-1}) \rfloor M,
$$
so any scalar factor cancels.

When you *do* want quantitative meaning (angles, distances, consistent signs), you fix conventions by choosing and normalizing the join pseudoscalar. That pins down a consistent scaling for meets computed relative to that join (see [[angle from meet magnitude]] and [[ordering and orientation sign]]).
