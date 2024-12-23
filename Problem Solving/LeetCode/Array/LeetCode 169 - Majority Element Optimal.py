# LeetCode 169 - Majority Element (https://leetcode.com/problems/majority-element/description/)
# Optimal Solution via the Boyer-Moore Voting Algorithm

def majorityElement(nums):
    # Initialize variables to track the potential majority element and its count
    candidate = None  # The current candidate for the majority element
    count = 0  # Counter to keep track of the candidate's "votes"

    for num in nums:
        if count == 0:
            candidate = num  # If count is 0, we select the current number as the new candidate
            count = 1  # And set the count to 1 for the new candidate
        elif num == candidate:
            count += 1  # If the current number matches the candidate, increment the count
        else:
            count -= 1  # If the current number does not match the candidate, decrement the count

    # After the loop, the candidate variable holds the majority element
    # This works because the majority element will always "win" the count competition as it occurs more than n/2 times
    return candidate


# Test case
list1 = [2, 2, 1, 1, 1, 2, 2]
solution = majorityElement(list1)
print(solution)