# for : reverse iteration over values using slicing
text = "aviral"

for char in text[::-1]:  # Python strings are immutable. Slicing operation here returns a new string object.
    print(char, end = "")  # Output = lariva
