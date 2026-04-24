# Updating Dictionary values

squares = {1:1, 2:4, 3:27, 4:16, 5:25}
print(squares)  # Output = {1: 1, 2: 4, 3: 27, 4: 16, 5: 25}

# Updating an existing key: Keys are immutable, but their values can be updated
squares[3] = 9
print(squares)  # Output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
Keys in dictionaries are immutable and cannot be modified directly.
If a key needs to be changed, you must remove the old key and add a new one with the desired value.
"""
