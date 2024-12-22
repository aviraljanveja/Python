# Bubble Sort Algorithm

def bubble_sort(arr):
    # Given an array of length n, we only need to make n-1 passes:
    # After n-1 passes, the last n-1 elements are already in their correct sorted positions,
    # and hence the first element is already sorted by default.
    for i in range(len(arr)-1):

        # During the i-th pass, we only need to compare up to (len(arr) - 1 - i)
        # because each pass places the largest element of the unsorted part at the correct position in the end.
        for j in range(len(arr)-1-i):

            # If the current element is greater than the next element,
            # swap them so that the larger one moves towards the end.
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Test case
arr1 = [3, 2, 9, 4, 5, 1, 8, 6, 7, 0]

# Call the bubble_sort function on the array
bubble_sort(arr1)

# Print the sorted array
print(arr1)
