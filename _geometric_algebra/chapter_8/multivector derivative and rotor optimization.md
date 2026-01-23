# Multivector Derivative and Rotor Optimization

Vector differentiation is already richer than classical $\nabla$ because it uses the geometric product. Multivector differentiation goes one step further: it differentiates with respect to a **multivector argument** $X$. That's the right level for optimization over rotors/versors, because the natural variables in GA aren't always vectors.

## Directional multivector derivative: vary only in a grade-matched direction

Given $F(X)$ with multivector argument $X$, define the directional derivative in direction $A$ by

$$
(A \ast \partial_X) F(X) \equiv \lim_{\varepsilon \to 0} \frac{F(X + \varepsilon A) - F(X)}{\varepsilon}.
$$

It is again a scalar operator: the output has the same grade type as $F(X)$.

The scalar product "$\ast$" is doing the grade matching: it isolates the component of the variation aligned with the grades present in $X$.

## Total multivector derivative: assemble all directions

Choose a basis $\{e_I\}$ for the full multivector tangent space (dimension $2^m$ if the underlying vector space is $m$-dimensional), with reciprocal basis $\{e^I\}$. Then

$$
\partial_X \equiv \sum_I e^I \, (e_I \ast \partial_X).
$$

This contains earlier derivatives as special cases:

* If $X$ is a scalar $\tau$, then $\partial_\tau$ reduces to $d/d\tau$.
* If $X$ is a vector $x$, you recover $\partial_x$.

## A couple of "optimization-grade" identities

These are the ones that show up constantly when you differentiate objective functions:

* Squared norm:

$$
\partial_X |X|^2 = 2\tilde{X}
$$

(where $\tilde{X}$ is the reverse).

* Scalar product with a constant multivector $A$:

$$
\partial_X (X \ast A) = P[A]
$$

(with $P[\cdot]$ the projection onto the relevant tangent space when $X$ is constrained).

* Inverse (in scalar product form):

$$
\partial_X (X^{-1} \ast A) = P[-X^{-1} A X^{-1}].
$$

The pattern is consistent with the vector inversion derivative: inversion differentiates into a "sandwich" expression, not a commutative quotient.

## Application: optimal rotor from point correspondences (Wahba/Procrustes)

You observe $k$ vectors $u_i$ that were rotated into $v_i$. With noise, you can't solve exactly; you estimate the rotor $R$ by minimizing squared error:

$$
\Gamma(R) = \sum_{i=1}^k |v_i - R u_i \tilde{R}|^2.
$$

Expanding shows the $R$-dependence sits in a scalar part:

$$
\Gamma(R) = \sum_i (|v_i|^2 + |u_i|^2 - 2\langle v_i R u_i \tilde{R} \rangle_0),
$$

so minimizing $\Gamma$ is equivalent to maximizing

$$
\sum_i \langle v_i R u_i \tilde{R} \rangle_0.
$$

The constraint $R\tilde{R} = 1$ is annoying for direct differentiation. A common GA trick is to temporarily relax to an unconstrained versor $V$ and write $\tilde{R}$ as $V^{-1}$. Differentiate with respect to $V$ using multivector derivative rules; the stationarity condition collapses to a clean geometric statement:

$$
\sum_{i=1}^k (R u_i \tilde{R}) \wedge v_i = 0.
$$

Interpretation: after applying the optimal rotation, the residual "misalignment bivectors" cancel. Only the perpendicular components matter (parallel components are scalings a rotation can't fix).

To compute $R$ explicitly, introduce the linear map

$$
f[x] = \sum_{i=1}^k u_i \, (v_i \cdot x).
$$

The condition above can be rewritten to express that $R f[x] \tilde{R}$ is symmetric, so $f$ differs from a symmetric map only by an orthogonal factor—exactly the **polar decomposition** story.

Numerically, you typically compute that orthogonal factor via SVD on the matrix representation of $f$: if $[[f]] = U S V^T$, the optimal rotation matrix is $V U^T$, and you can convert that back to a rotor.

The big conceptual win of the GA derivation is that it justifies the SVD step as *a way to compute the polar factor*, not as a mysterious metric-dependent hack: the actual optimality condition is the wedge cancellation above, which is Euclidean-geometric from the start.
