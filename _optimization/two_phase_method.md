---
tags: optimization
---

The [[simplex]] is a procedure that iteratively "walks" along the edges of the feasible region (its vertices) to improve the objective function. It requires an initial basic feasible solution (BFS) to start.

In contrast, the [[two_phase_method]] is a technique used when an obvious BFS is not available. It works in two phases:

1. **Phase I:**  
    Artificial variables are added to the LP to form an auxiliary problem whose objective is to drive these artificial variables to zero. If this auxiliary problem can be solved with an optimal value of zero, it means a feasible solution to the original LP exists.
    
2. **Phase II:**  
    With a feasible solution in hand (all artificial variables at zero), the original LP is solved using the standard simplex method.
    

In short, the simplex method is used when you already have a starting point, while the two-phase method is a “**bootstrapping**” strategy to first find that starting point when it isn’t obvious.
