# Raising Exceptions in Python

# Python me raising exceptions ka matlab hai ki hum khud deliberately ek exception generate (raise) karte hain, jab koi condition invalid ho.
# Iske liye Python me raise keyword use hota hai

print(10 / 0)   # ZeroDivisionError: division by zero

# Lekin hum khud bhi exception raise kar sakte hain
age = 15
if age < 18:
    raise ValueError("You must be 18 or older")

# raise ka Real-Life Use
balance = 5000
withdraw = 7000

if withdraw > balance:
    raise ValueError("Insufficient balance")
balance -= withdraw
print("Withdrawal successful")

