# Function to print the hollow rectangular star pattern
# Example with rows = 4 & columns = 12 :
# ************
# *          *
# *          *
# ************

def rectangular_star_pattern(rows, columns):
    for i in range(rows):  # Outer loop for rows
        for j in range(columns):  # Inner loop for columns
            # Check if the current position is at the border : first / last row or first / last column
            if i == 0 or i == rows-1 or j == 0 or j == columns-1:
                print("*", end="")  # Print a star without moving to the next line
            else:
                print(" ", end="")  # Print a space for the hollow part

        print()  # Print a newline after completing one row


# Example usage
rectangular_star_pattern(4, 12)
