# Versor Inverse

In geometric algebra code, you invert things constantly—but almost never "arbitrary multivectors." The practical objects you build (reflections, rotors, motors, blades used as subspaces) are typically **versors** (geometric products of invertible vectors) or **invertible blades** (which are versors in disguise). The win is that versors admit an inversion formula that reduces to "reverse + divide by a scalar."

## The Structural Fact That Makes It Work

Let a versor be written as a product of vectors
$$
V = v_k v_{k-1}\cdots v_2 v_1,
$$
and let $\tilde V$ denote **reversion** (reverse the order of vector factors):
$$
\tilde V = v_1 v_2 \cdots v_{k-1} v_k.
$$

Then the product $V\tilde V$ is always **a scalar** (grade 0). The insight is that adjacent equal vectors collapse to their squared norm:
$$
V\tilde V
= (v_k\cdots v_2 v_1)(v_1 v_2 \cdots v_k)
= v_k^2 \cdots v_2^2 v_1^2,
$$
so every non-scalar grade cancels out during the telescoping contraction.

## The Inverse Formula

Because $V\tilde V$ is scalar (and nonzero for a true versor), the inverse is
$$
V^{-1}=\frac{\tilde V}{V\tilde V}.
$$

Algorithmically:

1. Compute $\tilde V$ (reversion is cheap: it's a sign flip per grade component, or a permutation-based sign when stored by basis blades).
2. Compute the scalar $s = V\tilde V$.
3. Return $V^{-1}=\tilde V/s$.

## When It Fails (and Why That's Correct)

If $V\tilde V = 0$, the formula "fails" because you can't divide by zero. But that's not an algorithmic inconvenience—it's a *mathematical certificate* that you don't have a versor built from invertible vectors. A null vector factor (or any noninvertible factor) can drive $V\tilde V$ to zero, and such an element is not invertible, hence not a versor by definition.

## Why Blades Are Covered

An invertible $k$-blade is an outer product of $k$ vectors, but it can also be written as a geometric product of $k$ vectors (a $k$-versor). So "invert versors well" is effectively "invert (invertible) blades well," which is why GA libraries lean so heavily on this method.
