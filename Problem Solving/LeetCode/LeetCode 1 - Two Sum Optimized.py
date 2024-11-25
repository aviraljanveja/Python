# LeetCode 1 - Two Sum Optimized

def twosum(arr, target):
    # Step 1: Create an empty dictionary to store array numbers as keys and their indices as values
    num_index = {}
    # Step 2: Iterate through the array using indices
    for i in range(len(arr)):
        # Step 3: Calculate the complement needed to reach the target
        complement = target - arr[i]
        # Step 4: Check if the complement exists as a key in the dictionary
        if complement in num_index:
            # Step 5: If it exists, return the indices of the complement and the current number
            return [num_index[complement], i]
        # Step 6: Store the current number (key) and its index (value) in the dictionary
        num_index[arr[i]] = i


list1 = [11,2,7,15]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)