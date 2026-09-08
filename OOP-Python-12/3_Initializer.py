"""" What is an Initializer?
An initializer is the __init__() method inside a Python class.
It is used to initialize (set the initial values of) an object's data when the object is created."""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create the object outside the class
s1 = Student("Aman", 20)

print(s1.name)
print(s1.age)


""" 
| Initializer                                 | Instance Variable              |


| `__init__()` method                         | `self.name`, `self.age` etc.   |
| Initializes object data                     | Stores object data             |
| Called automatically when object is created | Belongs to a particular object |
| It is a method                              | It is a variable               |
| Example: `def __init__(...)`                | Example: `self.name = name`    |
"""