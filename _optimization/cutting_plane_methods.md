---
tags: optimization
---

## The Cutting-Plane Method for Constrained Optimization

### Problem Setup

Consider the primal optimization problem:

$$\begin{aligned} \min_{x} \quad & f(x) \ \text{s.t.} \quad & h_j(x) \le 0, \quad j = 1,\dots,l,\ & e_i(x) = 0, \quad i = 1,\dots,m,\ & x \in X \end{aligned}$$

where $X$ is a compact set (ensuring minima exist).

### Dual Formulation

The Lagrange dual function is:

$$\theta(\lambda, \mu) = \min_{x \in X} \left[ f(x) + \lambda^T h(x) + \mu^T e(x) \right]$$

Leading to the dual problem: $\max_{\lambda \ge 0, \mu} \theta(\lambda, \mu)$

This can be reformulated as a linear program with infinite constraints:

$$\begin{aligned} \max_{z,\lambda,\mu} \quad & z \ \text{s.t.} \quad & z \le f(x) + \lambda^T h(x) + \mu^T e(x), \quad \forall x \in X,\ & \lambda \ge 0 \end{aligned}$$

Each $x \in X$ generates one constraint, creating infinitely many linear inequalities that define the feasible region as an intersection of half-spaces in $(z,\lambda,\mu)$-space.

### The Cutting-Plane Algorithm

Since infinite constraints are computationally intractable, the method works iteratively:

#### Step 1: Finite Approximation

Start with a finite set of points ${x^0, \dots, x^{k-1}}$ and solve:

$$\begin{aligned} \max_{z,\lambda,\mu} \quad & z\ \text{s.t.} \quad & z \le f(x^j) + \lambda^T h(x^j) + \mu^T e(x^j), \quad j=0,\dots,k-1,\ & \lambda \ge 0 \end{aligned}$$

#### Step 2: Violation Check

After solving for $(z^k, \lambda^k, \mu^k)$, verify if:

$$z^k \le f(x) + \lambda^{k^T}h(x) + \mu^{k^T}e(x) \quad \forall x \in X$$

#### Step 3: Add Cutting Plane

If violated, find the most violated point:

$$x^k = \arg\min_{x \in X} \left[ f(x) + \lambda^{k^T} h(x) + \mu^{k^T} e(x)\right]$$

Add the new constraint (the "cut"):

$$z \le f(x^k) + \lambda^T h(x^k) + \mu^T e(x^k)$$

This constraint cuts away a region of $(z,\lambda,\mu)$-space that cannot contain the optimal dual solution.

#### Step 4: Iterate

Return to Step 1 with the expanded constraint set. Continue until no violated constraints exist.

### Convergence

The algorithm converges when the finite approximation matches the true dual feasible region. At this point:

- $(z^*, \lambda^*, \mu^*)$ is optimal for the dual problem
- By strong duality, the corresponding $x^*$ is primal-optimal
- Each iteration tightens the approximation by adding exactly one half-space that refines the feasible region

The method's elegance lies in progressively building a finite representation of an infinite constraint set, adding only the constraints that matter for finding the optimum.
