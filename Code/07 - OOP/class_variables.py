# Class variables and their values are shared across all objects of a class.


class Dog:
    species = "pet dogs"  # Class variable, shared by all objects
    pet_num = 0  # Class variable to keep track of the number of dog objects created

    def __init__(self, name):
        self.name = name  # Object variable, unique to each object
        Dog.pet_num += 1  # Increment the class variable pet_num each time a new dog object is created


# Creating Dog objects
dog1 = Dog("Misty")
dog2 = Dog("Leo")
dog3 = Dog("Junior")
dog4 = Dog("Brownie")


# Accessing object variables
print(dog1.name)  # Output = Misty
print(dog2.name)  # Output = Leo
print(dog3.name)  # Output = Junior
print(dog4.name)  # Output = Brownie


# Accessing class variables
print(f"I have had {Dog.pet_num} {Dog.species} in life till now.")  # Output = I have had 4 pet dogs in life till now.
