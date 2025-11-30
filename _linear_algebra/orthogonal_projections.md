# Orthogonal Projections • Column Space • Row Space • Null Space

### What is an orthogonal projection?

Given a subspace $W$ and a vector $b$, the orthogonal projection of $b$ onto $W$ is the unique point $p\in W$ closest to $b$. Equivalently, the residual $r=b-p$ is orthogonal to every vector in $W$, and the (linear) projector $P$ that sends $b\mapsto p$ is idempotent: $P^2=P$.

---

### Projecting onto a column space

Think of the columns of $A$ as building blocks. Every point in $\mathrm{Col}(A)$ is a linear combination $Ax$. To project a vector $b$ in $\mathbb{R}^m$ onto $\mathrm{Col}(A)$, we look for the combination $A\hat x$ closest to $b$. That is exactly the least-squares problem

$$ \min_x |Ax-b|_2^2, $$

whose first-order optimality condition gives the normal equations

$$ A^\top (A\hat x - b) = 0 \quad\Longleftrightarrow\quad (A^\top A)\hat x = A^\top b. $$

When $A^\top A$ is invertible,

$$ \hat x = (A^\top A)^{-1}A^\top b, \qquad \boxed{P_{\mathrm{col}(A)}=A(A^\top A)^{-1}A^\top}, \qquad \Pi_{\mathrm{col}(A)}(b)=A(A^\top A)^{-1}A^\top b. $$

If the columns of $A$ are orthonormal ($A^\top A=I$), the projector simplifies cleanly to $\boxed{P_{\mathrm{col}(A)}=AA^\top}$. The least-squares and projection viewpoints are the same thing here: $A\hat x$ is the nearest point to $b$ in the span of the columns.

**Tiny example (column space).** Let $A=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix}$. Its columns are orthonormal, so $P_{\mathrm{col}(A)}=AA^\top=\mathrm{diag}(1,1,0)$. Projecting $b=(1,2,3)$ onto $\mathrm{Col}(A)$ (the $xy$-plane in $\mathbb{R}^3$) gives $(1,2,0)$.

---

### Projecting onto a row space

The row space of a matrix $M\in\mathbb{R}^{m\times n}$ is the column space of $M^\top$: $\mathrm{Row}(M)=\mathrm{Col}(M^\top)$. So we can reuse the column-space formula with $A=M^\top$:

$$ \boxed{P_{\mathrm{row}(M)}=M^\top (MM^\top)^{-1} M}, \qquad \Pi_{\mathrm{row}(M)}(x)=M^\top(MM^\top)^{-1}Mx. $$

This operator extracts the component of $x\in\mathbb{R}^n$ that is "visible" to the rows of $M$, i.e., the part that can be reconstructed from linear combinations of the rows.

---

### Projecting onto a null space

The null space $S=\mathrm{Null}(M)={x: Mx=0}$ sits orthogonally to $\mathrm{Row}(M)$. To project a vector $x\in\mathbb{R}^n$ onto $S$, write $x$ as

$$ x = \underbrace{(x - M^\top u)}_{\in S};+;\underbrace{M^\top u}_{\in \mathrm{Row}(M)} $$

and choose $u$ so that the first term truly lands in $S$. Enforcing the constraint,

$$ M(x - M^\top u)=0 ;\Longrightarrow; Mx - MM^\top u = 0 ;\Longrightarrow; (MM^\top)u=Mx ;\Longrightarrow; u=(MM^\top)^{-1}Mx. $$

Therefore

$$ \boxed{P_{\mathrm{null}(M)}=I - M^\top(MM^\top)^{-1}M}, \qquad \Pi_{\mathrm{null}(M)}(x)=\bigl(I - M^\top(MM^\top)^{-1}M\bigr)x. $$

Geometrically, you "slide" $x$ along $\mathrm{Row}(M)$ (the $M^\top u$ direction) until you hit the vertical line representing $\mathrm{Null}(M)$; the drop is orthogonal to $\mathrm{Row}(M)$.

Because $\mathbb{R}^n$ decomposes into an orthogonal direct sum $\mathrm{Row}(M)\oplus \mathrm{Null}(M)$, the two projectors are complementary:

$$ P_{\mathrm{null}(M)}=I-P_{\mathrm{row}(M)}. $$

Expanding the right-hand side with the row-space formula reproduces the boxed expression above.

**Tiny example (row/null as complements).** Take $M=\begin{bmatrix}1&1\end{bmatrix}$. Then $MM^\top=[2]$ and

$$ P_{\mathrm{row}(M)}=M^\top(MM^\top)^{-1}M =\tfrac{1}{2}\begin{bmatrix}1\\1\end{bmatrix}\begin{bmatrix}1&1\end{bmatrix} =\tfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix}, \quad P_{\mathrm{null}(M)}=I-P_{\mathrm{row}(M)} =\tfrac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix}. $$

Projecting $x=(3,1)$ onto $\mathrm{Null}(M)={(t,-t)}$ gives $\tfrac{1}{2}(2,-2)=(1,-1)$; onto $\mathrm{Row}(M)=\mathrm{span}{(1,1)}$ gives $\tfrac{1}{2}(4,4)=(2,2)$. The two pieces add back to $x$.

---

### At a glance (formulas you'll actually use)

- Onto a column space:
    
    $$ P_{\mathrm{col}(A)}=A(A^\top A)^{-1}A^\top,\quad \text{and if columns are orthonormal, }P_{\mathrm{col}(A)}=AA^\top. $$
    
- Onto a row space:
    
    $$ P_{\mathrm{row}(M)}=M^\top(MM^\top)^{-1}M. $$
    
    (Directly from the column-space formula with $A=M^\top$.)
    
- Onto a null space:
    
    $$ P_{\mathrm{null}(M)}=I-M^\top(MM^\top)^{-1}M, $$
    
    derived by enforcing $M(x-M^\top u)=0$.
    

---

### Final orientation

The column-space projection is "best approximation by your building blocks." The row-space projection is "what the measurements (rows) can see." The null-space projection is "what the measurements can't see." All three are the same geometric idea viewed through different faces of a matrix; the algebraic formulas above are the cleanest way to compute them.



### 



[[orthogonal_projections]] onto Nullspace

Consider some matrix M, with nullspace S. The matrix for the orthogonal projection onto S is:

$$\boxed{P = I - M^T(MM^T)^{-1}M}$$

**Why?**

## Diagram


<svg width="300" height="250" xmlns="http://www.w3.org/2000/svg">
  <!-- Grid lines for reference -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" 
            refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333" />
    </marker>
  </defs>
  
  <!-- Origin point -->
  <circle cx="50" cy="200" r="3" fill="#333"/>
  
  <!-- Vector x -->
  <line x1="50" y1="200" x2="200" y2="100" 
        stroke="#ff4444" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="130" y="140" font-size="16" font-weight="bold" fill="#ff4444">x</text>
  
  <!-- Projection onto col(M^T) -->
  <line x1="50" y1="200" x2="200" y2="200" 
        stroke="#4444ff" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="120" y="220" font-size="14" fill="#4444ff">y = M^T u</text>
  <text x="100" y="190" font-size="12" fill="#666">col(M^T)</text>
  
  <!-- Orthogonal component in S -->
  <line x1="200" y1="200" x2="200" y2="100" 
        stroke="#44aa44" stroke-width="2" marker-end="url(#arrowhead)"/>
  <text x="210" y="150" font-size="14" fill="#44aa44">x - M^T u ∈ S</text>
  
  <!-- Right angle indicator -->
  <path d="M 185 200 L 185 185 L 200 185" 
        stroke="#333" stroke-width="1" fill="none"/>
  
  <!-- Subspace S (nullspace) - vertical line -->
  <line x1="200" y1="50" x2="200" y2="250" 
        stroke="#44aa44" stroke-width="1" stroke-dasharray="5,5" opacity="0.5"/>
  <text x="205" y="70" font-size="12" fill="#44aa44" font-style="italic">S = null(M)</text>
</svg>

## Derivation

$$My = 0$$

$$M(x - M^T u) = 0$$

$$Mx - MM^T u = 0$$

$$(MM^T)u = Mx$$

$$u = (MM^T)^{-1} Mx$$

$$x - v = y = M^T u = M^T(MM^T)^{-1}Mx$$

$$v = (I - M^T(MM^T)^{-1}M)x$$

$$\boxed{v = Px}$$

## References
 https://www.youtube.com/watch?v=-HAzRZ5GK_A