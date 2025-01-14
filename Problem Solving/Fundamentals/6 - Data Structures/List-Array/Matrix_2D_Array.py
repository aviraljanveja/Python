# Working with 2D arrays / matrices / nested lists :

# Example: 3x3 2D array
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Indexing
# In order to access elements use two indices : matrix[row][column]
print(matrix[0][1])  # Output = 2 (First row, second column)
print(matrix[2][2])  # Output = 9 (Third row, third column)


# Iteration by Value
for row in matrix:  # First loop iterates over each row (which is a list).
    for value in row:  # Second loop iterates over each element in that row.
        print(value, end=" ")  # Output = 1 2 3 4 5 6 7 8 9


print() # Linebreak


# Iteration by Index
for i in range(len(matrix)):  # range(len(matrix)) gives row indices.
    for j in range(len(matrix[i])):  # range(len(matrix[i])) gives element indices for each row (which is a list).
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

"""
Output :
matrix[0][0] = 1
matrix[0][1] = 2
matrix[0][2] = 3
matrix[1][0] = 4
matrix[1][1] = 5
matrix[1][2] = 6
matrix[2][0] = 7
matrix[2][1] = 8
matrix[2][2] = 9
"""
