"""What is Inheritance?
Inheritance means that one class can use the properties and methods of another class.
The class whose properties/methods are inherited → Parent / Base class
The class that inherits them → Child / Derived class"""

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
dog1 = Dog()

dog1.eat()
dog1.bark()

#  Inheritance with __init__()

class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("My name is", self.name)
class Student(Person):
    def study(self):
        print(self.name, "is studying")
student1 = Student("Aman")

student1.introduce()
student1.study()

#The child class doesn't only inherit things. It can also create new methods.

class animal:
    def eat(self):
        print("Animal is eating ")

class Dog(animal):
    def bark(self):
        print("Dog is barking ")

    def run(self):
        print("Dog is running ")

dog = Dog()

dog.eat()    # inherited
dog.bark()  # own method
dog.run()   # own method
                    
