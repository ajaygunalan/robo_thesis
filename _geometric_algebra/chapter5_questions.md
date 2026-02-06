# Chapter 5: Intersection and Union of Subspaces - Conceptual Questions

## 5.1 The Phenomenology of Intersection

When two planes intersect in 3-D, the result is usually a line (grade 1), but if they coincide, the result is a plane (grade 2). Explain why this grade-switching behavior means intersection cannot be a linear product, and why the magnitude and orientation of the intersection blade are inherently ambiguous (as illustrated by reshaping the input 2-blades without changing their subspace).


## 5.2 Intersection Through Outer Factorization

The meet $M = A \cap B$ and join $J = A \cup B$ are defined through outer factorization: $A = A' \wedge M$, $B = M \wedge B'$, and $J = A' \wedge M \wedge B'$. Explain why this factorization is not unique (a scalar $\gamma$ can be traded between $M$ and $J$), and why this ambiguity does not affect geometric computations like projection onto the meet subspace via $(x \rfloor M^{-1}) \rfloor M$.


## 5.3 Relationships Between Meet and Join

Given blades $A$ and $B$ with meet $M$ and join $J$, the key computational formulas are $J = A \wedge (M^{-1} \rfloor B)$ and $M = (B \rfloor J^{-1}) \rfloor A$. The dual form $(A \cap B)^* = B^* \wedge A^*$ shows the meet's dual is the outer product of the duals. Explain why the duality here is relative to the join $J$ (not the full space $I_n$), and why the grade relationship $m + j = a + b$ must hold.


## 5.4 Using Meet and Join

When subspaces are in general position, the join is simply the pseudoscalar of their common space, and the meet formula $M = (B \rfloor J^{-1}) \rfloor A$ applies directly. For two planes $A$ and $B$ in 3-D with $J = I_3$, this gives $A \cap B = B^* \rfloor A$. Explain why the classical cross product of normal vectors $A^* \times B^*$ is a special case of this formula, and how the general formula extends to subspaces of any grade in any dimension.


## 5.5 Join and Meet Are Mostly Linear

Once the join $J$ is fixed, the meet formula $M = (B \rfloor J^{-1}) \rfloor A$ is linear in both $A$ and $B$ since contractions are linear. Explain why the meet becoming zero signals that the join must change (a degeneracy has occurred), and why within each "domain" where the join is constant, the meet varies smoothly and linearly with its arguments.


## 5.6 Quantitative Properties of the Meet

For normalized blades $A$ and $B$ within a normalized join, the magnitude of $A \cap B$ equals the sine of the angle from $A$ to $B$. The symmetry depends on grades: $B \cap A = (-1)^{(j-a)(j-b)} A \cap B$. Explain why two lines in a plane meet antisymmetrically (sine of opposite angles) while a line and plane in space meet symmetrically, and how the sign of the meet indicates "which side" of $B$ the subspace $A$ approaches from.


## 5.7 Linear Transformation of Meet and Join

Despite being nonlinear products, meet and join transform in a structure-preserving way under invertible linear transformations: $\mathsf{f}[A \cup B] = \mathsf{f}[A] \cup \mathsf{f}[B]$ and $\mathsf{f}[A \cap B] = \mathsf{f}[A] \cap \mathsf{f}[B]$. Explain why this works (linear transformations preserve the outer product factorization), and why meet and join are actually nonmetric products even though their computation uses the metric contraction (the two contractions cancel metrically).
