# String Validators :
# Python has built-in string validation methods for basic data.
# It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# isalnum() : This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9)
print("abc123".isalnum())  # True
print("abc.123#".isalnum())  # False


# isalpha() : This method checks if all the characters of a string are alphabetical (a-z and A-Z)
print("AbcD".isalpha())  # True
print("abcd1".isalpha())  # False


# isdigit() : This method checks if all the characters of a string are digits (0-9)
print("1234".isdigit())  # True
print("1234ab".isdigit())  # False


# islower() : This method checks if all the characters of a string are lowercase characters (a-z)
print("abcd123".islower())  # True
print("Abcd123".islower())  # False


# isupper() : This method checks if all the characters of a string are uppercase characters (A-Z)
print("ABCD123".isupper())  # True
print("Abcd123".isupper())  # False
