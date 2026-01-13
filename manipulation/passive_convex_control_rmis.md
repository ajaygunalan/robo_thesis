---
tags: research_paper_notes
title: A Passive Convex Optimal Control Algorithm for Teleoperating a Redundant Robotic Arm in Minimally Invasive Surgery
institute: University of Verona
year: 2025
keywords: medical_robotics, teleoperation, optimal_control, convex_optimization, remote_center_of_motion, passivity
doi: https://doi.org/10.1002/rnc.7613
video: 
---

## Passive Convex Optimal Control for R-MIS

### Problem Statement

In Robotic-Assisted Minimally Invasive Surgery (R-MIS), surgical tools must pivot around a specific point on the patient's body—the **Remote Center of Motion (RCM)**—to avoid injuring the abdominal wall. While mechanical RCMs exist, software-based RCM control allows for the use of redundant, anthropomorphic arms. However, controlling a redundant manipulator to strictly enforce the RCM while simultaneously guaranteeing **system stability** (passivity) under communication delays and respecting **physical limits** is a complex challenge. Traditional hierarchical approaches often separate these objectives, leading to conservative performance or instability.

### Model

The system is modeled as a redundant $n$-DOF manipulator controlled via a master-slave teleoperation architecture.

**1. RCM Geometry**
The RCM position $\mathbf{x}_{rcm}$ is defined as the projection of the trocar position $\mathbf{x}_{rcm}^d$ onto the tool shaft:

$$\mathbf{x}_{rcm}(t) = \mathbf{x}_f(t) + \lambda_l(t)\mathbf{n}(t)$$

Where:
- $\mathbf{x}_f(t)$: Flange position.
- $\mathbf{n}(t)$: Unit vector of the tool shaft.
- $\lambda_l(t)$: Distance along the shaft to the trocar.

**2. Passivity (Energy Tank)**
To guarantee stability, the system tracks a virtual energy tank with state $x_t$. The passivity condition requires that the energy extracted by the controller from the environment does not exceed the stored energy:

$$\dot{\mathcal{H}}(q) \le \dot{\mathbf{q}}^T (\boldsymbol{\tau} + \boldsymbol{\tau}_e)$$

### Given

- **Inputs:** Desired Cartesian velocity $[\dot{\mathbf{x}}_d; \omega_d]$ (from Master console, delayed by $\delta$).
- **State:** Current joint config $\mathbf{q} \in \mathbb{R}^n$ and Energy Tank level $T(x_t)$.
- **Constraints:**
    - Trocar position $\mathbf{x}_{rcm}^d$.
    - Kinematic Limits: $\mathbf{q}_{min}, \dot{\mathbf{q}}_{max}, \ddot{\mathbf{q}}_{max}$.
    - Workspace boundaries (virtual planes).
- **Delay:** Communication delay $\delta$ (approx. 300ms).

### To Find

- $\dot{\mathbf{q}}^* \in \mathbb{R}^n$: Optimal joint velocities for the remote manipulator.
- $\boldsymbol{\lambda}$: Slack variables allowing task relaxation if safety constraints are active.
- $\boldsymbol{\tau}$: Control torques to execute the motion passively.

### Method

```
┌─────────────────────┐
│ Step 1: Operator    │
│ Input (Master)      │──────► Desired Velocity (v_d)
└──────────┬──────────┘        (Delayed by δ)
           │
           ▼
┌─────────────────────┐
│ Step 2: Convex      │◄───── Constraint 1: RCM (Hard)
│ Optimization (QP)   │◄───── Constraint 2: Passivity (Energy Tank)
│                     │◄───── Constraint 3: Joint/Workspace Limits
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 3: Remote      │──────► Optimal Joint Velocity (q*)
│ Robot Control       │──────► Slack Variable (λ)
└─────────────────────┘
```

### 1. Convex Optimization Formulation (QP-IK)

The core contribution is formulating the Inverse Kinematics (IK) as a discrete-time **Quadratic Programming (QP)** problem. This replaces the Jacobian inverse and allows for explicit inequality constraints.

#### 1.1 Objective Function

We minimize the weighted norm of joint velocities (control effort) and the slack variables (tracking error):

$$\dot{\mathbf{q}}^*(k) = \arg \min_{\dot{\mathbf{q}}, \boldsymbol{\lambda}} \left( \frac{1}{2}\dot{\mathbf{q}}^T(k) \mathbf{W} \dot{\mathbf{q}}(k) + \boldsymbol{\lambda}^T(k) \mathbf{W}_s \boldsymbol{\lambda}(k) \right)$$

#### 1.2 Constraint: RCM (Hard Constraint)

The RCM must strictly align with the trocar. Any deviation $\mathbf{e}_{rcm}$ is corrected via a proportional gain. This is a strict equality constraint:

$$\mathbf{J}_{rcm}(\mathbf{q})\dot{\mathbf{q}}(k) = \mathbf{K}_{rcm}(\mathbf{x}_{rcm}^d - \mathbf{x}_{rcm})$$

> **Note:** Patient safety (incision integrity) takes precedence over task tracking; no slack variable is used here.

#### 1.3 Constraint: Task Tracking (Soft Constraint)

The robot attempts to follow the master's command, subject to relaxation via $\boldsymbol{\lambda}$:

$$\mathbf{J}_{ee}^c(\mathbf{q})\dot{\mathbf{q}}(k) = \begin{bmatrix} \dot{\mathbf{x}}_d(k) \\ \omega_d(k) \end{bmatrix} + \boldsymbol{\lambda}(k)$$

#### 1.4 Constraint: Passivity (Energy Aware)

A key innovation is embedding [[passivity_based_control]] directly into the QP. The power extracted by environment forces ($\mathbf{h}_e$) must not exceed the tank's residual energy:

$$T_s \mathbf{h}_e^T \mathbf{J}_{ee} \dot{\mathbf{q}} \le T(x_t(k)) - \epsilon$$

This ensures the system remains passive regarding the environment power port.

---

### 2. Bilateral Teleoperation Architecture

The QP controller is deployed on the **Remote** (Slave) side. The architecture handles time delays using a four-channel-like power exchange to maintain stability.

#### 2.1 Power Exchange

To prevent local energy tanks from depleting during standard operation, energy is exchanged over the communication channel:

$$P_o^{in}(t) = P_r^{out}(t-\delta)$$

$$P_r^{in}(t) = P_o^{out}(t-\delta)$$

#### 2.2 Transparency Layer

While the Remote side is velocity-controlled via the QP, the Operator (Master) side is force-controlled. The operator feels a virtual force based on the position error between Master and Slave:

$$\boldsymbol{\tau}_{d_o} = \mathbf{J}_{ee}^T \mathbf{K}_v (\mathbf{x}_{ee_r}(t-\delta) - \mathbf{x}_{ee_o}(t))$$

---

### 3. Experimental Validation

The system was validated using a **da Vinci Master console** controlling a **Franka Emika Panda** (7-DOF) in a peg-and-ring task with a **300 ms** round-trip delay.

#### 3.1 Accuracy

- **RCM Error:** The RCM constraint was maintained with sub-millimeter accuracy (RMSE $\approx 0.3$ mm).
- **Velocity Tracking:** The controller tracked operator inputs with an RMSE of $\approx 4.7$ mm/s.

#### 3.2 Safety & Stability

- **Constraint Activation:** When the operator attempted to violate workspace limits or velocity limits, the QP smoothly saturated the velocity using the slack variables ($\boldsymbol{\lambda}$), decoupling the master command from the slave motion to ensure safety without instability.
- **Passivity:** The energy tanks remained positive throughout the task, confirming the global passivity of the architecture.

---

### Key Insights

This paper proposes a unified framework that treats **Inverse Kinematics**, **Safety Constraints**, and **Passivity-Based Stability** as a single convex optimization problem solved at each control cycle. By embedding the energy tank constraint directly into the QP, the method guarantees stability under arbitrary communication delays without requiring separate passivity layers. The use of slack variables creates a graceful degradation mechanism: when physical or safety limits are reached, the system prioritizes the hard RCM constraint (patient safety) while smoothly relaxing trajectory tracking, maintaining both stability and intuitive operator feedback.
