# Factored Representations for Blades and Versors

Geometric algebra has an additive face (multivectors as sums) and a multiplicative face (important objects built as products of vectors). Factored representations try to store the multiplicative face *directly*.

## Store factors, not expansions

A $k$-blade can be stored as a list of $k$ vectors whose outer product is the blade. A versor can be stored as a list of vectors whose geometric product is the versor. Instead of recording "all coordinates," you record "how it was made."

The big motivation is scaling: for blades and versors, the storage cost becomes polynomial in the ambient dimension (the chapter highlights a quadratic scaling), rather than exploding with the full coordinate expansion.

## The tradeoff: what becomes hard vs trivial

Because the representation is multiplicative, the difficulty of operations flips relative to additive coordinate storage:

- Operations like **addition**—trivial for coordinate vectors—become one of the hardest problems, because adding two factored objects generally does not preserve a simple factorization.
- Some geometric operations become strikingly easy. The chapter notes that **meet and join** can be trivial in a factored setting if you have a solid linear algebra backend (think LAPACK), whereas in an additive basis-blade representation they tend to require more involved algorithms.

## Where it makes sense

This approach is most compelling in **high-dimensional** geometric algebras (the chapter uses $n > 10$ as the regime where it starts to matter). Since the book's focus is largely on lower-dimensional algebras used in computer science applications, it treats factored representations as an interesting alternative rather than the main path, with more details deferred to specialized research work (notably Daniel Fontijne's thesis).
