# meet from join

In applications you often know the ambient subspace where the incidence problem lives (e.g., “these objects live in 3D”), so you can choose a join pseudoscalar $J$ first. With that choice fixed, the meet becomes a contraction computation:
$$
M = A \cap B = (B \rfloor J^{-1}) \rfloor A.
$$
This is linear in each argument as long as the correct join stays the same; when a degeneracy forces a different join, the computation enters a new linear regime (see [[piecewise linearity and degeneracy]]).

The structure is cleanest in join-relative dual form. For any blade $X$ in the join space, define the join-relative dual as
$$
X^\ast := X \rfloor J^{-1}.
$$
Then the dual of the meet is an outer product of duals:
$$
M \rfloor J^{-1} = (B \rfloor J^{-1}) \wedge (A \rfloor J^{-1}),
$$
often remembered as $(A \cap B)^\ast = B^\ast \wedge A^\ast$ with the explicit warning that the dual is taken with respect to $J$, not with respect to a fixed pseudoscalar of the full ambient algebra unless they coincide.

For how join-relative duality behaves under coordinate changes (and why a Euclidean metric can be used as scaffolding when inverses are needed), see [[linear transformation invariance]].
