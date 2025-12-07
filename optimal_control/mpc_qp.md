

---
tags: optimal_control, algorithms
---

- [[mpc]]
- [[qp]]
-  How they work togather?
	- In MPC, the optimization problem in step 4 typically takes the form of a QP. The cost function ($J$) is a quadratic function of the input trajectory ($u$), and the constraints are affine constraints on the inputs and states.
	- The MPC algorithm formulates the control problem as a QP at each time step
	- A QP solver is then used to solve this optimization problem and determine the optimal input trajectory
	- The first element of this optimal trajectory is applied to the system
	- This process is repeated at each time step, with a new QP being formulated and solved based on the updated system state
 