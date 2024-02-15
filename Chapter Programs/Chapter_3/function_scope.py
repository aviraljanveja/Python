# Demonstrating how function scopes work.

global_var = 100


def my_function():
    global_var = 200  # Creates a new local variable named global_var
    # Shadows name 'global_var' from outer scope.
    # Avoid shadowing global variables by using different names for
    # local variables to prevent confusion and unexpected behavior.
    print("Inside function:", global_var)  # Prints the local variable


my_function()
print("Outside function:", global_var)  # Prints the global variable
