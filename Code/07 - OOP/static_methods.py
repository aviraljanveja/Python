# Static Methods = a method that belongs to a class rather than any instance of that class. 
# Static methods are defined using the @staticmethod decorator.
# They are best used for general utility functions that do not need access to class data.


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def get_info(self):  # Instance method that accesses instance variables
        return f"{self.name} = {self.position}"

    @staticmethod
    def valid_position(position):  # Static method that validates the position without needing access to class variables
        valid_positions = ["Manager", "Developer", "Designer"]
        return position in valid_positions
    

# Creating instances of Employee and calling the instance method get_info
emp1 = Employee("ronaldo", "Manager")
emp2 = Employee("kaka", "Developer")
print(emp1.get_info())  # Output: ronaldo = Manager
print(emp2.get_info())  # Output: kaka = Developer


# In order to call a static method, we can use the class name directly without needing to create an instance of the class.
print(Employee.valid_position("Manager"))  # Output: True
print(Employee.valid_position("Intern"))  # Output: False
