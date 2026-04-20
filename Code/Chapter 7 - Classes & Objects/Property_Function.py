# Property with the function syntax

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

    age = property(get_age, set_age)  # Using the in-built property function
    # to call getters and setters while still being able to
    # access and modify attributes in a regular way.


leo = Animal(2)
print(leo.age)  # Accessing the attribute like regular

leo.age = 3  # Modifying the attribute like regular
print(leo.age)

leo.age = "old"
print(leo.age)  # Still raises Type Error as required
