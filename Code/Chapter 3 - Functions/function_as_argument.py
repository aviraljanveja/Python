# Demonstrating how functions can be passed as arguments to other functions.
# We have three functions: greet, name and display_message.

def greet():
    return "Hello "


def name():
    return "Alice!"


def display_message(message_function, name_function):
    # The display_message function takes two function
    # arguments: message_function and name_function.
    message = message_function() + name_function()
    print(message)


# Pass 'greet' and 'name' functions as arguments to 'display_message'
display_message(greet, name)  # Output: Hello Alice!
