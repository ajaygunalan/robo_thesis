# linear transformation invariance

Meet and join are incidence operations defined by outer-product factorization, so they transform cleanly under any invertible linear map $f$ acting as an outermorphism:
$$
f[A \cup B] = f[A] \cup f[B],\qquad f[A \cap B] = f[A] \cap f[B].
$$
The structural reason is that an invertible linear map preserves containment and common outer factors: if $A$ was (not) contained in $B$ before, then $f[A]$ is (not) contained in $f[B]$ after.

The computational caveat is that meet-from-join formulas depend on *which join you dualize against*. If $J=A\cup B$ and you compute $A\cap B$ as a contraction with $J^{-1}$, then after transforming you must use the transformed join:
$$
f[A \cap B] = \big(f[B] \rfloor f[J]^{-1}\big) \rfloor f[A],
$$
which is generally not the same as contracting with $J^{-1}$.

This also explains why meet/join are **nonmetric** even though contractions appear in convenient formulas: the intermediate metric dependence cancels, because the underlying definition is purely outer-product factorization. In particular, when null vectors prevent inverses from existing in the intended model, you can temporarily assume a Euclidean metric (a computational scaffold) to make the required inverses exist, compute the incidence outcome there, and interpret the result back in the original setting.
