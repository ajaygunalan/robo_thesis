## Why estimation is different from construction

In synthetic graphics, you typically *choose* a rotation plane and angle, build a rotor, and move on. In vision and robotics, rotations come from data that is noisy and incomplete. Determining a rotor from exactly three vector correspondences (a frame) is brittle; you want an estimator that minimizes a meaningful cost over many measurements.

The chapter points to a rotor estimation approach derived via geometric calculus (treated earlier in the book) and then uses a concrete multi-camera calibration problem to show what "vector space model + optimization" looks like in practice.

## External camera calibration: directions observed, depths unknown

Assume cameras are internally calibrated so that an image pixel corresponds to a known **direction** in the camera frame. This turns each camera into a sensor for directions.

Take $M+1$ cameras and use camera 0 as reference. For camera $j$, let:

* $t_j$ be its translation (optical center) relative to camera 0,
* $R_j$ be its orientation rotor.

A world point $X_i$ is seen by camera $j$ along a ray direction $x_{ij}$ in the camera's coordinate frame, but at unknown depth $\sigma_{ij}$. So the (unknown) point in camera coordinates is $X_{ij}=\sigma_{ij}x_{ij}$ and the world-to-camera relationship is
$$
X_i = t_j + R_j X_{ij}\tilde R_j
= t_j + R_j(\sigma_{ij}x_{ij})\tilde R_j.
$$
This is exactly the vector space model's "directions at origin" meeting a pragmatic encoding of locations as vectors.

## The cost function

Measure reconstruction quality by the sum of squared errors over all cameras and all point instances:
$$
\Gamma = \sum_{j=1}^{M}\sum_{i=1}^{N}
\left|X_i - t_j - R_j\sigma_{ij}x_{ij}\tilde R_j\right|^2.
$$
Then solve by alternating partial optimizations of $(t_j,R_j,\sigma_{ij},X_i)$.

## Closed-form updates from differentiation

The chapter lists the optimal partial solutions (the "nice" outcome of doing the GA differentiation carefully):

### Translation (given $R_j,\sigma_{ij},X_i$)

$$
t_j = \frac1N \sum_{i=1}^N \left(X_i - R_j\sigma_{ij}x_{ij}\tilde R_j\right).
$$
Interpretation: average discrepancy between true world points and what camera $j$ would reconstruct with its current orientation and depths.

### Rotation condition (given $X_i$, data, and using optimal $t_j$)

The optimal $R_j$ satisfies a wedge-orthogonality condition:
$$
\sum_{i=1}^N (X_i - t_j)\wedge (R_j\sigma_{ij}x_{ij}\tilde R_j)=0.
$$
Substituting the optimal $t_j$ leads to the centroid form
$$
\sum_{i=1}^N (X_i - \bar X)\wedge (R_j\sigma_{ij}x_{ij}\tilde R_j)=0,
$$
where $\bar X=\frac1N\sum_k X_k$ is the centroid. Geometrically: the best rotor makes the reconstructed rays line up with the world-point deviations with minimal transverse error. Computationally, the chapter notes you can solve for $R_j$ via an SVD of an associated linear map.

### Depth scale along each ray (given $R_j,t_j,X_i$)

$$
\sigma_{ij} = (X_i - t_j)\cdot (R_j x_{ij}^{-1}\tilde R_j).
$$
This is "almost" division by the rotated direction, but the dot product forces the result to be a scalar by taking only the component along the ray.

### World points (given $t_j,R_j,\sigma_{ij}$)

$$
X_i = \frac1M \sum_{j=1}^M \left(t_j + R_j\sigma_{ij}x_{ij}\tilde R_j\right).
$$
Interpretation: average the reconstructed 3D point estimates across cameras.

## The iterative scheme

Combining the partial updates yields a linear(ish) iterative calibration loop:

1. Initialize $R_j$ (e.g., from a standard stereo method).
2. Update $t_j$ from the current $(R_j,\sigma_{ij},X_i)$.
3. Update $X_i$ from the current $(R_j,t_j,\sigma_{ij})$.
4. Update $\sigma_{ij}$ from the current $(R_j,t_j,X_i)$.
5. Update $R_j$ using the rotation condition and repeat.

The chapter reports that on the referenced data, roughly a dozen iterations are typically needed for convergence (depending on number of cameras). In modern workflows, you often take this as a strong *initialization* and then run a few steps of nonlinear optimization to squeeze out extra accuracy.

Figure 10.7 on PDF page 22 shows the reconstructed marker trajectory after calibration, with cameras drawn as wireframe pyramids and viewing directions indicated.

## "Convenient abuse": using direction vectors as position vectors

The chapter is candid: the vector space model is *the* natural model for directions, but you can (and people constantly do) treat vectors as positions by interpreting a location as "go in direction $p$ for distance $|p|$."

This works tolerably when your geometry is mostly point-like and especially when the measurements you get are directions anyway (exactly the situation in camera calibration). But it is not structural:

* If you represent a line by "point + direction," translations must update the point but not the direction. That forces you to track object types and apply the right bookkeeping manually.
* The algebra does not give you a uniform translation operator that acts correctly on *all* objects, because the model is fundamentally local-to-origin.

This is not philosophical nitpicking; it's a real source of programming errors. The fix is to move to an extended model (at least homogeneous, often conformal) where translations are native operations and geometry types don't require ad-hoc handling.
