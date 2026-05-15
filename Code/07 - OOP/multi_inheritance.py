#  multiple and multi-level Inheritance in Python.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Inherits from Animal

    # You can extend the __init__ method of the parent class to include additional attributes specific to the Dog class using the super() function.
    def __init__(self, name, breed=None):
        super().__init__(name)  # Inheriting Animal's __init__ method and
        self.breed = breed  # extending it with the 'breed' attribute, with default value set to None

    # Method overriding: we can override the speak method of the parent class to provide a specific implementation for Dog objects.
    def speak(self):
        print(f"{self.name}, the {self.breed}, barks.")


# Creating objects
an_animal = Animal("Animal")
dog = Dog("Leo", "German Shepherd")


# Calling the speak method
an_animal.speak()  # Output: Animal makes a sound.
dog.speak()  # Output: Leo, the German Shepherd, barks.
