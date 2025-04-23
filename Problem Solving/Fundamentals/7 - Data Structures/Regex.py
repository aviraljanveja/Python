# Regular Expressions (Regex) in Python
# Regex or Regular Expression, is a sequence of characters that forms a search pattern.
# Regex can be used to check if a string contains the specified search pattern.

"""
Why Learn Regex?
- String validation (email, phone number, IP address)
- Text extraction (finding all numbers in a document)
- Data cleaning and preprocessing
"""

# Python has a built-in package called 're', which can be used to work with Regular Expressions.
# Import the 're' module:
import re

text = """
abcaviral 123janveja_ end
+91-9157790759
+91-98251
"""

pattern = re.compile(r'\+91-\d+') # r stands for raw string, which interprets the string as it is without
# implementing any special characters like backslashes for example.

matches = pattern.finditer(text)

for match in matches:
    print(match)

"""
Common Regex Sequences and Metacharacters : 

\d - Digit (0-9)
\D - Not a Digit
\w - Word Character (a-z, A-Z, 0-9, _)
\W - Not a Word Character
\s - Whitespace (space, tab, newline)
\S - Not Whitespace

. - Any character except newline
^ - Start of a String
$ - End of a String
"""
