---
tags: research_paper_notes
title: Real-time Inverse Kinematics for Robotic Manipulation under Remote Center-of-Motion Constraint using Memetic Evolution
institute: Nagoya University
year: 2024
keywords: surgical_robotics, inverse_kinematics, evolutionary_algorithm, rcm_constraint, pivot_ik
doi: https://doi.org/10.1093/jcde/qwae047
video: 
---

## PivotIK: Real-Time Constrained Inverse Kinematics

### Problem Statement

In Robot-Assisted Minimally Invasive Surgery (RMIS), surgical instruments must enter the patient through a small incision. To prevent tissue damage, the tool shaft must pivot around this fixed insertion point, known as the **Remote Center of Motion (RCM)**.

Controlling a redundant manipulator to track a 6-DoF trajectory while strictly adhering to this geometric constraint creates a complex, non-linear [[inverse_kinematics]] (IK) problem. Traditional numerical methods (like Newton-Raphson) often get stuck in local minima due to the non-convex nature of the constraints, while global evolutionary algorithms are typically too slow for real-time control (< 10 ms).

### Model

The system is modeled as a multi-objective optimization problem where the joint configuration $q$ must minimize both the trajectory tracking error and the RCM deviation.

$$^B\mathbf{T}_{ee}(q) \to ^B\mathbf{T}_{des} \quad \text{s.t.} \quad ||\mathbf{p}_{trocar} - \mathbf{p}_{tool\_axis}|| \approx 0$$

Where:
- $^B\mathbf{T}_{ee}$: End-effector pose in the base frame.
- $\mathbf{p}_{trocar}$: Fixed position of the incision port (trocar).
- $\mathbf{p}_{tool\_axis}$: The point on the tool shaft closest to the trocar.
- $\mathbf{p}_{rcm}$: The projection of the trocar point onto the tool axis $\hat{p}_s$:
  $$p_{rcm} = p_{pre} + (p_{trocar} - p_{pre})^T \hat{p}_s \hat{p}_s$$

### Given

- **Robot Model**: Serial manipulator with $n$ joints ($q \in \mathbb{R}^n$).
- **Target Pose**: Desired End-Effector pose $^B\mathbf{T}_{des} \in SE(3)$.
- **Constraint**: Fixed trocar position $\mathbf{p}_{trocar} \in \mathbb{R}^3$.
- **Joint Limits**: $q_{min} \le q \le q_{max}$.

### To Find

- **Optimal Joint Configuration** $q^* \in \mathbb{R}^n$ that minimizes:
    1. **RCM Error:** $e_{rcm} = ||p_{trocar} - p_{rcm}||$
    2. **Tracking Error:** $e_{ee} = ||\log_6(^B\mathbf{T}_{des} \cdot ^B\mathbf{T}_{act}^{-1})||$
- A solution suitable for high-frequency control loops (< 10 ms).

### Method

```
┌─────────────────────┐
│ Step 1: Population  │
│ Initialization      │──────► Random Genomes
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 2: Fitness     │──────► Rank Individuals
│ Evaluation          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 3: Elite       │──────► Jacobian-based Update
│ Exploitation        │        (Fast Gradient Descent)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 4: Evolution   │──────► Crossover
│ Operators           │──────► Adaptive Mutation
└─────────────────────┘
```

### 1. Fitness Function

The fitness function $\Phi(v)$ evaluates an individual (joint configuration $v$) based on a linear combination of the task errors.

$$\Phi(v) = \mu_{rcm} e_{rcm}(v) + \mu_{ee} e_{ee}(v)$$

Where:
- $\mu_{rcm}, \mu_{ee}$: Weights for the RCM and Tracking tasks.
- $e_{ee}$: The pose error calculated using the logarithmic map of $SE(3)$ (twist vector), capturing both position and orientation.

### 2. Elite Exploitation (Memetic Step)

Standard [[evolutionary_algorithms]] rely on random mutation, which makes fine-tuning slow. **PivotIK** accelerates this by applying a hierarchical **Jacobian-based update** to the top-performing ("Elite") individuals.

#### 2.1 Update Law

For an elite individual $v$, a single iteration of the Newton-Raphson update is applied:

$$v' = v + J_{ee}^{\dagger} K_{ee} r_{ee} + (I - J_{ee}^{\dagger} J_{ee}) J_{rcm}^{\dagger} K_{rcm} r_{rcm}$$

Where:
- $J^\dagger$: The [[pseudo-inverse]] of the task Jacobian.
- $(I - J^\dagger J)$: Null-space projection operator (ensures the secondary task does not disrupt the primary task).
- $r$: Task residuals (error vectors).

This allows the elites to "snap" to the constraint manifold using analytical gradients.

### 3. Evolutionary Operators (Global Search)

To avoid the local minima that plague pure numerical solvers, the non-elite population undergoes robust diversification operations.

#### 3.1 Crossover

Rank-based selection chooses parents to generate offspring via linear interpolation:

$$v_{offspring} = \alpha v_{parent_A} + (1-\alpha) v_{parent_B}, \quad \alpha \in [0, 1]$$

#### 3.2 Adaptive Mutation

To prevent stagnation, an "extinction factor" measures population diversity. If the population converges prematurely (stagnates), the mutation rate increases automatically to force exploration of new regions in the configuration space.

### 4. RCM Task Jacobian Derivation

To enable the fast exploitation step (Section 2), the analytical Jacobian of the RCM constraint is derived explicitly, avoiding computationally expensive numerical differentiation.

$$J_{rcm}(q) = -2 p_e^T \frac{\partial p_{rcm}}{\partial q}$$

The term $\frac{\partial p_{rcm}}{\partial q}$ captures how the point on the tool shaft moves relative to the joints:

$$\frac{\partial p_{rcm}}{\partial q} = (I_3 - \hat{p}_s\hat{p}_s^T)J_{pre} + (\hat{p}_s p_r^T + p_r^T \hat{p}_s I_3) \frac{\partial \hat{p}_s}{\partial q}$$

Where $J_{pre}$ is the Jacobian of the kinematic chain up to the insertion point.

---

### Key Insights

The **PivotIK** method employs a hybrid "memetic" solution approach that strategically combines the global exploration of evolutionary algorithms with the local precision of gradient-based optimization. This architecture overcomes the fundamental trade-off in constrained IK: evolutionary methods avoid local minima but converge slowly, while Jacobian methods converge quickly but get trapped. By applying analytical gradient updates only to elite individuals, PivotIK achieves real-time performance (< 10 ms) while maintaining robustness against the non-convex constraint landscape inherent to RCM-constrained manipulation.
