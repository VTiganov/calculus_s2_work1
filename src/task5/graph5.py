import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Define the x range
x = np.linspace(2/3, 18, 400)

# Calculate z and y from the equations
z = np.cbrt(12 * x)  # Real root of z^3 = 12x
y = 2 / z  # From 2zy = 4

# Plot the solution curve
ax.plot(x, y, z, label='Solution curve: z³=12x and y=2/z', linewidth=3, color='blue')

# Create bounding planes at x=2/3 and x=18
yy, zz = np.meshgrid(np.linspace(min(y)-1, max(y)+1, 20), 
                     np.linspace(min(z)-1, max(z)+1, 20))

# Plane at x=2/3 (lower bound)
ax.plot_surface(np.full_like(yy, 2/3), yy, zz, 
                alpha=0.3, color='green', label='x=2/3 plane')

# Plane at x=18 (upper bound)
ax.plot_surface(np.full_like(yy, 18), yy, zz, 
                alpha=0.3, color='red', label='x=18 plane')

# Add points at the boundaries
ax.scatter([2/3, 18], 
           [2/np.cbrt(12*2/3), 2/np.cbrt(12*18)], 
           [np.cbrt(12*2/3), np.cbrt(12*18)], 
           color='black', s=100, label='Boundary points')

# Add labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Plot of the System with Bounding Planes')

# Set axis limits to properly show the planes
ax.set_xlim(0, 20)
ax.set_ylim(min(y)-1, max(y)+1)
ax.set_zlim(min(z)-1, max(z)+1)

# Add legend
ax.legend()

# Set viewing angle
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.show()