# Function to print the right-angled triangle pattern
# Example with rows = 5:
# *
# **
# ***
# ****
# *****

def right_triangle_pattern(rows):
    for i in range(rows):  # Outer loop for rows
        for j in range(i + 1):  # Inner loop for columns (up to i)
            print("*", end="")  # Print a star without moving to the next line
        print()  # Print a newline after completing one row

# Example usage
right_triangle_pattern(5)