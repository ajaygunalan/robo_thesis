# Basis-Blade List Implementation and Sparsity

The dense matrix viewpoint is convenient and general, but it has a brutal mismatch with how geometric algebra is typically used: most multivectors you care about are sparse in the basis-blade expansion (single-grade blades for geometry objects, restricted-grade versors for operators). The chapter's second implementation approach embraces that reality: store a multivector as a **list of weighted basis blades** and implement products/operations by distributing them over those lists.

## Representation: a multivector as "just the nonzero blades"

Instead of a length-$2^n$ coordinate array, represent

$$
A = \sum_{p=1}^{P} \alpha_p B_p
$$

as a list of $P$ items, each item being a pair (basis blade identifier, weight). If $A$ is sparse, $P \ll 2^n$.

This shifts the implementation goal from "compute with all coordinates" to "compute only what exists."

## The engine: linearity + distributivity pushed down to blades

Because the products and operations in this chapter are linear, they distribute over sums. For a bilinear product $\star$,

$$
\left( \sum_i a_i \right) \star \left( \sum_j b_j \right) = \sum_i \sum_j (a_i \star b_j).
$$

And for unary linear operations (like reversion),

$$
\left( \sum_i b_i \right)^\sim = \sum_i (b_i^\sim).
$$

So you implement multivector-level operations by:

1. Looping over blades in the left list,
2. Looping over blades in the right list (for binary products),
3. Applying a basis-blade primitive operation (from the previous chapter),
4. Accumulating the results into a new list.

The chapter shows this explicitly with Java code for the outer product: a double loop over blades, compute the basis-blade outer product, append, then run a `simplify()` pass that merges equal blades by adding coefficients.

## Simplification is not optional

Distributing products generates repeated basis blades (same blade appearing from different pairs). You must combine them:

- identify identical blades (same basis blade, possibly differing only by scale/sign),
- add coefficients,
- drop near-zero terms (implementation-dependent).

That "combine like terms" step is the difference between "a correct algebra element" and "a bag of redundant partial results."

## The honest tradeoff: sparse correctness vs raw speed

This approach automatically exploits sparsity and is conceptually faithful to the algebra (it mirrors the distributive definition). But the chapter is blunt: the explicit double loops and repeated basis-blade product evaluations are computationally expensive, and straightforward implementations can be **one to two orders of magnitude slower** than approaches that expand, specialize, and optimize the loops. That performance gap is why the book flags optimization as a separate topic later on.
