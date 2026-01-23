# Four Levels of Geometric Algebra Implementation

Once you commit to a concrete representation, a geometric algebra system naturally decomposes into levels—not for philosophical purity, but because different kinds of operations want different implementation tactics.

## 1) Basis blades and their elementary rules

At the bottom is the discrete world: a fixed set of basis blades and the elementary products/operations you can perform on them. This is where sign rules, metric effects, and combinatorial structure live. Getting this level right gives you a trustworthy "ground truth" for building everything above it.

## 2) Linear multivector operations

Many GA operators are linear (and typically distributive over addition). At this level, you exploit that property: if you can compute an operator on basis blades, you can extend it to arbitrary multivectors by linearity. Implementation-wise, this can look like:

- precomputing linear maps (matrix-style thinking), or
- iterating over stored basis-blade terms (list/sparse thinking).

Either way, linearity is the reason this middle layer can be made both simple and fast.

## 3) Nonlinear operations

Some fundamental operations are "elementary" in the GA toolkit but do not fit the linear/distributive pattern. They require dedicated algorithms that don't reduce to "apply operator to each term and sum." Efficiency concerns may also force these algorithms to look directly at the multivector's coordinates (for example, to choose numerically stable pivots or detect dominant components).

## 4) The application level

Finally, there's the layer that isn't about algebra anymore: using GA inside a real program. Here the design problem is representation choice and computational strategy for *your* domain—what objects you store, what primitives you use, and what operations you treat as first-class.

---

The important insight is that "geometric algebra implementation" isn't one problem; it's a stack of problems with different invariants, different performance levers, and different failure modes.
