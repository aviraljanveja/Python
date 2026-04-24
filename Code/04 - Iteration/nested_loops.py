# nested loop = a loop inside a loop.
# outer loop :
#   inner loop :
# Inner loop will finish all of its iterations before the outer loop goes on to its next iteration.

for x in range(4):
    for y in range(10):
        print("*", end = "")
    print() # this is used to print a new line after the inner loop finishes.

# Output = **********
#          **********
#          **********
#          **********