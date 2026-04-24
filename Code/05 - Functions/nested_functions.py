# Nested functions are functions defined inside other functions.
# They have access to variables and parameters from the enclosing function's scope,
# and they can also access global variables.

# Nested functions are often used as helper functions to perform specific tasks
# within the context of the outer function,
# improving code readability and modularity without polluting the global namespace.

# A simple nested-functions example.
def outer_function(x):
    def inner_function(y):
        return x + y

    # Call the inner function
    result = inner_function(5)
    return result


# Call the outer function
print(outer_function(4))  # Output = 9
