# A first simple function example.

def even(a):  # Function definition and name.
    # Function Body.
    if a % 2 == 0:
        return print("Even Number")  # Using the return statement...
    else:
        return print("Odd Number")  # ...to print out the result.


num1 = int(input("Enter any integer : "))
even(num1)  # Calling the function with parameter 'num1'.
