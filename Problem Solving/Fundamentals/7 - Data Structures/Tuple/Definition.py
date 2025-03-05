# Tuples in Python :
# A tuple is an immutable, ordered collection of elements.
# They are often used when you want to ensure the data cannot be changed,
# providing a layer of protection for the data integrity.

"""
Key Characteristics:
Ordered: Elements have a defined order and can be indexed.
Immutable: Once created, the elements cannot be changed, added, or removed.
Allows Duplicates: Like lists, tuples can contain duplicate elements.
Heterogeneous: Can contain elements of different data types.
"""

# Defining Tuples
tuple0 = ()  # Empty Tuple
tuple1 = (1,)  # Single element tuple, comma is mandatory
tuple2 = (1)  # just (1) would be considered an integer in parenthesis
tuple3 = (1, 2, 3, 4)

print(tuple0)  # Output = ()
print(type(tuple1))  # Output = <class 'tuple'>
print(type(tuple2))  # Output = <class 'int'>
print(tuple3)  # Output = (1, 2, 3, 4)
