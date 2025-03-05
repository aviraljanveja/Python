# Second Largest Element in an Array

def secondLargest(nums):
    # Initialize 'largest' and 'second_largest' to negative infinity so that it works for negative numbers
    largest = float('-inf')  # This will hold the largest number in the list.
    second_largest = float('-inf')  # This will hold the second largest number in the list.

    for num in nums:  # Loop through each number in the list 'nums'
        if num > largest:  # If the current number is greater than the current largest
            second_largest = largest  # Then largest becomes the second largest
            largest = num  # and the current number becomes the new largest.

        # If any remaining number is smaller than largest, but greater than second_largest
        if second_largest < num < largest:
            second_largest = num  # then, update second_largest.

    return second_largest  # Return the second largest number found in the list


# Test case
nums1 = [-1, 2, -4, -7, -7, 5]
print(secondLargest(nums1))  # Output: 2
