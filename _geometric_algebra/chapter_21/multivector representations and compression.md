# Multivector Representations and Compression

Specialized multivector types only work when the type of each variable is fixed in the relevant scope—often true in well-structured geometric code, but not always. Some programs accept noisy data, interactive input, or dynamically changing representations where you can't know at compile time which multivector "shape" you'll receive. The chapter therefore insists on a dual design: always provide a **general multivector** that can represent anything, and treat specialized types as the performance path when types are stable.

The general multivector is where compression matters, because storing all $2^n$ coordinates naively is wasteful, but compression can backfire if it replaces arithmetic with branches and pointer chasing. The chapter frames compression as a balancing act between "don't process zeros" and "don't drown in control-flow overhead."

It lays out three compression styles, each trading memory for predictability:

## Per-coordinate compression

Store only nonzero coordinates in a list, tagging each with the basis blade it belongs to. This captures sparsity aggressively, but it tends to make inner loops branchy: you iterate over variable-length lists, do per-entry checks, and often pay for unpredictable memory access.

## Per-grade compression

Instead of tracking individual coordinates, group coordinates by grade. Many multivectors are sparse by grade (a blade lives in one grade; a versor is even or odd), so you can often omit entire grade blocks. This allows you to process coordinates in larger predictable chunks—reducing branching compared to per-coordinate compression—while still skipping unused grades. The chapter argues this is a good balance for low-dimensional algebras.

A representative structure is: a grade-usage bitmap and a pointer to dynamically allocated coordinate storage. In pseudocode terms:

- `gu`: an integer bitmap; bit $i$ indicates whether grade $i$ is present.
- `c`: a contiguous block of coordinates for all present grades, stored in a known layout.

This keeps "is grade present?" decisions coarse, avoiding per-coordinate branching.

## Per-group compression

Grades are sometimes still too coarse. In a 5D conformal algebra, a 2-blade "flat point" uses far fewer than the full set of 10 grade-2 coordinates, so per-grade compression still stores a lot of zeros. The chapter proposes more refined groupings tailored to the model and usage (e.g., grouping based on whether $\infty$ appears in the basis blades), but stresses that the "right" grouping depends on the geometry you're actually doing (even within conformal models, Euclidean vs hyperbolic use suggests different groupings).

---

Specialized multivector classes avoid this whole compression dilemma by construction: a specialized type stores a fixed, minimal set of coordinates in a fixed order (and may omit known constants), and conversion functions bridge between specialized and general multivectors when needed. That fixed layout is what later makes it feasible to generate branchless, loop-free arithmetic for operations on those types.
