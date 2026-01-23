Tangents show up in the conformal model as the "zero-size" limit of rounds, but they are not degeneracies—they are new blades with their own clean algebraic signature.

## Tangents from touching rounds

Consider the intersection of two spheres as you shrink their radii while keeping their centers separated. For most radii you get a (real or imaginary) circle of intersection. Exactly at the "just touching" radius, the intersection collapses into what you'd intuitively call a tangent element: "a point with an attached direction."

In 3D, the chapter's symmetric example produces, at tangency, a 2-blade of the form
$$
o \wedge (2e_1),
$$
which is *not* a point and *not* a flat circle—it's a **tangent blade**.

## Standard tangent form and its geometry

Setting the radius of a direct round to zero in the standard form yields
$$
\text{direct tangent at origin:}\quad o \wedge A_k.
$$

What it encodes:

* **location**: the point $o$ (or another point after translation),
* **direction**: the Euclidean blade $A_k$ (a direction element, but localized).

What it does *not* encode:

* it does not contain $\infty$, so it is not a flat element.

If you *want* the associated flat direction passing through infinity, you can force it by wedging with $\infty$:
$$
(o\wedge A_k)\wedge \infty,
$$
which makes the directional content explicit.

## Algebraic signature: "null but not ideal"

A tangent blade $X$ is characterized by two facts:

* it has **zero square**: $X^2=0$ (zero "size"),
* it is **not** an ideal element: $\infty\wedge X\neq 0$ (it's localized, not "at infinity").

Dual tangents satisfy the dual conditions (same conceptual role, different representation), and—crucially—direct and dual tangents transform the same way under even versors. So you only need to track "direct vs dual" for interpretation, not for correct motion.

## Tangents as a tangent bundle, and the size/weight split

The chapter makes a point that's easy to miss: a tangent element can have **finite weight** (like a vector with "length" drawn in your visualization) while having **zero size** (because its square vanishes). This is the first place where the conformal model cleanly separates "geometric size" from "density/weight."

Seen this way, tangents embed a copy of the Euclidean vector space at every point—exactly the mathematical "tangent bundle," but now as ordinary computable blades.

As an edge case, a point can be viewed as a tangent with scalar directional content: a "localized scalar" of the form $p\wedge \alpha$ (weight $\alpha$).
