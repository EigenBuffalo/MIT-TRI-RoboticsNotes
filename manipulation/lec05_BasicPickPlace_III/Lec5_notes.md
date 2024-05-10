**Last Lecture** 
**1**: Kinematic Frames / Spatial Algebra
**2**: Gripper Frame Plan Sketch
**3**: Forward Kinematics of iiwa
**4**: Differential Inverse Kinematics

# Today's Topic: Pseudo-inverse as an optimization
- $\underset{v}{find} \quad \text{s.t.}\quad J^{G}(q)v \approx V^{G_d}$
- when q is measured, this is linear $Ax \approx b$, A is jacobian, b is desired velocity
- $\underset{x}{min} \left | ax-b \right |^2$