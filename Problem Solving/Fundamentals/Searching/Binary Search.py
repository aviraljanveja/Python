# Binary Search on Sorted List via Iteration

def binary_search(arr, target):
    # Step 1: Initialize the pointers to the first and last index of the list
    start = 0  # first index of the list
    end = len(arr) - 1  # last index of the list

    # Step 2: Continue searching as long as start is less than or equal to end
    while start <= end:

        # Step 3: Find the middle index via integer division
        mid = (start + end) // 2

        # Step 4: Check if the target is equal to the middle index
        if arr[mid] == target:
            return f"Element found at index : {mid}"  # If Target found, return the index

        # Step 5: If the target is greater than the middle element,
        # we can ignore the smaller-half knowing that the list is already sorted
        elif arr[mid] < target:
            start = mid + 1  # Move start to the right of mid

        # Step 6: If the target is smaller than the middle element,
        # ignore the bigger-half
        else:
            end = mid - 1  # Move end to the left of mid

    # Step 7: If the loop exits without finding the target element :
    return "Element not found"


# Driver code
arr1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target1 = 30

result = binary_search(arr1, target1)
print(result)  # Output: "Element found at index: 2"
