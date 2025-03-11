# Dictionary Membership Check : membership checks in dictionaries are
# generally used to check if a key exists in the dictionary.
# The in operator is commonly used for this purpose.

squares = {1:1, 2:4, 3: 9}

# Membership Check by Key
print(3 in squares)  # Output: True
print(5 in squares)  # Output: False

# Membership Check by Value
print(9 in squares.values())  # Output: True
print(10 in squares.values())  # Output: False
