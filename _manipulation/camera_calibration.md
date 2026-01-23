# Camera Calibration

## Camera Model (Forward Imaging Mode)

- Maps a point in 3D to its projection in pixels
- **Linear Model** (Projection Matrix)
  - **Intrinsic** parameters
  - **Extrinsic** parameters

### Coordinate Systems


![[camera_calibration.jpeg]]

The imaging pipeline transforms points from the **World Frame** through the **Camera Frame** to the **Image Plane**, with focal length $f$ along the optical axis.

---

## Perspective Projection

The projection equations from camera coordinates to image coordinates:

$$x_i = \frac{f}{z_c} \cdot x_c \qquad y_i = \frac{f}{z_c} \cdot y_c$$

where $(x_c, y_c, z_c)$ are camera coordinates and $(x_i, y_i)$ are image coordinates in mm.

---

## Converting to Pixel Coordinates

Since $x_i, y_i$ are in mm but we need pixel coordinates $(u, v)$:

$$u = m_x \cdot x_i \qquad v = m_y \cdot y_i$$

where $(m_x, m_y)$ are the pixel densities (pixels/mm) — **unknown**.

Also, the principal point is not at the origin, so we add offsets $(O_x, O_y)$:

$$u = m_x x_i + O_x \qquad v = m_y y_i + O_y$$

Substituting the projection equations:

$$u = m_x \frac{f}{z_c} x_c + O_x \qquad v = m_y \frac{f}{z_c} y_c + O_y$$

Defining $f_x = m_x f$ and $f_y = m_y f$:

$$\boxed{u = f_x \frac{x_c}{z_c} + O_x \qquad v = f_y \frac{y_c}{z_c} + O_y}$$

The **intrinsic parameters** are: $(f_x, f_y, O_x, O_y)$

> ⚠️ This formulation is **non-linear** (division by $z_c$).

---

## Homogeneous Coordinates

To obtain a **linear model**, we use homogeneous coordinates:
- 2D → 3D
- 3D → 4D

("Fictitious coordinates")

### Calibration Matrix $K$

$$\begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = \begin{bmatrix} f_x & 0 & O_x & 0 \\ 0 & f_y & O_y & 0 \\ 0 & 0 & 1 & 0 \end{bmatrix} \begin{bmatrix} x_c \\ y_c \\ z_c \\ 1 \end{bmatrix}$$

### Intrinsic Matrix

$$M_{int} = \begin{bmatrix} K & \mathbf{0} \end{bmatrix}$$

where $K = \begin{bmatrix} f_x & 0 & O_x \\ 0 & f_y & O_y \\ 0 & 0 & 1 \end{bmatrix}$

$$\tilde{u} = M_{int} \tilde{X}_c \quad \text{(2D ← 3D)}$$

---

## World to Camera Transformation

$$X_c = R(X_W - C_W) = RX_W - RC_W$$

Let $t = RC_W$:

$$X_c = RX_W - t$$

### Extrinsic Matrix (Homogeneous)

$$M_{ext} = \begin{bmatrix} R_{3\times3} & t \\ \mathbf{0}_{1\times3} & 1 \end{bmatrix}$$

$$\tilde{X}_c = M_{ext} \tilde{X}_W$$

---

## Full Projection Model

Combining intrinsic and extrinsic:

$$\tilde{u} = M_{int} \cdot M_{ext} \cdot \tilde{X}_W = P \tilde{X}_W$$

where $P$ is the **Projection Matrix** $(3 \times 4)$.

---

## Summary

| Component | Matrix | Size | Parameters |
|-----------|--------|------|------------|
| Intrinsic | $M_{int}$ | $3 \times 4$ | $f_x, f_y, O_x, O_y$ |
| Extrinsic | $M_{ext}$ | $4 \times 4$ | $R$ (rotation), $t$ (translation) |
| Projection | $P = M_{int} M_{ext}$ | $3 \times 4$ | 11 DOF |

---

## Next: Estimate Projection Matrix

*(To be continued...)*
