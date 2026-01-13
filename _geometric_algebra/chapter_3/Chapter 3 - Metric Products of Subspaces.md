---
title: " Metric Products of Subspaces"
chapter: 3
tags:
  - geometric-algebra
  - blades
  - metric
---
# Metric products of subspaces

The **outer product** $A \wedge B$ is great at _building_ subspaces (it tells you "what span do these directions generate?"), but it has no built-in ruler: it can't compare the length of one line to another line, or the area of one plane to another plane unless they already live in the same attitude. This chapter fixes that by importing a **metric on vectors** (the dot product) and lifting it to blades via the [[Scalar Product]], so every $k$-blade gets a meaningful **size** and a meaningful **angle** to any other blade of the same grade.

Once you start making those metric comparisons, a recurring simplification shows up: when two same-grade blades share directions, the comparison should depend only on the part that _isn't shared_. Turning that geometric instinct into a consistent algebraic rule forces a new product—the [[Contraction (⌋)|contraction]]—a grade-dropping "factor-out what's common" operator. Contraction is the metric-aware "take $A$ out of $B$" operation: it returns a specific subblade of $B$ that stays **inside $B$** and ends up **orthogonal to $A$**. Even better, these orthogonality operations compose cleanly: being perpendicular to $A$ and then to $B$ is the same as being perpendicular to $A \wedge B$—which makes contraction algebraically well-behaved enough to build everything else on top of it.

Now the killer move: once you have contraction, you can define an **inverse of any nonnull blade**, and then [[Duality and Orthogonality|duality]] drops out as a one-liner. Contracting any blade $A$ with the inverse pseudoscalar $I_n^{-1}$ produces the **orthogonal complement** $A^*$—a $(n-k)$-blade representing the complement subspace with consistent orientation. "Normal-vector style" representations are no longer a separate dual-space hack; they are just dual blades inside the same algebra.

The same idea works _inside any subspace_. If $B$ is a nonnull blade spanning some subspace $S$, then $B$ acts as the pseudoscalar **of $S$**, so "dual within $B$" is the same pattern with a different pseudoscalar. That [[Geometric Operations#Why $B^{-1}$ acts as "dual within $B$"|localized duality]] is exactly what powers projection: contraction followed by dual-in-$B$ lands you on the projected copy. Algebraically contraction stays the better primitive—it's bilinear in both arguments—while projection hides a $B^{-1}$ and is nonlinear in $B$.

Then **[[Geometric Operations#Reciprocal frames (coordinates without orthonormality)|reciprocal frames]]** become almost embarrassingly geometric instead of "minors of determinants." The construction dualizes the hyperplane spanned by "all basis vectors except $b_i$", producing the 1-vector orthogonal to that hyperplane—hence orthogonal to every $b_j$ with $j \neq i$. The result: coordinate extraction in a skew basis becomes a simple inner product with the reciprocal vector, and the cofactor/minor bookkeeping of linear algebra is replaced by a single complement operation.

Finally, the [[The 3-D Cross Product|cross product]] gets demoted from "mysterious primitive" to "3-D duality trick." It's just "span a plane" ($\wedge$) followed by "take the orthogonal complement" (dual). Once you're allowed to keep the bivector $a \wedge b$ as the plane itself, you stop needing a 3-D-only vector surrogate.

The whole chapter is one insistence repeated until the algebra gives in: metric comparisons should reduce to lower-dimensional comparisons by factoring out common directions. The scalar product supplies size and angles; that demand forces contraction; contraction plus inverses yields duality; and then projection, reciprocal frames, and the cross product all collapse into short compositions of $\wedge$, $\lrcorner$, and "dual."