# Multivectors as Coefficient Vectors

The core representational move is to treat any multivector as a weighted sum of **basis blades**. In a $3$-D geometric algebra, one natural ordered basis is

$$
1,\ e_1,\ e_2,\ e_3,\ e_1 \wedge e_2,\ e_2 \wedge e_3,\ e_3 \wedge e_1,\ e_1 \wedge e_2 \wedge e_3.
$$

This basis already encodes the graded structure: scalars (grade $0$), vectors (grade $1$), bivectors (grade $2$), and a trivector (grade $3$).

Combinatorially, the number of independent basis $k$-blades in an $n$-dimensional algebra is

$$
\binom{n}{k},
$$

so the total number of basis blades spanning the full algebra is

$$
\sum_{k=0}^{n} \binom{n}{k} = 2^n.
$$

Once you pick an ordering of those $2^n$ blades, any multivector $A$ can be represented by a coefficient column vector $[[A]] \in \mathbb{R}^{2^n}$ (or over whatever scalar field you're using). Conceptually, recovering the multivector from its coordinates is "just" the symbolic basis row times the numeric coefficient column:

$$
A = [\text{basis blades in order}] \cdot [[A]].
$$

The catch—the one that motivates everything about "efficient" implementation—is that this representation is dense even when the object is not. A $k$-blade lives entirely in grade $k$, so most coordinates in $[[A]]$ are necessarily zero. The higher the dimension, the more severe this mismatch becomes, and the more you're pushed toward representations (or algorithms) that respect sparsity and grade structure rather than pretending every multivector is fully populated.
