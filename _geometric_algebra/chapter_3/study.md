# Study Session: Chapter 3 - Metric Products of Subspaces


1. The contraction $A \lrcorner B$ is defined implicitly via $(X \wedge A) * B = X * (A \lrcorner B)$. Why does this make contraction the "adjoint" of the outer product under the scalar product?


- [ ]  Because the outer product and contraction have the same grade formula: $\text{grade}(A \wedge B) = \text{grade}(A \lrcorner B)$
- [ ] Because contraction undoes the grade-raising of $\wedge$: moving $A$ from the left of $*$ to inside the right argument via $\lrcorner$ preserves the scalar product value
- [ ] Because both operations are associative and commutative under the scalar product
- [ ] Because the scalar product is symmetric, so $(X \wedge A) * B = B * (A \lrcorner X)$

Hint: [[<filename>]]

---

## Question 2 (What-if)
Consider a 2-blade $A = e_1 \wedge e_2$ and a 3-blade $B = e_1 \wedge e_2 \wedge e_3$ in Euclidean $\mathbb{R}^3$. The contraction $A \lrcorner B = e_3$. What happens if you swap the order and compute $B \lrcorner A$?

**Options:**
A) $B \lrcorner A = e_3$ as well, since contraction is symmetric

B) $B \lrcorner A = -e_3$ due to the sign rule for swapping contraction order

C) $B \lrcorner A = 0$ because the grade of $B$ exceeds the grade of $A$

D) $B \lrcorner A = e_1 \wedge e_2$ because contraction removes the lower-grade blade

---

## Question 3 (Compare)
When would you use the scalar product $A * B$ versus the contraction $A \lrcorner B$ for two blades of equal grade?

**Options:**
A) Use scalar product for computing angles; use contraction for projections—they give different results

B) Use scalar product when you need a scalar (norm, angle); contraction gives the same scalar but with different sign conventions

C) They're identical for same-grade blades: $A \lrcorner B = A * B$, so the choice is purely notational

D) Use scalar product for orthonormal bases only; contraction works for arbitrary bases

---

## Question 4 (Debug)
A student computes the dual of $A = e_1 \wedge e_2$ in $\mathbb{R}^3$ as $A^* = A \lrcorner I_3 = (e_1 \wedge e_2) \lrcorner (e_1 \wedge e_2 \wedge e_3)$, getting $e_3$. They then compute $(A^*)^* = e_3 \lrcorner I_3$ expecting to recover $A$, but get $e_1 \wedge e_2$. They claim duality is an involution. What's wrong?

**Options:**
A) Nothing is wrong—duality is indeed an involution in $\mathbb{R}^3$

B) The formula should be $A^* = A \wedge I_3^{-1}$, not $A \lrcorner I_3$

C) Double dualization includes a dimension-dependent sign: $(A^*)^* = (-1)^{n(n-1)/2} A$, so in $\mathbb{R}^3$ it gives $-A$, but the student missed the sign

D) The student used $I_3$ instead of $I_3^{-1}$ in the second dualization

---

## Question 5 (Derive)
Starting from the projection formula $P_B[X] = (X \lrcorner B) \lrcorner B^{-1}$, explain why this produces a blade of the same grade as $X$ that lies in $B$.

**Options:**
A) $X \lrcorner B$ has grade $\text{grade}(B) - \text{grade}(X)$; contracting with $B^{-1}$ (same grade as $B$) reduces by $\text{grade}(B)$ again, giving grade $-\text{grade}(X)$, which wraps to $\text{grade}(X)$

B) Both contractions reduce grade by $\text{grade}(X)$ each, so the total is grade $0$—the projection is always a scalar

C) First contraction gives grade $(\text{grade}(B) - \text{grade}(X))$; second contraction with $B^{-1}$ (grade same as $B$) gives $\text{grade}(B) - (\text{grade}(B) - \text{grade}(X)) = \text{grade}(X)$. The result lies in $B$ because both contractions produce subblades of $B$.

D) The grade is preserved because $B^{-1}$ acts as an identity on subblades of $B$

---

## Question 6 (What-if)
In a space with signature $(2,1)$ (two positive, one negative basis vector), you have a blade $A = e_1 \wedge e_3$ where $e_1 \cdot e_1 = 1$ and $e_3 \cdot e_3 = -1$. What is $\|A\|^2 = A * \tilde{A}$, and what does this imply?

**Options:**
A) $\|A\|^2 = 2$; the blade has positive norm

B) $\|A\|^2 = 0$; the blade is null and has no inverse

C) $\|A\|^2 = -1$; the blade has negative squared norm but still has an inverse

D) $\|A\|^2 = 1$; mixed-signature blades always have unit norm

---

## Question 7 (Compare)
The cross product $a \times b$ and the dual of the wedge $(a \wedge b)^*$ both give vectors in $\mathbb{R}^3$. Why is the wedge-then-dual formulation preferred in geometric algebra?

**Options:**
A) The cross product is faster to compute and gives the same result

B) The wedge product $(a \wedge b)$ captures the plane spanned by $a$ and $b$ independent of dimension and metric; dualization to get a normal is a separate, explicit step. The cross product conflates these, hiding metric dependence.

C) The cross product only works for orthonormal bases, while the wedge works for any basis

D) The wedge product automatically normalizes the result, while the cross product doesn't

---

## Question 8 (Why)
The duality transformation satisfies $(A \wedge B)^* = A \lrcorner B^*$ and $(A \lrcorner B)^* = A \wedge B^*$. Why does duality "swap" the outer product and contraction?

**Options:**
A) Because $\wedge$ and $\lrcorner$ are inverse operations, and duality is just relabeling

B) The outer product adds dimensions to a subspace; contraction removes them. Duality maps a $k$-blade to an $(n-k)$-blade, so adding dimensions in the original space corresponds to removing dimensions in the complement, and vice versa.

C) This is a special case that only holds in Euclidean spaces where $I_n^{-1} = \tilde{I}_n$

D) Because the scalar product is bilinear and duality is defined via contraction with $I_n^{-1}$

