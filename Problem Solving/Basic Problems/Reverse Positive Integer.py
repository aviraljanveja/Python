# Reversing an integer without converting to string
# For example 12345 is reversed to 54321

# Take an integer input from the user
n = int(input("Enter an integer: "))

# Initialize the result variable to store the reversed integer
result = 0

# Start a loop that will continue as long as there are digits left in n
while n > 0:
    # Extract the last digit from n using modulus operator and store it in the remainder variable
    remainder = n % 10

    # Update the result by multiplying it with 10 and adding the last digit.
    # This effectively appends the last digit to the end of the result.
    result = result * 10 + remainder

    # Remove the last digit from n via integer division by 10
    n = n // 10

# Print the reversed integer
print("Reversed integer:", result)
