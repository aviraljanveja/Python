# Arbitrary arguments are used when you do not know how many arguments will be passed into your function by the user beforehand.
# To handle this, you can use the *args & **kwargs syntax in the function definition.

# * is the unpacking operator, and it allows you to pass a variable number of arguments to a function.
# *args allows you to pass a variable number of arguments to a function. It collects them into a tuple.
# **kwargs allows you to pass a variable number of keyword arguments to a function. It collects them into a dictionary.
# You can also use *args and **kwargs together in the same function definition, but *args must come before **kwargs.


def arbitrary_arguments(*args, **kwargs):
    print("Positional arguments (args) =", args)
    print("Keyword arguments (kwargs) =", kwargs)


# Example usage:
arbitrary_arguments(1, 2, 3, name = "Avi", age = 31, work = "AI Engineer")
# Output:   
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Avi', 'age': 31, 'work': 'AI Engineer'}
