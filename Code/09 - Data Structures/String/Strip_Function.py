# The strip() method removes any leading and trailing whitespaces.
# You can specify which characters to remove, if not, any whitespaces will be removed.


txt1 = "     banana     "
x = txt1.strip()
print("of all fruits", x, "is my favorite")  # Output = of all fruits banana is my favorite


txt2 = ",,,,,rrttgg.....banana....rrr"
x2 = txt2.strip(",.grt")
print(x2)  # Output = banana
