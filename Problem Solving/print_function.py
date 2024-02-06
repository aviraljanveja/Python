# See the following link for problem statement:
# https://www.hackerrank.com/challenges/python-print/problem

n = int(input())
if 1 <= n <= 150:
    for i in range(1, n+1):
        print(i, end='')
else:
    print("Enter an integer between 1 and 150!")
