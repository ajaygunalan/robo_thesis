# meet and join

Meet/join are incidence products on blades: degeneracies can force the output grade to jump, so any faithful intersection/union operator is nonlinear and does not extend cleanly to arbitrary multivectors.

For blades $A$ and $B$, define their **meet** $M = A \cap B$ as the largest common outer-product factor (a greatest common divisor in the exterior algebra). Equivalently, there exist blades $A'$ and $B'$ such that
$$
A = A' \wedge M,\qquad B = M \wedge B'.
$$
Their **join** $J = A \cup B$ is the smallest blade containing both subspaces (a least common multiple under $\wedge$), and the same factorization gives
$$
J = A' \wedge M \wedge B'.
$$
Disjoint subspaces have $M$ as a scalar (a $0$-blade). Coincident subspaces force $M$ to have the higher grade, which is the source of the grade-switching discontinuity.

Grade bookkeeping follows directly. Writing $a=\mathrm{grade}(A)$, $b=\mathrm{grade}(B)$, $m=\mathrm{grade}(M)$, and $j=\mathrm{grade}(J)$,
$$
\mathrm{grade}(A')=a-m,\qquad \mathrm{grade}(B')=b-m,\qquad j=a+b-m,\qquad m+j=a+b.
$$

The factorization does not canonically fix absolute weight or sign for $M$ and $J$; only the represented subspaces (attitudes) are intrinsic. Keep that ambiguity explicit via [[scalar ambiguity and attitude]], and compute meets efficiently once a join is chosen via [[meet from join]] (with degeneracy handled by [[piecewise linearity and degeneracy]]).
