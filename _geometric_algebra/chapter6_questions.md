# Chapter 6: The Fundamental Product of Geometric Algebra - Conceptual Questions

## 6.1 The Geometric Product for Vectors

The inner product $\mathbf{x} \cdot \mathbf{a} = \alpha$ constrains $\mathbf{x}$ to a hyperplane, and the outer product $\mathbf{x} \wedge \mathbf{a} = B$ constrains $\mathbf{x}$ to a line; neither alone determines $\mathbf{x}$, but together they do. The geometric product $\mathbf{x}\mathbf{a} \equiv \mathbf{x} \cdot \mathbf{a} + \mathbf{x} \wedge \mathbf{a}$ combines both, making it invertible with $\mathbf{a}^{-1} = \mathbf{a}/(\mathbf{a} \cdot \mathbf{a})$. Explain why commutativity fails (it would require $\mathbf{x} \wedge \mathbf{a} = 0$), and how the ratio $\mathbf{b}\mathbf{a}^{-1}$ acts as a rotation-and-scaling operator that solves the similarity problem $\mathbf{x} : \mathbf{c} = \mathbf{b} : \mathbf{a}$ via $\mathbf{x} = (\mathbf{b}\mathbf{a}^{-1})\mathbf{c}$.


## 6.2 The Geometric Product of Multivectors

The geometric product is defined algebraically by: scalars multiply as usual and commute with everything, $\mathbf{x}^2 = \mathbf{x} \cdot \mathbf{x}$ ties it to the metric, it is distributive and associative, but not commutative. From these axioms, the polarization identity $\mathbf{x} \cdot \mathbf{y} = \frac{1}{2}(\mathbf{x}\mathbf{y} + \mathbf{y}\mathbf{x})$ recovers the inner product as the symmetric part. Explain why the geometric product of a $k$-blade and an $l$-blade produces grades $|k-l|, |k-l|+2, \ldots, k+l$ (each shared vector reduces grade by 2), and why this mixed-grade output is what makes the product invertible.


## 6.3 The Subspace Products Retrieved

The outer product and contraction can be extracted from the geometric product via symmetry or grade selection. The symmetry approach gives $\mathbf{a} \wedge B = \frac{1}{2}(\mathbf{a}B + B\hat{\mathbf{a}})$ and $\mathbf{a} \rfloor B = \frac{1}{2}(\mathbf{a}B - B\hat{\mathbf{a}})$ where $\hat{B} = (-1)^{\text{grade}(B)}B$ is grade involution. The grade approach gives $A_k \wedge B_l = \langle A_k B_l \rangle_{k+l}$ and $A_k \rfloor B_l = \langle A_k B_l \rangle_{l-k}$. Explain why these approaches prove the geometric product is more fundamental than the subspace products, and how the decomposition $\mathbf{a}B = \mathbf{a} \rfloor B + \mathbf{a} \wedge B$ generalizes the vector formula $\mathbf{a}\mathbf{b} = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \wedge \mathbf{b}$.


## 6.4 Geometric Division

The inverse of a blade is $A^{-1} = \tilde{A}/(A * \tilde{A})$, enabling geometric division. The identity $\mathbf{x} = (\mathbf{x}A)A^{-1}$ decomposes into projection $(\mathbf{x} \rfloor A)A^{-1}$ (the component in $A$) plus rejection $(\mathbf{x} \wedge A)A^{-1}$ (the component perpendicular to $A$). Explain why left-division $\mathbf{a}^{-1}\mathbf{x}\mathbf{a}$ produces reflection of $\mathbf{x}$ in $\mathbf{a}$ (projection minus rejection) rather than recovering $\mathbf{x}$, and why sandwiching $\mathbf{x}$ between $\mathbf{a}$ and $\mathbf{a}^{-1}$ is the fundamental construction for orthogonal transformations.
