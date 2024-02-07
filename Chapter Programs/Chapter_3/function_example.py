# A first simple function example.

def add(a, b):
    return a + b  # Directly returned a+b instead of defining a new variable


num1 = int(input("Enter first integer : "))
num2 = int(input("Enter second integer: "))

print("The sum is equal to :5", add(num1, num2))
# Directly passed the function as an argument in the print statement,
# instead of defining a new sum variable.
