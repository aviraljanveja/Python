# list() constructor
# The list() function is a built-in Python constructor that creates a new list object.
# When used with a string, it iterates through each character of the string
# and stores them as individual elements in the list.

text = "python"
chars = list(text)
print(chars)  # Output = ['p', 'y', 't', 'h', 'o', 'n']

# Immutable to Mutable
# Strings are immutable, meaning their characters cannot be modified individually.
# Converting them to a list makes it possible to modify individual characters.
