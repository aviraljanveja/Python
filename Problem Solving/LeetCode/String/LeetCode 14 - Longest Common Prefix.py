# LeetCode 14 - Longest Common Prefix
# Problem Link : https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    res = ""  # Initialize an empty string to store the result

    for i in range(len(strs[0])):   # Outer loop: iterate over each character of the first word
        for j in range(1, len(strs)):  # Inner loop: For this character position, do all words have the same character?
            if i == len(strs[j]) or strs[j][i] != strs[0][i]:  # Check if we have reached the end of the current word or found a mismatch
                return res  # If either condition is true, return the current result as the longest common prefix

        res += strs[0][i]  # If the character at index 'i' matches across all words, add it to the result

    return res  # If the loop completes without returning, the entire first word is the common prefix


# Test Case
str1 = ["flower","flow","flight"]
print(longestCommonPrefix(str1))  # Output = "fl"
