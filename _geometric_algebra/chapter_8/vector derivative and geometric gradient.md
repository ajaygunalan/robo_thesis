# Vector Derivative and Geometric Gradient

The vector derivative $\partial_x$ is geometric algebra's coordinate-built, coordinate-free version of the $\nabla$ operator. The point isn't novelty; it's that $\nabla$ becomes a **geometric element** that multiplies via the full geometric product, so divergence/gradient/curl fall out by grade selection rather than by memorized formulas.

## Definition: assemble directional derivatives into one vector operator

Choose a basis $\{e_i\}_{i=1}^m$ for the (local) space in which $x$ lives, with reciprocal basis $\{e^i\}$ (needed if the basis isn't orthonormal). Write coordinates $x^i = e^i \cdot x$. Then define

$$
\partial_x \;\equiv\; \sum_{i=1}^m e^i \, (e_i \ast \partial_x) = \sum_{i=1}^m e^i \, \frac{\partial}{\partial x^i}.
$$

You should read $\partial_x$ as a **vector** operator (grade 1), not as a scalar operator with an arrow on top.

If $x$ lives in an $m$-dimensional manifold inside a larger ambient space, only tangent directions count; results naturally involve the projection $P[\cdot]$ of ambient vectors onto the tangent space.

## Why the geometric product matters

Because $\partial_x$ multiplies by the geometric product,

$$
\partial_x F = (\partial_x \cdot F) + (\partial_x \wedge F).
$$

* If $F$ is **vector-valued**, $\partial_x \cdot F$ is the divergence-like scalar, and $\partial_x \wedge F$ is the curl-like bivector (in 3D its dual is the classical curl vector).
* If $F$ is **scalar-valued**, only $\partial_x \wedge F$ survives, and it is the gradient vector field.

This is the cleanest way to generalize "curl" beyond 3D: the natural object is a bivector, not a pseudo-vector.

## A few anchor identities (the ones worth remembering)

These are not "table trivia"; they encode how $\partial_x$ measures total variation over all directions.

* Identity function:

$$
\partial_x x = m, \qquad \partial_x \cdot x = m, \qquad \partial_x \wedge x = 0.
$$

Interpretation: there are $m$ independent directions of change, each contributing a unit coordinate sensitivity.

* Linear scalar field:

$$
\partial_x (x \cdot a) = P[a].
$$

The gradient is the tangent projection of $a$. Even if $a$ lives in the ambient space, only its tangential component can be realized by varying $x$ within its manifold.

* Norm:

$$
\partial_x |x| = \frac{x}{|x|}.
$$

Exactly the geometric expectation: the norm increases fastest in the radial direction with unit rate.

These are the kinds of results you want to internalize because they let you differentiate coordinate-free by algebraic rewriting plus product/chain rules.

## Product rule: noncommutativity forces you to track "who gets differentiated"

For scalar differentiation, the product rule is straightforward because the operator commutes. For $\partial_x$, the operator is a *vector* in the algebra and does not commute freely.

The chapter uses an "accent" bookkeeping notation to mark which factor the scalar differentiation part hits. In spirit, it's telling you:

* the basis-vector part of $\partial_x$ stays where it is,
* only the scalar partials distribute, and
* you often need to reorder factors to a standard form, which can create cancellations.

This is why blindly copying vector-calculus product rules into GA can go wrong: the algebra remembers the difference between left and right multiplication.

## Chain rule: derivatives transform by the adjoint

If you hide $x$ behind a vector-valued function $y(x)$ and consider $F(y(x))$, the chain rule has a clean geometric meaning: **pull back the derivative by the adjoint of $y$**.

Operationally, the derivative with respect to $x$ can be expressed through a directional differentiation in the $y(x)$-direction and then differentiating the leftover $x$-dependence. The chapter compresses this into a form that reads like "wrap $\partial$ by the adjoint."

That also motivates an explicit derivative-based definition of the adjoint of a (possibly nonlinear) vector function $f$:

$$
\bar{f}[x] \equiv \partial_y \, (f[y] \ast x),
$$

which reproduces the classical adjoint identity $x \ast \bar{f}[y] = f[x] \ast y$ but now as an actual differentiation formula.

The practical message: once you treat $\partial_x$ as a geometric object, coordinate-free differentiation becomes "rewrite into known patterns, then push $\partial$ through using the real product/chain rules of the algebra."
