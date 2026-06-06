# Generators in Python
# A generator is defined using a function that contains the "yield" statement instead of return.
# The yield statement allows us to pause a function, return a value and then resume again.
# A generator allows you to iterate over a sequence without loading everything in memory at once. (For example, when reading large files)
# return = returns a value and terminates the function (like pouring a bucket)
# yield = pauses the function, returns a value, resumes the function. (like using a tap)


# For example : 
def count_to(n):
    count = 1
    while count <= n:
        yield count  # This will return the current value of count and pause the function until the next value is requested.
        count += 1


# Using the generator
number = int(input("Enter a number: "))
for num in count_to(number):
    print(num)
