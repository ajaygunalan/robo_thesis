# Rotor Composition

Once rotations are rotors, "compose two rotations" stops being a special procedure. You multiply the operators. The interesting part is how familiar tools—complex numbers and quaternions—drop out as *restricted views* of that same multiplication, plus a geometric picture that makes the product feel inevitable rather than magical.

## Composition is just multiplication

If you apply $R_1$ and then $R_2$,

$$
x \mapsto R_2 \, (R_1 \, x \, \widetilde{R_1}) \, \widetilde{R_2} = (R_2 R_1) \, x \, \widetilde{(R_2 R_1)}.
$$

So the composite rotor is $R = R_2 R_1$. The reverse/inverse identity for unit rotors guarantees the product is still a rotor.

## Planar rotations: the complex-number shadow

In a single Euclidean plane with unit pseudoscalar $I$, pure rotors look like $\cos(\theta/2) - I\sin(\theta/2)$. Multiplying two of them adds angles, and because everything lives in the same commuting subalgebra $\{1, I\}$, planar rotations commute.

A further planar simplification happens because any in-plane vector anticommutes with $I$. That lets you convert the two-sided half-angle sandwich into a one-sided whole-angle multiplication. This is the "rotor → complex unit" effect: in 2-D you can rotate vectors by multiplying by $\cos\theta + I\sin\theta$ on one side, precisely because the plane algebra is closed and simple.

Complex numbers emerge if you *freeze a reference direction* (the "real axis" $e_1$) and represent a vector $a$ as a ratio $A = a/e_1$. That quotient lives in $\{1, I\}$, multiplies commutatively, and is isomorphic to the usual complex field (with $i$ corresponding to $-I$). The price is conceptual: you've collapsed the distinction between "vector" and "operator," because a complex number *is* a rotor-like operator encoded relative to a chosen axis.

## 3-D composition: scalar+bivector, plus a spherical picture

In 3-D, multiplying two rotors typically yields a scalar part and a bivector part (no grade-4 terms exist). If

$$
R_i = c'_i - I_i s'_i \quad\text{with}\quad c'_i = \cos(\phi_i/2), \; s'_i = \sin(\phi_i/2),
$$

then $R_2 R_1$ expands into five geometric terms because $I_2 I_1$ itself has both scalar and bivector parts. The scalar part of the composite satisfies

$$
\cos(\phi_t/2) = \cos(\phi_1/2)\cos(\phi_2/2) + \sin(\phi_1/2)\sin(\phi_2/2)\cos(\angle(I_1, I_2)),
$$

which is exactly the spherical cosine law. That identity is the giveaway for a powerful visualization:

* Treat each rotor as an **oriented half-angle arc on the unit sphere**, lying on the great circle whose plane is the rotation plane.
* Compose rotations by sliding arcs so the endpoint of the first meets the start of the second.
* The composite rotation is the arc that closes the spherical triangle.

This is not metaphor; it's the geometry encoded by the scalar part of rotor multiplication.

## Quaternions: rotors with their context stripped away

Unit quaternions match 3-D rotors because the even subalgebra of $\mathcal{G}(\mathbb{R}^{3,0})$ has basis $\{1, e_{23}, e_{31}, e_{12}\}$, exactly a scalar plus a bivector. Under the standard identification, quaternion "imaginaries" correspond to *coordinate bivectors*, not vectors, and the "axis vector" interpretation is really the dual of a rotation plane.

A clean correspondence is:

* quaternion $q = q_0 + \vec{q}$
* rotor $R = q_0 - \vec{q} \, I_3$,

where $I_3$ is the 3-D pseudoscalar and $\vec{q}$ is treated as a real axis vector whose dual bivector is the rotation plane. Under this embedding, quaternion multiplication becomes ordinary geometric product. The cross product that appears in the classic quaternion product formula is just the dual of a wedge, so it's automatically 3-D-specific—while the rotor product itself generalizes to any dimension.

The practical punchline: quaternions work well for 3-D vector rotation, but rotors are the same idea without the dimension lock-in and with a natural action on every grade.
