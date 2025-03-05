# LeetCode 344 : Reverse String
# Problem Link : https://leetcode.com/problems/reverse-string/description/

def reverseString(s):
    i = 0  # Pointer 1: Starts from the beginning of the list
    j = len(s) - 1  # Pointer 2: Starts from the end of the list
    while i < j:  # Swap elements until the pointers meet
        s[i], s[j] = s[j], s[i]
        i += 1  # Move Pointer 1 towards the right
        j -= 1  # Move Pointer 2 towards the left

    return s  # The list is modified in place, so we can return it if needed


# Test cases
s1 = ["h","e","l","l","o"]
s2 = ["p","y","t","h","o","n"]

print(reverseString(s1))  # Output = ['o', 'l', 'l', 'e', 'h']
print(reverseString(s2))  # Output = ['n', 'o', 'h', 't', 'y', 'p']
