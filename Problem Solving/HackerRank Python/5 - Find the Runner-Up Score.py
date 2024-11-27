# HackerRank Python : Find the Runner-Up Score!
# Problem Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Step 1: Read the number of scores
n = int(input())
# The input specifies how many scores the user will enter, but it's not used directly in the logic.
# It serves as a guide for the user to input the correct number of values.

# Step 2: Read the scores as space-separated values and convert them to integers
arr = map(int, input().split())
# input() reads the entire line as a string.
# split() breaks the string into a list of individual strings, separated by whitespace.
# map(int, ...) converts each of these strings into integers.

# Step 3: Remove duplicates by converting the list of scores into a set
unique_arr = set(arr)
# A set automatically removes duplicate values, leaving only unique scores.

# Step 4: Sort the unique scores in descending order
result = sorted(unique_arr, reverse=True)
# sorted() returns a new list containing the elements of the set, sorted in ascending order by default.
# reverse=True sorts the elements in descending order.

# Step 5: Check if there are at least two unique scores
if len(result) < 2:
    # If there are fewer than two unique scores, we cannot determine a "runner-up."
    print("No Runner-Up Score!")
else:
    # Step 6: Print the Runner-Up score
    print(result[1])
    # result[1] accesses the second element in the sorted list (which is the runner-up score).
