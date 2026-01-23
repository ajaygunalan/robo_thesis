# Spherical Inversion and Reflections

## Inversion as the primitive conformal reflection

In the conformal model, the most elementary non-Euclidean conformal operation is **reflection in a sphere**, usually called **(spherical) inversion**. For the *real* unit sphere centered at the origin, the dual sphere vector is

$$
\sigma = o - \frac{1}{2}\infty,
$$

and the reflection/inversion is implemented by the usual reflection sandwich (vector-versor action)

$$
X' = -\sigma X \sigma^{-1}.
$$

For a unit sphere of weight $1$, $\sigma$ is its own inverse up to normalization, so the mechanics simplify.

A quick way to feel why inversion is "beyond Euclid" is to watch what it does to the conformal basis elements: it effectively trades the roles of the origin point $o$ and the point at infinity $\infty$ (with weights). In particular, $\infty$ does *not* stay fixed, so the operator cannot be Euclidean in the strict sense.

## What happens to a point

Write the standard conformal embedding of a Euclidean location $x \in \mathbb{R}^n$ as

$$
p(x) = T_x[o] = o + x + \frac{1}{2}x^2 \infty.
$$

Under inversion in the unit sphere, the location in Euclidean space becomes the multiplicative inverse directionally:

$$
p(x) \mapsto x^2 p(x^{-1}),
$$

so the point ends up at location $x^{-1}$ but also gets **reweighted** by a factor $x^2$. The weighting is not a nuisance detail—it's how the conformal model keeps inner products invariant while the *Euclidean* distances you read off (relative to the original $\infty$) behave like inversion should.

A subtle variant: using an **imaginary** dual unit sphere produces an inversion that also includes a **central reflection** (a sign flip through the origin) in addition to the distance inversion.

## Why it is conformal: angle preservation without Euclidean rigidity

Inversion can bend lines into circles and still preserve angles. The chapter's clean argument is to look locally: angles live in the relationship between **tangent directions** at a common point. If you take two tangents at the same location $p$ with Euclidean directions $u$ and $v$, inversion transforms those directions by a conjugation that amounts (in Euclidean terms) to a **reflection in the plane with normal $p$**. Reflections preserve the magnitude of relative sines/cosines, so the angle between $u$ and $v$ survives—even though the tangents may now live in a different plane. That local invariance is the operational content of "conformal."

## Reflections that change object class

Because inversion does not preserve $\infty$, it does not preserve the tests that classify conformal objects as flats/rounds via their relationships with $\infty$. Geometrically: swapping the meaning of "infinity" and "center" is exactly why a line can become a circle through the center of inversion (as in the chapter's figures), and why directions can turn into tangents based at the origin. Inversion is structure-preserving in a conformal sense (incidence, containment, angles), not in the stricter Euclidean taxonomy sense.

## Two practical reflection tricks

### Center extraction by reflecting infinity

A sphere's center is latent in its dual representation, and inversion makes it explicit: reflect $\infty$ in the sphere to get the center point (then normalize appropriately). For a sphere with dual vector $\sigma$ and radius $\rho$, the normalized center point can be written as

$$
c = -\frac{1}{2} \rho^2 \sigma \infty \sigma^{-1} = -\frac{1}{2} \frac{\sigma \infty \sigma}{(\infty \cdot \sigma)^2}.
$$

This is translation-covariant (it works anywhere, not just at the origin), and it extends to general rounds because cutting a sphere by planes through its center doesn't move that center.

### Reflection in a circle via a sphere–plane product

You can manufacture "reflection in a circle" by composing reflections in a plane $\pi$ and a sphere $\sigma$ that intersect orthogonally ($\pi \cdot \sigma = 0$). The combined versor $\pi\sigma$ acts by sandwiching:

$$
X' = (\pi\sigma) X (\pi\sigma)^{-1}.
$$

Because $\pi\sigma$ is the dual representation of the meet circle, this gives a meaningful circle reflection that acts not only inside the plane but also off-plane—something that's awkward to define purely in classical planar inversion terms.
