# Linear Search via Iteration

def linear_search(arr, target):
    # Simply go through each element of the list
    # to search for the target element
    for i in range(len(arr)):
        if target == arr[i]:
            # If the element is found, return a message with the index where it was found.
            return f"Element found at index : {i}"
    # If the loop exits without finding the element then return Element not found
    return "Element not found"


# Driver code
arr1 = [10, 20, 30, 40, 50]
target1 = 30

result = linear_search(arr1, target1)
print(result)  # Output: "Element found at index: 2"
