"""Method Overriding ka matlab hai:---
Child class parent class ke existing method ko apne according redefine karti hai."""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog says Bark")
animal = Animal()
dog = Dog()

animal.sound()
dog.sound()


# 👉 Overloading = same class/method, different inputs
# 👉 Overriding = parent-child, same method, different   implementation