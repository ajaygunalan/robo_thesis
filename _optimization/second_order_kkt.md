---
tags: optimization
---

## Nonlinear Programming (NLP) Problem

- **Objective**: $\min f(x)$
- **Subject to**:
    - $h_j(x) \leq 0, \quad j = 1,\ldots,l$ (inequality constraints)
    - $e_i(x) = 0, \quad i = 1,\ldots,m$ (equality constraints)

## Lagrangian Function

$$\mathcal{L}(x, \lambda, \mu) = f(x) + \sum_{j=1}^{l} \lambda_j h_j(x) + \sum_{i=1}^{m} \mu_i e_i(x)$$

## KKT Conditions (Second Order)

If $x^* \in X$ is a local minimum of NLP and a regular point, then there exist unique vectors $\lambda^* \in \mathbb{R}^l_+$ and $\mu^* \in \mathbb{R}^m$ such that:

1. **First-order conditions**:
    - $\nabla_x \mathcal{L}(x^*), \lambda^*, \mu^*) = \mathbf{0}$ (stationarity)
    - $\lambda_j^* h_j(x^*) = 0 \quad \forall j = 1,\ldots,l$ (complementary slackness)
    - $\lambda_j^* \geq 0 \quad \forall j = 1,\ldots,l$ (dual feasibility)
2. **Second-order condition**:
    
    - $d^T \nabla^2_x \mathcal{L}(x^*, \lambda^*, \mu^*)d \geq 0$
    - For all $d$ such that $\nabla h_j(x^*)^T d \leq 0, j \in \mathcal{I}$ and $\nabla e_i(x^*)^T d = 0, i \in \mathcal{E}$
3. For $x^*$ is a strict local minimum of NLP, then
    - $d^T \nabla^2_x \mathcal{L}(x^*, \lambda^*, \mu^*)d > 0$
    
    For all $d \neq \mathbf{0}$ such that:
    
    - $\nabla h_j(x^*)^T d = 0, j \in \mathcal{I}$ and $\lambda_j^* > 0$
    - $\nabla h_j(x^*)^T d \leq 0, j \in \mathcal{I}$ and $\lambda_j^* = 0$
    - $\nabla e_i(x^*)^T d = 0, i \in \mathcal{E}$