# split() function
# Breaks a string into a list of substrings based on a specified delimiter.
# If no delimiter is specified, it splits on whitespace by default.
# Returns a list of strings.

text1 = "Hello World Python"
words = text1.split()
print(words)  # Output = ['Hello', 'World', 'Python']

text2 = "apple,banana,orange"
fruits = text2.split(",")
print(fruits)  # Output = ['apple', 'banana', 'orange']
