import numpy as np
import matplotlib.pyplot as plt

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)

# Create a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D line
ax.plot3D(xline, yline, zline, 'gray')

# Scatter the 3D points
sc = ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='viridis') #

fig.colorbar(sc) # Add the colorbar

# Set the labels for the axes
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Show the plot
plt.show()