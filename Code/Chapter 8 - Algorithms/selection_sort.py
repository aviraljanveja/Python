# Selection Sort Algorithm

def selection_sort(arr):
    # Initialize i to start from the first element
    i = 0

    # Outer loop: continue until the entire array is exhausted
    while i < len(arr):
        # Inner loop: iterate through the unsorted part of the array
        for j in range(i + 1, len(arr)):
            # If a smaller element is found, swap it with the current element at index i
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

        # The array is now sorted till index i, so move on to the next index
        i += 1


# Example array to sort
arr1 = [3, 2, 4, 9, 5, 1, 8, 6, 7]

# Call the selection sort function on the array
selection_sort(arr1)

# Print the sorted array
print(arr1)
