# computing complementary factors

Meet/join are defined by an outer-product factorization
$$
A = A' \wedge M,\qquad B = M \wedge B',
$$
so practical computation often reduces to extracting the “parts outside the meet” in a way that respects orientation and normalization. With careful ordering, the complementary factors are obtained by contraction with the inverse meet:
$$
B' = M^{-1} \rfloor B,\qquad A' = A \lfloor M^{-1}.
$$
The inverse supplies the normalization needed to avoid an additional arbitrary scalar drift.

Once $A'$ and $B'$ are available, the join can be expressed directly in terms of $A,B,$ and $M$:
$$
J = A \cup B = A \wedge (M^{-1} \rfloor B) = (A \lfloor M^{-1}) \wedge B.
$$

The appearance of $M^{-1}$ may suggest a metric restriction. Treat that inverse as computational scaffolding; see [[linear transformation invariance]].
