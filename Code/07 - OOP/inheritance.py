# Inheritance allows us to define a child class that inherits all the data attributes
# and methods from its parent class, allowing for code resuability and extensability. Here is an example : 


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):  # Inherits from Animal
    def __init__(self, name, breed=None):
        super().__init__(name)  # Inheriting Animal's __init__ method using the super() function and
        self.breed = breed  # extending it with the 'breed' attribute, with default value set to None

    def speak(self):  # Method overriding: we can override the speak method of the parent class 
        print(f"{self.name}, the {self.breed}, barks.")  # to provide a specific implementation for Dog objects.


# Creating objects
animal1 = Animal("Animal")
dog1 = Dog("Leo", "German Shepherd")


# Calling the speak method
animal1.speak()  # Output: Animal makes a sound.
dog1.speak()  # Output: Leo, the German Shepherd, barks.
