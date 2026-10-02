#   introR_Ex.py

# here to start regular esprasion (reg.ex)

import re 
messgae = "the current python version is 3.12"

# if python present in message 
print("python" in messgae)
print("3.12" in messgae)
print("hello" in messgae)

print(messgae.find("python")) # 12

# example

import re
email = "aman@gmail.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

    