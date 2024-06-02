**Last Lecture** 
**1**: Kinematic Frames / Spatial Algebra
**2**: Gripper Frame Plan Sketch
**3**: Forward Kinematics of iiwa
**4**: Differential Inverse Kinematics

# Today's Topic: Pseudo-inverse as an optimization
- $\underset{v}{find} \quad \text{s.t.}\quad J^{G}(q)v \approx V^{G_d}$
- when q is measured, this is linear $Ax \approx b$, A is jacobian, b is desired velocity
- $\underset{x}{min} \left | ax-b \right |^2$, think about a=1,0.5,0.25 etc..., the less of a, the less steep of the parabola, and it is more likely to have a optimization far away from origin.
- add constraints to the optimization, <br> $min (ax-b)^2$  
  $s.t. \quad \left| x \right| \le 2$
- matrix case: $min \left \| Ax-b \right \|_2^2$  
    expands to: $x^TA^TAx - 2x^TA^Tb + b^Tb $
- $A^TA$ is real and symmetric, so it is positive definite, so it has real eigen values.
- A small eigen value indicates the parabola is strenched out in that direction.  
- Remember don't think about the rank of jacobian, but the singular values of jacobian.
- $A= U \Sigma V^T$, singular value decomposition. U and V: unitary matrix, $UU^T=I$; $\Sigma$: diagonal matrix with singular values
- $J^TJ$ 's singular values are close to zero. the shape of the parabola goes flat in some direction and you get very large joint velocities.
- Solving optimization by derivatives
  - scalar case: $2(ax^*-b)=0, x^*=\frac{b}{a}$
  - vector case: $x^*=(A^TA)^{-1}A^Tb$, $A^{\dagger}=(A^TA)^{-1}A^T$, pseudo-inverse 
    - pinv will return closest $x^*$ if there is no solution

# Quadratice Programming
- $min \quad \left | Ax-b \right | ^{2}_{2}$ 
- $s.t. \quad Cx \le d$
- quadratic objective with linear constraints
- convex QP are the ones we wanted. it requires $Q=Q^T$, so all the eigen values are greater than (or equal to) zero.

# Drake's optimization solver
- Drake provides great resources for mathematical programs, solvers, interfaces, parsers, etc.
```
prog = MathematicalProgram()
x = prog.NewContinuousVariables(3)
prog.AddCost(x.dot(x))
prog.AddConstraint(eq(np.array([[2, 3, 1], [5, 1, 0]]).dot(x), [1, 1]))
prog.AddConstraint(le(x, 2 * np.ones(3)))
result = Solve(prog)
```

# Type of Constraints
- how to add Position and Acceleration Constraints based on joint velocity optimization? 
  - **By Euler integration and differentiation**
  - $\underset{v_n}{min} \quad \left| J^G(q)v_n - V^{G_{des}} \right|^2_2$, $v_n$ is next velocity
  - $s.t. \quad v_{min} \le v_n \le v_{max}$
  - $\quad \quad q_{min} \le q+hv_n \le q_{max} $, joint position limits
  - $\quad \quad \dot{v}_{min} \le \frac{v_n-v}{h} \le \dot{v}_{max}$, joint acceleration limits
- same approaches apply to the torque limits, manipulation equations are required to calculate the torques and linearization
- collision constraints
- similar to MPC with 1 timestep case. 1 timestep MPC is a linear problem. timestep over two will be nonlinear, predicting forward over q, adding nonlinearity to decision variables.

# Infinite solutions case (e.g. redundancy)
- Beautiful idea, task prioritization via nullspace projection
- Whenever $J^TJ$ has nullspace, you can put a secondary objective in the nullspace in the primary objective.
- Call P an orthonormal basis of null(J), $P = I - J^{\dagger}J$
- $min \left| Jv -V \right|^2_2 +  \left| P(v-K (q^d-q)) \right|^2_2$, joint centering constraint
- Do everything u can to fulfill first objective, pick some desired $q^d$(comfortable position), in the nullspace of primary objective, try to get to as close as possible to that position.
- by left multipy P, everything outside nullspace of primary task, turns into 0. Only in the directions that are completely flat that I allow second thing take a value, round in every direction. Joint centering is always the last level of priority.
- K is like a gain, stiffness


# diffIK and linear programming
- $\underset{v_\alpha,\alpha}{max} \quad \alpha$
  $s.t. \quad J^G v_n = \alpha V^G$
  $ \quad \quad \quad 0 \le \alpha \le 1$
- and additional constraints
- worst case: $\alpha = 0, v_n=0$, is a valid solution 

# Questions
## 1. solving qp with constraints vs. solving unconstrained qp, add constraints later
- Always the former one is better. Solving constrained objective with constraints simultaneously is the right way to do.

## 2. For problems that are close in configurations, warm start is useful?
- Yes, warm start is useful. It is a good idea to use the previous solution as the initial guess for the next optimization.

## 3. When formulating iiwa's acceleration limits, do we need to filter the signal?
- Usually not, iiwa's driver is running and filtering at higher rates. The position_measured are relatively smooth enough to use directly

## 4. What about having a small constant in P(nullspace projection matrix)
- It comes into the cost function tunning area, like RL, put a lot obj in cost function and tunes.
- way cleaner put in the nullspace