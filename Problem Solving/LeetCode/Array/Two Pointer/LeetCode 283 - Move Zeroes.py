# LeetCode 283 - Move Zeroes
# Problem Link : https://leetcode.com/problems/move-zeroes/description/

def moveZeroes(nums):
    i = 0  # Pointer 1 : traverses every element in the array.
    j = 0  # Pointer 2 : keeps track of the position where the next non-zero element should go.

    while i < len(nums):
        if nums[i] != 0:  # If the current element is non-zero,
            nums[j], nums[i] = nums[i], nums[j]  # Swap elements at i and j
            j += 1  # Move j to the next position to store the next non-zero element
        i += 1  # Increment i


# Test case
arr1 = [0, 1, 0, 3, 12]
moveZeroes(arr1)  # Modifies arr1 in place
print(arr1)  # Output: [1, 3, 12, 0, 0]
