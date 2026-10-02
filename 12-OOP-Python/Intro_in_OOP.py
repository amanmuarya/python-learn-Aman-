# here to creat class

class car:
    pass

"""  Car → Class name
class → Keyword used to create a class
pass → Nothing is defined yet  """


"""   What is an Object?
-- An object is an instance of a class."""
class Car:
    pass
car1 = Car()
car2 = Car() 

print(car1)

"""Class with Attributes--
Attributes are variables that store information about an object. """

class Student:
    name = "Aman"
    age = 20

# Create an object
student1 = Student()
print(student1.name)
print(student1.age) 

""" Class with Methods--
A method is a function inside a class."""
class Student:
    def introduce(self):
        print("Hello, I am a student")
# Create object
student1 = Student()
student1.introduce()        


# Complete Example
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)
student1 = Student("Aman", 20)
student1.introduce()

"""--Understanding self
self refers to the current object."""

class Student:
    def introduce(self):
        print("Hello")