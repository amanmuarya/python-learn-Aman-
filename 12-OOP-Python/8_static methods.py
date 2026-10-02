"""Static Method in Python
A static method is a method inside a class that does not use self or cls."""

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
result = Calculator.add(10, 20)
print(result)

