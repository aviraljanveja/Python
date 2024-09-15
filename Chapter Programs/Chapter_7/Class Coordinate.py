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


c = Coordinate(3, 4)  # Creating objects of type Coordinate
origin = Coordinate(0, 0)

print(c.x)  # 3
print(origin.x)  # 0

print(c.distance(origin))  # 5.0
print(origin.distance(c))  # 5.0

print(c)  # (3,4)
print(origin)  # (0,0)
