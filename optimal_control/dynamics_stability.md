---
tags: optimal_control
lecture: 1, 2
---


##  Dynamics




$$\dot{X} = f(X, u)$$


### Example: Pendulum

![[pendulum.png]]

Equation of motion:
$$ml^2 \ddot{\theta} + mgl\sin(\theta) = \tau.$$

State variables:
- $q = \theta$ (angle),
- $v = \dot{\theta}$ (angular velocity),
- $u = \tau$ (torque).

State-space form:
$$
X = \begin{bmatrix}\theta \\ \dot{\theta}\end{bmatrix},\quad
\dot{X} = \begin{bmatrix}\dot{\theta} \\ \ddot{\theta}\end{bmatrix}
= \begin{bmatrix}\dot{\theta} \\ -\frac{g}{l}\sin(\theta) + \frac{1}{ml^2}u\end{bmatrix} = f(X,u).
$$

State spaces:
- $q \in S^1$ (circle),
- $X \in S^1 \times \mathbb{R}$ (cylinder).

## Control-Affine Systems

$$\dot{X} = f_0(X) + B(X)u,$$
where $f_0(X)$ is the drift term and $B(X)$ is the input Jacobian. Many systems admit this form.

**Pendulum:**
$$
f_0(X) = \begin{bmatrix}\dot{\theta} \\ -\frac{g}{l}\sin(\theta)\end{bmatrix},\quad
B(X) = \begin{bmatrix}0 \\ \frac{1}{ml^2}\end{bmatrix}
$$
Where: $f_0(X)$ is the "drift" term and $B(X)$ is the "input Jacobian"
## Manipulator Dynamics

$$M(q)\ddot{q} + C(q,v) = B(q)u + F$$
with
- $M(q)$: mass matrix,
- $C(q,v)$: dynamic bias (Coriolis + gravity),
- $B(q)$: input Jacobian,
- $F$: external forces.

Velocity kinematics:
$$\dot{q} = G(q)v.$$

State-space form:
$$
\dot{X} = f(X,u) = \begin{bmatrix} G(q)v \\ M^{-1}(q)\big(B(q)u+F-C\big) \end{bmatrix}
$$

**Pendulum:**
$M(q)=ml^2,\; C(q,v)=mgl\sin(\theta),\; B=I,\; G=I.$

This is a re-writing of Euler–Lagrange for
$$
L = \underbrace{\tfrac{1}{2} v^\top M(q)v}_{\text{Kinetic}} - \underbrace{U(q)}_{\text{Potential}}.
$$

## Linear Systems

$$\dot{X} = A(t)X + B(t)u$$
- Time-invariant if $A(t)=A,\; B(t)=B$; otherwise time-varying.
- Nonlinear systems $\dot{X}=f(X,u)$ are often locally approximated by
$$
A = \frac{\partial f}{\partial X},\qquad B = \frac{\partial f}{\partial u}
$$


# Equilibria, and Stability

## Equilibria

![[pendulum._equi.png]]

An equilibrium $(X^*,u^*)$ satisfies $\dot{X}=f(X,u)=0$, i.e., a root of the dynamics.

**Pendulum:**
$$
\dot{X} = \begin{bmatrix}\dot{\theta} \\ -\frac{g}{l}\sin(\theta)\end{bmatrix} =
\begin{bmatrix}0\\0\end{bmatrix}
\;\Rightarrow\;
\dot{\theta}=0,\;\; \theta\in\{0,\pi\}.
$$
So $\theta=0$ (down) and $\theta=\pi$ (upright) are equilibria.

## First Control Problem: Move the Equilibrium

![[pendulum._equi_new.png]]

At $\theta=\pi/2$,
$$
\dot{X} = \begin{bmatrix} \dot{\theta} \\ -\tfrac{g}{l}\sin(\pi/2)+\tfrac{1}{ml^2}u \end{bmatrix}
= \begin{bmatrix}0\\0\end{bmatrix}
\;\Rightarrow\;
u = mgl.
$$
In general, we solve $f(X^*,u)=0$ for $u$ (a root-finding problem).

## Stability of Equilibria

**Question:** Do small perturbations return to the equilibrium?

### 1D

For $X\in\mathbb{R}$:
- $\tfrac{\partial f}{\partial X}<0 \Rightarrow$ stable,
- $\tfrac{\partial f}{\partial X}>0 \Rightarrow$ unstable.

The set of initial conditions that converge back is the **basin of attraction**.

![[stability.png]]

### Higher Dimensions

Linearize with the Jacobian $A=\tfrac{\partial f}{\partial X}$. Eigen-decompose to decouple into 1D modes:
- Stable if $\operatorname{Re}[\lambda_i(A)]<0$ for all eigenvalues,
- Otherwise unstable.

**Pendulum Jacobian:**

$$f(X) = \begin{bmatrix} \dot{\theta} \\ -\frac{g}{\ell}\sin(\theta) \end{bmatrix}\implies \frac{\partial f}{\partial X} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{\ell}\cos(\theta) & 0 \end{bmatrix}$$

$$\frac{\partial f}{\partial X} = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} \end{bmatrix}$$
$$\frac{\partial f}{\partial x}\bigg|_{\theta=0} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{\ell} & 0 \end{bmatrix} \implies\text{eigenvals}\left(\frac{\partial f}{\partial x}\right) = \pm i\sqrt{\frac{g}{\ell}}$$ $\Rightarrow$ Unstable oscillation

$$\frac{\partial f}{\partial x}\bigg|_{\theta=\pi} = \begin{bmatrix} 0 & 1 \\ \frac{g}{\ell} & 0 \end{bmatrix} \implies \text{eigenvals}\left(\frac{\partial f}{\partial x}\right) = \pm \sqrt{\frac{g}{\ell}}$$ $\Rightarrow$ Undamped oscillation

- Add damping ($u = -k_d \dot{\theta}$) results in strictly negative real part.
# Discrete-Time Dynamics

## Motivation
- Closed forms for $\dot{X}=f(X)$ are rare.
- Numerically, we track discrete samples $X_n$.
- Discrete-time models capture effects continuous ODEs can't.

## Explicit Form
$$X_{k+1}=f_d(X_k,u_k).$$

### Forward Euler (FE)
$$X_{k+1}=X_k + h\,f(X_k,u_k)$$
with step $h$.

**Pendulum simulation:** with $l=m=1$ and $h\in\{0.1,0.01\}$, FE “blows up.”

## Stability in Discrete Time

In discrete time, dynamics is an iterated map::
$$X_N = f_d(f_d(\dots f_d(X_0))).$$

Linearize and apply chain rule:
$$
\frac{\partial X_N}{\partial X_0} = \frac{\partial f_d}{\partial X}\bigg|_{X_0} \frac{\partial f_d}{\partial X}\bigg|_{X_0} ... \frac{\partial f_d}{\partial X}\bigg|_{X_0} = A_d^N
$$

Assuming equilibrium at $X_0=0$:
- Stable $\Rightarrow \lim_{k\to\infty} A_d^k X_0 = 0$ for all $X_0$
- $\Rightarrow \lim_{n\to\infty} A_d^n = 0$
- $\Rightarrow |\text{eigvals}(A_d)| < 1$ (inside unit circle)



> [!note] Continuous vs. Discrete System Evolution
> 
> The fundamental difference between discrete and continuous systems is how they evolve over time.
> 
> **Continuous-Time Systems ($\dot{X} = AX$):** The system's state **flows** continuously over time. The solution involves a matrix exponential: $X(t) = e^{At}X(0)$. For the state to go to zero, the exponent needs to be negative. This happens when the real part of the eigenvalues of $A$ are negative ($\text{Re}[\lambda(A)] < 0$), causing exponential **decay**.
> 
> **Discrete-Time Systems ($X_{k+1} = A_d X_k$):** The system **jumps** from one state to the next in discrete steps. The evolution is based on repeated **multiplication** rather than continuous flow:
> - $X_1 = A_d X_0$
> - $X_2 = A_d X_1 = A_d(A_d X_0) = A_d^2 X_0$
> - $X_k = A_d^k X_0$
> 
> This repeated multiplication structure shows why discrete systems behave differently from continuous ones.
> 
> **Why Did the Lecture Use the Chain Rule?**
> 
> That derivation isn't unnecessary, but it is a bit formal. It's the mathematical proof for the "repeated multiplication" idea we just discussed. The expression $\frac{\partial X_N}{\partial X_0} = A_d^N$ simply shows that after $N$ steps, the sensitivity of the final state ($X_N$) to the initial state ($X_0$) is governed by the matrix $A_d$ raised to the $N$th power.

### Example: Pendulum + FE
$$
X_{k+1}= \underbrace{X_k + h f(X_k)}_{f_d(X_k)}$$

$$A_d = \frac{\partial f_d}{\partial X} = I + h A = I + h \begin{bmatrix} 0 & 1 \\ -\frac{g}{l}\cos(\theta) & 0 \end{bmatrix}
$$
At $\theta=0$, $\lambda(A_d)\approx 1 \pm 0.313i$ with magnitude $>1$ $\Rightarrow$ unstable.










## Intuition

![[linear_approx.png]]

The linear approximation often overshoots certain trajectories, causing instability.

## Key Takeaways
- Be careful with numerical integration; always sanity-check energy/momentum trends.
- **Never use Forward Euler!**

## Better Explicit Integrator: RK4
- Fits a cubic to $x(t)$ (vs. a line for FE); much higher accuracy.

**Pseudo-code** for $X_{k+1}=f_d(X_k)$:
$$
\begin{aligned}
k_1 &= f(X_k), \\
k_2 &= f\!\left(X_k + \tfrac{h}{2}\,k_1\right), \\
k_3 &= f\!\left(X_k + \tfrac{h}{2}\,k_2\right), \\
k_4 &= f\!\left(X_k + h\,k_3\right), \\
X_{k+1} &= X_k + \tfrac{h}{6}\,(k_1 + 2k_2 + 2k_3 + k_4).
\end{aligned}
$$

### Final Takeaways
- Accuracy usually outweighs extra compute.
- Even good integrators have caveats—sanity-check results.
- Many simulators prefer **backward Euler** (implicit): typically underdamped vs. FE’s overshoot/blow-up.

### Backward Euler

$$X_{k+1} = X_k + hf(X_{k+1}, u_{k+1})$$






