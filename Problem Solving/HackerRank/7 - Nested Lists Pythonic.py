# HackerRank Python : Nested Lists alternate solution which is more "Pythonic"
# Problem Link : https://www.hackerrank.com/challenges/nested-list/problem

# Step 1: Read the number of students
n = int(input())

# Step 2: Collect input directly into a nested list
L = [[input(), float(input())] for i in range(n)]

# Step 3: Extract scores, find unique scores, and get the second lowest score
second_lowest_score = sorted({x[1] for x in L})[1]

# Step 4: Filter names of students with the second lowest score
names = sorted([x[0] for x in L if x[1] == second_lowest_score])

# Step 5: Print names alphabetically
print("\n".join(names))