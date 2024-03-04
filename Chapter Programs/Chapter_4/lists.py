# Define a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements of the list
print("First element:", my_list[0])  # Output: 1
print("Last element:", my_list[-1])  # Output: 5

# Length of the list
print("Length of the list:", len(my_list))  # Output: 5

# Slicing a list
print("Slice of the list:", my_list[2:4])  # Output: [3, 4]

# Modifying elements of the list
my_list[0] = 10
print("Modified list:", my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements to the list
my_list.append(6)
print("Appended list:", my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements from the list
my_list.remove(3)
print("List after removing '3':", my_list)  # Output: [10, 2, 4, 5, 6]

# Iterating over the list
for element in my_list:
    print(element)
