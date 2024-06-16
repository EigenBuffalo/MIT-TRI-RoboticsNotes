**Last Lecture** 
1. Hardware basics(iiwa + WSG)
2. Basic pick and place  
   - Kinematics / jacobian based control
   - moved a single known object assuming known pose
3. Geometric perception
   - pose estimation from depth for a single known object

## This week's Topic: 
- more complex scenes (many objects / diverse objects)
- still relatively simple manipulation(pick & place)
- try to build a "clutter" clearing at kitchen etc
- we are going to generalize perception system, build more complicated simulation, higher level state machine

## Simulation
1. How to generate diverse random simulations?
- Its actually pretty hard
2. Contact simulation
- Random dropping YCB objects and calculation the contact force to find a static equilibrium is actually doing a lot of work.
3. Spatial Forces
- $F = \begin{bmatrix}
\tau\\F 
\end{bmatrix}$
- $F_{name,C}^{B_P} = \begin{bmatrix}
\tau_{name,C}^{B_P}\\F_{name,C}^{B_P} 
\end{bmatrix}$, 6*1 vector, top 3 is rotational
- name: the name of the force; C is the force being expressed frame, $B_P$ is point where force is applied, recommendation use the body in the point name
- Spatial force addition: $F_{total,C}^{B_p} = \underset{i}{\sum}F_{i,C}^{B_p}$
- Shifting a spatial force from one application point, B_p, to another point, B_q, uses the cross product:
$$f_{C}^{B_p}= f_{C}^{B_q}, \tau_{C}^{B_q}=\tau_{C}^{B_p} + ^{B_q}P_{C}^{B_p}\times f_{C}^{B_p}$$

## Questions
### 1. 
