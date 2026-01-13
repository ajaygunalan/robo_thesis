---
title: "Chapter 2 — Spanning Oriented Subspaces"
chapter: 2
tags: [geometric-algebra, blades, outer-product, grassmann]
---
# Spanning Oriented Subspaces

Linear algebra is happy to *describe* subspaces; geometric algebra wants to *compute with them*. This chapter's pivot is to promote "line/plane/volume through the origin" from sets of vectors into algebraic elements you can add, scale, and multiply—all while staying inside the same algebra. We begin with the standard [[Vector Spaces (R^n)|real vector space]] $\mathbb{R}^n$, but treat homogeneous subspaces as first-class citizens rather than mere point-sets.

That promotion needs one new operation: the [[Outer Product (Wedge)|outer product]] $\wedge$. It doesn't measure with a metric; it records which subspace you span (**attitude**), which way it's oriented (**orientation**), and how much of it (**weight**). The result is called a **blade**. To capture a plane without choosing a special basis or a normal, you want something that flips sign when you swap spanning vectors and collapses to zero when they align—that desire crystallizes into $a \wedge b$. Negation flips "which way", scaling changes "how much", and the antisymmetry encodes the plane's handedness all in one object.

Once $\wedge$ is associative, higher span is just more of the same: $a \wedge b \wedge c$ is an oriented volume element, and in $\mathbb{R}^3$ any 4-fold wedge vanishes because you've run out of independent directions. This "possible subspaces by grade" forms [[The Ladder of Blades|a ladder of blades]]—scalars sit at grade 0, vectors at grade 1, bivectors (planes) at grade 2, trivectors (volumes) at grade 3, and so on up to the unique $n$-blade called the **pseudoscalar**. One pattern, different grade.

Grade then becomes your dimension bookkeeping that stays geometric, and it forces an important warning: in $\mathbb{R}^4$ and higher, not every 2-vector is a blade. A sum like $e_1 \wedge e_2 + e_3 \wedge e_4$ doesn't represent any single plane—it's a general bivector that *cannot* be factored into $a \wedge b$. The boundary between geometry (simple blades representing subspaces) and pure algebra (arbitrary sums of blades) is what makes [[Graded Algebra Concepts|graded algebra]] both powerful and subtle. In $\mathbb{R}^3$, every bivector happens to be simple, so the trap only springs in four or more dimensions.

The chapter stays metric-free on purpose—no inner product, no perpendicularity. If you catch yourself wanting a normal vector, that impulse is exactly what $\wedge$ is replacing. A plane *is* the bivector $a \wedge b$, not some vector pointing perpendicular to it. The [[Geometric Properties|geometric properties]] encoded in a blade—containment, orientation, relative magnitude—are all metric-independent. The incidence test $x \wedge A = 0$ checks whether $x$ lies in the subspace of $A$ without ever asking "how long is $x$?" or "what angle does it make?"

Finally, when subspaces are computable, familiar procedures snap into place. Cramer's rule becomes ratios of oriented areas, line intersection reshapes into bivector algebra, and incidence tests reduce to checking whether a wedge product vanishes. These [[Applications|applications]] show the real payoff: once subspaces are elements rather than sets, geometry becomes calculation.

If one slogan survives this chapter: $\wedge$ turns spanning into algebra. The relative content of a $k$-simplex is $\frac{1}{k!} a_1 \wedge \cdots \wedge a_k$, the span of a collection is just their wedge, and "does this point lie in that plane?" is a single multiplication. Everything that follows—metric products, duality, rotations—builds on this foundation of subspaces as algebraic objects you can manipulate directly.
