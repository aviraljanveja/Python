# LeetCode 217 - Contains Duplicate (https://leetcode.com/problems/contains-duplicate/description/)

def containsDuplicate(nums):
    # Initialize an empty set to keep track of numbers we have seen so far.
    # A set is used because it provides fast look-up : O(1) average time complexity.
    check = set()

    for n in nums:  # Iterate through the numbers in the input list.
        if n in check:  # Check if the current number is already in the set.
            return True  # If it is, we have found a duplicate, so return True.
        check.add(n)  # Otherwise, add the current number to the set.

    return False  # If the loop exits without finding any duplicates, return False.


# Test Case:
nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))  # Output : True