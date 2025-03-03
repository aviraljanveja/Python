# Adding Elements

my_list = [1,2,3,4,5]

# append() : Adds a single element to the end of the list.
my_list.append(6)
print(my_list)  # Output = [1, 2, 3, 4, 5, 6]

# extend() : Adds multiple elements from another sequence to the end of the list.
my_list.extend([7, 8, 9])
print(my_list)  # Output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert(index, element) : Adds a single element at the specified index, The existing elements are shifted to the right.
my_list.insert(0, 0)
print(my_list)  # Output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
