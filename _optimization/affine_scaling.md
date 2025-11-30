---
tags: optimization
---

We start interior to the feasible set, hence [[interior_point]] so we [[transform_into_y_space]] such that our starting point is the center of feasible set.


![[interior_points.png]]


but the [[steepest_descent_method]] direction may not be feasible, hence we need to [[project_the_steepest_direction]] onto the feasible set ($P_c$).

![[projection_onto_null_space.png]]

Next, find the step length $\alpha_k$

---


## Algorithm Steps
- Start with any interior point $x^0$
- while ([[stopping_condition_for_affine_scaling]])
  - Transform the current problem into an equivalent problem in $y$-space so that the current point is close to the centre of the feasible region
  - Use projected steepest descent direction to take a step in the $y$-space without crossing the feasible set boundary

![[steepest_descent_in_y_space.png]]

  - Map the new point back to the corresponding point in the $x$-space
- endwhile


[For exact math check here](https://youtu.be/LWXXhBIlj0o?list=PL6EA0722B99332589&t=3029)
