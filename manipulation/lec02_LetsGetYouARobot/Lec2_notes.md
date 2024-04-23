# Today's Topic: Review of Robot hardware
## Industrial Robot vs Cobot
- Industrial robots try to execute trajectory with high precision,and can't detect collisions. They don't equiped other sensors besides position encoders.
- Cobot: add more sensors; design new controller
- Information bottleneck: with only joint torque sensor, there are always limited information. Is it a Point contact? or Multiple points contact? Surface contact etc. We could not determine it.
## Position Controlled vs Torque Controlled robot
- Most robot arms are position controlled. Why?
  - Most use electrical motors. Motor current is proportional to torque; voltage is proportional to speed.
  - Electrical motor are good working in high speed less torque region. So we need transmission. The transmission is extemly complicated. Lossy and Messy.
  - So if you want to control the torque on the joints, you cannot only use the motor current. 
  - How to get around the transmission? Get a sensor on the joint side and do feedback control. It is much easier to push a position sensor on the output shaft. And do PID control.
- Reflected inertia
  - Motors have inertia, they are scaled by gear ratio squared on the joint side
  - Lind(load) has inertia, they are shrunk by gear ratio squared on the motor side.
  - Motorists most of the time have to do more work to move themselves rotating around.
  - URDF does not have a field for reflected inertia, this is not good.
## Direct Drive Robot
  - No gearbox or gear ratio is less than 10.
  - Motor current is proportional to output torque
## Kuka iiwa's joint torque sensing
  - Joint torque sensor, difference maker. Stiffness ~ 5000 Nm / rad
## Series elastic actuators
  - The spring is a torque sensor. Two encoders measure the defection of spring. Stiffness ~ 100 Nm /rad
  - Motor has bandwidth, spring has bandwidth. They are combined and your system has bandwidth. There will be bandwidth limitations.
## Robot hand
  - Dexterous hands
  - Two finger grippers, Schunk WSG 50, like iiwa in grippers, torque sensing etc.
  - Coffee ground suction, jamming gripper.
  - Soft hand/actuator
  - Soft-bubble gripper & depth camera surrounding. Force sensing and geometry sensing in the hand.

## Put hardware into Simulation
- Physics Engine:MultibodyPlant<T>, Class Template Reference
- Geometry Engine: Scene graph, things are in collision or not


# Students' Questions:
1. An unexpected change in joint torque sensor could not decide what to do next, requires more information.
  - Standard thing: you sense something huge expected, you stop.
  - Clever thing: behavior tree & learning, future
2. In PID control of Position control of joints, do you change PID gains?
  - Most time No. PID control works shockingly well on robots.
  - Robot arms set PID in the factory and good to go for a lifetime. 
  - IIWA has brake on each joint. Turn on brake if joint is not moving. Avoid overheating of joint motors.
  - In aircraft or other subtle cases, you do gain-scheduled control.
3. How to implement joint PID controllers? digital analog or mechanical?
  - Nowadays, we use digital servos that run faster than 10k hz to run the joint servo PID. The inertia time constants are lower than 10k hz. So most people have switched to digital.
  - But in slower cases, analog servos are no problem.
4. When you have dexterous hand, how do you do gravity compensation?
  - Pick a constant pose of hand, compute intertia and telling the low-level controller. If hand is moving, treat them as disturbances.