import numpy as np

def gradient_descent(f, grad_f, x0, y0, learning_rate=0.1, num_iterations=100):
    """
    Performs gradient descent to minimize a function.

    Args:
        f: The function to be minimized.
        grad_f: The gradient of the function.
        x0: Initial x-value.
        y0: Initial y-value.
        learning_rate: The learning rate for gradient descent.
        num_iterations: The number of iterations to perform.

    Returns:
        The final x and y values after optimization.
    """

    x = x0
    y = y0

    for i in range(num_iterations):
        gradient = grad_f(x, y)
        x -= learning_rate * gradient[0]
        y -= learning_rate * gradient[1]

    return x, y

# Define the function
def f(x, y):
    return x**2 + y**2 - x*y + x - y + 1

# Define the gradient of the function
def grad_f(x, y):
    return np.array([2*x - y + 1, 2*y - x - 1])

# Initial guess
x0, y0 = 0, 0

# Perform gradient descent
x_min, y_min = gradient_descent(f, grad_f, x0, y0)

print("Minimum value found at x =", x_min, "and y =", y_min)
