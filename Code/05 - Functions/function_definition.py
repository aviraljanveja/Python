# A function is a block of code that performs a specific task. 
# They are reusuable and hence make your code more organized.


# Functions are defined using the def keyword, followed by the function name and parentheses().
# Parameters are the variables listed within the parentheses of the function definition,
# acting as placeholders for the actual values that will be passed in while calling the function, for example "n" here.
def isEven(n):
    if n % 2 == 0:
        return True  # The return statement is used to exit a function and return a value to the caller. In this case, it returns True if n is even.
    else:
        return False  # If no return statement is present, the function implicitly returns None.


# Calling a function : function_name(arguments)
# Arguments are the actual values that are passed to the function when it is called, for example 3 and 4 here.
print(isEven(3))  # Output = False
print(isEven(4))  # Output = True
