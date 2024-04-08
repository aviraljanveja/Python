# Recursion Example :

def factorial(n):
    if n == 0:  # The base case
        return 1
    elif n > 0:
        return n * factorial(n - 1)  # The recursive step : function calling itself
    else:
        print(" I told you to enter a positive integer :/")


# Example usage:
user_int = int(input("Enter any positive integer : "))
result = factorial(user_int)
print("Factorial of", user_int, "is :", result)
