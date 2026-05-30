# A wrapper is a nested function that "wraps" around another function to modify or enhance its behavior.
# You can build powerful patterns like logging, authentication and timing using wrappers.
# The wrapper function calls the original function inside it. Often used alongside decorators in Python.


# A decorator is a function that takes in another function as an argument, nests it inside a wrapper function,
# and returns the wrapper. Hence extending the functionality of the original function without modifying it.
def my_decorator(original_function):

    # When writing a wrapper, we often don’t know in advance how many arguments the original function will take,
    # Hence, we use *args and **kwargs as placeholder parameters to accept an arbitrary number of arguments.
    def wrapper(*args, **kwargs):

        # Code to be executed BEFORE the original function is called
        print("Before the function runs...")

        # Calling the original function, it shares the parameters with the wrapper function using *args and **kwargs
        original_function(*args, **kwargs)

        # Code to be executed AFTER the original function is called
        print("After the function runs...")

    return wrapper  # Return the wrapper function, thereby effectively replacing the original function, whenever the decorator is applied.


# Decorating a simple function "greet" to extend its behavior with the my_decorator function defined above.
# @my_decorator is just elegant and shorter syntax (syntactic sugar) for "greet = my_decorator(greet)"
@my_decorator
def greet(name):
     print(f"Hello {name}")


greet("Aviral")  # Calling the decorated function "greet" with argument "Aviral"
# Output :
# Before the function runs...
# Hello Aviral
# After the function runs...
