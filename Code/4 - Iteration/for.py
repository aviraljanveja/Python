# for Loop : A for loop is used to iterate over a sequence. For example, a range of numbers or characters in a string. 
# It executes a block of code for each item in the sequence.


text = "aviral"


# Iterating directly over values
for char in text:
    print(char, end = " ")  # Output = a v i r a l


print()  # new line


# Iterating over indices
for i in range(len(text)):
    print(f"{text[i]}:{i}", end = " ")  # Output = a:0 v:1 i:2 r:3 a:4 l:5


print()  # new line


# Reverse iteration over values using slicing. The [::-1] slice creates a reversed copy of the string.
for char in text[::-1]:
    print(char, end = " ")  # Output = l a r i v a


print()  # new line


# Reverse iteration using the range function with a negative step. The range(length-1, -1, -1) generates indices from the last index to the first index.
for i in range(len(text)-1, -1, -1):
    print(f"{text[i]}:{i}", end = " ")  # Output = l:5 a:4 r:3 i:2 v:1 a:0


print()  # new line


# break : Terminates the loop early.
for i in range(10):
    if i == 5:
        break
    print(i, end = " ")  # Output = 0 1 2 3 4


print()  # new line


# continue : Skips the current iteration and moves on to the next.
for i in range(10):
    if i == 5:
        continue
    print(i, end = " ")  # Output = 0 1 2 3 4 6 7 8 9