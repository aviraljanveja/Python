# Class Methods = They allow operations related to the class itself, rather than instances of the class.
# Class methods are defined using the @classmethod decorator and take "cls" as the first parameter, which refers to the class itself.
# They are best used for methods that need to access or modify class-level data.


class Student:
    
    count = 0  # Class variable to keep track of the number of students
    total_gpa = 0  # Class variable to keep track of the total GPA of all students

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1  # Increment the count whenever a new student is created
        Student.total_gpa += gpa  # Add the GPA of the new student to the total GPA
    
    def get_info(self):  # Instance method
        return f"{self.name} has a GPA of {self.gpa}"
    
    @classmethod
    def get_count(cls):  # Class method to access the class variable count
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def average_gpa(cls):  # Class method to access the class variable total_gpa
        if cls.count == 0:
            return 0
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"  # Calculate the average GPA by dividing total GPA by the count of students


# Creating instances of Student
student1 = Student("Ronaldo", 8.5)
student2 = Student("Kaka", 7.8)
student3 = Student("Bale", 8.2)


# Calling instance method get_info for each student
print(student1.get_info())  # Output: Ronaldo has a GPA of 8.5
print(student2.get_info())  # Output: Kaka has a GPA of 7.8
print(student3.get_info())  # Output: Bale has a GPA of 8.2


# Calling class methods to get the total count of students and the average GPA
print(Student.get_count())
print(Student.average_gpa())
