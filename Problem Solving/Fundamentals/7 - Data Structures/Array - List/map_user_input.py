# Mapping User Input
"""
The map() function in Python is a built-in function that applies
a given function to every item in an iterable (like a list or string)
and returns a map object (which can be converted into a list, tuple, etc.).
It is widely used for efficient transformations and conversions,
especially during tasks like taking input and processing it immediately.
"""
# Syntax : map(function, iterable)
# function: The function to apply to each item in the iterable.
# iterable: An iterable like a list, tuple, or string.

user_input = "1 2 3 4"
nums = list(map(int, user_input.split()))
print(nums)  # Output = [1, 2, 3, 4]

# split() splits the input string into a list of substrings.
# map(int, ...) converts each substring to an integer.
# list() constructor converts the map objet back to a list.

"""
Lazy evaluation : 
The map() function in Python returns a lazy iterator (a map object) 
instead of an immediately evaluated list or tuple.
This is by design, as it allows for memory efficiency and performance when working with large datasets.
A map object computes values on demand instead of generating all values upfront.
This minimizes memory usage, especially for large iterables, since only one item is processed at a time.
"""
# Lazy Evaluation Example :
result = map(int, ["1", "2", "3"])
print(result)  # Output: <map object at 0x...>
# To display or access the items from the map object,
# you need to explicitly convert it into a list, tuple, or iterate through it
print(list(result))  # Output: [1, 2, 3]

# map() alternative with for loop :
user_input2 = "1 2 3 4"
user_input2_split = user_input2.split()
nums2 = []
for i in user_input2_split:
    nums2.append(int(i))
print(nums2)  # Output = [1, 2, 3, 4]
