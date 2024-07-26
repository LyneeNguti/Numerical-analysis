import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

# Generate some data points
x = np.linspace(0, 10, 100)
y = 2.5 * x + np.random.normal(0, 1, x.shape)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = sps.linregress(x, y)

# Plot the data and the fitted line
plt.scatter(x, y, label='Data')
plt.plot(x, slope * x + intercept, label='Fitted line', color='red')
plt.legend()
plt.show()
print(f"Slope: {slope}, Intercept: {intercept}")
