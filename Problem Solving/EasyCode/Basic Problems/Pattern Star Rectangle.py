# Function to print the rectangular star pattern
# Example with rows = 5 & columns = 5:
# *****
# *****
# *****
# *****
# *****

def rectangular_star_pattern(rows, columns):
    for i in range(rows):  # Outer loop for rows
        for j in range(columns):  # Inner loop for columns
            print("*", end="")  # Print a star without moving to the next line
        print()  # Print a newline after completing one row

# Example usage
rectangular_star_pattern(5, 5)