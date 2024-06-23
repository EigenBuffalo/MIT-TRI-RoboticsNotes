import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(-10, 10, 400)

# Calculate the potential energy V(x) = 0.5 * alpha * x^2
alpha = 1  # You can adjust the value of alpha as needed
V = 0.5 * alpha * x**2

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, V, label='V(x) = 1/2 * alpha * x^2')
plt.title('Potential Energy vs. x for dot{x} = -alpha x')
plt.xlabel('x')
plt.ylabel('V(x) (Energy)')
plt.grid(True)
plt.legend()
plt.show()
