# Merge Sort Algorithm
# Time Complexity = O(nlogn) | Log-Linear

def merge_sort(arr):
    # Step 1 : Find the middle & split recursively
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, it is already sorted
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])


    # Step 2 : Merge the sorted halves
    res = []  # Create an empty list to store the merged result
    l = 0  # Initialize two pointers for elements
    r = 0  # in the left and right halves

    while l < len(left) and r < len(right):
        if left[l] < right[r]:  # Compare elements from both halves
            res.append(left[l])  # and merge them in sorted order
            l += 1
        else:
            res.append(right[r])
            r += 1

    res.extend(left[l:])  # Append the remaining elements
    res.extend(right[r:])  # from both halves

    return res  # Return the sorted result


# Example :
arr1 = [3, 2, 9, 4, 5, 1, 8, 6, 7, 0]

print(arr1)
result = merge_sort(arr1)
print(result)
