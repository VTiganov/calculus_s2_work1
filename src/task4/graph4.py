import numpy as np
import matplotlib.pyplot as plt

a = 1

# Create a grid of x and y values
x = np.linspace(-1.5, 1.5, 400)
y = np.linspace(-1.5, 1.5, 400)
X, Y = np.meshgrid(x, y)

# Define the function for the implicit plot
F = X**7 + Y**7 - a * X**3 * Y**3

# Create the plot
plt.figure(figsize=(8, 8))
plt.contour(X, Y, F, levels=[0], colors='blue')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.title('Plot of $x^7 + y^7 = x^3y^3$')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('docs/img/graph_task4.png', dpi=600)