# Nested if statements
# You can place if statements inside other if statements for more complex conditions.

x = int(input("Enter a number : "))

if x > 0:
    print("Positive")
    if x % 2 == 0:
        print("...and Even Number")
else:
    print("Non-Positive")
