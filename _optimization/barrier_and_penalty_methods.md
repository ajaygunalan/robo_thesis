---
tags: optimization
---


## Constrained Optimization Problem
> [!info] Problem Statement
> min $f(x)$  
> s.t. $x \in X$  
> where $X \in \mathbb{R}^n$

![[penalty_barrier_func.png]]

## Core Idea
> [!abstract] Approach
> - Approximation by an unconstrained problem
> - Solve a sequence of unconstrained optimization problems

> [!note] [[penalty_method]]
> Penalize for violating a constraint
> - Add penalty terms to the objective function that increase cost when constraints are violated
> - Converts constrained problems into unconstrained ones

> [!note] [[barrier_methods]]
> Penalize for reaching the boundary of an inequality constraint
> - Create "barriers" that prevent solutions from violating constraints
> - The barrier function grows to infinity as the solution approaches the constraint boundary

> [!important] Key Differences
> - **Penalty methods**: Allow constraint violation but penalize it
> - **Barrier methods**: Strictly enforce constraints by creating mathematical barriers hence this better

