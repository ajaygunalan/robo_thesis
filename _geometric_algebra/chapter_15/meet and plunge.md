# meet and plunge

## Incidence as meet (and why dual form matters)

In the conformal model, "intersection" is still the meet: given blades $A$ and $B$, the meet is the largest subblade contained in both. In practice, meet computations are often easiest in dual form (especially because points, spheres, and planes have convenient *dual* vector representations). The dual meet is expressed as
$$(A \cap B)^* = B^* \wedge A^*,$$
with the warning that the $*$ here is taken relative to the **join** of the elements you're meeting; if you chain meets, the relevant join (and therefore the duality) can change between steps.

A key geometric consequence in CGA is that meets of rounds can be **imaginary**. Three spheres that do not truly intersect can still produce a perfectly valid "meet blade," but it represents an imaginary point pair (the algebra is telling you: "intersection exists in the representational space, not as real Euclidean points").

## Co-incidence as plunge: "what intersects everything perpendicularly?"

The chapter then asks the natural question: if the meet blade can be imaginary, but its dual can be a perfectly real round, what is the *operation* that produces that dual object directly?

Define $X$ to be the *lowest-grade element perpendicular to each of* $A$ and $B$. Perpendicularity is expressed by contraction:
$$X \perp A \iff X \rfloor A = 0.$$
Dualizing flips this into outer-product incidence with the duals:
$$X \rfloor A = 0 \iff X \wedge A^* = 0.$$
Choosing the duality relative to the join of $A$ and $B$ makes $A^*$ and $B^*$ independent (so their outer product is nontrivial), and the minimal-grade solution becomes
$$X = B^* \wedge A^*.$$

This is the **plunge**: an operation that constructs the simplest element that intersects the given arguments **orthogonally**. Unlike the meet, plunge is inherently **metric** (because "perpendicular" depends on the inner product). It extends immediately by associativity: plunging into multiple elements is just wedging their appropriate duals in sequence.

Figures 15.1–15.3 (pages 3–6) are the visual intuition builder: depending on whether spheres intersect, the meet can be real (a real point pair) and the plunge imaginary (an imaginary circle), or vice versa.

## Real vs imaginary: meet/plunge as polars on a common surround

For rounds, meet and plunge are dual to each other relative to their join, and that duality becomes a **polar relationship** on the smallest sphere that contains both results. A useful mental model the chapter states explicitly:

* Treat a real circle as an "equator" on a sphere.
* Its dual is an **imaginary point pair** representing the "poles."
* Conversely, a real point pair dualizes to an **imaginary equator**.

This gives a concrete way to *locate* an imaginary meet: find the real dual (often via plunge), then identify the smallest sphere on which they are polar to each other. The sphere is the geometric stage that hosts both objects, whether one is real and the other imaginary or vice versa.

## Plunge of flats: why $p \wedge E \wedge \infty$ feels like a perpendicular construction

A "flat" in CGA has direct form $p \wedge E \wedge \infty$. The chapter emphasizes you can read this as a plunge-style specification:

* Wedging $p$ and $\infty$ enforces containment of the point and the point at infinity (the hallmark of a flat).
* The Euclidean direction blade $E$ supplies the orthogonality constraints that pick out the correct direction subspace.

A concrete example is the line $p \wedge u \wedge \infty$: it is the line through $p$ in Euclidean direction $u$ (Figure 15.4(a), page 7). Removing the Euclidean direction factor yields the flat point $p \wedge \infty$, interpretable as the element that "connects" the zero-radius sphere at $p$ to infinity.

The chapter pushes this even further: purely Euclidean blades (e.g., $v \wedge u$) can be interpreted directly as "perpendicular-to" constructions (and, operationally, they are also generators for rotors like $\exp(\alpha, v \wedge u)$). Figure 15.5 (page 8) frames this as a family of circular orbits induced by a rotation axis.
