# for : Reverse iteration using range

text = "aviral"

for i in range(len(text)-1, -1, -1):
    print(f"{text[i]}:{i}", end = " ")  # Output = l:5 a:4 r:3 i:2 v:1 a:0
