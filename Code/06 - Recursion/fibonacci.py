# Function to calculate Fibonacci numbers using recursion in Python :

# Note : The Fibonacci numbers were first described in Indian mathematics as early as 200 BC
# in work by Maharishi Pingala on enumerating possible patterns of Sanskrit poetry.
# They are named after the Italian mathematician Leonardo of Pisa, also known as Fibonacci,
# who introduced the sequence to Western European mathematics in 1202.

def fibonacci(n):
    if n <= 1:  # Base case
        return n

    else:  # Recursive Step
        return fibonacci(n-1) + fibonacci(n-2)


# Example usage:
for i in range(0, 11):
    print(i, ":", fibonacci(i))
