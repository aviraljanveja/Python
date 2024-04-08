# Cloning Example :

list1 = [1, 2, 3]  # Creating a list

list2 = list1.copy()  # Creating a copy using the copy() function
list3 = list1[:]  # Creating another copy using slicing

# Modifying the copies
list2.append(4)
list3.extend([4, 5])

# Printing the copies
print(list3)  # Output : [1, 2, 3, 4, 5]
print(list2)  # Output : [1, 2, 3, 4]
print(list1)  # Output : [1, 2, 3]
