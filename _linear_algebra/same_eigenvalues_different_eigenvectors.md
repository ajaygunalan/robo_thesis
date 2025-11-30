## Same nonzero eigenvalues even though different eigenvectors

It's a beautiful fact in linear algebra: $CD$ and $DC$ share the same non-zero eigenvalues, even though matrix multiplication is generally non-commutative $(CD \neq DC)$.

#### The Core Idea

If $CD\mathbf{v} = \lambda\mathbf{v}$, then applying $D$ yields:  
$DC(D\mathbf{v}) = \lambda(D\mathbf{v})$ so $D\mathbf{v}$ is an eigenvector of $DC$ with the same eigenvalue $\lambda$.

The eigenvalue stays the same; the eigenvector transforms.

#### Geometric Interpretation

Think of $C$ and $D$ as transformations:

- $CD$ means applying $D$ then $C$
- $DC$ means applying $C$ then $D$

These compositions differ, but preserve scaling along certain directions — the non-zero eigenvalues capture this intrinsic "stretching."

#### Trace, Determinant, and Structure

- $\text{tr}(CD) = \text{tr}(DC)$
- $\det(CD) = \det(DC)$ (for square matrices)

These invariants reflect how both products encode the same overall deformation.

#### SVD Viewpoint

From SVD: the non-zero eigenvalues of $CD$ and $DC$ are the squares of shared singular values.  
So, regardless of order, the same fundamental stretching is measured.

#### A Rubber Sheet Analogy

Imagine deforming a rubber sheet:

- $C$ stretches and twists
- $D$ does the same differently

$CD$ and $DC$ deform the sheet differently, but the net amount of stretch along principal axes (non-zero eigenvalues) is unchanged.

#### Why Zero Eigenvalues Differ

Zero eigenvalues relate to nullspaces—directions that collapse. Since order matters in collapse, $CD$ and $DC$ can nullify different subspaces.

#### Final Takeaway

The non-zero eigenvalues of $CD$ and $DC$ are invariant—revealing deep geometric structure that transcends multiplication order, even when the matrices don't commute.