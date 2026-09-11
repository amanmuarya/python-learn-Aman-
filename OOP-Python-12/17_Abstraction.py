"""Definition

Abstraction means hiding unnecessary implementation details and showing only the essential features to the user."""

#User ko sirf "kya karna hai" dikhana, "andar kaise ho raha hai" hide karna = Abstraction.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):

    def start(self):
        print("Car starts with a key")
car = Car()
car.start()

#   Abstraction = What to do दिखाना, How to do छिपाना।

"""Abstract Class in Python

An abstract class is a class that is used as a blueprint for other classes. It can contain abstract methods, which are methods declared in the parent class but implemented by its child classes."""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass