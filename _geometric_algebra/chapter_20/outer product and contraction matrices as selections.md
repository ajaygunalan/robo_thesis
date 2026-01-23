# Outer Product and Contraction Matrices as Selections

Once you can represent left-multiplication by $A$ via an operator matrix for the geometric product, you can build operator matrices for other products too: outer product, left contraction, right contraction, scalar product, commutator, etc. The chapter's key point is that many of these are not "new multiplications," but **grade-filtered parts** of the geometric product—so their matrices look like the geometric-product matrix with systematic zeros.

## Derived-product operator matrices

For any bilinear product $\star$ that's linear in its right argument, you can define an operator matrix $A^\star$ such that

$$
A \star B \leftrightarrow (A^\star) \mathbf{b}.
$$

The chapter explicitly shows this for the outer product and left contraction, and illustrates that their symbolic matrices largely mirror the geometric-product matrix with entries removed where the grade rule forbids contributions.

## "Mostly the same matrix, but with zeros" is not an accident

Outer product and contractions can be expressed as grade selections of the geometric product. Operationally:

- Build the same underlying multiplication table (structure coefficients).
- Keep only those contributions that land in the grades permitted by the product definition.
- Zero out the rest.

That's why the chapter's symbolic matrices for $A^G$, $A^O$ (outer), and $A^L$ (left contraction) are visually close, yet differ by strategically placed zeros.

## Bootstrapping with symbolic matrices

The chapter points out a practical trick: you only need to do the expensive "basis blade times basis blade" work once, up front, to build **symbolic** operator matrices (entries expressed in terms of the coefficients of $A$). After that, computing an actual product $C = AB$ becomes:

1. Instantiate a numeric operator matrix for the current $A$ by plugging in $A$'s coefficients into the symbolic template.
2. Multiply by $\mathbf{b}$ to get $\mathbf{c}$.

This turns "recompute blade products every time" into "reuse a compiled multiplication pattern," which is crucial for general Clifford algebras—even if it still doesn't automatically exploit sparsity.

## Structural facts you can read off the matrices

The chapter ends with exercises that are basically "matrix literacy for geometric algebra." Here are the underlying structural reasons (no busywork):

### Why the first columns of $A^G$ and $A^O$ equal the coordinate vector of $A$

Column $j = 0$ corresponds to multiplying by the scalar basis blade $1$ (i.e., the coordinate in $B$ that selects $L_0 = 1$). For both the geometric product and the outer product,

$$
A \cdot 1 = A, \qquad A \wedge 1 = A,
$$

so the operator applied to the "scalar basis vector" must return $A$—hence the first column reproduces $A$'s coordinates.

### Why this fails for left contraction

Left contraction is grade-reducing. Contracting with a scalar ($\mathrm{grade} = 0$) can only produce something nonzero when the left operand has grade $0$ as well (otherwise you're trying to reduce below grade $0$). So generally

$$
A \,\lrcorner\, 1 = \langle A \rangle_0,
$$

not $A$. That means column 0 of the left-contraction operator matrix carries only the scalar part of $A$, not the full multivector.

### Why the outer-product matrix is lower triangular (in the chapter's ordering)

If your basis ordering is grouped by increasing grade (as in the 3D example shown), then wedging with a basis blade cannot decrease grade. Outer product contributions land at grades that are "at or above" the input's grade in that ordering, which forces a one-sided (triangular) sparsity pattern in the operator matrix. The chapter highlights this as an observable property of the symbolic $A^O$ matrix.

### Recognizing $aB = a \lrcorner B + a \wedge B$ in matrix form

When $a$ is a vector and $B$ is a blade, the geometric product splits cleanly into an inner-like (grade-lowering) part and an outer-like (grade-raising) part. In the operator-matrix picture, that means the nonzero entries of $a^G$ partition into exactly those grade-lowering entries (matching $a^L$) and grade-raising entries (matching $a^O$).

You *don't* get $A^G = A^L + A^O$ for a general multivector $A$ because a general $A$ mixes grades, and the grade-selection rules for contraction/wedge across mixed-grade operands don't linearly decompose the full multiplication operator into two fixed masks independent of the operand grades.
