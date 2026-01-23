# Dual Flats and Hyperplanes

Direct blades encode flats by span/containment ("a point is on the flat if wedging gives zero"). Dual blades encode flats by orthogonality/constraints ("a point is on the flat if contraction gives zero"). The homogeneous model needs both because different computations become trivial in different forms, and the bridge between them is duality in the representation space.

## Duality in the Representation Space

Let the pseudoscalar of the representation space be
$$I_{n+1} = e_0 \wedge I_n,$$
with $I_n$ the pseudoscalar of the base subspace. The representational dual of a blade $X$ is
$$
X^* = X I_{n+1}^{-1} = X(I_n^{-1} e_0^{-1}),
$$
so duality is literally "divide by the pseudoscalar," just in the $(n+1)$-dimensional algebra. The chapter keeps $e_0^{-1}$ explicit to avoid committing to the sign choice in $e_0^2=\pm 1$.

The practical meaning is the same as for origin-based subspaces: a direct $(k+1)$-blade corresponds to an offset $k$-flat, and its dual is the complementary object that encodes the same flat as a constraint rather than as a span. In computations, this often turns "intersection" problems into wedge products and "membership" checks into contractions.

## The Hyperplane Case: Dual as a Single Vector

The cleanest example is a hyperplane, because its dual in $\mathbb R^{n+1}$ has grade $1$, so it's just a vector. If a hyperplane has unit normal $\mathbf{n}$ in the base space and oriented distance $\delta$ from the origin (positive in the $\mathbf{n}$ direction), then its dual representative is
$$
\pi = -\mathbf{n} + \delta e_0^{-1}.
$$
Figure 11.4 (PDF p. 20) draws this in 2D (a line) and 1D (a point), emphasizing how the $\delta e_0^{-1}$ component is what localizes the otherwise pure direction $\mathbf{n}$.

## Dual Membership Test Recovers the Normal Equation

If $x=e_0+\mathbf{x}$ is a unit point, then the condition "$x$ lies on the dual flat" is expressed by contraction:
$$
x \cdot \pi = 0.
$$
For the hyperplane vector above, this becomes
$$
0 = (e_0+\mathbf{x})\cdot(-\mathbf{n} + \delta e_0^{-1})
= \delta - \mathbf{x}\cdot \mathbf{n},
$$
so the base-space membership condition is the familiar Hesse normal form:
$$
\mathbf{x}\cdot \mathbf{n} = \delta.
$$
This matches the classical homogeneous-coordinate story: hyperplanes behave like covectors acting on point vectors, and "incidence" is a single linear equation.

## Why Duals Matter Beyond Hyperplanes

In higher-grade cases, the dual of a flat is not necessarily a vector, but the same idea persists: dual representation packages "direction-like" information together with "offset" information in a way that is naturally probed by contraction with points, and naturally combined by wedge/meet operations. The chapter tabulates direction/support/moment extraction for dual flats (Table 11.3, PDF p. 21) to emphasize that you can treat dual flats as first-class computational objects, not just a trick for planes.
