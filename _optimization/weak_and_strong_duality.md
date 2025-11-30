---
tags: optimization
---

[If this looks weird, watch the two player game to get a feel for it](https://youtu.be/x4CJe-OWVds?list=PL6EA0722B99332589)

$$\underset{x \in \mathcal{X}}{\min} \quad \underbrace{\underset{y \in \mathcal{Y}}{\max}\psi(x,y)}_{\text{primal function}}$$


$$\underset{y \in \mathcal{Y}}{\max} \quad \underbrace{\underset{x \in \mathcal{X}}{\min}\psi(x,y)}_{\text{dual function}}$$


- The two problems are **dual** to each other
- For any $x \in \mathcal{X}$ and $y \in \mathcal{Y}$:
$$\min_{x \in \mathcal{X}} \psi(x,y) \leq \psi(x,y) \leq \max_{y \in \mathcal{Y}} \psi(x,y)$$
$$\therefore \min_{x \in \mathcal{X}} \psi(x,y) \leq \max_{y \in \mathcal{Y}} \psi(x,y)$$
$$\therefore \max_{y \in \mathcal{Y}} \min_{x \in \mathcal{X}} \psi(x,y) \leq \min_{x \in \mathcal{X}} \max_{y \in \mathcal{Y}} \psi(x,y)$$

## Weak Duality

$$\underset{y \in \mathcal{Y}}{\max} \quad \underset{x \in \mathcal{X}}{\min}\psi(x,y) \leq \underset{x \in \mathcal{X}}{\min} \quad \underset{y \in \mathcal{Y}}{\max}\psi(x,y)$$

## Strong Duality

$$\underset{y \in \mathcal{Y}}{\max} \quad \underset{x \in \mathcal{X}}{\min}\psi(x,y) = \underset{x \in \mathcal{X}}{\min} \quad \underset{y \in \mathcal{Y}}{\max}\psi(x,y)$$

if and only if there exists a saddle point, $(x^*, y^*)$ for $\psi(x, y) \implies$ game is in equilibrum.


## Geometric 

no duality gap $\implies$ ![[duality_geomtric.png]]

![[duality_gap.png]]