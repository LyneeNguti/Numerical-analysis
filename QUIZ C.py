# Step 1: Define the known points
x1, y1 = 2.00, 7.2
x2, y2 = 4.25, 7.1

# Step 2: Define the point at which we want to estimate the value of y
x = 4.0

# Step 3: Use the linear interpolation formula to find y at x = 4.0
y = y1 + ((x - x1) / (x2 - x1)) * (y2 - y1)

# Display the result
print(f"The value of y at x = {x} is {y}")
