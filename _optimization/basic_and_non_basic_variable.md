---
tags: optimization
---


### Standard Linear Program (SLP)

- **Objective Function**: $\min c^T x$
- **Constraints**:
    - $Ax = b$
    - $x \geq 0$
- **Where**:
    - $A \in \mathbb{R}^{m \times n}$
    - $\text{rank}(A) = \text{rank}(A|b) = m$


**The basic and non-basic variables are tight and loose variables so that you can move from on vertex to another vertex watch [here](https://youtu.be/E72DWgKP_1Y?t=366).**

### Basic and Non-Basic Variables

Let $B \in \mathbb{R}^{m \times m}$ be formed using $m$ linearly independent columns of $A$.

The system of equations $Ax = b$ can be written as:

$\begin{pmatrix} B & N \end{pmatrix} \begin{pmatrix} x_B \\ \ x_N \end{pmatrix} = b$

Where:

- $B$ is the basis matrix
- $x_B$ represents the basic variables
- $x_N$ represents the non-basic variables

### Basic Solution

By setting $x_N = 0$, we get:

$Bx_B = b \implies x_B = B^{-1}b$

$\begin{pmatrix} x_B & 0 \end{pmatrix}^T$: The basic solution with respect to the basis matrix $B$ is.
- Not the solution to LP. Only solution to the system $Ax=b$



### Basic Feasible Solution


If $x_B \geq 0$, then $(x_B\text{ }0)^T$ is called a basic feasible solution of $$Ax = b$$ $$x \geq 0$$

with respect to the basis matrix $B$.

### Theorem on Extreme Points

Let $X = \{x : Ax = b, x \geq 0\}$,  $x$ is an extreme point of $X$ if and only if $x$ is a basic feasible solution of $$Ax = b$$ $$x \geq 0$$

