# Class : a class in python is a blueprint for creating objects. It defines a set of attributes(variables) and methods(functions) that the created objects will have.
# For example, the inbuilt list class in Python.

# Object : an object is an instance of a class. It is a specific realization of the class with its own unique data.
# For example, when we create a specific list object like list1 = [1, 2, 3]


# Defining our own class.
class Coordinate:

    def __init__(self, x, y):  # Special method for initializing class objects, also called constructor.
        self.x = x  # self refers to the current object.
        self.y = y  # x and y are the coordinate values passed-in while creating the current object.

    def distance(self, other):  # Distance method to calculate euclidean distance between two coordinate objects
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5  # Euclidean distance formula

    def __str__(self):  # Special method for printing string representations of Coordinate objects.
        return f"({self.x}, {self.y})"


# Creating objects of type Coordinate
c = Coordinate(3, 4)
o = Coordinate(0, 0)


# Accessing data-attributes of the object using dot-notation
print(c.x)  # 3
print(o.x)  # 0


# Calling the distance method on Coordinate objects
# As we have done for lists previously, for example list1.extend(list2)
print(c.distance(o))  # 5.0


# Printing out the string representation of Coordinate objects as per the __str__ method defined above
print(c)  # (3, 4)
print(o)  # (0, 0)
