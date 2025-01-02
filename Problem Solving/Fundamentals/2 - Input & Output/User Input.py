# User Input
# The input() function is used to take user input as a string in Python.

# Basic Input
name = input("Enter your name : ")
print(f"Hello {name} !")

# Type Casting
# The input is always read as string by default, so you need to cast it to other types as needed.
age = int(input("Enter your age : "))
print(f"Wow, glad to know you are {age} years old !")

pi = float(input("Enter the value of pi upto 5 decimal places : "))
print(f"The pi is approximately : {pi:.2f}")
