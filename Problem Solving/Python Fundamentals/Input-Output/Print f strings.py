# f-strings (formatted string literals) in Python
# provide a way to embed expressions inside string literals using curly braces {}.
# They were introduced in Python 3.6 to make string formatting more readable, concise, and efficient.

# An f-string is a string that is prefixed with an f or F and allows
# you to insert expressions inside curly braces {} directly within the string.
# These expressions are evaluated at runtime and formatted using the __format__() method.

# Basic Example
name = "Avi"
age = 25
print(f"Hello my name is {name}, I am {age} years old.")

# Math Expressions
x = 10
y = 20
print(f"The sum of {x} and {y} is {x+y}.")

# Formatting Numbers, Precision Control
pi = 3.1415926535
print(f"Pi rounded to 2 decimal places is {pi:.2f}")
