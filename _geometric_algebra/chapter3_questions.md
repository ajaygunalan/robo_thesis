# Chapter 3: Metric Products of Subspaces - Conceptual Questions

## 3.1 Sizing Up Subspaces

The scalar product $A * B$ between two $k$-blades is defined as a determinant of all pairwise dot products between their vector factors. Explain why this determinant structure naturally captures both the squared norm $\|A\|^2 = A * \tilde{A}$ (giving area, volume, etc.) and the angle between subspaces via $\cos \theta = \frac{A * \tilde{B}}{\|A\|\|B\|}$. What does it mean geometrically when two blades have zero cosine in higher dimensions?


## 3.2 From Scalar Product to Contraction

The contraction $A \rfloor B$ is motivated by wanting to "factor out" $A$ from a scalar product: $(X \wedge A) * B = X * (A \rfloor B)$. Explain why this makes contraction a grade-reducing product with $\text{grade}(A \rfloor B) = \text{grade}(B) - \text{grade}(A)$, and why we need the explicit axioms (3.7-3.11) rather than just this implicit definition.


## 3.3 Geometric Interpretation of the Contraction

The contraction $A \rfloor B$ produces a blade that is simultaneously contained in $B$ and perpendicular to $A$. Explain why this is characterized as "the largest subspace of $B$ that is most unlike $A$," and how the weight of $A \rfloor B$ relates to how much of $A$ projects onto $B$.


## 3.4 The Other Contraction

The right contraction $B \lfloor A$ differs from the left contraction $A \rfloor B$ only by a grade-dependent sign: $B \lfloor A = (-1)^{a(b+1)} A \rfloor B$. Why do both reduce to the ordinary dot product for vectors, and when would you prefer one over the other in a formula?


## 3.5 Orthogonality and Duality

The duality relationships $(A \wedge B)^* = A \rfloor (B^*)$ and $(A \rfloor B)^* = A \wedge (B^*)$ show that dualization swaps the outer product and contraction. Explain how the dual $A^* = A \rfloor I_n^{-1}$ represents the orthogonal complement of $A$, and why testing $\mathbf{x} \in A$ can be done either via $\mathbf{x} \wedge A = 0$ (direct) or $\mathbf{x} \rfloor A^* = 0$ (dual).


## 3.6 Orthogonal Projection of Subspaces

The projection formula $P_B[X] = (X \rfloor B) \rfloor B^{-1}$ works by first contracting (which gives the dual of the projection within $B$) then contracting again to undo the dualization. Explain why this two-step process is necessary and why projection is nonlinear in $B$ but linear in $X$.


## 3.7 The 3-D Cross Product

The cross product is defined as $\mathbf{a} \times \mathbf{b} = (\mathbf{a} \wedge \mathbf{b}) \rfloor I_3^{-1}$, revealing it as the dual of the outer product. What are the two geometric operations hidden inside the cross product, and why does using $\mathbf{a} \wedge \mathbf{b}$ directly generalize to $n$ dimensions while $\mathbf{a} \times \mathbf{b}$ does not?


## 3.8 Application: Reciprocal Frames

The reciprocal basis vector $\mathbf{b}^i$ is constructed as the dual of the $(n-1)$-blade formed by all basis vectors except $\mathbf{b}_i$. Explain why this makes $\mathbf{b}^i$ perpendicular to all $\mathbf{b}_j$ for $j \neq i$, and why extracting the coefficient $x^i$ from $\mathbf{x} = \sum x^i \mathbf{b}_i$ requires knowing all basis vectors, not just $\mathbf{b}_i$.
