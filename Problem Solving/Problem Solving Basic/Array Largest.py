# Largest Element in an Array

def largestElement(nums):
    largest = float('-inf')  # Initialize 'largest' to negative infinity so it works for negative numbers too

    for num in nums:  # Loop through each number in the list 'nums'
        if num > largest:
            largest = num   # If the current number is greater than largest, update largest.

    return largest  # Return the largest number found in the list


# Test case
nums1 = [-4, -2, 1, -7, -5]
print(largestElement(nums1))   # Output: 1
