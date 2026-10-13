# Removing Elements

# Example dictionary: numbers as keys, squares as values
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# using del() : used to delete a key-value pair from the dictionary by specifying the key.
del(squares[3])
print(squares)  # Output = {1: 1, 2: 4, 4: 16, 5: 25}

# using pop() : removes the key-value pair at the specified key and returns the value associated with that key.
popped_value = squares.pop(4)
print(squares)  # Output = {1: 1, 2: 4, 5: 25}
print(popped_value)  # Output = 16
