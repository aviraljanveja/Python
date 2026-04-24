# list copy

# Using Slicing : Slices the entire list to create a new list.
list1 = [1, 2, 3, 4, 5]
list1_copy = list1[::]
print(list1_copy)  # Output = [1, 2, 3, 4, 5]

# Using copy() Method : Calls the list's built-in copy() method
list1_copy2 = list1.copy()
print(list1_copy2)  # Output = [1, 2, 3, 4, 5]
