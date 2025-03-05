# list inbuilt sort
# Efficiency: O(n log n) on average due to the underlying
# Timsort algorithm (a hybrid of merge sort and insertion sort).

# sort(key=None, reverse=False) function for in-place sorting
# Sorts the list in place, modifying the original list.
# By default, it sorts in ascending order.
# key parameter allows custom sorting logic by providing a function. For example : Sort by absolute value
# reverse=True sorts in descending order.
list1 = [1, -3, 2, -5, 4]
list1.sort()
print(list1)  # Output = [-5, -3, 1, 2, 4]
list1.sort(reverse=True)
print(list1)  # Output = [4, 2, 1, -3, -5]
list1.sort(key = abs)
print(list1)  # Output = [1, 2, -3, 4, -5]


# sorted(iterable, key=None, reverse=False) function returns a new sorted list
# Returns a new sorted list without modifying the original.
list2 = [1, -3, 2, -5, 4]
sorted_list2 = sorted(list2)
print(sorted_list2)  # Output = [-5, -3, 1, 2, 4]
reverse_sorted_list2 = sorted(list2, reverse=True)
print(reverse_sorted_list2)  # Output = [4, 2, 1, -3, -5]
absolute_value_sorted_list2 = sorted(list2, key=abs)
print(absolute_value_sorted_list2)  # Output = [1, 2, -3, 4, -5]
