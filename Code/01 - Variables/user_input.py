# User Input
# The input() function is used to take user input in Python.

# Basic Input
name = input("Enter your name : ")
print("Hello", name, "!")  # Output = Hello Avi !

# Type Casting
# The input is always read as a string by default, so you need to cast it to other types as required.
x = input("Enter a number : ")
print(5 * x)  # Output = 5 * "5" = "55555" (string concatenation)

y = int(input("Enter a number : "))
print(5 * y)  # Output = 5 * 5 = 25 (integer multiplication)