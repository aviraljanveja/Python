# Mutability and Iteration : Faulty Version

def remove_duplicates(l1, l2):
    for e in l1:
        if e in l2:
            l1.remove(e)  # Mutating the list that is being iterated upon


list1 = [1, 2, 3, 4]
list2 = [1, 2, 5, 6]
remove_duplicates(list1, list2)
print(list1)  # Output : [2, 3, 4]

# As seen above, the above program does not produce the desired result.
# Element 2 gets skipped because the list size is changed midway,
# meanwhile the loop counter continues on to the next index, 
# without adjusting for the modified list size.
