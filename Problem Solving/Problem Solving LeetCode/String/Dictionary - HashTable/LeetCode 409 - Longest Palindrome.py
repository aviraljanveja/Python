# LeetCode 409 - Longest Palindrome
# Problem Link : https://leetcode.com/problems/longest-palindrome/description/

def longestPalindrome(s):
    dct = {}  # Dictionary to count the frequency of each character in the string
    n = 0  # Variable to keep track of the maximum length of the palindrome
    odd_found = False  # Flag to check if there's at least one character with an odd count

    for ch in s:  # Iterate through each character in the input string
        if ch in dct:  # Increment the character count in the dictionary
            dct[ch] += 1
        else:
            dct[ch] = 1

    for val in dct.values():  # Iterate through the frequency of each character
        if val % 2 == 0:  # If the frequency is even, it can fully contribute to the palindrome
            n += val
        else:  # If the frequency is odd, contribute the largest even part to the palindrome
            n += val - 1
            odd_found = True  # Mark that an odd frequency character was found

    # If any odd frequency character was found, we can place one such character
    # in the middle of the palindrome, increasing the length by 1
    if odd_found:
        n += 1

    return n  # Return the maximum length of the palindrome


# Test case
s1 = "abccccdd"
print(longestPalindrome(s1))  # Output = 7

s2 = "a"
print(longestPalindrome(s2))  # Output = 1
