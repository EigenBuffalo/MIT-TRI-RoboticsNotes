# Today's Topic outline: Motion Planning
There are two types of Motion Planning, Optimization based and Sample based
- Motivation: move fast, within dynamic limit
- Forward kinematics: $^{w}X^{B}=^{w}f_{kin}^{B}(q)$
- Inverse kinematics:  $q = f_{kin}^{-1}(X^{B})$
  - closed solution for 6 dof robot, given some redundency paramter(elbow-up etc)
  - "IKFast" usually sampling on last dof and call IKFast, almost a closed form solution
  - A rich history of IK, roboticsist doing in the 1980s.
  - Kinematics of rigid bodies are actually polynomials with polynomial constraints. There are tools for solving algebratic geometry
  numerical algebraic geometry and algebraic kinematics.pdf
- Optimization-based Inverse Kinematics:
  - rule of thumb: keep your objective super simple，a minimum touch of constraints
  - $\min_{q}\left | q-q_{0} \right |^{2}$, $q_{0}$ is a robot comfort configuration
  - $st. X^{B} = f_{kin}^{B}(q)$
  - Play interactive IK KUKA example
  - When you add a minimum distance constraint, a collision avoidance constraint, then it is doing smart things behind the scenes. It's not KD tree. It is x along bounding box, broad face collision detection. It does try to give you an interface to say the thresholds on that and it will do smart stuff for you.
- Motion-Planning, Optimization Based
  1. Diff IK or IK? DiffIK is only thinking about incremental changes
  2. How to form your optimization problem, very important
- Examples of setting up gripper constraints:
  - If i said, solve for the position on the grasp on the handle bar and then call IK for that exact position, then I would have overly constrained the solution space. It would be much better to leave for the freedom for the IK to solve. 
  - if adding static balance of the cylinder, estimating friction and adding kinematics constraints might be a good direction.
  - MinimumDistanceConstraint Class Reference
    - N bodies, distance between each two of them, the smallest distance has to be greater than the MDC constraint
    - Go through N*N pairs distances, make sure all is greater than constraints. How to make it computationally efficient? It has filter and clever data structures
    - Collision free motion planning game, but picking stuff up is a pain. there are some trick and dirty codes.
- Minimum Distance Constraint Geometry Example
  - 2-link robot with a narrow wall, the configuration space will be like (on the left)
  - adding grasp constraint, green region indicates end pos inside a small region(easier to visualize)
  - pink: collision with shelf, make it all complex.
  - Optimization has to find the corridor inside the pink on green
  - Optimization base Motion Planning: solving a handful of positions at the same time, solving for N*q. We asked they are related so they dont jump over the places. At every q, we ask it to handle the kinematic constraints.
  - Motion Planning as a (nonconvex) optimization
    - $min_{q_{0}...q{N}}\sum|q_{n+1}-q_{n}|^{2}$, evenly distributed
    - $st.q_{0}=q_{start}$
    - $q_{N}=q_{goal}$
    - $|q_{n}|_{1}\geq 1 (\forall n)$, outside the red box
    - The classic local minima of trajectory optimization. It happens when you have to move violate constraints. It used last point result as initial comfort guess for next one. 
    - The richness of costs and constraints that we have in optimization, are harder to do in the sampling world
    - The most important idea here is that rich costs and constraints, solve these optimizations, sequence them together and you have trajectories. The details there are about maybe how you parameterize that trajectory
    - Dynamic trajectory optimization vs Kinematic trajectory optimization(suggesting Use B-Spline)
| Column 1 | Column 2 |
|:--------:|:--------:|
| Bezier Curves   | B-Splines (basis, a different choice of basis funtions)   |
| Piecewise Polynomial   | $q(t)=\sum\alpha_{k}N_{k}(t)$, <br> $N_{k}(t)$ is greater than 0 and can be normalized to 1, and its sparse. Always taking a weighted average of the points   |
| $q(t)=\sum\alpha_{k}(t-t_{0})^{k}$, one piece   | $\alpha_{k}$ are control points, weighted average on activated control points.   |
| search over coefficients $\alpha_{k}$   | convex hull property, guaranteed joint limits   |
| the derivation of bezier is one order less bezier   | the derivation of B-Spline is one order less B-spline. so easy to add velocity constraints  |

