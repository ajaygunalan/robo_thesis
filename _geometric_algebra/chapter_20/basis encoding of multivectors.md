# Basis Encoding of Multivectors

A geometric algebra over an $n$-dimensional vector space has $2^n$ basis blades. If you **choose an ordering** of those basis blades, you can represent any multivector as an ordinary coordinate vector of length $2^n$—one coordinate per basis blade. This is the foundational encoding that lets you implement geometric-algebra operations via linear algebra machinery.

Concretely, define a "basis-blade row" (a list written as a row)

$$
\mathcal{L} = [L_0, L_1, \dots, L_{2^n-1}],
$$

where each $L_i$ is a basis blade, listed in your chosen order. In 3D, one natural order is by increasing grade (scalar, vectors, bivectors, trivector), for example:

$$
\mathcal{L} = [1,\ e_1,\ e_2,\ e_3,\ e_1 \wedge e_2,\ e_2 \wedge e_3,\ e_1 \wedge e_3,\ e_1 \wedge e_2 \wedge e_3].
$$

This is exactly the kind of ordered basis list the chapter uses as the anchor for its implementations.

Now encode a multivector $A$ by a coordinate column vector

$$
\mathbf{a} =
\begin{bmatrix}
a_0 \\ a_1 \\ \vdots \\ a_{2^n-1}
\end{bmatrix},
$$

and interpret that encoding via

$$
A = \mathcal{L} \mathbf{a} = \sum_{i=0}^{2^n-1} a_i L_i.
$$

So the *data structure* is just the array $\mathbf{a}$, while $\mathcal{L}$ (the basis blades and their ordering) is the *shared convention* that gives the array meaning.

Two details matter immediately:

1. **Indexing is semantic.** Coordinate $a_i$ is not "the $i$th number"; it is "the coefficient of blade $L_i$," and every operator you implement must respect that same $\mathcal{L}$ ordering.

2. **Grade becomes metadata.** Each $L_i$ has a grade $\mathrm{grade}(L_i) \in \{0, 1, \dots, n\}$. Many operations (especially unary involutions and grade projections) are "diagonal" precisely because they act per basis blade based on its grade.
