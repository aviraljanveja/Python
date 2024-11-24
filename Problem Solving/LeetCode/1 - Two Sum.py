# LeetCode : Two Sum

def twosum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]


list1 = [2,11,15,7]  # Given list
target1 = 9  # Target integer

solution = twosum(list1, target1)
print(solution)
