# Simple example of Inheritance

class Animal:
    def __init__(self, name):
        self.name = name  # Initialize 'name' attribute

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Inherits from Animal
    def __init__(self, name, breed=None):
        Animal.__init__(self, name)  # Calling Animal's __init__ to inherit and avoid extra lines of code
        self.breed = breed  # Initialize 'breed' attribute, Default value set to None

    def speak(self):
        print(f"{self.name}, the {self.breed}, barks.")  # Overrides speak method of Animal


# Creating objects
any_animal = Animal("Animal")
dog = Dog("Leo", "German Shepherd")

# Calling the speak method
any_animal.speak()  # Output: Animal makes a sound.
dog.speak()  # Output: Leo, the German Shepherd, barks.
