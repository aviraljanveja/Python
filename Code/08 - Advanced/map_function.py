# The map() function in Python is a built-in function that applies a given function to every item in an iterable (like a list or tuple)
# and returns a map object (which can be converted into a list or tuple) It is widely used for efficient transformations and conversions,
# especially during tasks like input-processing.

# Syntax : map(function, iterable)
# function : The function to apply to each item in the iterable.
# iterable : An iterable like a list, tuple or string.

# Mapping User Input
user_input = "1 2 3 4"  # split() function splits the input string into a list of substrings.
nums = list(map(int, user_input.split()))  # map(int, ...) converts each substring to an integer, list() constructor converts the map objet back to a list.
print(nums)  # Output = [1, 2, 3, 4]

"""
Lazy evaluation : 
The map() function in Python returns a map object instead of a list or tuple.
This is by design, as it allows for memory efficiency and performance when working with large datasets.
A map object computes values on demand instead of generating all values upfront.
This minimizes memory usage, especially for large iterables, since only one item is processed at a time.
"""

# Lazy Evaluation Example :
result = map(int, ["1", "2", "3", "4"])
print(result)  # Output: <map object at 0x...>
# To display or access the items from this map object,
# you need to explicitly convert it to a list, tuple or iterate through it.
print(list(result))  # Output = [1, 2, 3, 4]

# map() function alternative with for-loop :
user_input2 = "1 2 3 4"
user_input2_split = user_input2.split()
nums2 = []
for i in user_input2_split:
    nums2.append(int(i))
print(nums2)  # Output = [1, 2, 3, 4]
