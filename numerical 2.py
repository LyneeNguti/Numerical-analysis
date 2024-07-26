import numpy as np

def trapezoidal_integration(f, a, b, n):
  """Calculates the numerical integral of a function f using the trapezoidal rule.

  Args:
    f: The function to integrate.
    a: The lower limit of integration.
    b: The upper limit of integration.
    n: The number of intervals.

  Returns:
    The approximate integral of f over [a, b].
  """

  h = (b - a) / n
  x = np.linspace(a, b, n + 1)
  y = f(x)
  return h * (y[0] + y[-1] + 2 * np.sum(y[1:-1])) / 2

# Example usage:
def f(x):
  return x**2

a = 0.0
b = 2.0
n = 10
integral = trapezoidal_integration(f, a, b, n)
print(integral)  # Output: approximately 2.66666666667
