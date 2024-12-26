# First Repeating Element Quadratic
# Function to find the first repeating element in an array
# This function uses a brute-force approach with O(n^2) time complexity.

def repeatElement(nums):
    # Outer loop iterates through each element in the list
    for i in range(len(nums)):

        # Inner loop checks if the current element is repeated later in the list
        for j in range(i+1, len(nums)):

            # If a match is found, return the first repeating element
            if nums[i] == nums[j]:
                return nums[i]

    # If no repeating element is found, return -1
    return -1


# Test case
nums1 = [10, 5, 3, 4, 3, 5, 6]
solution = repeatElement(nums1)
print(solution)  # Output = 5
