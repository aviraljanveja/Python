# The while loop is used to execute a block of code repeatedly as long as a specified condition is true.


# For example
text = "aviral"


# while loop
i = 0
while i < len(text):
    print(f"{text[i]}:{i}", end = " ")  # Output = a:0 v:1 i:2 r:3 a:4 l:5
    i += 1


print("")  # new line


# while loop reverse
i = len(text)-1
while i >= 0:
    print(f"{text[i]}:{i}", end = " ")  # Output = l:5 a:4 r:3 i:2 v:1 a:0
    i -= 1
    