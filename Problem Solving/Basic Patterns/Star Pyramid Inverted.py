# Function to print the inverted star pyramid pattern
# Example with rows = 5:
# *********
#  *******
#   *****
#    ***
#     *

def inverted_star_pyramid(rows):
    for i in range(rows):  # Outer loop for rows
        # First inner loop: Print leading spaces for alignment
        for j in range(i):  # Number of spaces increases with each row
            print(" ", end="")  # Print a space without moving to the next line

        # Second inner loop: Print stars in the current row
        for k in range(2 * (rows - i) - 1):  # (2 * (rows - i) - 1) gives the odd number of stars
            print("*", end="")  # Print a star without moving to the next line

        # After printing spaces and stars for the current row, move to the next line
        print()

# Example usage
inverted_star_pyramid(5)