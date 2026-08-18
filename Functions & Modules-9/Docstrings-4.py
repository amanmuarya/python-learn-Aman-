# Docstrings in Python Functions

# A docstring (documentation string) is a special string used to describe what a function, class, or module does.

# Basic Syntax

# def function_name():
#     """This is the docstring of the function."""
    # function code

def greet():
    """This function prints a greeting message."""
    print("Hello, Aman!")

greet()

#   """This function prints a greeting message.""" → Docstring
# It explains what the greet() function does.
# It makes the code easier to understand.



def add(a, b):
    """
    This function adds two numbers.
    Parameters:
        a: First number
        b: Second number
    Returns:
        The sum of a and b.
    """
    return a + b
result = add(10, 20)
print(result)

