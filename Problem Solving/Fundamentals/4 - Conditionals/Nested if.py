# Nested if statements
# You can place if statements inside other if statements for more complex conditions.

x = 15
if x > 0:
    if x % 3 == 0:
        print("Positive and divisible by 3")
    else:
        print("Positive but not divisible by 3")
