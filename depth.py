# Define the function and its derivative
def f(x):
    return x**3 - 0.165*x**2 + 3.993e-4

def df(x):
    return 3*x**2 - 0.33*x

# Initial guess
x0 = 0.05  # This is a reasonable starting point based on the problem context

# Perform three iterations of Newton's method
iterations = 3

# Newton's method implementation
for i in range(iterations):
    f_x0 = f(x0)
    df_x0 = df(x0)
    
    if df_x0 == 0:
        print("Zero derivative. No solution found.")
        break
    
    x1 = x0 - f_x0 / df_x0
    absolute_relative_error = abs((x1 - x0) / x1) * 100
    
    print(f"Iteration {i+1}: x = {x1:.6f}, Absolute Relative Approximate Error = {absolute_relative_error:.6f}%")
    
    # Update x0 for the next iteration
    x0 = x1

# Final result
print(f"The estimated depth 'x' to which the ball is submerged under water after three iterations is approximately: {x1:.6f} meters")
