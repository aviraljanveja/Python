# Class Variable Example

class Dog:
    species = "Canine"  # Class variable, shared by all instances

    def __init__(self, name):
        self.name = name  # Instance variable, unique to each instance


# Creating two instances
dog1 = Dog("Misty")
dog2 = Dog("Leo")

# Accessing instance variables
print(dog1.name)  # Output: Misty
print(dog2.name)  # Output: Leo

# Accessing class variable
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine

# Changing class variable
Dog.species = "Wolf"

# Now all instances reflect the change
print(dog1.species)  # Output: Wolf
print(dog2.species)  # Output: Wolf
