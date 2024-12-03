# LeetCode 509 - Fibonacci Number (https://leetcode.com/problems/fibonacci-number/description/)

# Optimized implementation of Fibonacci number computation using memoization.
# Memoization helps avoid redundant recursive calls by storing precomputed results in a dictionary.
# Dictionary to store already computed Fibonacci values
fib_cache = {}

def fast_fib(n):
    if n in fib_cache:  # Check if the value is already computed and stored in the cache
        return fib_cache[n]

    if n <= 1:  # Base case: the first two Fibonacci numbers
        value = n  # Fib(0) = 0, Fib(1) = 1
    else:
        value = fast_fib(n - 1) + fast_fib(n - 2)  # Recursive case: Fib(n) = Fib(n-1) + Fib(n-2)

    fib_cache[n] = value  #  Store the value in dictionary for future use and return it.
    return value


# Compute and display Fibonacci numbers from 0 to 100
for i in range(0, 101):
    print(f"Fib({i}) = {fast_fib(i)}")