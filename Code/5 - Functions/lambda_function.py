# Lambda Functions
# Use lambda functions when an anonymous function is required for a short period of time.
# A lambda function can take any number of parameters, but can only have one expression.

# Example 1 : Add 10 to "a" and return the result
x = lambda a : a + 10
print(x(5))  # Output = 15

# Example 2 : Multiply "a" with argument "b" and return the result
x = lambda a, b : a * b
print(x(5, 6))  # Output = 30

# Example 3 : Sum a, b, c and return the result
x = lambda a, b, c : a + b + c
print(x(5, 3, 1))  # Output = 9

# Sorting a dictionary by values using a lambda function
dict1 = {'a': 3, 'b': 1, 'c': 2}
sorted_dict1 = dict(sorted(dict1.items(), key = lambda item : item[1]))
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}
