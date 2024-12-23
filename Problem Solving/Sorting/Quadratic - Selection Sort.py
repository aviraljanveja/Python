# Selection Sort Algorithm

def selection_sort(arr):
    # Given n is the length of array, we only need to make n-1 passes:
    # Because after n-1 swaps, the first n-1 positions are correctly sorted,
    # and hence the last element is already sorted by default.
    for i in range(len(arr) - 1):

        # Traverse the sub-array from index i+1 to the end,
        # searching for any element that is smaller than arr[i].
        for j in range(i + 1, len(arr)):

            # If we find an element smaller than the current element at i,
            # swap them so that the smaller element moves into position i.
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]


# Test case
arr1 = [3, 2, 9, 4, 5, 1, 8, 6, 7, 0]

# Call the selection_sort function on the array
selection_sort(arr1)

# Print the sorted array
print(arr1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
