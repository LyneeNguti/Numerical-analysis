import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

# Generate some data points
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Perform spline interpolation
spline = spi.CubicSpline(x, y)

# Generate points for interpolation
x_interp = np.linspace(0, 10, 100)
y_interp = spline(x_interp)

# Plot the data and the spline interpolation
plt.scatter(x, y, label='Data')
plt.plot(x_interp, y_interp, label='Spline interpolation', color='red')
plt.legend()
plt.show()
