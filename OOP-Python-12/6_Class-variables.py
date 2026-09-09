# Class Variables in Python
# Class Variable वह variable होता है जो class के अंदर define होता है और सभी objects के लिए common/shared होता है।
class Student:
    college = "Subharti"   # Class Variable

    def __init__(self, name):
        self.name = name    # Instance Variable

s1 = Student("Aman")
s2 = Student("Rahul")
print(s1.college)
print(s2.college)


# Class Methods in Python
# Class Method वह method होता है जो class के data (class variables) के साथ काम करता है। इसे @classmethod decorator से बनाया जाता है।

class Student:
    college = "Subharti"
    @classmethod
    def show_college(cls):
        print(cls.college)

# cls → current class को represent करता है।
# cls.college → class variable college को access करता है।  
# 
class Student:
    college = "Subharti"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college
Student.change_college("IIT")
print(Student.college)      