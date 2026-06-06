# Data Classes in Python
# A special type of class that is used to store data without having to write a lot of boilerplate code.
# It automatically generates special methods like __init__(), __repr__(), __eq__() and others based on the class attributes defined in the class body.


from dataclasses import dataclass  # Importing the dataclass decorator from the dataclasses module


@dataclass  # Using the dataclass decorator to define a data class
class Doggo:
    # Inside the data class, you just need to define the attributes with their types,
    # and the dataclass will automatically generate the __init__, __repr__ and __eq__ methods for you.
    name: str
    age: int
    is_alive: bool = True  # Default value for is_alive is set to True


doggo1 = Doggo("Leo", 5)
doggo2 = Doggo("Junior", 2)

print(doggo1)  # Output: Doggo(name='Leo', age=5, is_alive=True)
print(doggo2)  # Output: Doggo(name='Junior', age=2
print(doggo1 == doggo2)  # Output: False
