# Sorting Dictionaries by Values

squares = {3: 9, 1: 1, 2: 4}
print(squares)  # Output = {3: 9, 1: 1, 2: 4}

# Define a function to return the "value" from the (key, value) tuple.
def get_values(item):
    return item[1]

# Sorting by values using the custom function
sorted_sq = dict(sorted(squares.items(), key=get_values))
print(sorted_sq)  # Output: {1: 1, 2: 4, 3: 9}

# Sorting in descending order by setting the reverse parameter to True.
reverse_sorted_sq = dict(sorted(squares.items(), key = get_values, reverse=True))
print(reverse_sorted_sq)  # Output = {3: 9, 2: 4, 1: 1}
