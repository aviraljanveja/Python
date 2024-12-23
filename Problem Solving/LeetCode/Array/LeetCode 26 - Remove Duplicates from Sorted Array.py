# LeetCode 26 : Remove Duplicates from Sorted Array
# (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

def removeDuplicates(nums):
    k = 1  # Initialize k as 1, which represents the index to write the next unique element.

    for i in range(1, len(nums)):  # Iterate through the array starting from the second element (index 1).
        if nums[i] != nums[i-1]:  # Check if the current element is different from the previous one.
            nums[k] = nums[i]   # When a new element is found, write it to the current 'k' position.
            k += 1  # Increment k to the next position, where we will write the next unique element.

    return k  # Return k, which represents the number of unique elements in the array.


# Test case
arr1 = [0,0,1,1,1,2,2,3,3,4]
solution1 = removeDuplicates(arr1)
print(solution1)  # Output: 5 (unique elements count)
print(arr1)  # Output: [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
