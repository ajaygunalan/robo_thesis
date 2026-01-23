# Scaled Rigid Body Motions and Interpolation

## TRS is the natural "scaled motion" normal form

Once scaling exists as a conformal rotor, the familiar rigid motion (translation + rotation) generalizes naturally to **translation–rotation–scaling**. A key point is not just that you can compose these, but that you can **systematically reorder** them into a standard form $TRS$ by swapping adjacent factors while adjusting parameters:

- Translation and rotation swap with a rotated translation vector.
- Rotation and scaling (about the origin) commute.
- Translation and scaling do *not* commute; swapping them rescales the translation parameter (geometrically, scaling changes the "unit of length" used by the translation).

The practical payoff is that any product of these operators can be normalized back to $TRS$, so you have a stable representation for "scaled rigid body motions."

Repeated application of such a $TRS$ versor generates a **logarithmic spiral** in space; the chapter's "seashell" example is exactly this idea applied to circles/spheres, relying on the conformal model's ability to transform blades structurally under versors.

## Why interpolation needs a logarithm

To apply a motion "in $N$ small steps," you want

$$
V^{1/N} = \exp\left(\frac{\log V}{N}\right),
$$

so the core requirement is a usable $\log$ for the motion versor $V$. For rigid body motions (no scaling), this was already known earlier; here the new ingredient is the interaction between scaling and translation, which changes what the "infinitesimal" generator looks like.

## The new closed-form piece: $\log(TS)$ is not "$\log T + \log S$"

Rotation and scaling commute, so $\log(RS)$ is straightforward. The novel combination is translation with scaling. For a translation by $t$ followed by a scaling with parameter $\gamma$, the chapter gives

$$
\log(T_t S_\gamma) = \log\left(T_{t \frac{\gamma}{e^\gamma - 1}}\right) + \log(S_\gamma),
$$

with the understanding that as $\gamma \to 0$ the coefficient $\frac{\gamma}{e^\gamma - 1}$ tends to $1$. The conceptual punchline is:

> When scaling is present, the translation component in the logarithm is not the raw $t$; it is "tempered" by a scale-dependent factor.

That is exactly the kind of correction you need if you want $N$ small steps to compose back into the original finite transform.

## The TRS logarithm recipe

For a general positively scaled rigid body motion rotor $V$ in $TRS$ form, the chapter's method is constructive:

1. Extract the combined rotation+scaling contribution from $V\infty$ (the way $V$ maps $\infty$ encodes the non-translational part cleanly).
2. Enforce rotor normalization to split that into separate rotation and scaling parameters.
3. Divide them out of $V$ to isolate the translation.
4. Handle special cases (no rotation; or $R = -1$ where a unique logarithm is not available).
5. Assemble the final bivector generator, and (for numerical hygiene) take the grade-2 part.

The pseudocode in the chapter makes this explicit, including the "gamma-prime" correction factor and the exception handling around degenerate rotation cases.

## What you can and cannot interpolate

With $\log(V)$ in hand, interpolation becomes the standard rotor interpolation pattern. For example, interpolating from a source versor $V_s$ to a destination $V_d$ is naturally expressed as

$$
V(\alpha) = V_s \exp\big(\alpha \log(V_s^{-1} V_d)\big), \qquad \alpha \in [0,1].
$$

This works cleanly for **positive** scaling.

If negative scaling enters (via origin reflection), the versor is no longer a rotor and has no logarithm in this framework—so interpolation "by taking fractional powers" is simply not available, which matches the geometric fact that you can't continuously deform a transform through the identity if it contains a discrete central reflection.
