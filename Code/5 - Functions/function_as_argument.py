# An example of passing function as an argument to another function.

dict1 = {'a': 3, 'b': 1, 'c': 2}

def get_values(item):  # Define a function to return the "value" from the (key, value) tuple of the dictionary
    return item[1]  # and passing it as an argument in sorted() function.

sorted_dict1 = dict(sorted(dict1.items(), key=get_values))  # Sorting the dictionary by values.
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}
