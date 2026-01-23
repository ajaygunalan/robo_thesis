# Flats as Blades: Lines, Planes, k-Flats

Once points live as vectors in $\mathbb R^{n+1}$, the outer product becomes a universal "flat constructor": wedge together points and you get the blade representing the unique flat that contains them—*including offset information*. This is the structural leap of the chapter.

## Lines are 2-Blades

Given two point representatives $p$ and $q$, the line through them is the bivector
$$L = p\wedge q.$$
The direct containment test is algebraic: a point $x$ lies on the line iff $x\wedge L=0$. Figure 11.2 (PDF p. 10) shows the geometric meaning: in the embedding space, the line in the base space appears as a 2D plane through the origin of $\mathbb R^{n+1}$.

Expanding $p=e_0+\mathbf{p}$ and $q=e_0+\mathbf{q}$ reveals the internal "direction + moment" structure:
$$
p\wedge q
= (e_0+\mathbf{p})\wedge(e_0+\mathbf{q})
= e_0\wedge(\mathbf{q}-\mathbf{p}) + \mathbf{p}\wedge \mathbf{q}.
$$
The first term carries the line's direction (and its orientation/weight via $\mathbf{q}-\mathbf{p}$); the second term is the line's *moment*, encoding how the line is offset from the origin.

The wedge is "reshapeable": if $\mathbf{a}=\mathbf{q}-\mathbf{p}$, then $p\wedge q = p\wedge a$ where $a$ is the improper point/direction representative. This is why a line can be built from "two finite points" or "a point plus a direction" and end up as exactly the same bivector element (Figure 11.2(b), PDF p. 10).

A particularly useful normalization is via the support point: the unique point on the line closest to the origin. Writing the line as a geometric product
$$L = (e_0+\mathbf{d})\,\mathbf{a}$$
with $\mathbf{d}\cdot \mathbf{a}=0$ isolates the support vector $\mathbf{d}$ and makes the line's moment $\mathbf{M}=\mathbf{d}\mathbf{a}$ explicit (Figure 11.2(c), PDF p. 10). From a line blade $L$ you can extract these parameters by structured "selection" operations:
$$
\mathbf{a}=e_0^{-1}L,\qquad
\mathbf{M}=e_0^{-1}(e_0\wedge L),\qquad
\mathbf{d}=\frac{\mathbf{M}}{\mathbf{a}}.
$$
The book stresses that these look algebra-heavy but compile down to coordinate selection (except for the division in $\mathbf{d}$).

### Lines at Infinity

Wedge two improper points (pure base vectors) and you get a bivector that contains no finite points: an "improper line," equivalently a 2D direction element. This is how the algebra accounts for "the line at infinity" objects that make projective incidence statements uniform.

### Don't Add Lines

Even though bivectors form a vector space, adding two line bivectors generally produces something that is *not* a simple 2-blade, hence not a geometrically interpretable line. The chapter explicitly bans it as a universal operation. In 2D base space, special coincidences (all lines meet, possibly at infinity) make sums look line-like via pencils, but that's an accident of low dimension and not a robust programming principle.

## Planes are 3-Blades, and k-Flats Continue the Pattern

A plane through three points is the trivector
$$\Pi = p\wedge q\wedge r,$$
and it can be reshaped as
$$
p\wedge q\wedge r = p\wedge(\mathbf{q}-\mathbf{p})\wedge(\mathbf{r}-\mathbf{p})
= p\wedge A,
$$
with $A$ a pure base-space bivector encoding the plane's direction/orientation/weight. The chapter gives a symmetric support-vector formula in base-space terms:
$$
\mathbf{d}=\frac{p\wedge q\wedge r}{p\wedge q + q\wedge r + r\wedge p},
$$
and notes that the trivector's weight relates to triangle area (for unit points, it is twice the area).

The general statement is: wedging $(k+1)$ points yields a $(k+1)$-blade in $\mathbb R^{n+1}$ that directly represents an offset $k$-flat in the base space:
$$
X = p\wedge p_1\wedge\cdots\wedge p_k
= (e_0+\mathbf{p})\wedge A.
$$
If all points are improper, $X$ lies entirely in the base subspace and represents an "improper flat" (a pure direction element).

For a directly represented flat $X$, the standard parameter triple mirrors the line case:
$$
A = e_0^{-1}X,\qquad
M = e_0^{-1}(e_0\wedge X),\qquad
\mathbf{d}=\frac{M}{A},\qquad
\text{unit support point } d=\frac{X}{A}.
$$
These are the knobs you turn when you want to rewrite a flat for computation: sometimes you want direction, sometimes moment, sometimes the explicit support point.

## Direct Membership and the Base-Space Parametric Form

The direct containment test $x\wedge X=0$ translates into a purely base-space condition. For $X=p\wedge A$ and a unit point $x=e_0+\mathbf{x}$, the chapter shows this is equivalent to
$$
(\mathbf{x}-\mathbf{p})\wedge A=0,
$$
which is the familiar "offset subspace" membership statement: the difference vector from $\mathbf{p}$ to $\mathbf{x}$ lies in the direction subspace $A$. Figure 11.3 (PDF p. 18) depicts this both as "the difference vector lies in the direction blade" and as "the reshaped blades satisfy $x\wedge A = p\wedge A$."

Writing $A=\mathbf{a}_1\wedge\cdots\wedge\mathbf{a}_k$ immediately gives the parametric equation for the flat:
$$
\mathbf{x}-\mathbf{p} = \lambda_1 \mathbf{a}_1 + \cdots + \lambda_k \mathbf{a}_k.
$$
Improper flats have no finite solutions to the containment test—exactly what "at infinity" should mean.
