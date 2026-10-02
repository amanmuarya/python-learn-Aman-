# A nested if statement means an if block inside another if block.

age = 20
has_id = True
if age >= 18:
    if has_id:
        print("You can enter")

# next example
# 
marks = 75
if marks >= 50:
    if marks >= 70:
        print("Grade A")
    else:
        print("Grade B")
else:
    print("Fail")  

#  Ternary Operator
# 
# The ternary operator is a short way to write if-else in one line.

# value_if_true if condition else value_if_false

num = 7
print("Even" if num % 2 == 0 else "Odd") 

# next example

a = 10
b = 20
max_value = a if a > b else b
print(max_value)