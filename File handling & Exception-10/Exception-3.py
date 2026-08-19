#   Exception-3.py


# Exception kya hota hai?
# Exception ek error hota hai jo program run hone ke time par occur hota hai aur program ke normal flow ko rok sakta hai.
a = 10
b = 0
print(a / b)   # ZeroDivisionError: division by zero


# Exception Handling kya hai?
# Agar program me error aaye aur hum nahi chahte ki poora program crash ho, to hum Exception Handling use karte hain.

try:
    a = 10
    b = 0
    print(a / b)
except:
    print("Something went wrong")


#     else in Exception Handling
# else tab execute hota hai jab try block me koi exception nahi aata.

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)

#   7  finally in Exception Handling
# finally block almost always execute hota hai, chahe exception aaye ya na aaye.

try:
    num = 10 / 2
    print(num)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Program finished")



#     Easy way to remember
# try  "Code ko try karo"
# except  "Agar error aaye to handle karo"
# else  "Agar error nahi aaya to ye karo"
# finally → "Chahe kuch bhi ho, ye karo"