# Largest Element in an Array

def largestElement(nums):
    max_num = float('-inf')  # Initialize max_num to negative infinity so it works for negative numbers too

    for num in nums:  # Loop through each number in the list 'nums'
        if num > max_num:
            max_num = num   # If the current number is greater than max_num, update max_num

    return max_num  # Return the largest number found in the list


# Test case
nums1 = [-1, -2, -4, -7, -7, -5]
print(largestElement(nums1))   # Output: -1
