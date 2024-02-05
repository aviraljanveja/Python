# See the following link for problem statement:
# https://www.hackerrank.com/challenges/py-if-else/problem

n = int(input())
if 1 <= n <= 100:
    if n % 2 == 0:
        if n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
else:
    print("Enter an integer between 1 and 100")
