---
tags: research_paper_notes
title: A Concurrent Framework for Constrained Inverse Kinematics of Minimally Invasive Surgical Robots
institute: Nagoya University
year: Mar 2023
keywords: surgical_robots, inverse_kinematics, RCM_constraint, nonlinear_optimization, concurrent_solving
doi: https://doi.org/10.3390/s23063328
video: 
---

## Concurrent Constrained Inverse Kinematics

### Problem Statement

In Robot-Assisted Minimally Invasive Surgery (RMIS), the robotic manipulator must enter the patient's body through a small incision (trocar). To prevent tissue damage, the robot's motion is kinematically constrained to pivot around this specific insertion point, known as the **Remote Center of Motion (RCM)**. 

We need to identify a joint configuration that achieves a desired surgical tool pose while strictly satisfying the RCM constraint and physical joint limits. Standard iterative methods (Jacobian) are fast but unstable near limits, while optimization methods are robust but computationally slow.

### Model

The system is modeled as a serial manipulator where the tool shaft motion is constrained by a fixed trocar point.

**RCM Geometric Constraint:**
The RCM error is defined as the minimum distance between the fixed trocar point ($p_{trocar}$) and the surgical tool axis. The point on the tool axis closest to the trocar, $p_{rcm}$, is:

$$p_{rcm} = p_{pre} + p_r^T \hat{p}_s \hat{p}_s$$

$$e_{rcm} = ||p_{trocar} - p_{rcm}||$$

Where:
- $p_{trocar}$: Position of the trocar (insertion point).
- $p_{pre}$: Position of the joint immediately preceding the RCM on the tool.
- $\hat{p}_s$: Unit vector representing the direction of the surgical tool axis.
- $p_r$: Vector from the pre-joint to the trocar ($p_{trocar} - p_{pre}$).

**Differential Kinematics:**
The relationship between the RCM error velocity and joint velocities $\dot{q}$ is given by the Jacobian:

$$J_{rcm}(q) = p_e^T \left[ (I_3 - \hat{p}_s \hat{p}_s^T) J_{pre} + (\hat{p}_s p_r^T + p_r^T \hat{p}_s I_3) \frac{\partial \hat{p}_s}{\partial q} \right]$$

### Given

- Robot kinematic model ($n$ joints).
- $p_{trocar} \in \mathbb{R}^3$: Fixed Trocar Position.
- $^B T_{ee_{des}} \in SE(3)$: Desired End-Effector Pose.
- $q^{-}, q^{+}$: Joint limits.

### To Find

- $\dot{q}^* \in \mathbb{R}^n$: Optimal joint velocities.
- $q_{next} \in \mathbb{R}^n$: Next joint configuration satisfying:
    - $e_{rcm} \to 0$ (Primary Constraint).
    - $e_{ee} \to 0$ (Secondary Objective).
    - $q^{-} \le q \le q^{+}$ (Inequality Constraint).

### Method

```
┌─────────────────────┐
│ Global Task Request │
│ (Target + Limits)   │
└──────────┬──────────┘
           │
           ▼ (Spawn Threads)
┌──────────┼──────────┐
▼          ▼          ▼
┌──────┐ ┌──────┐ ┌──────┐
│ INVJ │ │ NLO  │ │ HQP  │
│Solver│ │Solver│ │Solver│
└──────┘ └──────┘ └──────┘
    │      │          │
    └──────┼──────────┘
           │
           ▼
┌─────────────────────┐
│ Selection Logic     │──────► q* (First Valid Solution)
│ (Speed vs Safety)   │──────► Terminate others
└─────────────────────┘
```

### 1. INVJ - Inverse Jacobian Solver (Iterative)

This solver uses a **Strict Hierarchical** approach via null-space projection. It is computationally fast but cannot natively handle inequality constraints (joint limits).

#### 1.1 Velocity Formulation

The joint velocities are computed by prioritizing the RCM task ($e_{rcm}$) and projecting the tool pose task ($e_{ee}$) into the null space:

$$\dot{q} = J_{rcm}^{\dagger} K_{rcm} e_{rcm} + (I_n - J_{rcm}^{\dagger} J_{rcm}) J_{ee}^{\dagger} K_{ee} e_{ee}$$

#### 1.2 Constraint Handling via Random Restart

To handle joint limits, the solver employs a **Random Restart** strategy. If the algorithm converges to a solution outside the joint limits ($q \notin [q^-, q^+]$), it resets to a random configuration and retries. This makes it probabilistic but fast for simple poses.

---

### 2. NLO - Nonlinear Optimization Solver

This solver formulates the IK problem as a **Weighted Multi-Objective Optimization**. It is robust and explicitly handles inequalities but has high computational cost.

#### 2.1 Cost Function

$$q^* = \arg \min_q \left( w_1 \|e_{ee}\|^2 + w_2 \|e_{rcm}\|^2 + w_3 \|\dot{q}\|^2 \right)$$

#### 2.2 Constraints

$$\text{s.t.} \quad q^{-} \le q \le q^{+}$$

This utilizes interior-point methods (IPOPT) to find a global optimum that strictly respects joint limits, though it creates a non-strict hierarchy between RCM and Pose tasks based on weights ($w_1, w_2$).

---

### 3. HQP - Hierarchical Quadratic Programming

This solver combines the **Strict Hierarchy** of INVJ with the **Inequality Handling** of optimization by solving a sequence of Quadratic Programs (QPs).

#### 3.1 Task 1: RCM Constraint

Minimize RCM error subject to joint velocity limits:

$$\min_{\dot{q}, w} \| J_{rcm} \dot{q} - K e_{rcm} \|^2 + \frac{1}{2}\|w\|^2$$

$$\text{s.t.} \quad \frac{q^- - q}{\delta t} \le \dot{q} \le \frac{q^+ - q}{\delta t}$$

#### 3.2 Task 2: Tool Pose

Minimize Pose error in the null-space of Task 1 ($N_1 = I - J_{rcm}^\dagger J_{rcm}$):

$$\min_{\nu} \| J_{ee} (N_1 \nu + \dot{q}_1^*) - K e_{ee} \|^2$$

This ensures the RCM constraint is never violated for the sake of the pose, while respecting physical limits.

---

### 4. Concurrent Framework Implementation

The proposed framework runs the solvers (INVJ, NLO, HQP) simultaneously in parallel threads. The system utilizes a "race" logic to determine the output.

#### 4.1 Selection Logic

- **Speed Priority:** The INVJ solver is extremely fast (<0.2ms) and solves the majority of standard poses. If it returns a valid solution (converged + within limits), it is immediately selected.
- **Robustness Fallback:** If INVJ fails (due to limits or singularities), the slower but robust HQP or NLO solvers (1.5ms - 4ms) provide the solution.
- **Termination:** Once a valid solution is found, a signal is sent to terminate the other running threads to save resources.

---

### Key Insights

The Concurrent Framework addresses the critical trade-off between speed and robustness in surgical robotics by leveraging the complementary nature of deterministic and probabilistic algorithms. The method demonstrates that running a fast, "greedy" solver (Inverse Jacobian) alongside a robust, computationally intensive solver (Hierarchical QP) results in a system that is as fast as the former in general cases and as safe as the latter in critical edge cases. Experimental validation on a 7-DOF manipulator with a hyper-redundant tool showed the **INVJ+HQP** combination achieving a **100% solve rate** while reducing average computation time by up to **85%** compared to pure optimization approaches. This architecture effectively handles the stringent RCM constraints required for patient safety without sacrificing the real-time performance needed for smooth teleoperation.
