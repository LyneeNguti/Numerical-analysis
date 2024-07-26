import numpy as np

def qr_algorithm(A, num_iterations=100, tol=1e-6):
  """Computes the eigenvalues and eigenvectors of a matrix using the QR algorithm.

  Args:
    A: The input matrix.
    num_iterations: The maximum number of iterations (default: 100).
    tol: The tolerance for convergence (default: 1e-6).

  Returns:
    A tuple containing the eigenvalues and eigenvectors.
  """

  n, _ = A.shape
  Ak = A.copy()

  for _ in range(num_iterations):
    Q, R = np.linalg.qr(Ak)
    Ak = R @ Q

    if np.allclose(Ak, np.diag(np.diagonal(Ak)), atol=tol):
      break

  eigenvalues = np.diagonal(Ak)
  eigenvectors = Q
  return eigenvalues, eigenvectors

# Example usage:
A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])
eigenvalues, eigenvectors = qr_algorithm(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
