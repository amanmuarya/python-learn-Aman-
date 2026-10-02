# Python me function banane ke liye def keyword use hota hai.
def greet():
    print("Hello Aman")

greet()

# def -  function banane ka keyword
# greet  - function ka naam
# () -  parameters ke liye
# : -  function block start
# print() -    function ke andar ka code

# Built-in Functions

# Ye Python me already available hote hain.
# Examples:

print()
len()
type()
max()
min()
sum()

# next--2
numbers = [10, 20, 30]
print(len(numbers))
print(max(numbers))

# User-Defined Functions
# Jo function programmer khud banata hai, use User-Defined Function kehte hain.

def say_hello():
    print("Hello Python")

say_hello()

# Function with Parameters
# Function ko information/input dene ke liye parameters use karte hain.

def greet(name):
    print("Hello", name)
greet("Aman")
greet("Rahul")


# Parameter vs Argument
def greet(name):      # name = parameter
    print("Hello", name)

greet("Aman")         # "Aman" = argument
# Simple rule:
# Function define karte waqt - Parameter
# Function call karte waqt - Argument
# Ek function me multiple parameters bhi ho sakte hain.

def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Aman", 20, "Python")