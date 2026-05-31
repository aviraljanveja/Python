# Python exception handling statements


# 1. try, except, finally : catch a specific exception and handle it safely without crashing the program.
try:  # Any code that might raise an exception goes here
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result is {result}")
except ValueError:
    print("That was not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # This runs only if no exception occurred
    print("Calculation completed successfully.")
finally:
    # This always runs, whether an exception occurred or not
    print("Finished the try-except block.")


print("\n---\n")


# 2. raise : manually raise an exception when a condition is not met.
age = int(input("Enter age : "))
if age < 0:
    raise ValueError("Age cannot be negative")
else: 
    print(f"Age is {age}")


print("\n---\n")


# 3. assert : assert a condition and stop execution if it is false
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
assert denominator != 0, "Cannot divide by zero!"
print(numerator / denominator)
