# list slicing : Works similar to string slicing

my_list = [1,2,3,4,5]

print(my_list[::])  # Copy of the list, Output = [1, 2, 3, 4, 5]
print(my_list[1:4])  # Sublist from index 1 to 3, Output = [2, 3, 4]
print(my_list[::-1])  # Reversed list, Output = [5, 4, 3, 2, 1]
