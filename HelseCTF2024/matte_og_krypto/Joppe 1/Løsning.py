from sympy import symbols, solve
from numpy.polynomial.polynomial import Polynomial

# Coordinates provided
points = [(-500, 1229), (500, 2229), (1000, 2729)]

# Fit a linear polynomial to these points
p = Polynomial.fit([point[0] for point in points], [point[1] for point in points], 1)

# The polynomial is of the form ax + b, we need to find the value at x=0, which is simply b
safe_code = p.convert().coef[0]  # Convert to standard form and get the constant term

#1729
