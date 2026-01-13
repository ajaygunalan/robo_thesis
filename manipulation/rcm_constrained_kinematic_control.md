---
tags: research_paper_notes
title: Constrained Kinematic Control in Minimally Invasive Robotic Surgery Subject to Remote Center of Motion Constraint
institute: University of Isfahan
year: 2019
keywords: robotic_surgery, RCM, kinematic_control, jacobian, manipulability
doi: https://doi.org/10.1007/s10846-018-0927-0
video: 
---

## RCM-Constrained Kinematic Control

### Problem Statement

In Minimally Invasive Robotic Surgery (MIRS), a surgical tool penetrates the patient's body through a small incision point called a trocar. To prevent tissue damage, the robotic system must strictly adhere to a Remote Center of Motion (RCM) constraint, meaning the tool shaft must always pivot around the incision point.

Existing mechanical solutions are bulky, and previous algorithmic solutions (using augmented Jacobians) often suffer from singularities or high computational complexity. This paper proposes a minimal RCM-constrained Jacobian formulation to actively control the robot for both fixed and moving trocars (e.g., due to breathing) while accurately measuring the system's dexterity.

### Model

The system consists of a serial robot arm ($n$ joints) and a surgical tool. The kinematics are modeled by augmenting the robot joints with a virtual prismatic joint ($\eta$) at the incision point to represent penetration depth.

The velocity relationships are defined as:

$$v_{e} = J_{e} \dot{q}$$

$$v_{RCM} = J_{RCM} \dot{q} = v_{trc}$$

Where:
- $\dot{q} \in \mathbb{R}^{n+3}$: Augmented joint velocity vector (Robot joints $\dot{q}_r$ + Virtual joint $\dot{\eta}$ + Tool DOFs).
- $J_{e}$: Unconstrained Jacobian mapping joint velocities to the end-effector velocity.
- $J_{RCM}$: Jacobian mapping joint velocities to the RCM point velocity.
- $v_{trc}$: Translational velocity of the trocar (incision point).

### Given

- Robot kinematics and current configuration $q$.
- Unconstrained Jacobian matrices $J_e$ and $J_{RCM}$.
- Trocar velocity $v_{trc}$ (0 for fixed trocar, measured value for moving trocar).
- Desired end-effector trajectory $\dot{x}_{des}$.

### To Find

- $J_c$: The minimal RCM-constrained Jacobian matrix.
- $\dot{q}_{com}$: Command joint velocities that satisfy the task and RCM constraint.
- $m(q)$: A manipulability index valid for the constrained system.

### Method

```
┌─────────────────────┐
│ Step 1: Kinematic   │
│ Partitioning        │──────► q_I (Independent)
└──────────┬──────────┘──────► q_II (Dependent)
           │
           ▼
┌─────────────────────┐
│ Step 2: Constraint  │
│ Resolution          │──────► q_II = f(q_I, v_trc)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 3: Constrained │
│ Jacobian (Jc)       │──────► Jc (Minimal Form)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Step 4: Control &   │──────► q_command
│ Dexterity Analysis  │──────► Manipulability Index
└─────────────────────┘
```

### 1. Kinematic Partitioning & Reordering

To isolate the constraint, the joint velocity vector $\dot{q}$ is reordered using an orthogonal transformation matrix $T$ into independent ($\dot{q}_I$) and dependent ($\dot{q}_{II}$) components.

$$\dot{q} = T \hat{\dot{q}} = T \begin{bmatrix} \dot{q}_I \\ \dot{q}_{II} \end{bmatrix}$$

The RCM Jacobian is similarly partitioned, where $J_{II}$ is a $3\times3$ invertible matrix:

$$\hat{J}_{RCM} = J_{RCM}T = \begin{bmatrix} J_{I} & J_{II} \end{bmatrix}$$

### 2. Resolution of RCM Constraint

The dependency between the joint sets is derived from the RCM velocity constraint.

#### 2.1 Fixed Trocar ($v_{trc} = 0$)

The velocity at the RCM point must be zero. This forces a strict relationship between dependent and independent joints:

$$\dot{q}_{II} = -J_{II}^{-1} J_I \dot{q}_I$$

#### 2.2 Moving Trocar ($v_{trc} \neq 0$)

If the trocar moves (e.g., patient breathing), the constraint equation includes the trocar velocity:

$$\dot{q}_{II} = J_{II}^{-1}(v_{trc} - J_I \dot{q}_I)$$

### 3. Deriving the RCM-Constrained Jacobian ($J_c$)

We substitute the dependency relations back into the end-effector kinematic equation to find the minimal Jacobian.

#### 3.1 Jacobian Definition

By substituting $\dot{q}_{II}$ into $\dot{x}_e = J_e \dot{q}$, we derive the RCM-Constrained Jacobian:

$$J_c = J_e T \begin{bmatrix} I_n \\ -J_{II}^{-1} J_I \end{bmatrix}$$

This matrix maps the independent joint velocities directly to the task space velocity, explicitly respecting the constraint.

#### 3.2 Moving Trocar Kinematics

For the moving trocar case, a feed-forward term appears in the task velocity equation:

$$\dot{x}_e = J_c \dot{q}_I + \underbrace{J_e T \begin{bmatrix} 0 \\ J_{II}^{-1} \end{bmatrix} v_{trc}}_{\text{Trocar Disturbance}}$$

### 4. Controller Design and Dexterity

With the constrained Jacobian identified, a closed-loop controller and a validity measure for dexterity are formulated.

#### 4.1 Control Law

The command velocities for the independent joints are computed using the pseudo-inverse of $J_c$:

$$\dot{q}_{I-com} = J_c^{\dagger} \left( \dot{x}_{des} + K_p(x_{des} - x_e) - J_e T \begin{bmatrix} 0 \\ J_{II}^{-1} \end{bmatrix} v_{trc} \right)$$

The dependent joints $\dot{q}_{II-com}$ are then calculated algebraically using the equations from Step 2.

#### 4.2 Constrained Manipulability Index

Standard manipulability measures fail because the joint velocities are not independent. The paper derives a new index based on the constrained manifold $\dot{q}_I^T (I + A^T A) \dot{q}_I = 1$ (where $A = -J_{II}^{-1} J_I$):

$$m(q) = \frac{\det(J_c J_c^T)}{\sqrt{\det(J_c K^T K J_c^T)}}$$

Where $K^T K = I + A^T A$. This index accurately reflects the volume of the manipulability ellipsoid subject to the RCM constraint.

---

### Key Insights

The proposed minimal Jacobian method offers a robust framework for surgical robotic control by systematically reducing the system dimensionality. Unlike "augmented Jacobian" approaches that stack the RCM constraint as an additional task (increasing matrix size and singularity risk), this method embeds the constraint directly into a reduced-dimension Jacobian ($J_c$), ensuring that the RCM constraint is satisfied structurally rather than algorithmically. Furthermore, the formulation naturally extends to moving trocars by treating the trocar velocity as a known feed-forward term, making it suitable for dynamic surgical environments (e.g., thoracic surgery). Finally, the derived manipulability index corrects the overestimation of dexterity found in standard measures, providing a realistic metric for surgical planning.
