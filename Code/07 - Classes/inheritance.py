# Inheritance allows us to define a child class that inherits all the data attributes
# and methods from its parent class. Here is a simple example.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Inherits from Animal
    def __init__(self, name, breed=None):
        Animal.__init__(self, name)  # Inheriting Animal's __init__ method
        self.breed = breed  # Initialize 'breed' attribute, Default value set to None

    def speak(self):
        print(f"{self.name}, the {self.breed}, barks.")  # Overrides speak method of Animal


# Creating objects
an_animal = Animal("Animal")
dog = Dog("Leo", "German Shepherd")

# Calling the speak method
an_animal.speak()  # Output: Animal makes a sound.
dog.speak()  # Output: Leo, the German Shepherd, barks.
