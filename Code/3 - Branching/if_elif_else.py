# Basic if-else : The if condition is evaluated, if it is True the code inside the if-block runs,
# otherwise the code inside the else-block runs.

x = int(input("Enter a number : "))

if x % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# The if-elif-else chain allows you to check multiple conditions sequentially.
# The first condition that evaluates to True will have its block executed, and the rest will be skipped.
y = int(input("Enter a number : "))

if y > 0:
    print("Positive")
elif y < 0:
    print("Negative")
else:
    print("Zero")
