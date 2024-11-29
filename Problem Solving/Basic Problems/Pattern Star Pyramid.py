# Function to print the star pyramid pattern using nested loops
# Pattern Example for rows = 5:
#     *
#    ***
#   *****
#  *******
# *********

def star_pyramid_pattern(rows):
    for i in range(rows):  # Outer loop for rows
        # First inner loop: Print spaces to center the stars
        for j in range(rows - i - 1):  # (rows - i - 1) spaces needed for alignment
            print(" ", end="")  # Print a space without moving to the next line

        # Second inner loop: Print stars in the current row
        for k in range(2 * i + 1):  # (2i + 1) gives the odd number of stars for row i
            print("*", end="")  # Print a star without moving to the next line

        # After printing spaces and stars for the current row, move to the next line
        print()

# Example usage
star_pyramid_pattern(5)