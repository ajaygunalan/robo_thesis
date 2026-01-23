# Directional Derivative in Geometric Algebra

If $F(x)$ is multivector-valued but depends on a **vector** argument $x$, you often want "the change in $F$ if I step from $x$ in direction $a$." Geometric algebra treats that as a scalar operator, which means it commutes with multivectors—even though the function itself may use noncommutative products internally.

## Definition: a scalar operator probing a vector argument

The directional derivative in direction $a$ is

$$
(a \ast \partial_x) F(x) \;\equiv\; \lim_{\varepsilon \to 0} \frac{F(x + \varepsilon a) - F(x)}{\varepsilon}.
$$

It is scalar in the operator sense: it doesn't carry a grade and can slide through products (product rule behaves like in ordinary calculus).

The "geometric surprise" is not the operator; it's that $F$ is built from geometric products, so the algebra inside the limit produces results that look unlike real-variable calculus but match the geometry.

## Warm-up: $x^2$ differentiates like you hope

Take $F(x) = x^2 = xx$ (a scalar field). Then

$$
(a \ast \partial_x) x^2 = (a \ast \partial_x)(xx) = ax + xa = 2(a \cdot x).
$$

So variation vanishes when $a \perp x$, and is maximal along $x$. No drama.

## The instructive case: differentiating inversion

Now take the vector inverse $x^{-1} = \dfrac{x}{x^2}$ (in Euclidean signature). Compute

$$
(a \ast \partial_x) x^{-1}.
$$

A first-order expansion gives the compact result:

$$
(a \ast \partial_x) x^{-1} = -x^{-1} a x^{-1}.
$$

If you tried to "pattern match" from real calculus, you'd expect something like $-a/x^2$. The GA answer is stricter because multiplication order matters: you don't just scale $a$; you also **reflect it** relative to the direction $x$ (the sandwiching $x^{-1} a x^{-1}$ is a versor-style action) and then scale by $1/|x|^2$.

Geometric meaning: inversion maps $x$ to the inverse-radius point on the same ray. A small displacement $a$ of the original point does *not* map to a parallel displacement after inversion; it flips the component of $a$ in a way consistent with the conformal geometry of inversion (the picture in the chapter shows exactly this: "reflect then scale").

## Norm powers behave classically because they're scalars

For the scalar function $|x|^k$,

$$
(a \ast \partial_x) |x|^k = k (a \cdot x) |x|^{k-2}.
$$

Here you really do recover the familiar "chain-rule-like" expression, because the function collapses the geometric product down to a scalar norm before differentiation.

## How to use it in practice

Directional differentiation is the right tool when:

* you want a **component** of variation (in direction $a$), and
* you want the result to remain the same grade type as $F$.

It's also the conceptual bridge to total derivatives: the vector derivative $\partial_x$ is essentially "bundle all directions $a$ into one geometric operator," but the directional operator is where the geometry of "move in direction $a$" is clearest.
