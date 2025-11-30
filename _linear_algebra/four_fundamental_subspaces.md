# The Four Fundamental Subspaces

## Motivation

Every matrix $A \in \mathbb{R}^{m \times n}$ defines four fundamental subspaces. Together, they reveal the geometry of linear transformations and explain the structure of solutions to $Ax = y$. 📐


![[four_subspaces.png]]



## Orthogonality and Vector Decomposition

The subspaces form orthogonal pairs that span the entire domain and codomain.

- In $\mathbb{R}^n$: Any vector $x$ can be uniquely split into a row space component and a nullspace component: $x = x_r + x_n$.
- In $\mathbb{R}^m$: Any vector $y$ can be uniquely split into a column space component and a left nullspace component: $y = y_c + y_l$.

## How to Compute a Basis: The SVD Approach

The most powerful factorization for understanding all four subspaces simultaneously is the **Singular Value Decomposition ([[SVD]])**. It provides a complete and orthonormal picture.

$$A = U\Sigma V^T$$

This single decomposition gives you orthonormal bases for all four subspaces without any further computation.

- **Column Space $C(A)$**: The first $r$ columns of $U$ (where $r$ is the rank) form an orthonormal basis for the column space. $C(A) = \text{span}(u_1, u_2, \ldots, u_r)$
    
- **Left Nullspace $N(A^T)$**: The remaining $m-r$ columns of $U$ form an orthonormal basis for the left nullspace. $N(A^T) = \text{span}(u_{r+1}, \ldots, u_m)$
    
- **Row Space $C(A^T)$**: The first $r$ columns of $V$ form an orthonormal basis for the row space. $C(A^T) = \text{span}(v_1, v_2, \ldots, v_r)$
    
- **Nullspace $N(A)$**: The remaining $n-r$ columns of $V$ form an orthonormal basis for the nullspace. $N(A) = \text{span}(v_{r+1}, \ldots, v_n)$
    

**The core takeaway is this**: The SVD directly constructs the orthonormal basis vectors ($u_i$ and $v_i$) that perfectly span these orthogonal subspaces. This is the ultimate "basis computation."

## Projections and the Pseudoinverse: An SVD Perspective

The SVD provides the most intuitive way to understand the pseudoinverse ($A^+$) and its role in projection. The pseudoinverse essentially "inverts" the action of the matrix $A$. Where $A$ maps the row space to the column space, $A^+$ maps the column space back to the row space.

### 1. Defining the Pseudoinverse

If the SVD of $A$ is $U\Sigma V^T$, the pseudoinverse is defined by inverting each part:

$$A^+ = V\Sigma^+ U^T$$

Here, $\Sigma^+$ is the diagonal matrix $\Sigma$ with its non-zero singular values inverted (i.e., $\sigma_i$ becomes $1/\sigma_i$).

### 2. Building the Projection Matrices

Now, combining $A$ and $A^+$ gives us the projection matrices. Watch what happens when we multiply them, remembering that $U^T U = I$ and $V^T V = I$ because $U$ and $V$ are orthogonal.

- **Projector onto the Column Space $(C(A))$:** $$P_{col} = AA^+ = (U\Sigma V^T)(V\Sigma^+ U^T) = U(\Sigma\Sigma^+)U^T$$
    
    The matrix $\Sigma\Sigma^+$ is a simple diagonal matrix with $r$ ones on the diagonal followed by zeros. This projector, $UU^T$ (in its reduced form), uses the basis vectors of the column space (the columns of $U$) to select the component of a vector that lies in that space.
    
- **Projector onto the Row Space $(C(A^T))$:** $$P_{row} = A^+A = (V\Sigma^+ U^T)(U\Sigma V^T) = V(\Sigma^+\Sigma)V^T$$
    
    Similarly, $\Sigma^+\Sigma$ is also a diagonal matrix of $r$ ones followed by zeros. This projector, $VV^T$ (in its reduced form), uses the basis vectors of the row space (the columns of $V$) to find a vector's component in that space.
    

**Connecting the dots**: The SVD provides the ideal bases ($U$ and $V$) for the four subspaces. The pseudoinverse, built from the SVD, allows us to construct the projection matrices that perfectly isolate a vector's components within these fundamental, orthogonal subspaces. This is the heart of Strang's "Big Picture" of linear algebra.



## Projections and the Pseudoinverse

The pseudoinverse ($A^+$) is a generalization of the matrix inverse that provides the best possible solution to $Ax=y$. Crucially, it helps create projection matrices that isolate a vector's components in each of the four fundamental subspaces.

As the diagram shows, the row space and nullspace are orthogonal complements in $\mathbb{R}^n$, while the column space and left nullspace are orthogonal complements in $\mathbb{R}^m$. The pseudoinverse allows us to build the specific projectors onto each of these spaces.

**Projector onto the Row Space, $C(A^T)$:**
$$P_{row} = A^+ A$$
This matrix takes any vector $x \in \mathbb{R}^n$ and finds its component in the row space, $x_r$. It zeros out the nullspace component ($A^+ Ax_n = 0$).

**Projector onto the Column Space, $C(A)$:**
$$P_{col} = AA^+$$
This matrix projects any vector $y \in \mathbb{R}^m$ onto the column space. It zeros out the left nullspace component.

**Projector onto the Nullspace, $N(A)$:**
$$P_{null} = I - A^+ A$$
Since $A^+ A$ perfectly captures the row space component, subtracting this from the identity matrix $I$ gives you what's left over: the orthogonal component, which lies in the nullspace.

**Projector onto the Left Nullspace, $N(A^T)$:**
$$P_{leftnull} = I - AA^+$$
Similarly, this projector finds the component of a vector in $\mathbb{R}^m$ that is orthogonal to the column space.

In short, the products $A^+ A$ and $AA^+$ are the fundamental building blocks for finding the orthogonal projections of any vector onto the four subspaces.


## Summary

The four fundamental subspaces tie together the core concepts of linear algebra, including rank, solutions to linear systems, projections, and the pseudoinverse. They provide the essential geometric language for understanding what a matrix does.