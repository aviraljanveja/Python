# Defining Getter and Setter Methods to control access and modification of private variables.

class Animal:
    def __init__(self, age):
        self.__age = age  # Private variable age

    def get_age(self):  # Getter method to access private variable
        return self.__age

    def set_age(self, new_age):  # Setter method to modify private variable
        if isinstance(new_age, int):  # with validation checks
            self.__age = new_age
        else:
            raise TypeError("Animal age must be an integer")


leo = Animal(2)
print(leo.get_age())  # Output : 2

leo.set_age(3)
print(leo.get_age())  # Output : 3

leo.set_age("old")  
print(leo.get_age())  # Raises Type Error as required
