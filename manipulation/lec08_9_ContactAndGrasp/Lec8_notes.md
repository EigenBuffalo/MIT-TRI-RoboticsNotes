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
$f_{C}^{B_p}= f_{C}^{B_q}, \tau_{C}^{B_q}=\tau_{C}^{B_p} + ^{B_q}P_{C}^{B_p}\times f_{C}^{B_p}$
- spatical force/torque representing in different frame
$f_{D}^{B_p}=^{D}R^{C}f_{C}^{B_p}, \tau_{D}^{B_p}=^{D}R^{C}\tau_{C}^{B_p}$
- ![statics](./assets/diagram1.png)
- $F_{g,W}^B = [0,0,0,0,0,-mg ]^T$
- contact frame z axis is the normal, it requires $f_{i,C_z}^B \ge 0$, (push not pull) 
- How to do the mechanics/ spatical force analysis?
   - step 1: Put all forces in same expressed-in frame, $F_{1,B}^{B_{Ci}}=^{B}R^{C}F_{C}^{B_{Ci}}$
   - step 2: same application point, **IMPORTANT**
      - apply a force and torque at some site of rigid body, i can always find a same spatial force apply at COM and have the exact same acceleration effect
      - do this to all spatial forces, after we move and shift, we do the analysis
      - $f_{1,B}^{B}= f_{1,B}^{B_{C1}}, \tau_{1,B}^{B}=\tau_{1,B}^{B_{C1}} + ^{B}P^{B_{C1}}\times f_{1,B}^{B_{B_{C1}}}$
      - three dimensional forces are real, but three dimensional torques are a summary of effect of a body. they differ 
- $F_{1,B}^{B}+F_{2,B}^{B}+F_{g,B}^{B}=0$, six equations, static equilibrium

## Horizontal force, fundamental concepts in manipulation
1. Friction Cone, at 43''
   - Coulomb friction: the magnitude of horizontal friction force is prop to the magnitude of normal force
   - most common friction is coulomb friction
   - $\left| f_{tangent} \right|_2 \le\mu f_{normal}$, $\mu:$ friction coefficient
   - $\sqrt{f_{1,cx}^{B^2}+f_{1,cy}^{B^2}}\le \mu f_{1,C_z}^B$
   - ![frictionCone](./assets/frictionCone.png), the force lives in side the cone to make it stable
   - if $f_z=0$, $f_x, f_y = 0$, $f_z$ is bigger, $f_{x,y}$ is bigger, which makes sense
   ![staticsII](./assets/diagram2.png)
   - the spatial force algebra make the equation neat, we move the cone at contacts to Center and analysis them together
   - **if the contact velocity can be made zero, friction will be whatever is necessay for contact acceleration to be zero**
   - else , **Principle of max dissipation**, largest force in the cone opposite direction of contact velocity

2. An interesting Example, table with four legs pushing
   - the level of rigid-body modelling doesnot capture everything
   - Since we donot know how force are distributed on the four legs. When pushing, the friction force on each leg is not determined. it could go left or go right or go straint.
   - whats the solver do? it picks one in the middle, least norm solution
   - any force that lives inside the cone is a possible solution
   - when u do simulation, u do LCP, linear Complimentarity problem, Polyhedral approximation

3. Contact points not at corners, penetrations
   -  even in 3D, you can pick the contact points for different contact pairs, but there is the **harder part**  
   -  when bodies are moving, contact points are moving. Their forces generated very uneasy to make consistent
   -  how do you define the normal vectors, even at corners： Use the gradient of the sign distance vectors
   -  Multi-point contact: put contact sphere at corners, many heuristics. More robust simulations
   -  "Hydroelastic contact" as implemented in drake: a pressure field model for fast robust approximation of the net contact force and moment between nominally rigid objects
   - Hydor-elastic is more expensive than point contact
   - less expensive than finite-element models
   - state space (for simulation, planning and control) is the original rigid body state
   - its not sampling, its taking an integral around the surface
   - summarize the integral of the pressure field in a wrench

## Questions
### 1. How to define the contact normal? Especially when it goes to a corner, its hard to define.

### 2. 3D force vs 3D torque, are they similar?
- No, they are different quantities. 3D force are real, 3D torque are a result of shifting frame to COMs. Only motors produce pure torque. 

### 3. How to contact force impact robot dynamics algorithm? or physice simulator?
- you calculate all kinds of contacts that are potential contacts and then in rigid body algorithm it does the recursive step through to common frame, summarizes things into a common frame, does all the algebra in the common frame

### 4. For a brick on a slope, is it still mg/2 at two corners?


### 5. How about friction cone in 3D?
- Polyhedral approximation, in order to use solvers. Square root makes cones, but not easy to use QP solvers. Sum of square root is nasty.
- After polyhedral approximation, write into linear complimentarity problem(LCP). The way to do simulation

### 6. How contact materials affect the equation? what is mu_static and mu_dynamic
- $\mu$ should comes in pairs of materials, but in simulation its a hassle to do it
![mu_dynamics vs mu_static](./assets/diagram3.png)
- the friction once you get start sliding tends to be lower than the sticking friction
