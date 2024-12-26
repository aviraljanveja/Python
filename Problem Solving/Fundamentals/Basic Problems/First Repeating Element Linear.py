# First Repeating Element Linear
# Function to find the first repeating element in the list
# This function uses a dictionary to achieve O(n) time complexity.

def repeatElement(nums):
    check = {}  # Dictionary to store the first index of each element
    min_index = len(nums) - 1  # Variable to track the smallest index among repeating elements
    answer = -1  # Variable to store the first repeating element or return -1 if none found

    for i in range(len(nums)):  # Iterate through the list

        if nums[i] in check:  # If the current element is already in the dictionary (Repeating Element)

            # Checking for minimum index among repeating elements
            if check[nums[i]] < min_index:  # If the index of its first occurrence is smaller than the current minimum index
                min_index = check[nums[i]]  # then update the minimum index
                answer = nums[i]  # and update the answer

        else:  # Otherwise, store the element and its first index of occurrence as key-value pairs in the dictionary
            check[nums[i]] = i

    return answer  # Having iterated over the entire list, return the first repeating element or -1 if none found


# Test case
nums1 = [10, 5, 3, 4, 3, 5, 6]
solution = repeatElement(nums1)
print(solution)  # Output = 5
