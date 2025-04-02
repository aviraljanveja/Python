# LeetCode 242 - Valid Anagram
# Problem Link : https://leetcode.com/problems/valid-anagram/description/

def isAnagram(s, t):
    # Helper function to convert a string into a dictionary with character counts
    def dictConvert(arr):
        d = {}
        for i in arr:
            if i in d:  # If the character is already in the dictionary, increment its count
                d[i] += 1
            else:  # else, add it with a count of 1
                d[i] = 1
        return d

    # Compare the dictionaries generated from both strings
    # If they are equal, the strings are anagrams
    return dictConvert(s) == dictConvert(t)


# Test cases
s1 = "anagram"
t1 = "nagaram"
print(isAnagram(s1, t1))  # Output = True

s2 = "rat"
t2 = "car"
print(isAnagram(s2, t2))  # Output = False
