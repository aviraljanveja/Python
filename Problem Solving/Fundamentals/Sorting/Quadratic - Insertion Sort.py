# Insertion Sort Algorithm

def insertion_sort(arr):
    # Start from the second element (index 1),
    # because the first element (index 0) is naturally already sorted.
    for i in range(1, len(arr)):

        # The, we iterate in reverse from i down to 1
        # comparing arr[j] with its previous element arr[j - 1]
        for j in range(i, 0, -1):

            # If the current element arr[j] is smaller than the previous element arr[j - 1], they are swapped.
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

            # As soon as we find that the current element is not smaller than its predecessor,
            # we know it's in the right spot because everything to the left is already sorted.
            else:
                break  # so we break out of the loop to stop unnecessary comparisons.


# Test case
arr1 = [9, 5, 1, 4, 3, 2, 8, 6, 7, 0]
insertion_sort(arr1)
print(arr1)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
