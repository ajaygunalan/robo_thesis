---
tags: optimization
---

[exact math here](https://youtu.be/LWXXhBIlj0o?list=PL6EA0722B99332589&t=4736)


While both Karmarkar's algorithm and the affine scaling method are interior point techniques for linear programming, they differ in a key way:

- The **affine scaling method** uses an affine transformation to recenter the current iterate (making it the "center" of the feasible set) and then takes a projected steepest descent step to stay within the feasible region.
    
- **Karmarkar's method**, on the other hand, applies a projective transformation rather than a simple affine one. This projective mapping repositions the current point and reshapes the feasible region in a way that often leads to stronger theoretical guarantees and different convergence behavior.
    

So, while they share a similar spirit—moving from an interior point and maintaining feasibility—the transformation step distinguishes Karmarkar's method from the affine scaling algorithm.