# Creating a dictionary
my_dict = {'apple': 5, 'banana': 3, 'orange': 7}

# Accessing values
print("Number of apples:", my_dict['apple'])  # Output: Number of apples: 5

# Adding a new key-value pair
my_dict['grapes'] = 8
print("Updated dictionary:", my_dict)
# Output: Updated dictionary: {'apple': 5, 'banana': 3, 'orange': 7, 'grapes': 8}

# Modifying an existing value
my_dict['apple'] = 10
print("Modified dictionary:", my_dict)
# Output: Modified dictionary: {'apple': 10, 'banana': 3, 'orange': 7, 'grapes': 8}

# Removing a specific key-value pair
del my_dict['banana']
print("Dictionary after removing 'banana':", my_dict)
# Output: Dictionary after removing 'banana': {'apple': 10, 'orange': 7, 'grapes': 8}

# Checking for key existence
if 'orange' in my_dict:
    print("Yes, 'orange' is present in the dictionary.")
else:
    print("No, 'orange' is not present in the dictionary.")

# Iterating through a dictionary
print("Iterating through the dictionary:")
for key, value in my_dict.items():
    print(key, '->', value)

# Dictionary methods
print("Keys:", my_dict.keys())        # Output: Keys: dict_keys(['apple', 'orange', 'grapes'])
print("Values:", my_dict.values())    # Output: Values: dict_values([10, 7, 8])
print("Items:", my_dict.items())      # Output: Items: dict_items([('apple', 10), ('orange', 7), ('grapes', 8)])
