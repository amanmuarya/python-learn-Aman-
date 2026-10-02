# Simple Definition
# A recursive function is a function that calls itself.

def count(n):
    if n == 0:
        return
    print(n)
    count(n - 1)
count(5)

# Factorial using Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))