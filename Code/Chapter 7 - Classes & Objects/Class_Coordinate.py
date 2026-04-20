#  Defining our own class.

class Coordinate:

    def __init__(self, x, y):  # Constructor method to initialize class objects
        self.x = x  # self refers to the class object
        self.y = y  # x and y are coordinate values passed in while creating the object.

    def distance(self, other):  # Distance method to calculate euclidean distance between two coordinate objects
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5  # Euclidean distance formula

    def __str__(self):  # Special method to specify string representation of Coordinate objects
        return "(" + str(self.x) + "," + str(self.y) + ")"


# Creating objects of type Coordinate
c = Coordinate(3, 4)
origin = Coordinate(0, 0)

# Accessing data-attributes of the object using dot-notation
print(c.x)  # 3
print(origin.x)  # 0

# Calling the distance method on Coordinate objects
# As we have done for lists previously, for example list1.append()
print(c.distance(origin))  # 5.0
print(origin.distance(c))  # 5.0

# Printing out the string representation of Coordinate objects as per the __str__ method defined above
print(c)  # (3,4)
print(origin)  # (0,0)
