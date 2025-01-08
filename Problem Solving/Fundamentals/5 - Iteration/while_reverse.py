# while reverse

text = "aviral"

i = len(text)
while i > 0:
    i -= 1
    print(f"{text[i]}:{i}", end = " ")  # Output = l:5 a:4 r:3 i:2 v:1 a:0
