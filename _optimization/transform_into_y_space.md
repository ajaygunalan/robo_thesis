---
tags: optimization
---

## Centering Transformation

### Key Idea

Position the current point close to the center of the feasible region.

### Implementation

- One possible choice for the initial point is: $$\mathbf{1} = (1, 1, \ldots, 1)^T$$
    
- Given a point $\mathbf{x}^k$ in the interior of the feasible region, define: $$X^k = \text{diag}(\mathbf{x}^k)$$
    
- Define the transformation: $$\mathbf{y} = T(\mathbf{x}) = (X^k)^{-1} \mathbf{x}$$

![[x_to_y_transformation.png]]
    
- This gives us: $$\mathbf{y}^k = (X^k)^{-1} \mathbf{x}^k = \mathbf{1}$$
    
- Or equivalently: $$X^k \mathbf{y}^k = \mathbf{x}^k$$

![[y_to_x_transformation.png]]
    

### Significance

This transformation maps the current point $\mathbf{x}^k$ to the unit vector $\mathbf{1}$, effectively "centering" the problem in a transformed space. This is crucial for interior point methods as it:

1. Improves numerical stability
2. Makes the algorithm more efficient by normalizing the problem
3. Helps avoid getting too close to the boundary of the feasible region


_Tags:_ #optimization #linear-programming #interior-point-methods #mathematics