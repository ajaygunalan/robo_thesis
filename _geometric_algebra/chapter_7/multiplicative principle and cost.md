# Multiplicative Principle and Cost

The chapter ends with two blunt themes: (1) a philosophy about what counts as "geometric algebra" in practice, and (2) what it costs to run it fast.

## Geometric algebra vs Clifford algebra: a practical distinction

Both Clifford algebra and geometric algebra live in the same multivector space and use the same geometric product. The chapter's proposed distinction is about *what you treat as constructively meaningful*.

In a "multiplicative principle" view, you build geometry by multiplying meaningful things:

* vectors and scalars,
* blades from wedges (subspaces),
* versors from geometric products (operators),
* and then apply operators by sandwiching.

You still use addition all the time computationally—because products are bilinear and you represent objects on a basis—but you avoid pretending that an arbitrary formal sum of basis blades is automatically a geometric object with a clean interpretation. In the literature, the meaningful elements tend to be exactly the "simple" ones: blades (outer-factorizable) and versors (geometric-factorizable).

The one explicit crack in the rule is exponentiation/logarithms: adding bivectors in an exponent is geometrically meaningful because it lives in the Lie algebra of the rotor group, but the *resulting* object is still used multiplicatively as an exponential operator.

## Efficiency: where rotors win, where they don't

The performance story is not "GA is faster" or "GA is slower." It's more precise:

* **Storage and composition:** Rotors/versors are compact for orthogonal maps, and composing them is cheap (a geometric product). In moderate dimensions, this beats matrix composition because matrices carry general linearity they don't need, while rotors exploit the orthogonality constraint directly.

* **Applying a transform to a vector:** A naïve rotor sandwich $R x \widetilde{R}$ can be more expensive than multiplying a vector by an $n \times n$ matrix, especially as dimension grows. That's why practical pipelines often *compose* with rotors but *apply* via a derived matrix (or via specialized formulas).

* **Transforming higher-grade blades:** For a fixed grade $k$, an outermorphism matrix acting on the $\binom{n}{k}$-dimensional coordinate space can be cheaper than a general rotor sandwich, because it targets exactly the subspace of interest.

* **The real optimum:** exploit structure. If your program knows "this thing is a vector" or "this thing is a bivector" (and knows the operator is orthogonal), you can generate specialized code with many cancellations baked in. Rotors are a unifying representation that a code generator can use to derive those specialized formulas.

## Practical bridges: matrices and "classics"

The chapter's programming examples underline how this lands in code:

* **Rotor ↔ matrix conversion:** a geometric but slow method is "apply the rotor to basis vectors and read off the columns." A faster method expands $R e_i \widetilde{R}$ symbolically to get the classic quaternion-style formula. The chapter also notes the unstable case near $180°$ rotations and the need for fallback planes/choices.

* **Rotor from two vectors:** there's a compact "smallest rotor" formula (unstable near antiparallel vectors) that's good enough to build robust conversions with sensible guards.

* **Julia fractals without complex numbers:** by viewing a complex number as a ratio of vectors relative to a fixed axis, the quadratic Julia iteration becomes a pure real-vector iteration $x_{k+1} = x_k e x_k + c$, which generalizes to higher dimensions without inventing new algebra.

The honest bottom line: GA buys you a simpler, more uniform operator story; you keep it fast by specializing the low-level computations instead of implementing the full general product machinery everywhere.
