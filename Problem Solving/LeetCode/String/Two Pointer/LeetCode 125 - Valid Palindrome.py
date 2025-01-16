# LeetCode 125 - Valid Palindrome
# Problem Link : https://leetcode.com/problems/valid-palindrome/

def isPalindrome(s):
    # First section : Cleaning the input string.
    val = "0123456789abcdefghijklmnopqrstuvwxyz"  # Define a string containing all valid alphanumeric characters
    s2 = ""  # Initialize an empty string to store the cleaned version of the input
    for char in s.lower():  # Convert the input string to lowercase and iterate through each character
        if char in val:  # If the character is alphanumeric, add it to the cleaned string
            s2 += char

    # Second section : Two-pointer technique used to check for a palindrome.
    i = 0  # Pointer 1 : Start of string
    j = len(s2) - 1  # Pointer 2 : End of String
    while i < j:  # Use a while loop to compare characters from both ends moving towards the center
        if s2[i] != s2[j]:  # If the characters at the current pointers do not match, return False (not a palindrome)
            return False
        i += 1  # Move the left pointer to the right
        j -= 1  # and the right pointer to the left
    return True  # If the loop completes without finding a mismatch, return True (it is a palindrome)


# Test cases
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
string3 = " "

print(isPalindrome(string1))  # Output = True
print(isPalindrome(string2))  # Output = False
print(isPalindrome(string3))  # Output = True
