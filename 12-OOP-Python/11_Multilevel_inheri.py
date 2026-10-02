""" --- Definition
Jab inheritance ek chain mein hoti hai, use Multilevel Inheritance kehte hain."""

class Grandfather:

    def house(self):
        print("Grandfather has a house")
class Father(Grandfather):
    def car(self):
        print("Father has a car")
class Son(Father):
    def bike(self):
        print("Son has a bike")
s = Son()

s.house()
s.car()
s.bike()


# Important Concept: super()
"""super() parent class ke methods/constructor ko access karne ke liye use hota hai."""

class Person:

    def __init__(self, name):
        self.name = name
class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
class EngineeringStudent(Student):
    def __init__(self, name, roll_no, branch):
        super().__init__(name, roll_no)
        self.branch = branch
s = EngineeringStudent("Aman", 101, "CSE")
print(s.name)
print(s.roll_no)
print(s.branch)