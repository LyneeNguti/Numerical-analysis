
import numpy as np

# Step 1: Define the function
def function(x):
    return np.sin(x)

# Step 2: Define the point at which to differentiate
x0 = np.pi / 4

# Step 3: Define a small interval (h)
h = 1e-5

# Step 4: Compute the finite difference approximation of the derivative
derivative_approx = (function(x0 + h) - function(x0)) / h

# Display the approximate derivative
derivative_approx


