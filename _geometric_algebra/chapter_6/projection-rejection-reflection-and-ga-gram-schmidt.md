# Projection, rejection, reflection, and GA Gram–Schmidt

Geometric division turns a tautology into geometry. Write $x = x(AA^{-1})$ and regroup:

$$
x = (xA)A^{-1}.
$$

Now split $xA$ into contraction + wedge (for vector $x$ against blade $A$):

$$
x = (x \rfloor A)A^{-1} + (x \wedge A)A^{-1}.
$$

The first term is the component "living in $A$" (projection), the second is the component orthogonal to $A$ (rejection). For a vector $a$, this becomes the clean decomposition

$$
x = \frac{x \cdot a}{a} + \frac{x \wedge a}{a},
$$

where the denominators are right-divisions by $a$. This is exactly why the product had to be invertible: projection/rejection become literal solvable equations, not definitions by coordinates.

Noncommutativity then gives you "the other division," and it is not cosmetic. Right-division gives $(xa)a^{-1} = x$. Left-division produces

$$
a^{-1}xa = (x \cdot a)a^{-1} - (x \wedge a)a^{-1},
$$

which flips the rejection part. Geometrically, that is reflection of $x$ in the line/axis defined by $a$. The same sandwiching pattern $axa^{-1}$ (equivalently $a^{-1}xa$ up to scalar commuting) is the basic template for orthogonal transformations in GA.

Two caveats keep you honest. First, projection extends nicely from vectors to blades by outermorphism, essentially by the same formula with $x$ replaced by $X$. Second, "rejection of a general blade" is less tidy: the naive extension $(X \wedge A)A^{-1}$ often collapses to zero when $X$ shares directions with $A$, and the alternative "$X$ minus its projection" need not be a blade at all. So rejection is clean for vectors, but becomes a subtler object for higher grades.

Gram–Schmidt drops out as repeated rejection written in one line of GA. Keep $b_1 = v_1$. Then orthogonalize by rejections encoded as wedge-then-divide:

$$
b_2 = \frac{v_2 \wedge b_1}{b_1}, \qquad
b_3 = \frac{v_3 \wedge b_1 \wedge b_2}{b_1 \wedge b_2},
$$

and so on. Each step forms the "volume element" with the existing basis and then divides by the previous subspace blade to "straighten" it into an orthogonal vector. This is the same algorithm as classical Gram–Schmidt, but expressed without coordinates and using exactly the chapter's two heroes: wedge for spanning, and division (via geometric product invertibility) for solving.
