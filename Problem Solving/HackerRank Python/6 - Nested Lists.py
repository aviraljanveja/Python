# HackerRank Python : Nested Lists
# Problem Link : https://www.hackerrank.com/challenges/nested-list/problem

# Step 1: Read the number of students
n = int(input())
L = []  # Initialize an empty list to store student names and scores

# Step 2: Collect input data for each student
for i in range(n):
    # Append a sub-list containing the student's name and score to L
    L.append([input(), float(input())])

# Step 3: Extract all scores into a separate list L2
L2 = []  # Initialize an empty list to store scores
for i in range(len(L)):
    L2.append(L[i][1])  # Append the score (second element) from each sub-list in L

# Step 4: Find the second-lowest score
# Convert L2 into a set to remove duplicates, then sort the unique scores
# The second-lowest score is the second element in the sorted list
score = sorted(set(L2))[1]

# Step 5: Collect names of students with the second-lowest score
names = []  # Initialize an empty list to store names of students with the target score
for i in range(len(L)):
    if L[i][1] == score:  # Check if the score matches the second-lowest score
        names.append(L[i][0])  # Append the student's name to the names list

# Step 6: Sort the names alphabetically
names.sort()

# Step 7: Print each name on a new line
for name in names:
    print(name)