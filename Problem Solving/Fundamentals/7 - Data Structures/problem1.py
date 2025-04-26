# Regular Expressions (Regex) allows us to search for and match specific patterns of text.
# You can create a regular expression for about any pattern of text you can think of.
# First of all, to use regular expressions within Python, we need to import the 're' module :

import re

search_text = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
'''

sentence = "Start a sentence and then bring it to an end"

# Use re.compile when you are using the same pattern multiple times
pattern = re.compile(r'end$')
# r'some string' is called a raw string in Python.
# It allows Python to evaluate strings literally,
# without accounting for special characters like backslashes \.
# They are commonly used with Regex patterns because we want our strings to be evaluated
# as regular expressions without any interference by the Python interpreter.

"""
Common Regex Functions : 
re.match() = Match pattern from start of string
re.search() = Match pattern anywhere in string (returns first match)
re.findall() = Returns all non-overlapping matches as a list
re.finditer() = Returns an iterator of match objects for all matches
re.sub() = Replaces all matches with a given replacement
re.split() = Splits the string by the pattern
re.compile() = Compiles the pattern into a reusable regex object for faster repeated use
"""

matches = pattern.finditer(search_text)
# finditer() method gathers all of the matches from the specified text
# along with their start/end index, storing them in the matches variable here.

for match in matches:  # Printing all the found matches
    print(match)

"""
Common Regex Sequences :
\d = Digits (0-9)
\D = Non-Digits
\w = Word character = letters(a-z, A-Z), digits(0-9) & Underscores(_)
\W = Non-word character
\s = Whitespaces (space, tab, newline)
\S = Non-whitespace character
"""

"""
Common Regex Metacharacters :
. = Any character except newline
^ = Start of a String
$ = End of a String
[...] = Any one character from the set. For example [aeiou] matches any vowel
[^...] = Any one character not in the set. For example [^aeiou] matches consonants
"""




