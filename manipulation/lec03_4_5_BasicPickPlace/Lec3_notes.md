## Last Lecture
- What is **Context** in Drake?
  - $x[n+1]=f(x[n],u[n],w[n],n,p)$
    - x: state, discrete, continuous states
    - u: input, multiple ports
    - w: random disturbances
    - n: time
    - p: parameters
  - Instead of asking API, what is x,u,w,n,p, there is struct recording actual values. One place write down everythin
    ```
    struct Context {
        x,
        u,
        w, 
        n,
        p
    };
    ```
  - What is Diagram?
    - array of subsystem context
    ```
    struct Context{
        subsystem context[]
    }
    ```
- Diagram abstraction is the way that you build heirarchies of more and more complicated systems by combining simple systems together

## Today's Topic outline
1. Kinematic Frames / Spatial Algebra
- Translations
  - $^{B}P_{C}^{A}:$position vector of A, relative to B, represented in frame C; 
in code, the vector is P_BA_C
  - XYZ axis ~ RGB in color. In world frame, X in front, Y in left, Z in upwards
  - It worth spending some time making your frame transforms notation consistent.
  - shorthand:
    - $^{B}P_{B}^{A}\equiv ^BP^{A}$, $^{W}P_{W}^{A}\equiv P^{A}$
- Rotations
  - $^{B}R^{A}$, rotation of frame A relative to frame B
  - either rotation matrix, unit quaterion, angle-axis, euler angles
- Question: if frame C and frame D are parallel, where are A,B's relationships in order to $^{B}P_{C}^{A}=^{B}P_{D}^{A}$?
- Spatial Algebra
  - Addition: $^{A}P_{F}^{B}+^{B}P_{F}^{C}=^{A}P_{F}^{C}$
  - Additive inverse: $^{A}P_{F}^{B}=-^{B}P_{F}^{A}$
  - Multiplication by R: $^{A}P_{G}^{B}=^{G}R^{F}\cdot^{A}P_{F}^{B}$
  - Multiplication: $^{A}R^{B}\cdot^{B}R^{C}=^{A}R^{C}$
  - Rotation inverse: $(^{A}R^{B})^{-1}=^{B}R^{A}$
  - Frame has both position and orientation, conbined called pose, $^{B}X^{A},(^{B}P_{B}^{A}+^{B}R^{A})$, pose A relative to B; 12 numbers are enough
  - pose is a noun; transform is a verb
  - For pose $^{B}X^{A}$, you never need a frame down at corner
2. Gripper Frame Plan "Sketch"
- Given object frame O, gripper frame G:
  - $O_{initial},^{W}X^{O_{initial}}$
  - $G_{initial},^{W}X^{G_{initial}}$
  - $O_{goal}, ^{W}X^{O_{goal}}$
- Intermediate quantity: where do you wanna put object in your hand frame: $^{G}X^{O}$
- Define $G_{pick},G_{prepick},G_{postpick},G_{place},G_{preplace},G_{postplace}$ these frames
- Given pose of gripper is pose in world in sequence, initial-prepick-pick-preplace-place-initial
- Linear interpolation(Lerp) and rotation interpolation(Slerp)
- In Drake, these interfaces are provided
- ```
  PiecewisePolynomial()
  PiecewisePose()
  PiecewiseQuaternionSlerp()
  PiecewiseTrajectory()
  BezierCurve()
  BsplineTrajectory()
  CompositeTrajectory()
  ExponentialPlusPiecewisePolynomial()
  ```  
3. Forward Kinematics of iiwa + WSG
- At joint, two frames overlapped at zero position and only rotate by joint by one angle
- $^{B_1}X^{M}\cdot^{M}X^{F}(q)\cdot^{F}X^{B_2}$
- In URDF, when adding bodies, they all have 6dof each;
- When adding joints, we are actually taking away 5dof from each body
- Kinematic tree for iiwa is more of a vine than a tree
- For dexterous hands, the picking up brick is like another branch off the world root node


