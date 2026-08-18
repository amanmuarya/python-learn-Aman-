# Function as an Argument in Python

# Python में function को दूसरे function के argument के रूप में pass किया जा सकता है।
# मतलब एक function को call करते समय हम दूसरे function का नाम argument में दे सकते हैं।

def square(x):
    return x * x
def calculate(func, number):
    return func(number)
result = calculate(square, 5)
print(result)

# square → function को argument के रूप में pass किया
# 5 → number argument
# calculate() के अंदर func में square function आ गया
# func(5) → square(5)
# Result = 25

# --  इसे Higher-Order Function concept भी कहते हैं।


# Lambda Function

# Lambda function Python में एक small anonymous function होता है।
# Anonymous का मतलब है कि इसका कोई normal function name नहीं होता।

square = lambda x: x * x
print(square(5))



#      Syntax
#    lambda arguments: expression



# filter() with Lambda

# filter() का use किसी sequence/list में से condition के आधार पर elements select करने के लिए किया जाता है।

#  Syntax:
#  filter(function, iterable)

# Example: केवल even numbers निकालना

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))


# map() with Lambda
# map() का use हर element पर कोई operation perform करने के लिए किया जाता है।

#   Syntax
#   map(function, iterable)

numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x * x, numbers)
print(list(squares))