# Assignment:
# Write a program that does the following in order:
# 1. Asks the user to enter a number “x”
# 2. Asks the user to enter a number “y”
# 3. Prints out number “x”, raised to the power “y”.
# 4. Prints out the log (base 2) of “x”.


# Solution:
import numpy  # Importing numpy package

# Taking numerical input from the user.
x = float(input("Enter a number : "))
y = float(input("Enter another number : "))

# Using exponent operator to calculate x raised to the power y.
print(x, "raised to the power", y, "is equal to :", x ** y)

# Using numpy package for calculating logarithm of the variable.
print("log(base2) of", x, "is equal to :", numpy.log2(x))
