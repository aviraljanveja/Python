# Property with the @decorator syntax

class Animal:
    def __init__(self, age):
        self.__age = age  # Private variable age

    @property  # Implementing the property method with @decorator syntax
    def age(self):
        return f"This animal is {self.__age} years old"  # Example of using Python f-strings

    @age.setter  # The method names should always be same as the attribute name : age in this case
    def age(self, new_age):
        if isinstance(new_age, int):
            self.__age = new_age
        else:
            raise TypeError("Animal age must be an integer")


leo = Animal(2)
print(leo.age)

leo.age = 3
print(leo.age)

leo.age = "old"
print(leo.age)
