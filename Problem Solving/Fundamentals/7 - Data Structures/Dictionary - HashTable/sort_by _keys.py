# Sorting Dictionaries by Keys

squares = {3: 9, 1: 1, 2: 4}
print(squares)  # Output = {3: 9, 1: 1, 2: 4}

# To sort a dictionary by its keys, you can use the sorted() function
# which returns the sorted key,value pairs as tuples (key, value)
# They can then be converted back to dictionary using the dict() constructor
sorted_squares = dict(sorted(squares.items()))
print(sorted_squares)  # Output = {1: 1, 2: 4, 3: 9}

# You can sort in descending order by setting the reverse parameter to True.
reverse_sorted = dict(sorted(squares.items(), reverse=True))
print(reverse_sorted)  # Output = {3: 9, 2: 4, 1: 1}
