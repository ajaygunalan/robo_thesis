# Drills

1. Given $a = e_1 + e_2$, $b = e_2 + e_3$ in $\mathbb{R}^{3,0}$ with orthonormal basis $\{e_1, e_2, e_3\}$. Compute each expression in the standard basis.

Preliminary: $a \wedge b = (e_1 + e_2) \wedge (e_2 + e_3) = e_1 \wedge e_2 + e_1 \wedge e_3 + e_2 \wedge e_3$

---

(a) Compute $e_1 \lrcorner a$

For vectors, contraction reduces to the dot product:

$e_1 \lrcorner a = e_1 \cdot (e_1 + e_2) = 1 + 0 =1$

---

(b) Compute $e_1 \lrcorner (a \wedge b)$

Apply the vector-on-bivector formula $x \lrcorner (u \wedge v) = (x \cdot u)v - (x \cdot v)u$ to each term:

$e_1 \lrcorner (e_1 \wedge e_2) = (1)e_2 - (0)e_1 = e_2$

$e_1 \lrcorner (e_1 \wedge e_3) = (1)e_3 - (0)e_1 = e_3$

$e_1 \lrcorner (e_2 \wedge e_3) = 0$ since $e_1$ is orthogonal to both $e_2$ and $e_3$

$$e_1 \lrcorner (a \wedge b) = e_2 + e_3$$

---

(c) Compute $(a \wedge b) \lrcorner e_1$

The left contraction $A \lrcorner B$ is zero when $\text{grade}(A) > \text{grade}(B)$:

$\text{grade}(a \wedge b) = 2 > \text{grade}(e_1) = 1$

$$(a \wedge b) \lrcorner e_1 = 0$$

---

(d) Compute $(2a + b) \lrcorner (a + b)$

Both arguments are vectors, so this is just a dot product:

$2a + b = 2e_1 + 3e_2 + e_3$

$a + b = e_1 + 2e_2 + e_3$

$(2a + b) \cdot (a + b) = 2(1) + 3(2) + 1(1)$

$$= 9$$

---

(e) Compute $a \lrcorner (e_1 \wedge e_2 \wedge e_3)$

Use the vector-on-trivector expansion:

$x \lrcorner (e_1 \wedge e_2 \wedge e_3) = (x \cdot e_1)(e_2 \wedge e_3) - (x \cdot e_2)(e_1 \wedge e_3) + (x \cdot e_3)(e_1 \wedge e_2)$

For $a = e_1 + e_2$: $a \cdot e_1 = 1$, $a \cdot e_2 = 1$, $a \cdot e_3 = 0$

$a \lrcorner I_3 = 1(e_2 \wedge e_3) - 1(e_1 \wedge e_3) + 0$

Converting $-e_1 \wedge e_3 = e_3 \wedge e_1$ to match the standard basis:

$$a \lrcorner I_3 = (e_2 \wedge e_3) + (e_3 \wedge e_1)$$

---

(f) Compute $a^*$

The dual in 3D is $a^* = a \lrcorner I_3^{-1}$ where $I_3^{-1} = -I_3$:

$a^* = a \lrcorner (-I_3) = -(a \lrcorner I_3)$

Using the result from part (e):

$$a^* = -(e_2 \wedge e_3) - (e_3 \wedge e_1)$$

---

(g) Compute $(a \wedge b)^*$

The duals of the basis bivectors in right-handed 3D are:

$(e_1 \wedge e_2)^* = e_3$, $(e_2 \wedge e_3)^* = e_1$, $(e_3 \wedge e_1)^* = e_2$

Since $a \wedge b = (e_1 \wedge e_2) + (e_2 \wedge e_3) - (e_3 \wedge e_1)$:

$$(a \wedge b)^* = e_3 + e_1 - e_2 = e_1 - e_2 + e_3$$

---

(h) Compute $a \lrcorner b^*$

First find $b^*$ using the same method as part (f). For $b = e_2 + e_3$:

$b \lrcorner I_3 = 0(e_2 \wedge e_3) - 1(e_1 \wedge e_3) + 1(e_1 \wedge e_2) = (e_1 \wedge e_2) + (e_3 \wedge e_1)$

$b^* = -b \lrcorner I_3 = -(e_1 \wedge e_2) - (e_3 \wedge e_1) = -e_1 \wedge e_2 + e_1 \wedge e_3$

Now contract $a = e_1 + e_2$ onto $b^*$:

$a \lrcorner (-e_1 \wedge e_2) = -[(a \cdot e_1)e_2 - (a \cdot e_2)e_1] = -[e_2 - e_1] = e_1 - e_2$

$a \lrcorner (e_1 \wedge e_3) = (a \cdot e_1)e_3 - (a \cdot e_3)e_1 = e_3$

$$a \lrcorner b^* = e_1 - e_2 + e_3$$

---

2. Compute the cosine of the angle between these subspaces using $\cos\theta = \dfrac{A * \tilde{B}}{|A||B|}$.

---

(a) Between $e_1$ and $\alpha e_1$

For vectors this is the familiar formula:

$\cos\theta = \dfrac{e_1 \cdot (\alpha e_1)}{|e_1||\alpha e_1|} = \dfrac{\alpha}{1 \cdot |\alpha|}$

$$\cos\theta = \text{sgn}(\alpha)$$

---

(b) Between $(e_1 + e_2) \wedge e_3$ and $e_1 \wedge e_3$

Let $A = e_1 \wedge e_3 + e_2 \wedge e_3$ and $B = e_1 \wedge e_3$, so $\tilde{B} = e_3 \wedge e_1$.

Only the $e_1 \wedge e_3$ component of $A$ contributes to the scalar product:

$A * \tilde{B} = (e_1 \wedge e_3) * (e_3 \wedge e_1) = 1$

$|A| = \sqrt{1 + 1} = \sqrt{2}$, $|B| = 1$

$$\cos\theta = \dfrac{1}{\sqrt{2}}$$

---

(c) Between $(\cos\varphi \, e_1 + \sin\varphi \, e_2) \wedge e_3$ and $e_2 \wedge e_3$

Let $A = \cos\varphi(e_1 \wedge e_3) + \sin\varphi(e_2 \wedge e_3)$ and $B = e_2 \wedge e_3$.

Only the $e_2 \wedge e_3$ part of $A$ survives in the scalar product:

$A * \tilde{B} = \sin\varphi \cdot (e_2 \wedge e_3) * (e_3 \wedge e_2) = \sin\varphi$

Both blades are unit: $|A| = \sqrt{\cos^2\varphi + \sin^2\varphi} = 1$, $|B| = 1$

$$\cos\theta = \sin\varphi$$

---

(d) Between $e_1 \wedge e_2$ and $e_3 \wedge e_4$

The two planes share no common directions—all cross dot products vanish.

$$\cos\theta = 0$$

---

3. In 2D Euclidean space with orthonormal basis $\{e_1, e_2\}$, let $b_1 = e_1$ and $b_2 = e_1 + e_2$. Construct the reciprocal frame $\{b^1, b^2\}$ and find the coordinates of $x = 3e_1 + e_2$.

The pseudoscalar for the frame:

$I_2 = b_1 \wedge b_2 = e_1 \wedge (e_1 + e_2) = e_1 \wedge e_2$

$I_2^{-1} = \tilde{I_2} = e_2 \wedge e_1$

Using formula $b^i = (-1)^{i-1}(b_1 \wedge \cdots \wedge \widehat{b_i} \wedge \cdots \wedge b_n) \lrcorner I_n^{-1}$:

$b^1 = b_2 \lrcorner I_2^{-1} = (e_1 + e_2) \lrcorner (e_2 \wedge e_1) = (1)e_1 - (1)e_2 = e_1 - e_2$

$b^2 = -b_1 \lrcorner I_2^{-1} = -e_1 \lrcorner (e_2 \wedge e_1) = -(-e_2) = e_2$

The coordinates are $x^i = x \cdot b^i$:

$x^1 = (3e_1 + e_2) \cdot (e_1 - e_2) = 3 - 1 = 2$

$x^2 = (3e_1 + e_2) \cdot e_2 = 1$

$$x = 2b_1 + b_2$$

---

# Structural

1. In $\mathbb{R}^{2,0}$ with orthonormal $\{e_1, e_2\}$, determine $e_1 \lrcorner (e_1 \wedge e_2)$ using the implicit definition (3.6), letting $X$ range over $\{1, e_1, e_2, e_1 \wedge e_2\}$.

The implicit definition says $(X \wedge A) * B = X * (A \lrcorner B)$. Write the unknown as:

$R = e_1 \lrcorner (e_1 \wedge e_2) = \alpha + \beta e_1 + \gamma e_2 + \delta(e_1 \wedge e_2)$

Each choice of $X$ determines one coefficient:

$X = 1$: LHS $= e_1 * (e_1 \wedge e_2) = 0$ (grade mismatch), so $\alpha = 0$

$X = e_1$: LHS $= (e_1 \wedge e_1) * (e_1 \wedge e_2) = 0$, so $\beta = 0$

$X = e_2$: LHS $= (e_2 \wedge e_1) * (e_1 \wedge e_2) = \det\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = 1$, so $\gamma = 1$

$X = e_1 \wedge e_2$: LHS $= 0$ since $(e_1 \wedge e_2) \wedge e_1 = 0$, giving $-\delta = 0$

$$e_1 \lrcorner (e_1 \wedge e_2) = e_2$$

---

2. Change the metric so that $e_2 \cdot e_2 = 0$ (making $e_2$ a null vector). Show the implicit method fails to determine the $e_2$-coefficient, but the explicit definition still works.

Why implicit fails for $X = e_2$:

$(e_2 \wedge e_1) * (e_1 \wedge e_2) = \det\begin{pmatrix} e_2 \cdot e_2 & e_2 \cdot e_1 \\ e_1 \cdot e_2 & e_1 \cdot e_1 \end{pmatrix} = \det\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = 0$

Meanwhile $e_2 * R = \gamma(e_2 \cdot e_2) = 0$ for any value of $\gamma$. The equation $0 = 0$ is satisfied regardless of $\gamma$.

The explicit definition still works using (3.10):

$e_1 \lrcorner (e_1 \wedge e_2) = (e_1 \cdot e_1)e_2 - (e_1 \cdot e_2)e_1 = 1 \cdot e_2 - 0$

$$e_1 \lrcorner (e_1 \wedge e_2) = e_2$$

---

3. Derive the right-contraction dualities corresponding to (3.20) and (3.21), and give the counterpart of (3.24).

The right contraction relates to left contraction by $B \llcorner A = (\tilde{A} \lrcorner \tilde{B})^{\sim}$.

(i) Universal identity: Starting from $((\tilde{A} \wedge \tilde{B}) \lrcorner \tilde{C})^{\sim}$ and applying (3.20):

$$C \llcorner (B \wedge A) = (C \llcorner B) \llcorner A$$

(ii) Conditional identity (when $A \subseteq C$): Using (3.21):

$$C \llcorner (B \llcorner A) = (C \llcorner B) \wedge A$$

(iii) Counterpart of $(A \wedge B)^* = A \lrcorner (B^*)$:

$$(A \wedge B)^* = (A^*) \llcorner B$$

---

4. Interpret the inner product $x \cdot a$ geometrically as a contraction.

For vectors, $x \lrcorner a = x \cdot a$ has grade $1 - 1 = 0$, producing a scalar.

A scalar (0-blade) is trivially contained in any blade and has no direction, so it can be considered perpendicular to everything. The contraction extracts the 0-dimensional "overlap" of $a$ with $x$.

---

5. Explain why $x \lrcorner \alpha = 0$ for a vector $x$ and scalar $\alpha$.

$\text{grade}(x \lrcorner \alpha) = \text{grade}(\alpha) - \text{grade}(x) = 0 - 1 = -1$

Negative grade blades do not exist. There is no subspace of a point that you can extract by removing a direction.

$$x \lrcorner \alpha = 0$$

---

6. Justify the identity $\alpha \lrcorner B = \alpha B$ geometrically.

$\text{grade}(\alpha \lrcorner B) = \text{grade}(B) - 0 = \text{grade}(B)$

Contracting by a scalar (a 0-dimensional object) removes nothing from $B$. It simply scales the weight.

$$\alpha \lrcorner B = \alpha B$$

---

7. Show explicitly that in 1D Euclidean space, double duality introduces no minus sign.

In 1D with basis $\{e_1\}$: $I_1 = e_1$ and $I_1^{-1} = e_1$ (since $e_1 \cdot e_1 = 1$).

Let $a = \alpha e_1$. First dual:

$a^* = (\alpha e_1) \lrcorner e_1 = \alpha(e_1 \cdot e_1) = \alpha$

Second dual:

$(a^*)^* = \alpha \lrcorner e_1 = \alpha e_1 = a$

$$(a^*)^* = a$$

---

8. Express $\det([[abc]])$ purely in terms of the subspace algebra, given $a \wedge b \wedge c = \det([[abc]]) \, I_3$.

Contract both sides with $I_3^{-1}$:

$(a \wedge b \wedge c) \lrcorner I_3^{-1} = \det([[abc]]) \cdot (I_3 \lrcorner I_3^{-1}) = \det([[abc]]) \cdot 1$

$$\det([[abc]]) = (a \wedge b \wedge c) \lrcorner I_3^{-1}$$

---

9. In a plane with unit pseudoscalar $I_2$, give a coordinate-free formula for rotating a vector $x$ by angle $\theta$.

Since $x \lrcorner I_2$ is perpendicular to $x$ within the plane (rotated by $\pi/2$ in the orientation of $I_2$), the pair $\{x, x \lrcorner I_2\}$ forms an orthogonal basis.

$$R_{I_2,\theta}(x) = x\cos\theta + (x \lrcorner I_2)\sin\theta$$

---

10. Using $a \times b = (a \wedge b)^*$, verify that $a \cdot (b \times c)$ gives the volume spanned by $a, b, c$. What is the formula using $\wedge$ and $\lrcorner$?

From the cross product definition: $b \times c = (b \wedge c) \lrcorner I_3^{-1}$

$a \cdot (b \times c) = a \lrcorner ((b \wedge c) \lrcorner I_3^{-1})$

Using associativity $(A \wedge B) \lrcorner C = A \lrcorner (B \lrcorner C)$ in reverse:

$$a \cdot (b \times c) = (a \wedge b \wedge c) \lrcorner I_3^{-1}$$

---

11. Derive the bac-cab identity $a \times (b \times c) = b(a \cdot c) - c(a \cdot b)$ from the cross product definition. Give the corresponding $\wedge, \lrcorner$ formula.

Since $b \times c = (b \wedge c)^*$ and double duality in 3D gives $(b \wedge c)^{**} = -(b \wedge c)$:

$(b \times c)^* = -(b \wedge c)$

So $a \times (b \times c) = a \lrcorner (-(b \wedge c)) = -a \lrcorner (b \wedge c)$

Applying (3.17): $a \lrcorner (b \wedge c) = (a \cdot b)c - (a \cdot c)b$

$$a \times (b \times c) = -[(a \cdot b)c - (a \cdot c)b] = b(a \cdot c) - c(a \cdot b)$$

---

12. Derive $(a \times b) \cdot (c \times d) = (a \cdot c)(b \cdot d) - (a \cdot d)(b \cdot c)$ from the cross product definition.

$(a \times b) \cdot (c \times d) = (a \wedge b)^* \cdot (c \wedge d)^*$

In 3D, the dot product of dual vectors equals the scalar product of the original bivectors:

$= (a \wedge b) * \widetilde{(c \wedge d)} = (a \wedge b) * (d \wedge c)$

This is the $2 \times 2$ determinant of dot products:

$$= \det\begin{pmatrix} a \cdot c & a \cdot d \\ b \cdot c & b \cdot d \end{pmatrix} = (a \cdot c)(b \cdot d) - (a \cdot d)(b \cdot c)$$

---

13. In a nonorthonormal basis $\{b_i\}$ with reciprocal basis $\{b^i\}$, show that $\sum_i b_i \wedge b^i = 0$.

Expand reciprocal vectors: $b^i = \sum_j g^{ij} b_j$ where $g^{ij}$ are entries of the inverse Gram matrix.

Since $G$ is symmetric, $g^{ij} = g^{ji}$.

$\sum_i b_i \wedge b^i = \sum_i b_i \wedge \left(\sum_j g^{ij} b_j\right) = \sum_{i,j} g^{ij} (b_i \wedge b_j)$

Pair up terms $(i,j)$ and $(j,i)$:

$g^{ij}(b_i \wedge b_j) + g^{ji}(b_j \wedge b_i) = g^{ij}(b_i \wedge b_j) + g^{ij}(-b_i \wedge b_j) = 0$

$$\sum_i b_i \wedge b^i = 0$$
