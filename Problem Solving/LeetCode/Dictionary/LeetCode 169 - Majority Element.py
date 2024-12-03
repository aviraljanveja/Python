# LeetCode 169 - Majority Element (https://leetcode.com/problems/majority-element/description/)

def majorityElement(nums):
    count = {}  # Initialize an empty dictionary to store the count of each element

    for num in nums:  # As the array is traversed, the dictionary is updated to store the count of each element.
        if num in count:  # If the number is already in the dictionary, increment its count
            count[num] += 1
        else:
            count[num] = 1  # If the number is not in the dictionary, store it and initialize its count to 1

        if count[num] > len(nums) / 2:  # Check if any number's count is already greater than n / 2
            return num  # If yes, then we can return it without having to traverse through the rest of the array


# Test case
list1 = [2,2,1,1,1,2,2]
print(majorityElement(list1))