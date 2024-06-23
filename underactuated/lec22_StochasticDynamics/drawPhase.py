import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(-10, 10, 400)

# Calculate dot{x} = -alpha * x
alpha = 1  # You can adjust the value of alpha as needed
xdot = -alpha * x

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, xdot, label='dot{x} = -alpha * x')
plt.title('Phase Portrait of dot{x} = -alpha * x')
plt.xlabel('x')
plt.ylabel('dot{x}')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
