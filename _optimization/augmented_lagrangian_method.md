---
tags: optimization
---

## Augmented Lagrangian Method

### Problem Formulation

$$\min \quad f(\mathbf{x})$$ $$\text{s.t.} \quad e(\mathbf{x}) = 0$$

### Starting Point: The Lagrangian

- Let $(\mathbf{x}^*, \mu^*)$ be a KKT point where $\nabla f(\mathbf{x}^*) + \mu^* \nabla e(\mathbf{x}^*) = \mathbf{0}$
- The **Lagrangian**: $\mathcal{L}(\mathbf{x}, \mu) = f(\mathbf{x}) + \mu^{\top} e(\mathbf{x})$

**The Challenge**: In practice, we don't know $\mu^*$ beforehand, and solving the equality constraint exactly during iterative optimization is hard.

### Penalty Method Attempt

- **Penalty Function**: $q(\mathbf{x}, c) = f(\mathbf{x}) + cP(\mathbf{x})$ where $P(\mathbf{x}) = \frac{1}{2}|e(\mathbf{x})|^2$
- As $c \to \infty$, $q(\mathbf{x}, c) \to f(\mathbf{x})$ for feasible points
- **Problem**: Optimization becomes difficult due to numerical ill-conditioning with large $c$

### The Augmented Lagrangian Solution

#### Derivation via Perturbed Problem

Consider the **perturbed problem**: $$\min \quad f(\mathbf{x})$$ $$\text{s.t.} \quad e(\mathbf{x}) = \theta$$

#### Penalty Function for Perturbed Problem

$$ \begin{align} \hat{q}(\mathbf{x}, c) &= f(\mathbf{x}) + c(e(\mathbf{x}) - \theta)^2 \\ &= f(\mathbf{x}) - 2c\theta e(\mathbf{x}) + ce(\mathbf{x})^2 \quad \text{(ignoring constant term)} \\ &= \underbrace{f(\mathbf{x}) + \mu e(\mathbf{x})}_{\mathcal{L}(\mathbf{x},\mu) ; \text{is the Lagrangian}} + ce(\mathbf{x})^2 \quad \text{where} ; \mu = -2c\theta \\ &= \hat{\mathcal{L}}(\mathbf{x}, \mu, c) \quad \text{Augmented Lagrangian Function} \end{align} $$

Therefore, the **Augmented Lagrangian**: $\boxed{\hat{\mathcal{L}}(\mathbf{x}, \mu, c) = f(\mathbf{x}) + \mu^{\top} e(\mathbf{x}) + \frac{c}{2}|e(\mathbf{x})|^2}$

**What's "augmented"?** The quadratic penalty term $\frac{c}{2}|e(\mathbf{x})|^2$ is added to the standard Lagrangian $\mathcal{L}(\mathbf{x}, \mu) = f(\mathbf{x}) + \mu^{\top} e(\mathbf{x})$, creating a hybrid that doesn't rely solely on finding the perfect $\mu^*$.

### Key Properties

At the KKT point $(\mathbf{x}^*, \mu^*)$: $\nabla_x \mathcal{L}(\mathbf{x}^*, \mu^*) = \nabla f(\mathbf{x}^*) + \mu^* \nabla e(\mathbf{x}^*) = \mathbf{0}$

$$ \begin{align} \therefore \nabla_x \hat{q}(\mathbf{x}^*, c) &= \nabla_x \hat{\mathcal{L}}(\mathbf{x}^*, \mu^*, c) \ &= \nabla_x \mathcal{L}(\mathbf{x}^*, \mu^*) + 2ce(\mathbf{x}^*)\nabla e(\mathbf{x}^*) \ &= \mathbf{0} ; \forall ; c \end{align} $$

This shows that $\mathbf{x}^*$ remains a stationary point of the augmented Lagrangian for any $c > 0$.

### Multiplier Estimation

**Question**: How to get an estimate of $\mu^*$?


Let $\mathbf{x}_c^*$ be a minimizer of $\hat{\mathcal{L}}(\mathbf{x}, \mu, c)$. Therefore: $$\nabla_x \hat{\mathcal{L}}(\mathbf{x}_c^*, \mu, c) = \nabla f(\mathbf{x}_c^*) + \mu\nabla e(\mathbf{x}_c^*) + ce(\mathbf{x}_c^*)\nabla e(\mathbf{x}_c^*) = \mathbf{0}$$

This implies: $$\nabla f(\mathbf{x}_c^*) = -\underbrace{(\mu + ce(\mathbf{x}_c^*))}_{\text{estimate of } \mu^*}\nabla e(\mathbf{x}_c^*)$$

**Key Insight**: The term $\mu + ce(\mathbf{x}_c^*)$ provides our updated estimate for the optimal multiplier $\mu^*$.

### Why Augmentation Works

**Normal Lagrangian vs Augmented**: $\mathcal{L} = f(\mathbf{x}) + \mu^{\top} e(\mathbf{x})$ becomes $\hat{\mathcal{L}} = f(\mathbf{x}) + \mu^{\top} e(\mathbf{x}) + \frac{c}{2}|e(\mathbf{x})|^2$

|Method|Formulation|Issue|
|---|---|---|
|**Lagrangian**|$f(\mathbf{x}) + \mu^{\top} e(\mathbf{x})$|Unknown $\mu^*$; constraint satisfaction fails during iterations|
|**Penalty**|$f(\mathbf{x}) + c\|e(\mathbf{x})\|
|**Augmented**|$f(\mathbf{x}) + \mu^{\top} e(\mathbf{x}) + \frac{c}{2}\|e(\mathbf{x})\|

**Interpretation**:

- The $\mu^{\top}e(\mathbf{x})$ term enforces constraints softly (Lagrangian contribution)
- The $\frac{c}{2}|e(\mathbf{x})|^2$ term stabilizes numerical behavior (penalty contribution)
- Together, they make the feasible region "attractive" without requiring $c \to \infty$

### Algorithm

#### Problem Formulation

- **Objective**: $\min f(\mathbf{x})$
- **Subject to**: $e(\mathbf{x}) = 0$

#### Augmented Lagrangian Algorithm

**Inputs**: $c > 0$, tolerance $\epsilon$  
**Initialize**: $k := 0$, $\mathbf{x}^k$, $\mu^k$

**While** $(\hat{\mathcal{L}}(\mathbf{x}^k, \mu^k, c) - f(\mathbf{x}^k)) > \epsilon$:

- (a) $\mathbf{x}^{k+1} = \arg\min_{\mathbf{x}} ; \hat{\mathcal{L}}(\mathbf{x}, \mu^k, c)$
- (b) $\mu^{k+1} = \mu^k + ce(\mathbf{x}^{k+1})$
- (c) $k := k + 1$

**EndWhile**  
**Output**: $\mathbf{x}^k = \mathbf{x}^*$ (optimal solution)

#### Algorithm Intuition

- **Step (a)**: Makes progress toward optimality by minimizing the augmented Lagrangian
- **Step (b)**: Updates the multiplier estimate based on constraint violation
- The constraint is gradually enforced without sending $c \to \infty$
- The termination condition $(\hat{\mathcal{L}}(\mathbf{x}^k, \mu^k, c) - f(\mathbf{x}^k)) = \mu^{\top}e(\mathbf{x}^k) + \frac{c}{2}|e(\mathbf{x}^k)|^2$ measures constraint violation

### Geometric View

The augmented Lagrangian creates a modified optimization landscape where:

- The Lagrange term $\mu^{\top}e(\mathbf{x})$ provides directional guidance toward the constraint surface
- The penalty term $\frac{c}{2}|e(\mathbf{x})|^2$ bends the objective contours toward the feasible region
- This combination creates a "valley" along the constraint surface $e(\mathbf{x}) = 0$ that guides iterates naturally toward feasibility without numerical instability