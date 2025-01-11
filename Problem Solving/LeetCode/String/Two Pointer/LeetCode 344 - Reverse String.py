# LeetCode 344 : Reverse String
# Problem Link : https://leetcode.com/problems/reverse-string/description/

def reverseString(s):
    j = len(s) - 1  # Initialize the right pointer 'j' to the last index of the list
    for i in range(len(s) // 2):  # Loop through the first half of the list using 'i' as the left pointer
        s[i], s[j] = s[j], s[i]  # Swap the elements at indices 'i' and 'j'
        j -= 1  # the right pointer 'j' moves one step towards the center

    return s  # The list is modified in place, so we can return it if needed


# Test cases
s1 = ["h","e","l","l","o"]
s2 = ["p","y","t","h","o","n"]

print(reverseString(s1))  # Output: ["o", "l", "l", "e", "h"]
print(reverseString(s2))  # Output: ["n", "o", "h", "t", "y", "p"]
