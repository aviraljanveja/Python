# HackerRank Python : Tuples
# Problem Link : https://www.hackerrank.com/challenges/python-tuples/problem

# Step 1: Read the number of elements in the tuple
n = int(input())

# Step 2: Read space-separated inputs and convert them to integers
integer_list = map(int, input().split())
# input() reads a line of input as a string.
# .split() breaks the string into a list of substrings based on spaces.
# map(int, ...) applies the int() function to each substring, converting them to integers.
# Example: If the input is "1 2 3 4", integer_list will contain [1, 2, 3, 4].

# Step 3: Convert the list of integers into a tuple
my_tuple = tuple(integer_list)
#
# the tuple() constructor takes an iterable (in this case, `integer_list`) and converts it into a tuple.
# Tuples are immutable sequences, making them hashable and suitable for use with the `hash()` function.
# Example: If integer_list is [1, 2, 3, 4], my_tuple will be (1, 2, 3, 4).

# Step 4: Compute and print the hash value of the tuple
print(hash(my_tuple))
# `hash()` computes a unique integer hash value for the tuple.
# This is useful for using the tuple as a key in a dictionary or storing it in a set.
# The `print()` function outputs the hash value to the console.
# Example: For `my_tuple = (1, 2, 3, 4)`, `hash(my_tuple)` might output an integer like 2528502973977326415.