# A wrapper function is a function that "wraps" around another function to modify or enhance its behavior.
# You can build powerful patterns like logging, authentication and timing using wrappers.
# The wrapper function calls the original function inside it. Often used as decorators in Python.


# A decorator is a function that takes in another function (or method or class) as argument, wraps it inside another function(wrapper),
# and returns the wrapper function. Hence extending the behavior of the original function.
def my_decorator(original_function):

    # This wrapper function is going to be wrapped around the original function so it can execute code before and after it.
    # *args = Collects arbitrary number of arguments into a tuple.
    # **kwargs = Collects arbitrary number of keyword-arguments into a dictionary.
    # When writing a wrapper, we often don’t know in advance how many arguments the original function takes,
    # so we use *args and **kwargs as placeholder parameters to accept an arbitrary number of arguments.
    def wrapper(*args, **kwargs):

        # The code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Calling the original function here
        original_function(*args, **kwargs)

        # The code you want to be executed AFTER the original function is called
        print("After the function runs")

    return wrapper  # Return the wrapper function


# Decorating a simple function "greet" to extend its behavior with the my_decorator function defined above.
# @my_decorator is just a shortcut syntax for greet = my_decorator(greet)
@my_decorator
def greet(name):
     print(f"Hello {name}!")


greet("Aviral")  # Calling the decorated function with argument = "Aviral"
# Output :
# Before the function runs
# Hello Aviral!
# After the function runs
