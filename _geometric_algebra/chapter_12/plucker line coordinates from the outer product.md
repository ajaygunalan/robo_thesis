## Lines are bivectors, not "two things stuffed in a struct"

In the 3D homogeneous model, points are represented (up to scale) as vectors of the form $e_0 + p$, with $p \in \mathbb{R}^3$. The line through two points is then the outer product of their homogeneous representatives. If we write the Euclidean position vectors as $p$ and $q$, the line blade expands as
$$
p \wedge q \;=\; e_0 \wedge (q-p) \;+\; p \wedge q.
$$
This is the crucial split: one part "touches" the homogeneous dimension $e_0$, and one part lives purely in the Euclidean subspace.

Geometrically (Figure 12.1, printed p.329), those two bivector pieces encode:

* a **direction** (coming from $q-p$), and
* a **moment** (encoding how the line sits relative to the origin via the plane through the line and the origin).

## Packaging the six coefficients: the Plücker pair

In 3D you can bundle the six bivector coefficients into two 3-vectors using the cross product and Euclidean pseudoscalar $I_3$:
$$
p \wedge q \;=\; (p-q)e_0 \;+\; (p \times q)\,I_3.
$$
Define

* $a = p-q$ (note: this is **minus** the usual direction from $p$ to $q$), and
* $m = p \times q$ (the moment vector; equivalently $m = -p \times a$).

Then a line can be stored as the Plücker coordinate pair $\{a, m\}$ (the chapter writes it as $-\{p-q\;;p\times q\}$ to match the traditional sign convention).

This representation carries one intrinsic dependency (the "Plücker relation") that collapses the raw 6 numbers to the correct 5 degrees of freedom. In this wedge-product construction it shows up as
$$
e_0 \wedge (q-p) \wedge (p \wedge q) = 0,
$$
and in the $a,m$ packaging it corresponds to the familiar orthogonality constraint $a \cdot m = 0$.

## The basis is the meaning

What makes this *not* a "6-number trick" is that those coefficients are attached to a specific bivector basis (the chapter uses the split into $e_i\wedge e_0$ and purely Euclidean bivectors). The tags $e_0$ and $I_3$ in
$$
L = a e_0 + m I_3
$$
aren't decoration; they tell you what algebraic rules apply automatically when you combine lines with points and planes.

## Dual lines are legitimate (and useful)

The chapter also introduces the *dual* representation of a line, still a bivector but with the "direction" and "moment" blocks swapped (up to a metric-dependent sign):
$$
L^* \;=\; L\,I_3^{-1} e_0^{-1} \;=\; a\,I_3 \;+\; m\,e_0^{-1}.
$$
Classical Plücker tables often avoid $L^*$ entirely, but in the geometric algebra view it's just another coordinate face of the same object—and it can make some meet computations collapse to a one-liner.
