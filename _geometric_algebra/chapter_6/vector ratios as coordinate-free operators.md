# Vector ratios as coordinate-free operators

Once division is legal, a "ratio of vectors" stops being metaphor and becomes an element you can compute and apply. The chapter's similarity problem in 2D is: given $a, b$ and a third vector $c$ in their plane, find $x$ such that "$x : c = b : a$". Interpreting the ratio as a geometric-product ratio suggests the equation

$$
x \, c^{-1} = b \, a^{-1},
$$

so the solution is immediate by right-multiplying by $c$:

$$
x = (b \, a^{-1}) \, c.
$$

The interesting object is not $x$ but $b \, a^{-1}$: it behaves like an operator that maps $a \mapsto b$ and then acts linearly on the whole plane.

In 2D Euclidean space, pick coordinates only to *identify* the action: if $a = e_1$ and $b = \rho(\cos\theta \, e_1 + \sin\theta \, e_2)$, then

$$
b \, a^{-1} = \rho(\cos\theta - \sin\theta \, e_{12}),
$$

so the operator has a scalar part and a bivector part. Acting on basis vectors reproduces the standard rotation+scaling formulas, and acting on a general $c$ yields exactly the familiar matrix form—except you never had to introduce the matrix in the first place.

The real value is conceptual: $b/a$ is "rotation+scaling from $a$ to $b$" packaged as a single coordinate-free algebraic element. That's the prototype for the next chapter, where products of vectors become a systematic language for orthogonal transformations rather than a one-off trick.
