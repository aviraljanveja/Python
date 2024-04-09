# An efficient implementation of the fibonacci number computing function.
# Using "memoization" : meaning caching already calculated values,
# using a dictionary, in order to prevent wasteful function calls.

fib_cache = {}  # Using dictionary to cache already computed values.


def fast_fib(n):
    # If we have the value cached already, then simply return it.
    if n in fib_cache:
        return fib_cache[n]

    # Otherwise, compute the Nth term.
    if n <= 1:
        value = 1
    else:
        value = fast_fib(n - 1) + fast_fib(n - 2)

    # Cache the value first and then return it.
    fib_cache[n] = value
    return value


for i in range(0, 101):
    print(i, ":", fast_fib(i))
