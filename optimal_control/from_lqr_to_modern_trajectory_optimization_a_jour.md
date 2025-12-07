---
tags: optimal_control
---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# From LQR to Modern Trajectory Optimization: A Journey Through Optimal Control

## Introduction: Why This Journey Matters

Picture yourself trying to control a robot arm, fly a quadcopter, or stabilize an inverted pendulum. At the heart of these challenges lies a fundamental question: **How do we compute control inputs that achieve our goals while respecting physical constraints?**[1][2]

This tutorial takes you on a journey through modern control theory, starting from the elegant simplicity of Linear Quadratic Regulators (LQR) and building up to sophisticated trajectory optimization methods. Unlike traditional presentations that treat these topics in isolation, we'll see how each method naturally emerges from the limitations of its predecessors[3][4].

## Part 1: The Foundation - Linear Quadratic Regulator (LQR)

### The Core Idea

LQR solves a deceptively simple problem: find the control input $u$ that minimizes a quadratic cost function for a linear system. Mathematically[5][6]:

$\min_{u_{0:N-1}} J = \frac{1}{2}x_N^T Q_N x_N + \sum_{k=0}^{N-1} \left[\frac{1}{2}x_k^T Q x_k + \frac{1}{2}u_k^T R u_k\right]$

subject to linear dynamics:
$x_{k+1} = A_k x_k + B_k u_k$

The beauty of LQR lies in its closed-form solution through the Riccati equation[7].

### Three Paths to the Same Solution

Your lecture materials brilliantly demonstrate three different approaches to solving LQR, each revealing different insights[1][5][6]:

#### 1. Quadratic Programming (QP) Formulation

```julia
# Stack all states and controls into one vector
z = [u0; x1; u1; ...; xN]

# Create sparse matrices
H = blockdiag(R, kron(I(N-2), blockdiag(Q,R)), Qn)
C = kron(I(N-1), [B -I(2)])  # Dynamics constraints

# Solve the linear system
y = [H C'; C zeros(size(C,1),size(C,1))]\[zeros(size(H,1)); d]
```

**Insight**: This approach reveals LQR as a structured optimization problem. The sparsity pattern tells us that each state only directly affects its neighbors - a key insight for computational efficiency[8].

#### 2. Riccati Recursion

```julia
P[:,:,N] = Qn
for k = (N-1):-1:1
    K[:,:,k] = (R + B'*P[:,:,k+1]*B)\(B'*P[:,:,k+1]*A)
    P[:,:,k] = Q + A'*P[:,:,k+1]*(A-B*K[:,:,k])
end
```

**Insight**: The backward recursion naturally leads to a feedback policy. This isn't just computational convenience - it's revealing the fundamental structure of optimal control: future costs propagate backward to influence current decisions[9].

#### 3. Shooting Method

```julia
# Backward pass for costate
λhist[:,N] = Qn*xhist[:,N]
for k = N-1:-1:1
    Δu[k] = -(uhist[k] + R\B'*λhist[:,k+1])
    λhist[:,k] = Q*xhist[:,k] + A'*λhist[:,k+1]
end

# Forward pass with line search
α = 1.0
while J(xnew, unew) > J(xhist, uhist) - b*α*Δu[:]'*Δu[:]
    α = 0.5*α
    unew = uhist + α.*Δu
    xnew = rollout(xhist, unew)
end
```

**Insight**: Shooting reveals the connection to Pontryagin's principle and sets the stage for nonlinear methods. The line search is our first hint that nonlinear problems will require iterative refinement[10].

### The Critical Connection: Lagrange Multipliers as Value Gradients

One of the most profound insights from the materials is[9]:

$\lambda_k = \nabla V_k(x_k) = P_k x_k$

The Lagrange multipliers aren't just mathematical artifacts - they represent the sensitivity of future cost to current state. This connection between optimization and dynamic programming is the key to understanding modern trajectory optimization[11].

## Part 2: Breaking Free from Linearity - Model Predictive Control (MPC)

### The Motivation

LQR gives us optimal control, but real systems have constraints[10]:

- Actuator limits (motors can only provide so much torque)
- State constraints (robots shouldn't collide with obstacles)
- Safety boundaries (quadcopters shouldn't fly upside down)

MPC elegantly handles these by solving a *constrained* optimization problem at each time step[12][13].

### The Planar Quadrotor Example

Your materials provide a perfect example with the planar quadrotor[10]:

```julia
# Nonlinear dynamics
ẍ = (1/m)*(u[1] + u[2])*sin(θ)
ÿ = (1/m)*(u[1] + u[2])*cos(θ) - g
θ̈ = (1/J)*(ℓ/2)*(u[2] - u[1])

# Linearize around hover
A = ForwardDiff.jacobian(x->quad_dynamics_rk4(x,u_hover), x_hover)
B = ForwardDiff.jacobian(u->quad_dynamics_rk4(x_hover,u), u_hover)

# Add constraints
umin = [0.2*m*g; 0.2*m*g]  # Minimum thrust
umax = [0.6*m*g; 0.6*m*g]  # Maximum thrust
```

The MPC formulation becomes:

```julia
# At each time step, solve:
min Σ(‖x[k]-xref‖²_Q + ‖u[k]‖²_R) + ‖x[N]-xref‖²_P
s.t. x[k+1] = A*x[k] + B*u[k]
     umin ≤ u[k] ≤ umax
```


### The Key Insight: Receding Horizon

MPC's genius lies in its receding horizon approach[14][15]:

1. Solve for optimal controls over a finite horizon
2. Apply only the first control
3. Shift the horizon and repeat

This provides three critical benefits:

- **Constraint satisfaction**: Hard constraints are explicitly enforced
- **Robustness**: Re-planning at each step handles disturbances
- **Computational tractability**: Finite horizon keeps problems manageable


### Implementation Details Matter

```julia
# Sparse QP formulation for efficiency
H = sparse([kron(I(Nh-1),[R zeros(Nu,Nx); zeros(Nx,Nu) Q]) zeros((Nx+Nu)*(Nh-1), Nx+Nu); 
            zeros(Nx+Nu,(Nx+Nu)*(Nh-1)) [R zeros(Nu,Nx); zeros(Nx,Nu) P]])

# Dynamics constraints as sparse matrices
C = sparse([[B -I zeros(Nx,(Nh-1)*(Nu+Nx))]; 
            zeros(Nx*(Nh-1),Nu) [kron(I(Nh-1), [A B]) zeros((Nh-1)*Nx,Nx)] + 
            [zeros((Nh-1)*Nx,Nx) kron(I(Nh-1),[zeros(Nx,Nu) -I])]])
```

**Critical observation**: The sparsity pattern isn't accidental - it encodes the temporal structure of the problem. Modern MPC implementations exploit this structure for real-time performance[16].

## Part 3: Embracing Nonlinearity - Differential Dynamic Programming (DDP)

### The Challenge

MPC handles constraints well but struggles with highly nonlinear dynamics. Consider the acrobot swinging up from rest - linearizing around a single point can't capture the full motion[11][17].

### DDP: The Best of Both Worlds

DDP combines the feedback structure of LQR with the ability to handle nonlinear dynamics[11]:

```julia
# Backward pass: compute local LQR approximations
for k = (Nt-1):-1:1
    # Derivatives at current trajectory point
    A = dfdx(xtraj[:,k], utraj[k])
    B = dfdu(xtraj[:,k], utraj[k])
    
    # Second-order approximations (full DDP)
    Gxx = Q + A'*P[:,:,k+1]*A + tensor_term  # Includes second-order dynamics
    Guu = R + B'*P[:,:,k+1]*B + tensor_term
    
    # Compute feedback gains
    d[k] = Guu\gu                # Feedforward
    K[:,:,k] = Guu\Gux          # Feedback
end
```


### The Power of Second-Order Information

The materials show a critical comparison between iLQR (Gauss-Newton) and full DDP (Newton)[11]:

```julia
# iLQR: First-order dynamics only
Gxx = Q + A'*P[:,:,k+1]*A
Guu = R + B'*P[:,:,k+1]*B

# DDP: Include second-order terms
Ax = dAdx(xtraj[:,k], utraj[k])  # Tensor!
Gxx = Q + A'*P[:,:,k+1]*A + kron(p[:,k+1]',I(Nx))*comm(Nx,Nx)*Ax
```

**Key insight**: While DDP can converge in fewer iterations, iLQR often wins in wall-clock time. This illustrates a fundamental trade-off in optimization: better local models vs. computational cost per iteration[18][19].

### The Algorithm That Thinks Ahead

```julia
# Forward rollout with line search
xn[:,1] = xtraj[:,1]
α = 1.0
for k = 1:(Nt-1)
    # This is the magic: feedback during rollout!
    un[k] = utraj[k] - α*d[k] - dot(K[:,:,k], xn[:,k]-xtraj[:,k])
    xn[:,k+1] = dynamics_rk4(xn[:,k], un[k])
end
```

The feedback term `-K*δx` is crucial: it prevents the forward rollout from diverging due to integration errors or model mismatch[20].

## Part 4: When Forward Integration Fails - Direct Collocation

### The Limitation of Shooting Methods

All previous methods share a common structure: they integrate dynamics forward from an initial condition. This creates two problems[21]:

1. **Sensitivity to initial guess**: Bad initial controls can cause numerical explosion
2. **Constraint handling**: Path constraints are difficult to enforce during integration

### Direct Collocation: A Fundamentally Different Approach

Instead of integrating dynamics, direct collocation enforces them as *constraints*[21][22]:

```julia
# Hermite-Simpson collocation
function dircol_dynamics(x1, u1, x2, u2)
    f1 = dynamics(x1, u1)
    f2 = dynamics(x2, u2)
    
    # Midpoint state and control
    xm = 0.5*(x1 + x2) + (h/8.0)*(f1 - f2)
    um = 0.5*(u1 + u2)
    
    # Collocation constraint
    fm = dynamics(xm, um)
    ẋm = (-3/(2*h))*(x1 - x2) - 0.25*(f1 + f2)
    
    return fm - ẋm  # Should equal zero
end
```


### The Elegant Mathematics

Hermite-Simpson collocation uses cubic polynomials for states and linear interpolation for controls[23]:

$x(t) = x_k + (t-t_k)\dot{x}_k + (t-t_k)^2 c_2 + (t-t_k)^3 c_3$

The collocation constraint ensures the polynomial satisfies dynamics at the midpoint, achieving third-order accuracy with just one dynamics evaluation per segment[22].

### Why This Matters

Direct collocation offers several advantages[24]:

1. **Constraint flexibility**: Easy to add path constraints at collocation points
2. **Initialization robustness**: Can start with dynamically infeasible trajectories
3. **Computational efficiency**: 30-50% fewer dynamics evaluations than RK3
```julia
# Compare computational cost
# RK3: 3 dynamics calls per timestep
# Hermite-Simpson: 1 dynamics call per timestep (reused from adjacent segments)
```


## Critical Insights and Connections

### 1. The Optimization-Dynamics Duality

Throughout this journey, we see a fundamental duality[9][11]:

- **Optimization view**: Minimize cost subject to dynamics
- **Dynamic programming view**: Propagate value functions backward

LQR reveals they're the same: $\lambda = \nabla V(x)$. This insight extends to all methods.

### 2. The Spectrum of Structure Exploitation

Each method makes different trade-offs[16][25]:


| Method | Structure Exploited | Computational Complexity | Constraint Handling |
| :-- | :-- | :-- | :-- |
| LQR | Linear dynamics | $O(N(n+m)^3)$ | None |
| MPC | Finite horizon | $O(H^3(n+m)^3)$ | Excellent |
| DDP | Dynamic programming | $O(N(n+m)^3)$ | Limited |
| Collocation | Sparsity | $O(N^3)$ but sparse | Excellent |

### 3. The Importance of Problem Formulation

The materials demonstrate that *how* you formulate the problem often matters more than *which* algorithm you use[26][27]:

```julia
# Poor formulation: Large condition number
Q = Diagonal([1000.0*ones(2); 0.001*ones(2)])

# Better formulation: Balanced weights
Q = Diagonal([1.0*ones(2); 0.1*ones(2)])
```


### 4. Theory Meets Practice

The gap between textbook algorithms and working implementations is filled with crucial details[28]:

- Regularization strategies for numerical stability
- Line search methods for global convergence
- Warm-starting techniques for real-time performance


## Looking Forward: The Modern Landscape

This journey from LQR to direct collocation represents just the beginning. Modern developments include[15][29]:

- **GPU acceleration**: MPPI leverages massive parallelism for sampling-based MPC
- **Learning integration**: Neural networks approximate value functions or dynamics
- **Differentiable simulation**: Automatic differentiation through contact and collisions


## Conclusion: A Unified View

What started as a simple quadratic optimization problem (LQR) has evolved into a rich tapestry of methods, each addressing specific challenges while building on fundamental principles. The key takeaway isn't to memorize algorithms, but to understand the underlying trade-offs and connections.

Whether you're implementing a simple stabilizing controller or planning complex robotic motions, the principles remain the same:

1. Model your system dynamics
2. Define what "good" behavior means
3. Choose the right tool for your constraints and computational budget
4. Iterate and refine

The journey from LQR to modern trajectory optimization isn't just about more sophisticated mathematics - it's about building intuition for when and why different approaches work, and having the tools to tackle whatever control challenge comes your way.

