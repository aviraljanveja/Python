# LeetCode 7 - Reverse Integer (https://leetcode.com/problems/reverse-integer/description/)

def reverse(x):
    value = abs(x)  # Get the absolute value of the input to simplify reversing logic.
    result = 0  # Initialize the result to 0, where the reversed number will be stored.

    while value > 0:
        remainder = value % 10  # Extract the last digit of 'value'.
        result = result * 10 + remainder  # Append the digit to 'result' in the reversed position.
        value = value // 10  # Remove the last digit from 'value'.

    if result > 2 ** 31 - 1:  # Check for overflow: if the reversed number exceeds the 32-bit upper bound.
        return 0

    if x < 0:  # Reapply the sign to the result if the original input was negative.
        return result * -1
    else:
        return result


# Example usage
reverse_number = reverse(-654321)  # Test the function with an example input.
print(reverse_number)  # Output: -123456