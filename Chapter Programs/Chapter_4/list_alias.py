# Aliasing Example :

list1 = [1, 2, 3]  # Creating a list

list2 = list1  # Creating an alias by assigning list1 to another variable

list2.append(4)  # Modifying the alias

# Printing both lists
print(list2)  # Output : [1, 2, 3, 4]
print(list1)  # Output : [1, 2, 3, 4]
