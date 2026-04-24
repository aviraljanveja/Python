# Iterating through a dictionary

squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# Iterating Over Keys : Default Behavior
for i in squares:
    print(i, end = " ")  # Output = 1 2 3 4 5

print()  # Newline

# Iterating Over Values : use the values() method.
for i in squares.values():
    print(i, end = " ")  # Output = 1 4 9 16 25

print()  # Newline

# Iterating Over Key-Value Pairs : use the items() method, which returns tuples of (key, value) pairs.
for i, j in squares.items():
    print(f"key:{i} Value:{j}")

"""
Output : 
key:1 Value:1
key:2 Value:4
key:3 Value:9
key:4 Value:16
key:5 Value:25
"""