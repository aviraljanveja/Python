# Using break and continue in a for loop

for number in range(6):
    if number == 3:
        break  # Exit the loop when number 3 is encountered
    print(number)

print("--------------")

for number in range(6):
    if number == 3:
        continue  # Skip rest of the loop code for number 3
    print(number)
