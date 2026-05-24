# multiple inheritance = Inheritance from more than one parent class : C(A, B)
# mulit-level inheritance = Inheritance from a parent class that inherits from another parent class : A, B(A), C(B)


class Living:
    def __init__(self, name):
        self.name = name
    
    def breathe(self):
        print(f"{self.name} breathes.")


class Animal(Living):  # Inherits from Living
    def eat(self):
        print(f"{self.name} eats.")


class Dog(Animal, Living):  # Inherits from both Animal and Living, demonstrating multiple inheritance and multi-level inheritance
    def bark(self):
        print(f"{self.name} says bow wow.")


# Creating objects
dog1 = Dog("Leo")
dog1.breathe()  # Output: Leo breathes.
dog1.eat()  # Output: Leo eats.
dog1.bark()  # Output: Leo says bow wow.
