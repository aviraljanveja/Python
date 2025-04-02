# LeetCode 26 : Remove Duplicates from Sorted Array
# (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

def removeDuplicates(nums):
    i = 1  # pointer 1, to Iterate through the sorted array.
    k = 1  # Pointer 2, which represents the indices to write the unique elements.

    while i < len(nums):
        # Comparing adjacent elements, utilizing the fact that the array is sorted already.
        if nums[i] != nums[i-1]:  # Check if the current element is different from the previous one.
            nums[k] = nums[i]  # If yes, then a new element is found. Write it to the 'k' position.
            k += 1  # Increment k, for storing the next unique element.
        i += 1

    return k  # After loop, Return k, which holds the number of unique elements in the array.


# Test case
arr1 = [0, 0, 0, 1, 1, 1, 2, 2, 2]
solution1 = removeDuplicates(arr1)
print(solution1)  # Output: 3 (number of unique elements = 0, 1, 2)
print(arr1)  # Output array, duplicates removed in-place = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
