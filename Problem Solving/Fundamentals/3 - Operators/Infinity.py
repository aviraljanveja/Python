# Positive and Negative Infinity
# Why Use Them?
# Useful in algorithms that require boundary conditions. For example, finding min/max in an array.
# Handle overflows or represent unbounded ranges in mathematical computations.

a = float('inf')  # Positive Infinity (inf): Represents a value greater than any finite number.
b = -float('inf')  # Negative Infinity (-inf): Represents a value less than any finite number.

print(a > 1e308)  # Output: True
print(b < -1e308)  # Output: True

# So, 1e308 equals 1 * 10^308
# It is close to the upper limit of floating-point numbers in Python.
# Since float('inf') is indeed greater than any finite value, the output is True.
