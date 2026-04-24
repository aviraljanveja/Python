# set() constructor : Convert a list, tuple, or string into a set to remove duplicates.
# use-case : Removing Duplicates
# Sets inherently remove duplicates.

list1 = [1, 2, 2, 3, 3, 4]
list2 = list(set(list1))
print(list2)  # Output = [1, 2, 3, 4]
