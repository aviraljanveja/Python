# Dictionary Membership Check

squares = {1:1, 2:4, 3:9}

# Membership Check by Key
print(3 in squares)  # Output: True
print(5 in squares)  # Output: False

# Membership Check by Value
print(9 in squares.values())  # Output: True
print(10 in squares.values())  # Output: False

# Membership Check by Key-Value pairs
print((1,1) in squares.items())  # Output: True
print((2,4) in squares.items())  # Output: True

