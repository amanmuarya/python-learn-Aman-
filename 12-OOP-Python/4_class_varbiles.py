# Class Variable
# A class variable is a variable that belongs to the class itself, not to a particular object.

class Student:
    college = "Subharti University"   # Class Variable

    def __init__(self, name):
        self.name = name               # Instance Variable
s1 = Student("Aman")
s2 = Student("Rahul")
print(s1.college)
print(s2.college)


""" Class Variable                     Instance Variable            

| Belongs to class                      | Belongs to object            |
| Shared by objects                     | Separate for each object     |
| Usually defined directly inside class  | Usually defined using `self` |
| Example: `college`                    | Example: `name`              |
"""



# Class Method
# A class method is a method that works with the class, rather than a particular object.


class Student:
    college = "Subharti University"
    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

Student.change_college("IIT Delhi")
print(Student.college)


#last example 
class Student:

    college = "Subharti"       # Class Variable

    def __init__(self, name):
        self.name = name       # Instance Variable

    def show_name(self):       # Instance Method
        print(self.name)

    @classmethod
    def show_college(cls):     # Class Method
        print(cls.college)

    @staticmethod
    def hello():               # Static Method
        print("Hello Student")