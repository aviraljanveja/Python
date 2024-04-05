# Function to calculate the nth Fibonacci number using recursion in Python :

# The Fibonacci numbers were first described in Indian mathematics as early as 200 BC
# in work by Maharishi Pingala on enumerating possible patterns of Sanskrit poetry.
# They are named after the Italian mathematician Leonardo of Pisa, also known as Fibonacci,
# who introduced the sequence to Western European mathematics in 1202.
# We therefore refer to them as Pingala numbers going forward.

def pingala(n):
    if n <= 1:  # Base case
        return n
    else:  # Recursive Step
        return pingala(n-1) + pingala(n-2)


# Example usage:
print(pingala(9))
