""" Initialization ka matlab hai object ke andar starting values set karna."""
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Aman", 20)

print(student1.name)
print(student1.age)

#Arguments in Python

#  Argument wo actual value hoti hai jo hum function/method ko call karte waqt pass karte hain.
def add(a, b):
    print(a + b)
add(10, 20)  # ye 10 aur 20 ko argument kaht hai 


"""Arguments with __init__()"""
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Aman", 20)