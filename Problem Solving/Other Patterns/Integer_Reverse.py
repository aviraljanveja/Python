# Reversing an integer without converting to string

# Take an integer input from the user
n = int(input("Enter an integer: "))

# Initialize the result variable to store the reversed integer
result = 0

# Start a loop that will continue as long as there are digits left in n
while n > 0:
    # Get the last digit of n using modulus operator
    remainder = n % 10

    # Add remainder to the current result, while moving current digits to the left via multiplication by 10
    result = result * 10 + remainder

    # Remove the last digit from n by doing integer division by 10
    n = n // 10

# Print the reversed integer
print("Reversed integer:", result)
