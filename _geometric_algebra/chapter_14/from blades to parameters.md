Once rounds and tangents are available, geometric computation becomes "take products, get blades." The practical problem then flips: given a blade $X$, how do you (1) classify what it is, and (2) extract parameters like direction, location, size, weight, orientation?

The chapter's Table 14.1 is essentially a decoding manual. Here is the distilled logic.

## 1) Classify by incidence with infinity and by nullity

Two tests separate the main species:

1. **Does it contain infinity?**
   Check $\infty\wedge X$.

   * If $\infty\wedge X=0$, the blade lives entirely "at infinity" in the sense of the flat/direction family.
   * If $\infty\wedge X\neq 0$, it's localized (flats, rounds, tangents).

2. **Does it have zero square?**
   Check $X^2$.

   * Tangents (and points-as-tangents) satisfy $X^2=0$.
   * Proper rounds satisfy $X^2\neq 0$ (their size is nonzero, possibly imaginary).
   * Flats/directions don't have a size parameter (size "not applicable").

You also use the contraction $\infty\!\rfloor\!X$ (or the dual variants) to tell apart direct vs dual encodings when the grade pattern alone can't.

## 2) Direction: strip position, force an $\infty$

Every Euclidean object here has a "directional part" that ultimately lives in the ideal subspace and looks like $E\wedge\infty$ (or $E\,\infty$), with $E$ purely Euclidean.

The decoding rules are simple in spirit:

* **If the object already contains $\infty$** (flats/directions), direction is obtained by contracting with $\infty$ (it peels off the positional factor).
* **If the object does not contain $\infty$** (rounds/tangents), direction is obtained by contracting with $\infty$ and then wedging back with $\infty$ to reattach the ideal direction.

Table 14.1 gives the exact grade-correct formulas for each class (flat, dual flat, tangent, dual tangent, round, dual round).

## 3) Weight and orientation live in the direction

Once you have a direction blade $E\wedge\infty$, its Euclidean part $E$ carries:

* **weight**: magnitude of $E$,
* **orientation**: sign relative to your chosen Euclidean pseudoscalar convention.

A robust way to compute weight is: strip off the $\infty$ by contracting with any normalized "probe point" $q$ (often just take $q=o$), then take the Euclidean magnitude:
$$
\text{weight}^2 \sim \left|\,q\!\rfloor\!(E\wedge \infty)\,\right|^2.
$$
This is coordinate-free as long as you're consistent about the Euclidean inner product you use for that magnitude.

## 4) Location: centers for rounds, closest points for flats

* For **rounds**, the natural location is the center. Algebraically, you can "strip off the carrier direction" to get a dual-sphere-like element around the center, or compute the center point directly via the chapter's compact expression:
  $$
  c = -\tfrac12 \,\frac{X\,\infty\,X}{(\infty\!\rfloor\!X)^2}.
  $$
  The chapter notes this will later be recognized as a reflection construction (once conformal operators are treated explicitly).

* For **flats** (lines/planes), there is no unique intrinsic "center." The table therefore gives a *relative* location: the point on the flat closest to a chosen probe point $q$ (often the origin). The formulas return a normalized dual sphere representing that closest point.

## 5) Squared size: normalize and read $\rho^2$ (real or imaginary)

Size is best tracked as **squared size** $\rho^2$ (to allow negative values without complex numbers).

For rounds, after normalizing appropriately and fixing grade-dependent signs, the table provides formulas of the schematic form
$$
\rho^2 = \pm\,\frac{X\,\widehat X}{(\infty\!\rfloor\!X)^2},
$$
where $\widehat X$ denotes the grade involution (a sign flip depending on grade). The sign differs between direct and dual round encodings because the "round factor" in the direct form looks like an imaginary dual sphere.

Tangents always have $\rho^2=0$.
