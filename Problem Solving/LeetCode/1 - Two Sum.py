# LeetCode 1 - Two Sum

def twosum(arr, target):
    # Outer loop to pick the first number
    for i in range(len(arr)):
        # Inner loop to pick the second number, starting after the first
        for j in range(i+1, len(arr)):
            # Check if the two numbers sum up to the target
            if arr[i] + arr[j] == target:
                # If condition is met, return their indices
                return [i,j]


list1 = [2,11,15,7]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)
