# A simple nested-functions example.


def outer_function(x):
    def inner_function(y):
        return x + y
        # So, to clarify, x here is not accessed as a global variable,
        # nor is it defined in the enclosing scope of the outer_function.
        # Still, inner_function has access to x from the enclosing scope
        # of outer_function because, x is a parameter of outer_function
        # and hence, accessible within the scope of inner_function.

    # Call the inner function
    result = inner_function(5)
    return result


# Call the outer function
print(outer_function(4))  # Output: 9
