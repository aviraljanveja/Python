# Second Largest Element in an Array

def secondLargest(nums):
    # Initialize max_num and sec_max_num to negative infinity so that it works for negative numbers
    max_num = float('-inf')  # This will hold the largest number in the list.
    second_largest = float('-inf')  # This will hold the second largest number in the list.

    for num in nums:  # Loop through each number in the list 'nums'
        if num > max_num:  # If the current number is greater than max_num
            second_largest = max_num  # The current max_num becomes the second largest
            max_num = num  # and the current number becomes the new max_num.

        # If any upcoming number is greater than second_largest but smaller than max_num,
        if second_largest < num < max_num:
            second_largest = num  # update second_largest to this number.

    return second_largest  # Return the second largest number found in the list


# Test case
nums1 = [-1, -2, -4, -7, -7, -5]
print(secondLargest(nums1))  # Output: -2
