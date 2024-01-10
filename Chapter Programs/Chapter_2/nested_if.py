# Simple nested-if example.

x = float(input("Enter a number x: "))
y = float(input("Enter a number y: "))

if x == y:
    print("x and y are equal.")
    if y != 0:  # nested if condition.
        print("therefore, x/y is equal to", x/y)
elif x < y:
    print("x is smaller.")
else:
    print("y is smaller.")

print("Thanks!")
