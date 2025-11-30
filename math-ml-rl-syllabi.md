# Master Syllabus: Advanced Mathematical Foundations for ML & Robotics

This master markdown compiles the detailed syllabi of foundational courses for machine learning, robotics, and optimization, each annotated with comprehensive topics, instructor credits, source links, and structural notes for advanced learners.

---

## 1. MIT 6.041 / 6.431: Probabilistic Systems Analysis and Applied Probability
- **Institution:** MIT
- **Authors:** Prof. John Tsitsiklis, Prof. Dimitri Bertsekas, Prof. Munther Dahleh (varies by year)
- **Course Link:** [MIT OCW 6.041](https://ocw.mit.edu/courses/6-041-probabilistic-systems-analysis-and-applied-probability-fall-2010/)

### Syllabus Overview
- Sample space, probability laws, conditional probability
- Independence, Bayes’ Theorem
- Random variables: discrete and continuous
- Useful distributions: binomial, Poisson, geometric, exponential, normal
- Functions of random variables
- Expectations, conditional expectation, variances
- Sums of independent random variables, convolution
- Moment generating functions, transforms
- Law of large numbers, central limit theorem
- Markov processes, random processes, Poisson process
- Elements of statistical inference

### Prerequisites
Calculus (Single and Multivariable)

---

## 2. Gilbert Strang: Linear Algebra
- **Book:** Linear Algebra and Its Applications
- **Author:** Prof. Gilbert Strang (MIT)
- **Course Link:** [MIT OCW 18.06](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

### Syllabus Overview
- Systems of linear equations
- Row reduction and echelon forms
- Matrix operations and inverses
- Subspaces, basis, dimension
- Orthogonality, Gram-Schmidt, least squares
- Determinants, Cramer’s rule
- Eigenvalues and eigenvectors
- Diagonalization, matrix exponentials
- Symmetric and positive definite matrices
- Linear transformations
- Singular Value Decomposition (SVD)
- Applications: networks, Markov matrices, Fourier, Fast Fourier Transform

### Prerequisites
Familiarity with vectors/matrices and basic linear algebra

---

## 3. Convex Optimization (robothesis.com)
- **Instructor/Author:** To be confirmed
- **Course Link:** [robothesis Convex Optimization](https://robothesis.com/_optimization/_optimization)

### Syllabus Overview
- Convex sets and functions: basic theory
- Convex optimization problem formulation
- Examples: linear, quadratic, geometric, semidefinite programs
- Duality: Lagrangian, Fenchel, conic, saddle point theory
- Optimality conditions, theorems of alternatives
- Algorithms: subgradient, interior-point, proximal, ADMM, stochastic gradient
- Applications: signal processing, control, ML, statistics, circuit/finance
- Topics: minimax, extremal volume, large-scale optimization, monotone operators, branch & bound

### Standard References
- Boyd, S., Vandenberghe, L. "Convex Optimization"
- Bertsekas, D.P. "Convex Optimization Theory"

---

## 4. CMU 16-745: Optimal Control and Reinforcement Learning
- **Institution:** Carnegie Mellon University
- **Instructor:** Prof. Zachary Manchester
- **Course Link:** [CMU 16-745 Optimal Control](https://optimalcontrol.ri.cmu.edu)

### Syllabus Overview
- Review of nonlinear dynamics & linear systems
- Stability analysis, discretization
- Numerical optimization intro
- Optimal control: Pontryagin, shooting, LQR methods
- Dynamic programming & convexity in control
- Convex & nonlinear trajectory optimization (DDP, iLQR)
- Model Predictive Control (MPC)
- Hybrid systems, attitude & quadrotor dynamics
- State estimation, system identification, stochastic optimal control (LQG)
- Data-driven & iterative learning control
- Robust & minimax control, RL links
- Project-based applications: rockets, walking robots, driving

### Prerequisites
- Strong linear algebra, differential equations, Python/Julia/MATLAB

---

## 5. UC Berkeley CS 285: Deep Reinforcement Learning
- **Institution:** University of California, Berkeley
- **Instructor:** Prof. Sergey Levine and collaborators
- **Course Link:** [CS285 Deep RL](https://rail.eecs.berkeley.edu/deeprlcourse/)

### Syllabus Overview
- Supervised behavioral cloning
- Markov Decision Processes: Policies, Value Functions
- Reinforcement learning foundations: Policy gradients, actor-critic, Q-learning
- Deep RL: Policy/value function approximation, DQN, A3C, PPO, TRPO, SAC, DDPG
- Model-based RL
- Imitation learning
- Exploration in RL
- Offline RL, RL theory basics
- Advanced: Inverse RL, meta-RL, transfer, sequence models
- Applications: robotics, control, games, vision

### Course Structure
- 5 HWs
- Final project
- Lecture videos/slides available

### Prerequisites
- Undergrad ML, RL familiarity, deep learning basics, strong math/coding skills

---

**End of Master Syllabus**
