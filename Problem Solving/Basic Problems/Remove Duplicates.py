# Mutability and Iteration : Corrected Version

def remove_duplicates(l1, l2):
    l1_copy = l1[:]  # Creating a copy of the original first
    for e in l1_copy:  # Using the copy for iteration
        if e in l2:
            l1.remove(e)  # Then mutating the original list


list1 = [1, 2, 3, 4]
list2 = [1, 2, 5, 6]
remove_duplicates(list1, list2)
print(list1)  # Output : [3, 4]

# The above program gave the desired result
# because we first created a separate copy of our list
# to iterate over before editing the original list.
# This approach ensured that the iteration process
# remained consistent and predictable.
