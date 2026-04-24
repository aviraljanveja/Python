# Regular Expressions (Regex) allows us to search for and match specific patterns of text.
# You can create a regular expression for about any pattern of text you can think of.
# First of all, to use regular expressions within Python, we need to import the 're' module :

import re

search_text = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
+91-9156690838
9156690838
aviral123@gmail.com
aviral.123@uni.in
aviral-123@my-work.in
https://www.aviral.com
https://aviral.com
http://aviral.com
http://www.aviral.in
'''

# Use re.compile when you want to use the same pattern multiple times
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# r'some string' is called a raw string in Python. It allows Python to evaluate strings literally,
# without accounting for special characters like backslashes \.
# They are commonly used with Regex patterns because we want our strings to be evaluated
# as regular expressions without any interference by the Python interpreter.

matches = pattern.finditer(search_text)
# finditer() method gathers all of the matches from the specified text
# along with their start/end index, storing them in the matches variable here.

for match in matches:  # Printing all the found matches
    print(match)

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

"""
Common Regex Sequences :
\d = Digits [0-9]
\D = Non-Digits
\w = Word character = letters[a-zA-Z], digits[0-9] & Underscore[_]
\W = Non-word character
\s = Whitespaces (space, tab, newline)
\S = Non-whitespace character
"""

"""
Common Regex Metacharacters :
. = Any character except newline
^ = Start of a String
$ = End of a String
[...] = Any one character from the set. For example [aeiou] matches any vowel, [a-zA-Z] matches alphabets
[^...] = Any one character not in the set. For example [^aeiou] matches consonants
* = 0 or more repetitions of the preceding character. For example ab* matches a, ab, abb.
+ = 1 or more repetitions of the preceding character. For example ab+ matches ab, abb.
? = 0 or 1 occurrence (optional) of the preceding character. For example colou?r matches color, colour.
{n} = Exactly n repetitions. For example \d{3} matches 123, 345, 981, etc.
{n,m} = Between n and m repetitions. For example \d{2,3} matches 12, 123, etc.
() = Grouping and capturing. For example (ab)+ captures ab, abab, ababab, etc.
"""

"""
Common Regex Samples :
Sample Regex Pattern for Indian Phone Number = (\+91-)?\d{10}
Sample Regex Pattern for Email Id = [\w.-]+@[\w-]+\.[a-zA-Z]{2,3}
Sample Regex Pattern for Website URl = https?://(www\.)?(\w+)(\.\w+)
"""
