# Python exception handling statements : 


# 1. try-except, else, finally : catch a specific exception and handle it safely without crashing the program.
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result is {result}")
except ValueError:
    print("That was not a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    # This runs only if no exception occurred
    print("Calculation completed successfully.")
finally:
    # This always runs, whether an exception occurred or not
    print("Finished the try-except block.")

print("\n---\n")


# 2. raise : manually raise an exception when a condition is not met.
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as err:
    print(f"Raised an exception: {err}")

print("\n---\n")


# 3. assert : assert a condition and stop execution if it is false
def divide(a, b):
    assert b != 0, "Divisor must not be zero"
    return a / b

try:
    print(divide(10, 2))
    print(divide(5, 0))
except AssertionError as err:
    print(f"Assertion failed: {err}")
