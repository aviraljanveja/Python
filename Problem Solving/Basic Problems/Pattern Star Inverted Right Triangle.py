# Function to print the inverted right-angled triangle pattern
# Example with rows = 5:
# *****
# ****
# ***
# **
# *

def inverted_right_triangle(rows):
    for i in range(rows):  # Outer loop for rows
        for j in range(rows - i):  # As i increases, the number of stars decreases (rows - i).
            print("*", end="")  # Print a star without moving to the next line
        print()  # Print a newline after completing one row

# Example usage
inverted_right_triangle(5)