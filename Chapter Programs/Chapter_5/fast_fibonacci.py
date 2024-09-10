# Optimized implementation of the fibonacci number computing function using memoization.
# That is, storing already computed values, using a dictionary.
# In order to prevent wasteful function calls.

fib_cache = {}  # Using dictionary to store already computed values.


def fast_fib(n):
    # If we have the value computed and stored already, then simply return it.
    if n in fib_cache:
        return fib_cache[n]

    # Otherwise, compute the Nth term.
    if n <= 1:
        value = 1
    else:
        value = fast_fib(n - 1) + fast_fib(n - 2)

    # Store the value in dictionary and then return it.
    fib_cache[n] = value
    return value


for i in range(0, 101):
    print(i, ":", fast_fib(i))
