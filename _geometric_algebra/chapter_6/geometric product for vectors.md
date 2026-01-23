# Geometric product for vectors

The motivating problem is "solve $x$ from partial geometric information." If you only know $x \cdot a = \alpha$, the endpoint of $x$ lives on a hyperplane perpendicular to $a$; infinitely many $x$ fit. If you only know $x \wedge a = B$, the endpoint of $x$ lives on a line parallel to $a$; again infinitely many $x$ fit. The key observation is that these two constraints are complementary: their intersection pins down $x$. That's the geometric demand behind inventing an *invertible* product that contains both pieces at once.

The construction is dictated by symmetry. The inner product is symmetric under swapping arguments; the outer product is antisymmetric. Define a new product (write it as juxtaposition) whose symmetric part *is* the inner product and whose antisymmetric part *is* the outer product:

$$
x \cdot a = \tfrac{1}{2}(xa + ax), \qquad x \wedge a = \tfrac{1}{2}(xa - ax).
$$

Add them and the product is forced:

$$
xa \;\equiv\; x \cdot a \;+\; x \wedge a.
$$

So multiplying two vectors yields a multivector with a scalar part plus a bivector part—mixed grade by design—so nothing "mixes away" the information you'll want to recover later.

Noncommutativity is not a quirk; it's the point. If $xa = ax$ then the antisymmetric part vanishes and the vectors are parallel. If $xa = -ax$ then the symmetric part vanishes and the vectors are orthogonal. In the generic case neither happens, so order matters. Linearity and distributivity come for free because they come for $\cdot$ and $\wedge$, and associativity is adopted because invertibility without associativity is a mess (division wouldn't be well-defined or unique).

On an orthonormal basis $\{e_i\}$, you get the two essential multiplication rules: $e_i^2 = e_i \cdot e_i$ is the metric sign (1 in Euclidean space), and for $i \neq j$, $e_i e_j = e_i \wedge e_j = -e_j e_i$. A payoff appears immediately in 2D Euclidean space: the unit bivector $e_{12} = e_1 e_2$ satisfies $e_{12}^2 = -1$. This isn't importing complex numbers; it's a real oriented plane element that *behaves* like $\sqrt{-1}$ under the geometric product.
