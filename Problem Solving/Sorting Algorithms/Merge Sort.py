# Merge Sort Algorithm

def merge_sort(arr):
    # Base case: If the list has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Step 1: Find the middle of the list
        mid = len(arr) // 2

        # Step 2: Recursively split and sort the left half
        left_half = merge_sort(arr[:mid])

        # Step 3: Recursively split and sort the right half
        right_half = merge_sort(arr[mid:])

        # Step 4: Merge the sorted halves
        return merge(left_half, right_half)


# Merge Function to sort and combine the two halves
def merge(left, right):
    # Create an empty list to store the merged result
    merged_list = []

    # Initialize two index pointers to track positions in the left and right halves
    li = 0
    ri = 0

    # Step 1: Compare elements from both halves and merge them in sorted order
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            merged_list.append(left[li])
            li += 1
        else:
            merged_list.append(right[ri])
            ri += 1

    # Step 2: If any elements are left in the left half, append them
    while li < len(left):
        merged_list.append(left[li])
        li += 1

    # Step 3: If any elements are left in the right half, append them
    while ri < len(right):
        merged_list.append(right[ri])
        ri += 1

    # Return the merged list which is now fully sorted
    return merged_list


# Example usage:
arr1 = [3, 2, 4, 9, 5, 1, 8, 6, 7]
result = merge_sort(arr1)
print(result)
