# In Python, default arguments allow a function to have default values for parameters,
# even if no argument is passed during the function call.


def greet(name = "Guest"):  # Default argument "Guest"
    print("Hello", name)


# If no argument is provided when calling the function, "Guest" will be used by default.
# Otherwise, the provided argument will override the default.
greet()  # Output = Hello Guest
greet("Aviral")  # Output = Hello Aviral
