# Structural

1. In 3D, point inversion reverses the orientation of 3-blades. Show that a mirror reflection in a plane through the origin does the same.

Let the mirror plane be spanned by independent vectors $u, v$, with $a$ perpendicular to the plane.

The reflection $r$ keeps in-plane components fixed and flips the normal:

$r[u] = u$, $r[v] = v$, $r[a] = -a$

Apply to the volume element $I = u \wedge v \wedge a$:

$r[I] = r[u] \wedge r[v] \wedge r[a] = u \wedge v \wedge (-a) = -(u \wedge v \wedge a)$

$$r[I] = -I$$

Since the space of 3-blades is 1-dimensional, any 3-blade $A_3 = \alpha I$ transforms as $r[A_3] = -A_3$.

---

2. In 2D with basis $\{b_1, b_2\}$, let $f[b_1] = x = x_1 b_1 + x_2 b_2$ and $f[b_2] = y = y_1 b_1 + y_2 b_2$. Compute $\det(f)$ and verify it matches the classical matrix determinant.

Let $I_2 = b_1 \wedge b_2$. By outermorphism:

$f[I_2] = f[b_1] \wedge f[b_2] = x \wedge y$

$x \wedge y = (x_1 b_1 + x_2 b_2) \wedge (y_1 b_1 + y_2 b_2)$

$= x_1 y_2 (b_1 \wedge b_2) + x_2 y_1 (b_2 \wedge b_1)$

$= (x_1 y_2 - x_2 y_1)(b_1 \wedge b_2)$

The matrix of $f$ has columns as coordinates of images:

$[f] = \begin{pmatrix} x_1 & y_1 \\ x_2 & y_2 \end{pmatrix}$

Classical determinant: $x_1 y_2 - x_2 y_1$

$$\det(f) = x_1 y_2 - x_2 y_1$$

---

3. Why can't you define a determinant on a $k$-dimensional subspace by replacing $I_n$ with $I_k$ in $f[I_n] = \det(f) I_n$?

The formula works for $n$ because $\Lambda^n(\mathbb{R}^n)$ is 1-dimensional—every $n$-blade is proportional to $I_n$.

For $k < n$, the space $\Lambda^k(\mathbb{R}^n)$ has dimension $\binom{n}{k} > 1$. A generic map sends $I_k$ to a $k$-blade not parallel to $I_k$.

Example: A 2D rotation has no real eigenvectors, so $f[u]$ is not proportional to $u$ for any vector $u$.

$$f[I_k] \neq \delta \, I_k \text{ in general}$$

---

4. In the plane $a \wedge b$, a linear map satisfies $f[a] = 5a - 3b$ and $f[b] = 3a - 5b$. Find eigenvectors, eigenvalues, the determinant, and an eigen-2-blade.

Part 1 - Eigenanalysis:

Matrix in basis $\{a, b\}$: $A = \begin{pmatrix} 5 & 3 \\ -3 & -5 \end{pmatrix}$

Characteristic polynomial: $\det(A - \lambda I) = \lambda^2 - 16$

Eigenvalues: $\lambda = 4$ and $\lambda = -4$

Eigenvectors: $v_+ = -3a + b$ (for $\lambda = 4$), $v_- = a - 3b$ (for $\lambda = -4$)

Part 2 - Determinant and eigen-2-blade:

$f[a \wedge b] = f[a] \wedge f[b] = (5a - 3b) \wedge (3a - 5b)$

$= (5 \cdot (-5) - (-3) \cdot 3)(a \wedge b) = -16(a \wedge b)$

$$\det(f) = -16, \quad \text{eigen-2-blade } a \wedge b \text{ with eigenvalue } -16$$

Part 3 - Geometry:

Scaling by 4 in both eigen-directions, combined with a reflection (one negative eigenvalue). Area scales by $4 \times 4 = 16$ with orientation flip.

---

5. Construct a non-identity linear map in 2D with an eigenvector of eigenvalue 1 and an eigen-2-blade of eigenvalue 1.

A shear with $s \neq 0$:

$f[e_1] = e_1$, $f[e_2] = e_2 + s e_1$

$e_1$ is an eigenvector with eigenvalue 1.

$f[e_1 \wedge e_2] = e_1 \wedge (e_2 + s e_1) = e_1 \wedge e_2$

$$e_1 \wedge e_2 \text{ is an eigen-2-blade with eigenvalue 1}$$

---

6. Since $A * B$ is a scalar, $f[A * B] = A * B$. Show this does not imply norms are preserved.

The squared norm after transforming is:

$|f[A]|^2 = f[A] * \widetilde{f[A]}$

This is not the same as $f[A * \tilde{A}]$.

Counterexample: Scaling $S[x] = \alpha x$ with $\alpha \neq \pm 1$:

$|S[a]|^2 = (\alpha a) \cdot (\alpha a) = \alpha^2 (a \cdot a) \neq a \cdot a$

The error: $f[\text{scalar}] = \text{scalar}$ is true, but $f[A] * f[B] = A * B$ is generally false.

---

7. Express $|f[A]|^2$ in the form $A * g[\tilde{A}]$ and find $g$ in terms of $f$.

$|f[A]|^2 = f[A] * \widetilde{f[A]} = f[A] * f[\tilde{A}]$

Using the adjoint identity $f[A] * B = A * \bar{f}[B]$ with $B = f[\tilde{A}]$:

$f[A] * f[\tilde{A}] = A * \bar{f}[f[\tilde{A}]] = A * (\bar{f} \circ f)[\tilde{A}]$

$$g = \bar{f} \circ f$$

In matrix terms: $g = f^T f$.

---

8. Show that for an orthogonal transformation, the metric mapping $g = \bar{f} \circ f$ is the identity.

For orthogonal $f$: $\bar{f} = f^{-1}$

$g = f^{-1} \circ f = \text{id}$

Therefore:

$|f[A]|^2 = A * g[\tilde{A}] = A * \tilde{A} = |A|^2$

$$\text{Norms and angles are preserved.}$$

---

9. In a nondegenerate metric space with basis $\{b_i\}$ and reciprocal basis $\{b^i\}$, write an explicit formula for the adjoint $\bar{f}$.

$$\bar{f}[x] = \sum_{i=1}^n (x \cdot f[b_i]) b^i$$

Verification: For any $x, y$:

$\bar{f}[x] \cdot y = \sum_i (x \cdot f[b_i])(b^i \cdot y)$

Since $y = \sum_i (b^i \cdot y) b_i$:

$x \cdot f[y] = \sum_i (b^i \cdot y)(x \cdot f[b_i])$

These match, confirming $\bar{f}[x] \cdot y = x \cdot f[y]$.

---

10. Prove that if $f$ is orthogonal then $\det(f) = \pm 1$.

For orthogonal $f$, norms are preserved: $|f[I_n]|^2 = |I_n|^2$

But $f[I_n] = \det(f) \, I_n$, so:

$|f[I_n]|^2 = (\det f)^2 (I_n * \tilde{I}_n)$

Setting equal: $(\det f)^2 (I_n * \tilde{I}_n) = I_n * \tilde{I}_n$

Since the metric is nondegenerate, $I_n * \tilde{I}_n \neq 0$:

$$(\det f)^2 = 1 \implies \det f = \pm 1$$

---

11. Give a formula for how the adjoint map acts on a contraction.

The contraction transforms as: $f[A \lrcorner B] = \bar{f}^{-1}[A] \lrcorner f[B]$

Replacing $f$ with $\bar{f}$ and using $\overline{\bar{f}} = f$:

$$\bar{f}[A \lrcorner B] = f^{-1}[A] \lrcorner \bar{f}[B]$$

---

12. Give a linear map $f$ and vectors $a, b$ such that $f[a \times b]$ is not parallel to $f[a] \times f[b]$.

Define a shear in 3D: $f[e_1] = e_1 + e_2$, $f[e_2] = e_2$, $f[e_3] = e_3$

Take $a = e_1$, $b = e_3$:

$a \times b = e_1 \times e_3 = -e_2$

$f[a \times b] = f[-e_2] = -e_2$

$f[a] \times f[b] = (e_1 + e_2) \times e_3 = -e_2 + e_1 = e_1 - e_2$

$$-e_2 \text{ is not parallel to } e_1 - e_2$$

---

13. For the shear $f_s[x] = x + s(x \cdot e_1)e_2$, compute the matrix on vectors and the matrix for the dual map. Verify geometrically.

Matrix on vectors:

$f_s[e_1] = e_1 + s e_2$, $f_s[e_2] = e_2$, $f_s[e_k] = e_k$ for $k \geq 3$

$[[f_s]] = \begin{pmatrix} 1 & 0 \\ s & 1 \end{pmatrix}$

Matrix for dual map ($f^* = \det(f) f^{-T}$ with $\det(f_s) = 1$):

$[[f_s]]^{-1} = \begin{pmatrix} 1 & 0 \\ -s & 1 \end{pmatrix}$, so $[[f_s^*]] = \begin{pmatrix} 1 & -s \\ 0 & 1 \end{pmatrix}$

Geometric check: Line direction $d = e_1$ transforms to $d' = e_1 + s e_2$. Normal $n = e_2$ should transform to stay perpendicular.

$n' = f_s^*[e_2] = -s e_1 + e_2$

$n' \cdot d' = (-s e_1 + e_2) \cdot (e_1 + s e_2) = -s + s = 0$ ✓

Using $f_s[e_2] = e_2$ wrongly gives $e_2 \cdot (e_1 + s e_2) = s \neq 0$.

---

14. Verify that formula (4.18) produces the identity matrix when $f$ is the identity.

Formula (4.18): $[[f]]^j{}_i = (b_1 \wedge \cdots \wedge b_{j-1} \wedge f[b_i] \wedge b_{j+1} \wedge \cdots \wedge b_n) \lrcorner I_n^{-1}$

If $f = \text{id}$, then $f[b_i] = b_i$:

If $i = j$: wedge is $b_1 \wedge \cdots \wedge b_n = I_n$, so $[[f]]^j{}_j = I_n \lrcorner I_n^{-1} = 1$

If $i \neq j$: wedge contains repeated $b_i$ (appears twice, $b_j$ missing), so equals 0

$$[[f]] = I$$

---

15. Show that $A^{-1} = \text{adj}(A)/\det(A)$ matches the coordinate-free inverse formula (4.16).

Formula (4.16) for vectors: $f^{-1}[x] = \dfrac{f[x \lrcorner I_n^{-1}] \lrcorner I_n}{\det(f)}$

Apply to $x = b_j$:

$b_j \lrcorner I_n^{-1}$ is the $(n-1)$-blade from wedging all basis vectors except $b_j$

Applying $f$ wedges together images of all basis vectors except $b_j$

Contracting with $I_n$ extracts cofactors $(-1)^{i+j} \det(A_{ji})$

$f^{-1}[b_j] = \dfrac{1}{\det(A)} \sum_{i=1}^n (-1)^{i+j} \det(A_{ji}) b_i$

$$(A^{-1})^i{}_j = \dfrac{(-1)^{i+j} \det(A_{ji})}{\det(A)} = \dfrac{\text{adj}(A)^i{}_j}{\det(A)}$$

---

16. Give the matrix expression for $f^* = \det(f) \bar{f}^{-1}$ and explain the geometric meaning of the cofactor matrix.

In orthonormal Euclidean basis:

$[[f^*]] = \det(A) \, A^{-T} = \text{adj}(A)^T = \text{cofactor matrix}$

Geometric meaning: The cofactor matrix transforms dual objects (normals, hyperplanes) correctly under the linear map.

---

17. Show the projection $P = B(B^T B)^{-1} B^T$ equals $(x \lrcorner \mathbf{B}) \lrcorner \mathbf{B}^{-1}$ with $\mathbf{B} = b_1 \wedge \cdots \wedge b_k$.

Let $\{b^i\}$ be reciprocal vectors within the subspace, with $G_{ij} = b_i \cdot b_j$.

$P_{\mathbf{B}}[x] = \sum_{i=1}^k (x \cdot b^i) b_i$

The reciprocal vectors satisfy $b^i = \sum_j (G^{-1})^{ij} b_j$, so $x \cdot b^i = \sum_j (G^{-1})^{ij} (x \cdot b_j)$

Let matrix $B$ have columns $b_i$. Then:

$(x \cdot b_j) = B^T x$

Coefficient vector: $c = (B^T B)^{-1} B^T x$

Reconstruction: $Bc = B(B^T B)^{-1} B^T x$

$$P_{\mathbf{B}}[x] = B(B^T B)^{-1} B^T x$$

The outermorphism extension in standard linear algebra is the exterior power—compound matrices built from minors.
