# String examples and functions

# Concatenation : Combining two or more strings using the + operator.
a = "Hello"
b = "World"
result = a + " " + b
print(result)

print("------------------")

# Repetition : Repeating a string using the * operator.
original = "python "
repeated = original * 3
print(repeated)

print("------------------")

# length function : Returns the length of the string.
s = "abc"
length = len(s)
print(length)

print("------------------")

# Indexing : Allows you to access individual characters in a string
# by their position (index) within the string.
word = "Hello"
print(word[0])

print("------------------")

# Slicing : allows you to extract a portion of a string by specifying a range of indices.
slice1 = word[1:3:1]
# Extracts the substring from index 1 till 2, with single step.

slice2 = word[::]
# Extracts the full string.

slice3 = word[::-1]
# Extracts the entire string but in reverse
# as the step is negative.

print(slice1)
print(slice2)
print(slice3)
