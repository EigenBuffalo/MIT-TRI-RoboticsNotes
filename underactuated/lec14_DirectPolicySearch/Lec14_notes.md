## Last Lecture
- Limit Cycle Stability (Van Der Pol Oscillator)
  - $\underset{t\rightarrow \infty}{lim} \quad x(t)\rightarrow x^{*}$, 
  - stability type 1, too much to ask, 
    - $\left \| x(t)- x^{*} \right \|\rightarrow 0$
    - difference between trajectory and nominal traj goes to zero
  - stability type 2, orbital stability, humanoid seeks this kind of stability
    - $\underset{\tau}{min}\left \| x(t)- x^{*} \right \|\rightarrow 0$
    - Like at each state do a search, find the minimum and satfifies the constraint
- Contact Dynamics
  - ![rimlessWheel](./rimlessWheel.svg)
  - continuous "stance phase pendulum dynamics"
  - discrete impact event at "foot strike"
  - $\dot{\theta}^{+}=cos(2\alpha)\dot{\theta}^{-}$
  - $\dot{\theta}(t^+)=cos(2\alpha)\dot{\theta}(t^-)$
  - the larger $\alpha$, the more energy it will lose after contact. $\alpha$ goes to 0, it will like a wheel

## Today's Topic: Hybrid Trajectory Optimization
1. How do we find limit cycle? How do we find fix points
  - $\dot{x}=f(x)$




