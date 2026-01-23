## Homogeneous points: the easy part

A Euclidean point at position vector $p\in\mathbb{R}^3$ is represented (up to scale) by the 1D homogeneous subspace spanned by
$$
P = e_0 + p.
$$
On a basis $\{e_1,e_2,e_3,e_0\}$, that's the familiar coordinate tuple $(p_1,p_2,p_3,1)$ (the chapter notes the classical notation $(p:1)$).

## Planes: duals hide in plain sight

Take a Euclidean plane described by the affine equation
$$
x \cdot n = \delta,
$$
with normal $n$ and offset $\delta$.

In the homogeneous model, a probe point is $e_0 + x$, and the plane condition can be written as a homogeneous inner product constraint:
$$
(e_0 + x)\cdot(-n + \delta e_0^{-1}) = 0.
$$
So the **dual** plane is represented (up to scale) by the vector
$$
\Pi^* \equiv \pi = -n + \delta e_0^{-1}.
$$

Here's the pitfall: as a *coordinate list*, $\pi$ looks like a 4-vector—just like a point does. And since the homogeneous metric is chosen so that $e_0^{-1}=\pm e_0$, the coordinate basis for points and dual planes effectively coincides. You cannot reliably tell "point vs dual plane" from the numbers alone.

That's why classical Plücker-style notation uses different brackets: round for points $(p:1)$, square for planes $[n:-\delta]$. It's a human reminder that the basis/grade semantics differ.

## Direct plane blades live in a different grade (and basis)

If $\pi$ is the dual of a plane blade, the direct plane blade is obtained by undualizing relative to the homogeneous pseudoscalar $e_0 I_3$:
$$
\Pi = \pi\,(e_0 I_3) = (-n + \delta e_0^{-1})(e_0 I_3) = -n\,e_0 I_3 + \delta I_3.
$$
So, in direct form, a plane is a trivector with coefficients attached to a trivector basis (the chapter spells out one such basis explicitly). This is why planes don't "belong" in the same coordinate slots as points, despite what a naïve 4-number encoding suggests.

## The honest fix: keep algebraic tags, not just numbers

The chapter's blunt message is that coefficient-only representations are brittle: you end up inventing side-channel bookkeeping (brackets, row/column conventions, separate structs) just to prevent category errors.

Geometric algebra already has that bookkeeping: the *grade* and the *basis blade tags* are part of the data, and they determine the multiplication rules mechanically. If you drop that structure and keep only the six (or four) numbers, you're choosing confusion.
