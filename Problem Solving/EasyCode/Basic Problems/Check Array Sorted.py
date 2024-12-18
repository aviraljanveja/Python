# Checking if an Array is Sorted

def isSorted(nums):
    for i in range(1, len(nums)):  # Loop starts from index 1 since we compare nums[i] with nums[i-1]
        if nums[i] < nums[i-1]:  # If the current element is less than the previous one, the list is not sorted
            return False

    return True  # If the loop completes, the list is sorted


# Test case
nums1 = [1, 2, 3, 4, 5]
print(isSorted(nums1))  # Output: True
