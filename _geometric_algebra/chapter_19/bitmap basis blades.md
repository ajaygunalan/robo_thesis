# bitmap basis blades

A *basis blade* is a unit scalar or a nonzero outer product of distinct basis vectors from $\{e_i\}_{i=1}^n$. The key observation behind the bitmap representation is brutally simple: a basis blade either contains a particular basis vector $e_i$, or it doesn't. That makes a blade naturally representable as a boolean list over indices $i=1,\dots,n$—and therefore as a bitmap packed into an integer.

The convention is: bit 0 corresponds to $e_1$, bit 1 to $e_2$, bit 2 to $e_3$, and so on. The unit scalar contains no basis vectors, so it is the all-zero bitmap. A blade like $e_1\wedge e_3$ contains indices 1 and 3, so its bitmap has bit 0 and bit 2 set: $101_b$. In the same scheme, $e_2$ is $10_b$, $e_1\wedge e_2$ is $11_b$, and $e_1\wedge e_2\wedge e_3$ is $111_b$. When you extend the algebra by one dimension, you just allocate the next most significant bit; existing encodings don't change.

There's a small cognitive tax here: the "visual order" of bits is reversed relative to how we write blades. In $e_1\wedge e_2\wedge e_3$, the $e_1$ factor is leftmost in algebraic notation, but bit 0 is rightmost in binary. The payoff is implementation convenience: bit shifts, masks, and integer ops behave predictably as you scale up dimensions.

Practical implementations typically store a basis blade as two fields:

* `bitmap`: the integer bitset indicating which basis vectors appear.
* `scale`: a floating-point weight carrying the blade's coefficient, including sign.

That `scale` is what lets the representation stay canonical while still expressing antisymmetry. You never store "$e_3\wedge e_1$" as a separate bitmap; you store the canonical blade "$e_1\wedge e_3$" with a negative scale to account for the swap.

Using a 32-bit integer for the bitmap gives you basis blades up to 32 dimensions "for free." In practice, the limiting factor is not the bitmap width but the explosion of basis blades in a full multivector: there are $2^n$ basis blades in an $n$-D algebra, so "basis-of-blades" multivectors and their products become expensive well before you hit the integer's bit limit.
