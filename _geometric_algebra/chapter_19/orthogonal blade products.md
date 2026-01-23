# orthogonal blade products

In an orthogonal basis, basis-blade multiplication collapses to three concerns: (1) whether the outer product is allowed (independence), (2) which basis vectors survive in the resulting blade, and (3) the sign from reordering into canonical form.

## Outer product as "independence + symmetric difference + sign"

The outer product $A\wedge B$ is zero whenever $A$ and $B$ share a basis vector factor. In bitmap form, "sharing a factor" is exactly "sharing a 1-bit," so dependence is detected by a single mask:

* If $(a \mathbin{\&} b) \neq 0$, then $A\wedge B = 0$.

When they are independent, the resulting blade contains exactly those basis vectors that appear in either blade. Since the sets are disjoint in this case, "union" and "exclusive or" coincide; implementation-wise you compute the output bitmap as:

* `bitmap = a ^ b`

Then you correct the antisymmetry sign using the canonical reordering sign and multiply the operand scales.

A concrete example: $(e_2\wedge e_3)\wedge e_1$ must be reordered into $e_1\wedge e_2\wedge e_3$, which costs one swap (so a minus sign). On bitmaps, $110_b$ combined with $001_b$ gives $111_b$, and the sign routine supplies the $-1$ factor.

## Geometric product in diagonal orthogonal metrics

Assume an orthogonal metric where
$$e_i\cdot e_j = 0 \quad (i\neq j), \qquad e_i^2 = m_i,$$
so the metric matrix is diagonal with diagonal entries $m_i$ (Euclidean space is the special case $m_i=1$).

Now the difference from the outer product is exactly what happens when basis vectors repeat between multiplicands. The outer product would force zero, but the geometric product uses the Clifford relation: a repeated $e_i e_i$ collapses to the scalar $m_i$ and disappears from the blade factors. That means:

* The *surviving basis-vector set* is obtained by "toggling" indices that appear twice: indices common to both operands vanish from the blade part.
* The *scalar scale* picks up a multiplicative factor of $m_i$ for each cancelled index $i$.

In bitmap terms, the indices that cancel are the 1-bits of `(a & b)`. You multiply the output scale by $\prod_{i\in \text{common}} m_i$.

The implementation structure mirrors the outer product:

* The output bitmap is still computed with `a ^ b` (because shared bits are removed, and unshared bits remain).
* The sign is still the canonical reordering sign (because you still must permute factors into canonical order).
* The only new ingredient is the metric-factor multiplier driven by `(a & b)`.

Example: $(e_1\wedge e_2)(e_2\wedge e_3)$ shares $e_2$, so the $e_2 e_2$ collapses to $m_2$, and the blade part becomes $e_1\wedge e_3$:
$$(e_1\wedge e_2)(e_2\wedge e_3) = m_2 \cdot (e_1\wedge e_3).$$

In a Euclidean metric, all $m_i=1$, so the geometric product reduces to exactly "XOR + canonical sign" for basis blades. In that case, the only difference between the outer product routine and the geometric product routine is that the outer product has the dependence check and returns zero when there is overlap.
