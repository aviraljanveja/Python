# LeetCode 125 - Valid Palindrome
# Problem Link : https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    val = "0123456789abcdefghijklmnopqrstuvwxyz"  # Define a string containing all valid alphanumeric characters
    s2 = ""  # Initialize an empty string to store the cleaned version of the input
    for char in s.lower():  # Convert the input string to lowercase and iterate through each character
        if char in val:  # If the character is alphanumeric, add it to the cleaned string
            s2 += char

    return s2 == s2[::-1]  # Check if the cleaned string is equal to its reverse (palindrome check)


# Test cases
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
string3 = " "

print(isPalindrome(string1))  # Output = True
print(isPalindrome(string2))  # Output = False
print(isPalindrome(string3))  # Output = True
