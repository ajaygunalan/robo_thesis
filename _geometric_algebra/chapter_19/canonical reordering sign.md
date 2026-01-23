# canonical reordering sign

Bitmap blades encode *which* basis vectors are present, but they silently assume the blade is written in canonical increasing index order (e.g., $e_1\wedge e_3$, not $e_3\wedge e_1$). Multiplying blades breaks that assumption: you conceptually concatenate factors, then reorder them back into canonical order. Because the wedge-like antisymmetry is built into the geometric algebra basis structure, every swap of two distinct basis vectors flips the sign. So the only information you need is the *parity* of the number of swaps.

For two basis blades represented by bitmaps $a$ and $b$, the "swap count" can be computed without ever expanding the blades. The trick is to count, for each basis vector present in the left operand, how many basis vectors in the right operand must move past it when forming canonical order. In bit terms, this becomes a running "how many set bits overlap after shifting" computation.

A compact implementation pattern is:

* Shift $a$ right by one bit.
* Repeatedly:
  * Add the population count of $(a \mathbin{\&} b)$ to an accumulator.
  * Shift $a$ right by one again.
* If the accumulator is even, the sign is $+1$; if odd, the sign is $-1$.

In Java-flavored pseudocode (omitting boilerplate):

```java
double canonicalReorderingSign(int a, int b) {
    a >>>= 1;
    int swaps = 0;
    while (a != 0) {
        swaps += popcount(a & b);
        a >>>= 1;
    }
    return ((swaps & 1) == 0) ? 1.0 : -1.0;
}
```

What this is doing geometrically is computing $(-1)^N$, where $N$ is the number of pairwise crossings between the two ordered lists of basis indices when you interleave them into canonical order. It's the same sign you'd get by explicitly swapping symbols by hand—just measured with bit operations.

This sign primitive is reusable: it depends only on permutation parity induced by canonical ordering, not on the metric coefficients. That's why the same function can be used for the outer product sign and the geometric product sign in orthogonal settings.
