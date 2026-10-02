"""Method Overloading ka matlab hai same method name ko different parameters ke saath use karna."""

#Java/C++ ki tarah Python mein traditional method overloading directly supported nahi hai.

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


obj = Calculator()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))

#Isliye Python mein method overloading achieve karne ke liye commonly default arguments ya *args use karte hai

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c
obj = Calculator()

print(obj.add(10, 20))
print(obj.add(10, 20, 30))