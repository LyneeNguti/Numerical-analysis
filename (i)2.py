import numpy as np

def divided_difference(x, y):
  """Computes the divided differences for the given data points.

  Args:
    x: The x-values of the data points.
    y: The y-values of the data points.

  Returns:
    The divided difference table.
  """

  n = len(x)
  diff = np.zeros((n, n))
  diff[:, 0] = y

  for j in range(1, n):
    for i in range(n - j):
      diff[i, j] = (diff[i + 1, j - 1] - diff[i, j - 1]) / (x[i + j] - x[i])

  return diff

def newton_interpolation(x, data):
  """Computes the coefficients of the Newton's interpolation polynomial.

  Args:
    x: The x-values of the data points.
    data: The y-values of the data points.

  Returns:
    The coefficients of the Newton's interpolation polynomial.
  """

  diff = divided_difference(x, data)
  coeffs = diff[:, 0]
  return coeffs

# Example usage:
x_data = np.array([1, 2, 3, 4])
y_data = np.array([1, 4, 9, 16])

newton_coeffs = newton_interpolation(x_data, y_data)
print(newton_coeffs)
