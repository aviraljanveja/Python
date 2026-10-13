# Removing Elements

my_list = [0, 5, 1, 2, 3, 4, 5]

# remove() : Removes the first occurrence of the specified element.
my_list.remove(5)
print(my_list)  # Output = [0, 1, 2, 3, 4, 5]


# pop() : Removes and returns the element at the specified index.
# If no index is provided, it removes and returns the last element.
my_list.pop()
print(my_list)  # Output = [0, 1, 2, 3, 4]
my_list.pop(0)
print(my_list)  # Output = [1, 2, 3, 4]


# del() : Deletes the element at a specified index
# can be used to delete a slice of elements as well
# Can also delete the entire list.
del(my_list[0])
print(my_list)  # Output = [2, 3, 4]
del(my_list[1:])
print(my_list)  # Output = [2]
