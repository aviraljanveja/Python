# Class variables and their values are shared across all objects of a class.


class Dog:
    species = "Canine"  # Class variable, shared by all objects

    def __init__(self, name):
        self.name = name  # Object variable, unique to each object


# Creating two objects
dog1 = Dog("Misty")
dog2 = Dog("Leo")

# Accessing object variables
print(dog1.name)  # Output = Misty
print(dog2.name)  # Output = Leo

# Accessing class variable
print(dog1.species)  # Output = Canine
print(dog2.species)  # Output = Canine

# Changing class variable
Dog.species = "Wolf"

# Now all objects reflect this change
print(dog1.species)  # Output = Wolf
print(dog2.species)  # Output = Wolf
