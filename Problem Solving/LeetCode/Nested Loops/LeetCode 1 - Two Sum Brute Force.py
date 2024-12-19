# LeetCode 1 - Two Sum (https://leetcode.com/problems/two-sum/description/)

def twosum(arr, target):
    for i in range(len(arr)):  # Outer loop to pick the first number
        for j in range(i+1, len(arr)):  # Inner loop to pick the second number, starting after the first
            if arr[i] + arr[j] == target:  # Check if the two numbers sum up to the target
                return [i,j]  # If condition is met, return their indices


list1 = [2,11,15,7]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)  # Output : [0, 3]
