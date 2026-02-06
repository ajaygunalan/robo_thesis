# Drills

Convention: The join $J = A \cup B$ is the unit pseudoscalar of the smallest subspace containing both blades. The meet is $A \cap B = (B \lrcorner J^{-1}) \lrcorner A$.

---

1. Compute $A \cup B$ and $A \cap B$ for $A = e_1$ and $B = e_2$.

The smallest subspace containing both lines is the $e_1 e_2$-plane:

$A \cup B = e_1 \wedge e_2$

With $J = e_1 \wedge e_2$ and $J^{-1} = -J$:

$A \cap B = (e_2 \lrcorner (-e_1 \wedge e_2)) \lrcorner e_1 = e_1 \lrcorner e_1 = 1$

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = 1$$

---

2. Compute $A \cup B$ and $A \cap B$ for $A = e_2$ and $B = e_1$.

Same join as Drill 1:

$A \cup B = e_1 \wedge e_2$

$A \cap B = (e_1 \lrcorner (-e_1 \wedge e_2)) \lrcorner e_2 = (-e_2) \lrcorner e_2 = -1$

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = -1$$

This shows the antisymmetry: swapping order flips the sign.

---

3. Compute $A \cup B$ and $A \cap B$ for $A = e_1$ and $B = 2e_1$.

They span the same line, so choose unit join $J = e_1$:

$A \cup B = e_1$

With $J^{-1} = e_1$:

$A \cap B = ((2e_1) \lrcorner e_1) \lrcorner e_1 = 2 \lrcorner e_1 = 2e_1$

$$A \cup B = e_1, \quad A \cap B = 2e_1$$

Parallel case: meet returns the common line, weighted.

---

4. Compute $A \cup B$ and $A \cap B$ for $A = e_1$ and $B = \dfrac{e_1 + e_2}{\sqrt{2}}$.

They span the $e_1 e_2$-plane:

$A \cup B = e_1 \wedge e_2$

With $J^{-1} = -J$:

$(e_1 + e_2) \lrcorner (e_1 \wedge e_2) = e_2 - e_1$

$B \lrcorner J^{-1} = \dfrac{e_1 - e_2}{\sqrt{2}}$

$A \cap B = \dfrac{e_1 - e_2}{\sqrt{2}} \lrcorner e_1 = \dfrac{1}{\sqrt{2}}$

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = \dfrac{1}{\sqrt{2}}$$

---

5. Compute $A \cup B$ and $A \cap B$ for $A = e_1$ and $B = \cos\theta \, e_1 + \sin\theta \, e_2$.

For $\sin\theta \neq 0$, they span the $e_1 e_2$-plane:

$A \cup B = e_1 \wedge e_2$

$B \lrcorner (e_1 \wedge e_2) = \cos\theta \, e_2 - \sin\theta \, e_1$

$B \lrcorner J^{-1} = \sin\theta \, e_1 - \cos\theta \, e_2$

$A \cap B = (\sin\theta \, e_1 - \cos\theta \, e_2) \lrcorner e_1 = \sin\theta$

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = \sin\theta$$

---

6. Compute $A \cup B$ and $A \cap B$ for $A = e_1 \wedge e_2$ and $B = \cos\theta \, e_1 + \sin\theta \, e_2$.

$B$ lies in the plane $A$, so:

$A \cup B = e_1 \wedge e_2$

The intersection of a plane with a line inside it is the line itself:

$B \lrcorner J^{-1} = \sin\theta \, e_1 - \cos\theta \, e_2$ (from Drill 5)

$A \cap B = (\sin\theta \, e_1 - \cos\theta \, e_2) \lrcorner (e_1 \wedge e_2) = \cos\theta \, e_1 + \sin\theta \, e_2 = B$

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = \cos\theta \, e_1 + \sin\theta \, e_2$$

---

7. Compute $A \cup B$ and $A \cap B$ for $A = e_1 \wedge e_2$ and $B = e_2$.

$B$ lies in the plane $A$:

$A \cup B = e_1 \wedge e_2$

Intersection of plane with line inside is the line:

$$A \cup B = e_1 \wedge e_2, \quad A \cap B = e_2$$

---

8. Compute $A \cup B$ and $A \cap B$ for $A = e_1 \wedge e_2$ and $B = e_2 + 0.00001 \, e_3$.

$B$ has an $e_3$ component, so the smallest containing subspace is full 3D:

$A \cup B = e_1 \wedge e_2 \wedge e_3 = I_3$

The meet is a scalar measuring how much the line pierces the plane. With $J = I_3$ and $J^{-1} = -I_3$:

$A^* = A \lrcorner J^{-1} = (e_1 \wedge e_2) \lrcorner (-I_3) = e_3$

$A \cap B = e_3 \cdot (e_2 + 10^{-5} e_3) = 10^{-5}$

$$A \cup B = e_1 \wedge e_2 \wedge e_3, \quad A \cap B = 0.00001$$

---

# Structural

1. Verify $(B \lrcorner J^{-1}) * (A \llcorner M^{-1}) = 1$ and prove $(M^{-1} \lrcorner B) * (J^{-1} \llcorner A) = 1$.

Part (a): Start from $M^{-1} * M = 1$ with $M = (B \lrcorner J^{-1}) \lrcorner A$:

$M^{-1} * ((B \lrcorner J^{-1}) \lrcorner A)$

Using $X * (Y \lrcorner Z) = (X \wedge Y) * Z$:

$= (M^{-1} \wedge (B \lrcorner J^{-1})) * A$

Using $(X \wedge Y) * Z = Y * (Z \llcorner X)$:

$= (B \lrcorner J^{-1}) * (A \llcorner M^{-1}) = 1$

Part (b): Start from $J^{-1} * J = 1$ with $J = A \wedge (M^{-1} \lrcorner B)$:

$J^{-1} * (A \wedge (M^{-1} \lrcorner B))$

Using $X * (Y \wedge Z) = (X \llcorner Y) * Z$:

$= (J^{-1} \llcorner A) * (M^{-1} \lrcorner B) = 1$

$$(M^{-1} \lrcorner B) * (J^{-1} \llcorner A) = 1$$

---

2. Find the error in this proof fragment: "From $J^{-1} * J = 1$, we get $f[J^{-1} * J] = f^{-1}[J^{-1}] * f[J]$, so $f^{-1}[J^{-1}] = f[J]^{-1}$."

The error is treating the scalar product $*$ as if it transforms nicely under an arbitrary linear map $f$.

The scalar product depends on the metric. A general linear transformation is not metric-preserving unless orthogonal. You cannot push $f$ through a scalar product.

$$\text{The wedge is outermorphic; the scalar product is not.}$$

---

3. Compute meet and join of two vectors $a$ and $b$ in general position. Show $|a \cap b|$ equals the sine of their angle (times norms).

Assume $a \wedge b \neq 0$. The join is the unit bivector of their plane:

$a \cup b = J = \dfrac{a \wedge b}{|a \wedge b|}$

Two distinct lines through the origin meet at the origin, so the meet is a scalar.

Since $J$ is unit, $J^{-1} = -J$. Contracting $a \wedge b = |a \wedge b| J$ with $J^{-1}$:

$(a \wedge b) \lrcorner J^{-1} = |a \wedge b|$

This scalar is exactly the meet:

$a \cap b = |a \wedge b| = |a| |b| \sin\theta$

For unit vectors: $|a \cap b| = |\sin\theta|$

Sign/order: $b \wedge a = -(a \wedge b)$ implies $b \cap a = -(a \cap b)$

$$a \cap b = |a||b|\sin\theta, \quad b \cap a = -(a \cap b)$$

---

4. Compute meet and join of two parallel vectors $u$ and $v = \alpha u$. Show the meet is symmetric.

Since $u \wedge v = 0$, the join is the common line:

$u \cup v = J = u$

With $J^{-1} = u/u^2$:

$v \lrcorner u^{-1} = v \cdot \dfrac{u}{u^2} = \dfrac{\alpha u^2}{u^2} = \alpha$

$u \cap v = \alpha \lrcorner u = \alpha u = v$

Swapping: $v \cap u = (u \lrcorner u^{-1}) \lrcorner v = 1 \lrcorner v = v$

$$u \cup v = u, \quad u \cap v = v = v \cap u$$

---

5. Consider the meet of $a \wedge B$ and $a \wedge C$, where $a$ is a vector and $B, C$ have no common factor. Show the meet is proportional to $a$.

The common factor is $a$, so the meet must be $a$ times a scalar.

With join proportional to $a \wedge B \wedge C$:

$$(a \wedge B) \cap (a \wedge C) = a \cdot (a \wedge B \wedge C)^*$$

---

6. Verify the computation $(a \wedge B) \cap (a \wedge C) = a \wedge (a \wedge B \wedge C)^*$.

Let $J$ be the normalized join, with dual $X^* = X \lrcorner J^{-1}$.

Step 1 (dual meet identity):

$(a \wedge B) \cap (a \wedge C) = ((a \wedge C)^* \wedge (a \wedge B)^*)^{-*}$

Step 2 (duality swaps wedge and contraction):

$(a \wedge C)^* = a \lrcorner C^*$, $(a \wedge B)^* = a \lrcorner B^*$

Step 3 (graded derivation rule):

$(a \lrcorner C^*) \wedge (a \lrcorner B^*) = a \lrcorner (C^* \wedge (a \lrcorner B^*))$

The second term vanishes because $a \lrcorner (a \lrcorner (\cdot)) = 0$.

Step 4-5: Replace $a \lrcorner B^*$ by $(a \wedge B)^*$; undualizing turns contraction into wedge.

Step 6-8: For equal grades, contraction equals scalar product, which is symmetric.

Step 9: $(a \wedge B) \lrcorner C^* = (a \wedge B \wedge C)^*$

$$(a \wedge B) \cap (a \wedge C) = a \wedge (a \wedge B \wedge C)^*$$

Since $(a \wedge B \wedge C)^*$ is a scalar, this equals $a \cdot (a \wedge B \wedge C)^*$.

---

7. Derive the general factorization $(A \wedge B) \cap (A \wedge C) = A \cdot (A \wedge B \wedge C)^*$ where $A, B, C$ have no common factors.

The derivation in Structural 6 depends only on:

- the dual meet identity
- duality swapping wedge and contraction
- $A$ being the common factor

Repeating with $a$ replaced by general blade $A$:

$$(A \wedge B) \cap (A \wedge C) = A \cdot (A \wedge B \wedge C)^*$$

This is equation (5.11).
