# piecewise linearity and degeneracy

The join $J = A \cup B$ is part of the incidence data: it specifies the smallest subspace in which the problem lives. Once you fix a join, meet is an ordinary contraction expression
$$
A \cap B = (B \rfloor J^{-1}) \rfloor A,
$$
so within a region of configurations where the correct join stays the same, the meet varies linearly with $A$ and $B$.

The nonlinearity is concentrated in *when the join must change*. As subspaces become coincident, slip into containment, or lose rank (near-parallel directions), the smallest containing subspace changes discontinuously. The computation then switches to a different join and therefore a different linear regime.

A practical diagnostic falls straight out of this: if you compute a meet relative to a chosen join and it collapses to zero, treat that as an alarm that your assumed join is too large for the current configuration, and pick a smaller join that matches the geometry.

Concrete 3D example (line vs. plane through the origin). Let $a$ be a line (a vector) and $B$ a plane (a bivector). In general position you take $J=I_3$ and obtain a scalar meet
$$
a \cap B = (B \rfloor I_3^{-1}) \rfloor a = B^\ast \cdot a,
$$
which changes sign as the line pierces the oriented plane from opposite sides. As the line rotates into the plane, this scalar meet degrades to $0$; at coincidence the correct join becomes the plane pseudoscalar, and the meet becomes the line itself (up to a weight inherited from $B$).

Near these transitions, implementations must decide an output grade, so tiny perturbations can flip the computation between regimes; practical consequences and workarounds live in [[computational stability]].
