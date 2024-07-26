import numpy as np

def power_iteration(A, num_simulations):
    b_k = np.random.rand(A.shape[1])
    
    for _ in range(num_simulations):
        # calculate the matrix-by-vector product Ab
        b_k1 = np.dot(A, b_k)
        
        # calculate the norm
        b_k1_norm = np.linalg.norm(b_k1)
        
        # re normalize the vector
        b_k = b_k1 / b_k1_norm
    
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k))
    return eigenvalue, b_k

# Define the matrix
A = np.array([[4, 1, 1],
              [1, 3, -1],
              [1, -1, 2]])

# Number of iterations
num_simulations = 1000

# Compute the largest eigenvalue and corresponding eigenvector
eigenvalue, eigenvector = power_iteration(A, num_simulations)
print("Power Iteration Method:")
print("Eigenvalue:", eigenvalue)
print("Eigenvector:", eigenvector)
