# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

# Length of the tuple
print("Length of the tuple:", len(my_tuple))  # Output: 5

# Accessing elements of the tuple
print("First element:", my_tuple[0])          # Output: 1
print("Last element:", my_tuple[-1])          # Output: 5

# Slicing a tuple
print("Slice of the tuple:", my_tuple[2:4])    # Output: (3, 4)

# Concatenating tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)       # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Iterating over a tuple
for element in my_tuple:
    print(element)

# Count occurrences of an element
print("Count of '3' in the tuple:", my_tuple.count(3))  # Output: 1
