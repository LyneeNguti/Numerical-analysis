import numpy as np
import scipy.optimize as spo
import matplotlib.pyplot as plt

# Generate some data points
x_data = np.linspace(0, 10, 100)
y_data = 3 * np.sin(x_data) + np.random.normal(0, 0.5, x_data.shape)

# Define the model function
def model(x, a, b):
    return a * np.sin(b * x)

# Perform curve fitting
params, params_covariance = spo.curve_fit(model, x_data, y_data, p0=[2, 1])

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, model(x_data, *params), label='Fitted curve', color='red')
plt.legend()
plt.show()
print(f"Fitted parameters: {params}")
