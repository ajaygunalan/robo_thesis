---
title: "Matrix Representations"
tags: [matrices, basis, reciprocal-frame, implementation]
---

A matrix is a linear transformation seen through a chosen basis. That choice is why matrices are efficient and also why they hide geometry.

## Vector matrix
Given a basis $\{b_i\}$ with reciprocal $\{b^j\}$ ($b_i \cdot b^j = \delta_i^j$), define
$$[f]^j_i = f(b_i) \cdot b^j$$
The $i$th column is the image of $b_i$ written in that coordinate system.

## Outermorphism matrices (one per grade)
On $k$-vectors, pick the blade basis $b_I = b_{i_1} \wedge \ldots \wedge b_{i_k}$ with reciprocal $b^I$. Then
$$[f]^J_I = f(b_I) \ast b^J$$

For bivectors this expands to the familiar 2x2 minor pattern:
$$[f]^{j_1 j_2}_{i_1 i_2} = [f]^{j_2}_{i_2}[f]^{j_1}_{i_1} - [f]^{j_1}_{i_2}[f]^{j_2}_{i_1}$$

So "transforming areas/volumes" in coordin