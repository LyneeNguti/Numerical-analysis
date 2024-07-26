

import random

def generate_random_number(lower_bound, upper_bound):
  """Generates a random integer between the given bounds.

  Args:
    lower_bound: The lower limit of the random number.
    upper_bound: The upper limit of the random number.

  Returns:
    A random integer between lower_bound and upper_bound (inclusive).
  """

  return random.randint(lower_bound, upper_bound)

# Example usage:
random_number = generate_random_number(1, 10)
print(random_number)
