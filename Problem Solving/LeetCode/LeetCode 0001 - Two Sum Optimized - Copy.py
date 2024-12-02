# LeetCode 1 - Two Sum Optimized Solution

def twosum(arr, target):
    num_index = {}  # Step 1: Create an empty dictionary to store array numbers as keys and their indices as values

    for i in range(len(arr)):  # Step 2: Iterate through the array
        complement = target - arr[i]  # Step 3: Calculate the complement needed to reach the target
        if complement in num_index:  # Step 4: Check if the complement already exists as a key in the dictionary
            return [num_index[complement], i]  # Step 5: If yes, return the indices of the complement and the current number

        num_index[arr[i]] = i  # Step 6: Store the current number (key) and its index (value) in the dictionary


list1 = [11, 2, 7, 15]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)  # Output : [1, 2]