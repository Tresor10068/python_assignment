import numpy as np

# Define grid resolution
N = 100
x = np.linspace(0, 1, N)
y = np.linspace(0, 1, N)
dx = dy = 1 / N

# Create 2D grid of x and y values
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # z = x² + y²

# Approximate volume using summation
volume = np.sum(Z) * dx * dy
print("Approximate Volume under z = x^2 + y^2:", round(volume, 4))
