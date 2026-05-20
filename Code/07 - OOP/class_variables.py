# Class variables and their values are shared across all objects of a class.


class Dog:
    species = "doggos"  # Class variable, shared by all objects
    doggo_num = 0  # Class variable to keep track of the number of dog objects created

    def __init__(self, name):
        self.name = name  # Object variable, unique to each object
        Dog.doggo_num += 1  # Increment the class variable doggo_num each time a new dog object is created


# Creating Dog objects
dog1 = Dog("Misty")
dog2 = Dog("Leo")
dog3 = Dog("Junior")
dog4 = Dog("Brownie")


# Accessing class variables
# It is good practice to access class variables using the class name rather than through an object, to make it clear that they are class variables.
print(f"I have had {Dog.doggo_num} {Dog.species} in my life till now.")  # Output = I have had 4 doggos in my life till now.


print(dog1.name)  # Output = Misty
print(dog2.name)  # Output = Leo
print(dog3.name)  # Output = Junior
print(dog4.name)  # Output = Brownie
