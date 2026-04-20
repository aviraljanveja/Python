# Set declaration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Length of a set
print("Length of set1:", len(set1))

# Membership check
print("Is 3 in set1?", 3 in set1)

# Iteration over a set
print("Elements of set1:")
for element in set1:
    print(element)

# Union of sets : all items from both sets
union_set = set1 | set2
print("Union of set1 and set2:", union_set)

# Intersection of sets : only the items that are present in both sets
intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)

# Difference of sets
difference_set = set1 - set2
print("Difference of set1 and set2:", difference_set)

# Symmetric difference of sets :
# contains all items from both sets, except items that are present in both
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)
