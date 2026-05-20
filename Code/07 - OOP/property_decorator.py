# Using the inbuilt property function with @decorator syntax.
# It allows us to define getters & setters, thereby controlling access & modification of private variables,
# while still using them like regular variables.

class Animal:
    def __init__(self, age):
        self.__age = age  # Private variable age

    @property  # Property-getter via @decorator syntax
    def age(self):  # While using the property function, the method name should always be same as the attribute name : age in this case
        return self.__age

    @age.setter  # Property-setter via @decorator syntax
    def age(self, new_age):
        if isinstance(new_age, int):  # Validation check
            self.__age = new_age
        else:
            raise TypeError("Animal age must be an integer")


leo = Animal(2)
print(leo.age)  # Accessing the private variable like regular

leo.age = 4  # Modifying the private variable like regular
print(leo.age)

leo.age = "old"
print(leo.age)  # Still raises Type Error as required
