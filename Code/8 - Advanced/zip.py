# zip : allows simultaneous iteration over multiple sequences.

alphabets = "abcde"
numbers = "12345"

for char, num in zip(alphabets, numbers):
    print(f"{char} is alphabet number {num}")

# Output :
# a is alphabet number 1
# b is alphabet number 2
# c is alphabet number 3
# d is alphabet number 4
# e is alphabet number 5
