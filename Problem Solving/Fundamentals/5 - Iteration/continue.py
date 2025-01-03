# continue : Skips the current iteration and moves to the next.

for i in range(10):
    if i == 5:
        continue
    print(i, end = " ")  # Output = 0 1 2 3 4 6 7 8 9
