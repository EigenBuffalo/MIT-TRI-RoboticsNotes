import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(-1.5, 1.5, 500)
xdot = x - x**3

# Create the plot
plt.figure(figsize=(8, 4))
plt.plot(x, xdot, label=r'$\dot{x} = x - x^3$')
plt.title('Phase Portrait')
plt.xlabel('x')
plt.ylabel(r'$\dot{x}$')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Marking the equilibrium points
plt.scatter([0, 1, -1], [0, 0, 0], color='red')
plt.annotate('Unstable', xy=(0, 0.1), xytext=(0, 10), textcoords='offset points', ha='center')
plt.annotate('Stable', xy=(1, 0.1), xytext=(0, 10), textcoords='offset points', ha='center')
plt.annotate('Stable', xy=(-1, 0.1), xytext=(0, 10), textcoords='offset points', ha='center')

# Add arrows to indicate direction of movement
for pt in np.linspace(-1.5, 1.5, 20):
    slope = pt - pt**3
    plt.arrow(pt, 0, 0.1*np.sign(slope), 0, color='blue', head_width=0.05, head_length=0.1)

plt.grid(True)
plt.legend()
plt.show()
