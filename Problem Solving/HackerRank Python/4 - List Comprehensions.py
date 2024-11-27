# HackerRank Python : List Comprehensions
# Problem Link : https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())
n = int(input())

# List comprehension is a concise way to create lists in Python, similar to set-builder notation in mathematics.
# Syntax: [expression for variable in iterable if condition]
# [i, j, k] is the required expression of 3D coordinates in list notation.
# The range for i, j and k is defined using for-loops
# And the condition i + j + k ≠ n is to ensure that only valid combinations are selected.

# List comprehension implementation:
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(result)

# Equivalent nested loop implementation:
# result = []  # Initialize an empty list to store the valid coordinates
# for i in range(x + 1):  # Outer loop for 'i' from 0 to x
#     for j in range(y + 1):  # Middle loop for 'j' from 0 to y
#         for k in range(z + 1):  # Inner loop for 'k' from 0 to z
#             if (i + j + k) != n:  # Check if the sum of i, j, and k is not equal to n as required
#                 result.append([i, j, k])  # Append the coordinate to the result list