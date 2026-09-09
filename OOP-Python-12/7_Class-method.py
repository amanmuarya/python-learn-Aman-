class Student:
    college = "Subharti"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
Student.change_college("IIT")
print(Student.college)

#A class method is a method that works with the class itself, rather than with a particular object (instance).

#In Python, we create a class method using the @classmethod decorator.

""" `self`                         `cls`                    

| Refers to an **object/instance** | Refers to the **class**  |
| Used in instance methods         | Used in class methods    |
| Accesses instance variables      | Accesses class variables |
| Example: `self.name`             | Example: `cls.school`    |
"""