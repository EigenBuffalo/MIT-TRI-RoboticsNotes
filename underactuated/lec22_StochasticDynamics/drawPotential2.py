import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values
x = np.linspace(-2, 2, 400)

# Calculate the potential energy U(x) = -0.5 * x^2 + 0.25 * x^4
U = -0.5 * x**2 + 0.25 * x**4

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, U, label=r'$U(x) = -\frac{1}{2}x^2 + \frac{1}{4}x^4$')
plt.title('Potential Energy Function U(x)')
plt.xlabel('x')
plt.ylabel('U(x)')
plt.grid(True)
plt.legend()
plt.show()
