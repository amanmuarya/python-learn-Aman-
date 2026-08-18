# Function with return
# Function sirf output print hi nahi karta. Function value return bhi kar sakta hai.

def add(a, b):
    return a + b
result = add(10, 20)
print(result)
# calculated value ko function ke bahar bhej raha hai.

# print vs return

print("aman")
# ye valuse ko screen par print karta hai 

def add(a, b):
    return a + b
# Ye value ko function ke bahar return karta hai, jise hum variable me store kar sakte hain.

# normar example 

def add(a, b):
    result = a + b
    return result
answer = add(10, 20)
print("Answer:", answer)