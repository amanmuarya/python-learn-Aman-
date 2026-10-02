# Arguments are the values that we pass to a function when we call it.

def greet(name):
    print("Hello", name)
greet("Aman")


# Python mainly has 5 types of arguments:

# Positional Arguments
# Keyword Arguments
# Default Arguments
# Variable-Length Arguments (*args)
# Variable-Length Keyword Arguments (**kwargs)


# Positional Arguments
# Arguments are matched with parameters according to their position/order.

def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Aman", 20)

# Keyword Arguments
# Here, we explicitly specify the parameter name while calling the function.
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=20, name="Aman")


# Default Arguments
# A parameter can have a default value.
def greet(name, message="Good Morning"):
    print(name, message)

greet("Aman")


# Variable-Length Arguments — *args
# Sometimes we don't know how many arguments will be passed.
# For this, we use *args.

def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)
add(10, 20)
add(10, 20, 30)
add(10, 20, 30, 40)


# Variable-Length Keyword Arguments  **kwargs

# **kwargs is used when we don't know how many keyword arguments will be passed.
def student(**details):
    print(details)
student(name="Aman", age=20, course="B.Tech")