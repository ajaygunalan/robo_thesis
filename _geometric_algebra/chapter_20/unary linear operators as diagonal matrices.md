# Unary Linear Operators as Diagonal Matrices

Once multivectors are encoded as coordinate vectors (one coordinate per basis blade in a fixed ordering), the *linear space* aspect of geometric algebra becomes literal: addition is vector addition, scalar multiplication is scalar–vector multiplication. The chapter emphasizes this because it's the lowest-friction way to implement the easy half of the algebra.

## Addition and scalar multiplication are coordinate-wise

If $A \leftrightarrow \mathbf{a}$ and $B \leftrightarrow \mathbf{b}$, then

$$
A + B \leftrightarrow \mathbf{a} + \mathbf{b}, \qquad \alpha A \leftrightarrow \alpha \mathbf{a}.
$$

There's no hidden geometry here—just the fact that multivectors form a linear space.

## Unary involutions are basis-wise sign flips

Operations like **reversion**, **grade involution**, and **Clifford conjugation** act predictably on basis blades; they do not mix blades, they only change signs (depending on grade). That makes their matrix representations **constant diagonal matrices** (constant = depends only on the basis ordering, not on the specific multivector).

Let $L_i$ be the $i$th basis blade in your ordered list, and let $r_i = \mathrm{grade}(L_i)$. Then you can implement:

### Reversion

Reversion reverses the order of vectors inside each blade; a grade-$r$ blade picks up the factor

$$
(-1)^{r(r-1)/2}.
$$

So define a diagonal matrix $R$ by

$$
R_{ii} = (-1)^{r_i(r_i-1)/2},
$$

and implement

$$
A^\sim \leftrightarrow R \mathbf{a}.
$$

This is exactly the diagonal-entry rule given in the chapter.

### Grade involution

Grade involution flips the sign of odd grades (or, equivalently, multiplies grade-$r$ components by $(-1)^r$). So define $J$ diagonal with

$$
J_{ii} = (-1)^{r_i},
$$

and compute

$$
\widehat{A} \leftrightarrow J \mathbf{a}.
$$

(The chapter lists grade involution alongside reversion as a matrix-implementable unary operator.)

### Clifford conjugation

Clifford conjugation is the composition of grade involution and reversion, so it also stays diagonal. On a grade-$r$ blade the sign is

$$
(-1)^{r(r+1)/2},
$$

so again you get a diagonal matrix determined solely by grade.

## Grade extraction is diagonal "selection"

Extracting the grade-$k$ part of a multivector is a linear projection. In coordinates, it's just "keep entries whose basis blade has grade $k$, zero the rest."

Define a diagonal selection matrix $S_k$ with

$$
(S_k)_{ij} =
\begin{cases}
1 & \text{if } i = j \text{ and } \mathrm{grade}(L_i) = k, \\
0 & \text{otherwise}.
\end{cases}
$$

Then

$$
\langle A \rangle_k \leftrightarrow S_k \mathbf{a}.
$$

This is the chapter's construction: a diagonal projector that depends on grade metadata for each basis blade.
