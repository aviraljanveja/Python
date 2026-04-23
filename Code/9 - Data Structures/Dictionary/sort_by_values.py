# Sorting a dictionary by values using a lambda function

dict1 = {'a': 3, 'b': 1, 'c': 2}

# Sorting by values using the lambda function
sorted_dict1 = dict(sorted(dict1.items(), key = lambda item : item[1]))
print(sorted_dict1)  # Output = {'b': 1, 'c': 2, 'a': 3}

# Sorting in descending order by setting the reverse parameter to True
reverse_sorted_dict1 = dict(sorted(dict1.items(), key = lambda item : item[1], reverse = True))
print(reverse_sorted_dict1)  # Output = {'a': 3, 'c': 2, 'b': 1}
