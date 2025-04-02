# LeetCode 50 - Powxn (https://leetcode.com/problems/powx-n/description/)

def Pow(x, n):
    if x == 0 and n < 0:  # Check for an edge case: if the base is 0 and the exponent is negative
        return "undefined"  # 0 raised to a negative power is mathematically undefined.
    else:
        return x ** n  # Use Python's built-in power operator (**) to calculate x raised to the power of n.

solution1 = Pow(2, 3)
solution2 = Pow(2, -3)
print(solution1)  # Output = 8
print(solution2)  # Output = 0.125