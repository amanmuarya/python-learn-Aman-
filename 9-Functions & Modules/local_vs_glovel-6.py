# Local Variable
# A local variable is a variable that is created inside a function.
# It can be accessed only inside that function.

# Example

def my_function():
    name = "Aman"   # Local variable
    print(name)
my_function()


#  Global Variable
# A global variable is a variable that is created outside any function.
# It can be accessed from different parts of the program, including inside functions.

# Example

name = "Aman"   # Global variable
def my_function():
    print(name)
my_function()
print(name)
