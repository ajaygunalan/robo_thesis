---
tags: linear_algebra
---

### The Problem: Aligning Point Clouds

Imagine you have two sets of corresponding 3D points from different coordinate systems and need to find the best rotation to align them. This is the **Orthogonal Procrustes Problem**—a fundamental challenge in computer vision and robotics.

Named after the mythological Greek bandit who forcibly "fitted" travelers to his bed, this mathematical problem uses elegant linear algebra to optimally align datasets through pure rotation, without distortion.

### Mathematical Setup

Given two sets of corresponding points:
- Source points: $Y = [y_1 ; y_2 ; \cdots ; y_n]$ 
- Target points: $X = [x_1 ; x_2 ; \cdots ; x_n]$ 

We seek the optimal orthogonal matrix $Q$ that minimizes:

$$\min_{Q \in \mathbb{O}(d)} ||Y Q - X||_F^2$$

subject to the orthogonality constraint $Q^T Q = I$ and $||- |_F$ is the  [[frobenius_norm]]

### The Elegant Solution

**Algorithm:**
1. Form the correlation matrix $H = Y^T X$
2. Compute its [[svd]]: $H = U\Sigma V^T$
3. The optimal rotation is $Q^* = UV^T$

**Intuition:** Think of two constellations of stars. The correlation matrix $H$ captures how each star in $Y$ "sees" each star in $X$—encoding all pairwise relationships. The SVD decomposes this into:
- $U$: How $Y$ relates to the principal alignment directions
- $\Sigma$: The strength of each alignment axis
- $V^T$: How $X$ relates to these same directions

The solution $Q = UV^T$ rotates $Y$ to maximally preserve these relationships by aligning the principal directions.

### Ensuring Proper Rotations

The basic solution can yield reflections (determinant = -1). For applications requiring proper rotations only (like spacecraft attitude), we modify the result:

$$Q^* = U \cdot \text{diag}(1, 1, ..., 1, \det(UV^T)) \cdot V^T$$

This constraint distinguishes the general **Orthogonal Procrustes Problem** from **Wahba's Problem**, which specifically requires proper rotations.

### Practical Implementation

**Centering:** Typically, we first center both point sets to remove translation ambiguity and focus purely on rotation.

**Distance Preservation:** Procrustes maintains all pairwise distances within each point cloud—it's a rigid transformation.

### Extensions

- **Generalized Procrustes:** Allows scaling ($\min |X - sYQ|_F^2$)
- **Weighted Procrustes:** Different points have different importance
- **Partial Procrustes:** Handles missing correspondences

### The Deeper Insight

Procrustes reveals a fundamental principle: optimal geometric alignment emerges from maximizing correlation in the right coordinate system. The SVD provides exactly this coordinate system, transforming a geometric problem into pure linear algebra.

Unlike its violent mythological namesake, mathematical Procrustes achieves perfect fit through elegant rotation—a beautiful demonstration of how the right mathematical tools can solve complex spatial problems.

### Reference
[34. Distance Matrices, Procrustes Problem](https://www.youtube.com/watch?v=0Qws8BuK3RQ)