## 1. Double Pendulum Dynamics

Let the state be $$\mathbf{x} = \begin{bmatrix}\theta_1 \ \dot{\theta}_1 \ \theta_2 \ \dot{\theta}_2\end{bmatrix},$$

and define $$c = \cos(\theta_1-\theta_2), \quad s = \sin(\theta_1-\theta_2).$$

The equations of motion are then given by:

$$\begin{aligned} \dot{\theta}_1 &= \dot{\theta}_1, \\ \ddot{\theta}_1 &= \frac{ m_2,g,\sin\theta_2,c - m_2,s\Bigl(L_1,c,\dot{\theta}_1^2 + L_2,\dot{\theta}_2^2\Bigr) - (m_1+m_2),g,\sin\theta_1}{L_1\Bigl(m_1+m_2,s^2\Bigr)}, \\ \dot{\theta}_2 &= \dot{\theta}_2, \\ \ddot{\theta}_2 &= \frac{ (m_1+m_2)\Bigl(L_1,\dot{\theta}_1^2,s - g,\sin\theta_2 + g,\sin\theta_1,c\Bigr) + m_2,L_2,\dot{\theta}_2^2,s,c}{L_2\Bigl(m_1+m_2,s^2\Bigr)}. \end{aligned}$$

Here, $\dot{\theta}_1$ and $\dot{\theta}_2$ denote the angular velocities, and $\ddot{\theta}_1$ and $\ddot{\theta}_2$ their accelerations.

## 2. Double Pendulum Energy

### Positions

For the first mass, the Cartesian coordinates are:

$$\mathbf{r}_1 = \begin{bmatrix}L_1\sin\theta_1 \\ 0 \\ -L_1\cos\theta_1 + 2\end{bmatrix}.$$

For the second mass, they are:

$$\mathbf{r}_2 = \begin{bmatrix}L_1\sin\theta_1 + L_2\sin\theta_2 \\ 0 \\ -L_1\cos\theta_1 - L_2\cos\theta_2 + 2\end{bmatrix}.$$

### Velocities

Differentiating the positions with respect to time gives:

$$\mathbf{v}_1 = \frac{d\mathbf{r}_1}{dt} = \begin{bmatrix}L_1\dot{\theta}_1\cos\theta_1 \\ 0 \\ L_1\dot{\theta}_1\sin\theta_1\end{bmatrix},$$

$$\mathbf{v}_2 = \frac{d\mathbf{r}_2}{dt} = \begin{bmatrix}L_1\dot{\theta}_1\cos\theta_1 + L_2\dot{\theta}_2\cos\theta_2 \\ 0 \\ L_1\dot{\theta}_1\sin\theta_1 + L_2\dot{\theta}_2\sin\theta_2\end{bmatrix}.$$

### Kinetic Energy

The kinetic energy is given by:

$$T = \frac{1}{2}m_1|\mathbf{v}_1|^2 + \frac{1}{2}m_2|\mathbf{v}_2|^2,$$

where

$$|\mathbf{v}_1|^2 = L_1^2\dot{\theta}_1^2,$$

and

$$|\mathbf{v}_2|^2 = \left(L_1\dot{\theta}_1\cos\theta_1 + L_2\dot{\theta}_2\cos\theta_2\right)^2 + \left(L_1\dot{\theta}_1\sin\theta_1 + L_2\dot{\theta}_2\sin\theta_2\right)^2.$$

Using the trigonometric identity $\cos^2\alpha + \sin^2\alpha = 1$ and the cosine of a difference, the second term simplifies to:

$$|\mathbf{v}_2|^2 = L_1^2\dot{\theta}_1^2 + L_2^2\dot{\theta}_2^2 + 2L_1L_2,\dot{\theta}_1\dot{\theta}_2,\cos(\theta_1-\theta_2).$$

Thus,

$$T = \frac{1}{2}\left[m_1L_1^2\dot{\theta}_1^2 + m_2\Bigl(L_1^2\dot{\theta}_1^2 + L_2^2\dot{\theta}_2^2 + 2L_1L_2,\dot{\theta}_1\dot{\theta}_2,\cos(\theta_1-\theta_2)\Bigr)\right].$$

### Potential Energy

The potential energy is determined from the vertical (z) positions:

$$V = m_1g,r_{1z} + m_2g,r_{2z},$$

where

$$r_{1z} = -L_1\cos\theta_1 + 2, \quad r_{2z} = -L_1\cos\theta_1 - L_2\cos\theta_2 + 2.$$

### Total Energy

The total energy $E$ of the system is:

$$E = T + V.$$

These expressions capture the continuous dynamics and energy of the double pendulum as given in the code.