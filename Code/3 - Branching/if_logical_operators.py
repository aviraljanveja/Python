# Logical operators like and, or, not can be used to combine multiple conditions

x = 10
y = 20

if x > 5 and y > 15:
    print("Both conditions are True")

if x > 15 or y > 15:
    print("At least one condition is True")

if not x < 5:
    print("x is not less than 5")


# Python supports chaining conditions for readability.

if 0 < x < 20:  # short hand for x > 0 and x < 20
    print("x is between 0 and 20")
