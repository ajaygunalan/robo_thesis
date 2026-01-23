# grade-derived operations

Once you can compute the geometric product $AB$, most of the other operations you care about are either (a) *grade filters* applied to $AB$ or (b) simple linear combinations of products.

## Grades from bitmaps and grade projection

For a basis blade represented by a bitmap, its **grade** is the number of basis vectors in the blade—implemented as the population count of the bitmap (the number of 1-bits). This makes grade tests effectively free at the bit level.

Write $\langle X\rangle_k$ for the grade-$k$ part of a multivector $X$ (a grade projection). Then many metric-related products can be defined entirely as "compute $AB$ then keep only one grade."

## Metric products as grade selections of the geometric product

Let $A$ and $B$ be basis blades of grades $a$ and $b$.

The "metric products" family (scalar product, contractions, and inner-product variants) are defined by selecting specific grades from $AB$:

* **Left contraction**: if $a\le b$, keep grade $b-a$ from $AB$; otherwise return $0$.
* **Right contraction**: if $a\ge b$, keep grade $a-b$ from $AB$; otherwise return $0$.
* **Dot product**: if $a\le b$, it agrees with the left contraction; otherwise it agrees with the right contraction.
* **Hestenes metric product**: like the dot product, except it is defined to be $0$ whenever either operand is a scalar (grade 0).
* **Scalar product**:
  $$A * B = \langle AB\rangle_0.$$

From an implementation viewpoint, this is attractive because it keeps one "master" multiply (geometric product) and makes everything else a thin wrapper.

A useful micro-optimization for contraction-like products: before doing the multiply, check whether the lower-grade blade is **contained** in the higher-grade blade (in the orthogonalized setting where bit inclusion corresponds to factor inclusion). In bitmap form this is the subset test
$$\text{contained} \iff (\text{low} \mathbin{\&} \text{high}) = \text{low}.$$
If containment fails, the contraction (of whatever flavor) must be $0$. For nonorthogonal metrics, this containment test should be performed after transforming to the orthogonal eigenbasis, because "containment of orthogonal factors" is what controls whether those products can be nonzero.

## Commutator product

The commutator product is directly derived from the geometric product by antisymmetrization:
$$A\times B \equiv \tfrac12(AB - BA).$$
Implementation-wise, it's "two geometric products and a subtraction," and it's the standard route to the Lie-algebra structure carried by bivectors.

## Grade-dependent sign operators on basis blades

Several involution-like operations act on a basis blade by multiplying it with a sign that depends only on its grade $a$ (so they are cheap once you have the grade via popcount):

* **Reversion**:
  $$\widetilde{A} = (-1)^{a(a-1)/2} A.$$
* **Grade involution**:
  $$\hat{A} = (-1)^a A.$$
* **Clifford conjugation**:
  $$\overline{A} = (-1)^{a(a+1)/2} A.$$

Because a basis blade in bitmap form is stored as `(bitmap, scale)`, implementing these is literally: compute $a$, compute the $\pm 1$ multiplier from the appropriate exponent parity, and multiply the `scale` field—no changes to the bitmap itself.
