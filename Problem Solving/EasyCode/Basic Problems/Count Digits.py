def countDigits(num):
    count = 0  # Initialize a counter to keep track of the number of digits

    while num > 0:  # Loop continues as long as num is greater than 0
        count += 1  # Increment the count to reflect one digit per iteration        
	num = num // 10  # Remove the last digit of num by performing integer division by 10
        
    return count  # Return the total count of digits


# Test the function with an example
print(countDigits(77890))  # Output: 5 (since 77890 has 5 digits)
