# Reversing an integer without converting to string

# Take an integer input from the user
n = int(input("Enter an integer: "))

# Initialize the result variable to store the reversed integer
result = 0

# Start a loop that will continue as long as there are digits left in n
while n > 0:
    # Get the last digit of n using modulus operator
    remainder = n % 10

    # Add the remainder to the current result, moving existing digits to the left by multiplying result by 10
    result = result * 10 + remainder

    # Remove the last digit from n by doing integer division by 10
    n = n // 10

# Print the reversed integer
print("Reversed integer:", result)
