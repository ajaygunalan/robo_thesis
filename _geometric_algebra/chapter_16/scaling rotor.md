# Scaling Rotor

## Scaling from "parallel spheres" the way translation comes from parallel planes

A translation in CGA can be built from reflections in two parallel planes. The scaling analogue is: take **two concentric spheres** (think "parallel" in the sense of sharing a center) and compose their inversions. For concentric dual spheres

$$
\sigma_1 = o - \frac{1}{2}\rho_1^2 \infty, \qquad \sigma_2 = o - \frac{1}{2}\rho_2^2 \infty,
$$

their product simplifies to a scalar plus an $o \wedge \infty$ term:

$$
\sigma_2 \sigma_1 = (\rho_1^2 + \rho_2^2) - \frac{1}{2}(\rho_1^2 - \rho_2^2) \, o \wedge \infty.
$$

Only the ratio of radii should matter, so you normalize and introduce a parameter $\gamma$ via

$$
e^{\gamma/2} = \frac{\rho_2}{\rho_1}.
$$

Then the scaling versor has the tidy hyperbolic form

$$
S_\gamma = \cosh(\gamma/2) + \sinh(\gamma/2) \, O, \qquad O := o \wedge \infty,
$$

and because $O^2 = 1$ this is also an exponential rotor,

$$
S_\gamma = \exp\left(\frac{\gamma}{2} O\right).
$$

This is the conformal model's uniform scaling operator.

## What it does to the conformal primitives

The generator $O = o \wedge \infty$ has simple commutation properties: it anticommutes with $o$, commutes (up to sign) with $\infty$, and commutes with purely Euclidean blades. That makes the action easy to characterize:

- $\infty$ is preserved up to a weight factor (it scales),
- $o$ scales with the reciprocal weight,
- Euclidean directions/blades are unchanged.

For a conformal point $p(x) = T_x[o]$, the net effect is

$$
S_\gamma[p(x)] = e^{-\gamma} p(e^\gamma x) = e^{-\gamma} T_{e^\gamma x}[o].
$$

So the **Euclidean location** scales by $e^\gamma$, while the **conformal weight** scales by $e^{-\gamma}$. Practically: to scale spatial coordinates by a factor $s > 0$, use $\gamma = \ln s$.

## Why scaling preserves "round vs flat" even though inversion doesn't

Unlike spherical inversion, scaling doesn't swap $o$ and $\infty$; it only **reweights** $\infty$. The classification conditions that depend on whether $\infty \cdot X$ or $\infty \wedge X$ vanish are unaffected by an overall weight on $\infty$, so scaling preserves the type of an element: rounds stay rounds, flats stay flats.

## The distance "paradox" is actually the model doing its job

At first glance, it feels contradictory that Euclidean distance is defined via inner-product ratios (which are invariant under orthogonal transformations), yet scaling changes distances. The resolution is that scaling trades off **spatial scale** against **point weight**, and the distance definition should be read relative to the original $\infty$. With that interpretation, Euclidean distances scale exactly as expected after applying $S_\gamma$.

## Scaling about an arbitrary center

Scaling "about the origin" is not a real restriction: because this is a versor operator, you translate the scaling operator to a new center by conjugation with a translation rotor. The result is a scaling about any point without changing the structure of any construction you apply it to.

## Negative scaling as a non-rotor: reflection in the origin

If one of the two composing spheres is imaginary, the product produces a transformation equivalent to **reflection in the origin** (a negative scaling). A prototypical case is the product of a real and an imaginary unit sphere:

$$
(o - \infty/2)(o + \infty/2) = o \wedge \infty.
$$

Acting on a conformal point, this sends

$$
T_x[o] \mapsto -T_{-x}[o].
$$

This versor is even, but it is **not** a rotor (it fails the unit-rotor normalization condition), so it cannot be expressed as $\exp(\text{bivector})$ and cannot be "done in small amounts." You can combine it with a positive scaling versor to realize an overall negative scaling, but you don't get a logarithm-based interpolation the way you do for positive scaling.
