# Sorting a dictionary by values using a lambda function

"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Example 1 : Add 10 to argument a and return the result
x = lambda a : a + 10
print(x(5))  # Output = 15

Example 2 : Multiply argument a with argument b and return the result
x = lambda a, b : a * b
print(x(5, 6))  # Output = 30

Example 3 : Sum arguments a, b, c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))  # Output = 13
"""

dict1 = {'a': 3, 'b': 1, 'c': 2}
print(dict1)  # Output = {'a': 3, 'b': 1, 'c': 2}

# Sorting by values using the lambda function
sorted_dict1 = dict(sorted(dict1.items(), key = lambda item : item[1]))
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}

# Sorting in descending order by setting the reverse parameter to True.
reverse_sorted_dict1 = dict(sorted(dict1.items(), key = lambda item : item[1], reverse = True))
print(reverse_sorted_dict1)  # Output = {'a': 3, 'c': 2, 'b': 1}


"""
Use lambda functions when an anonymous function is required for a short period of time.
It is the same as defining a function to return the "value" from the (key, value) tuple, 
and using it as the key in sorted().

def get_values(item):
    return item[1]

# Sorting by values using a regular function
sorted_dict1 = dict(sorted(dict1.items(), key=get_values))
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}
"""
