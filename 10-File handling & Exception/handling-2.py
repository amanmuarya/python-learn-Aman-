# Appending into a File
# Appending ka matlab hai kisi existing file ke end mein new data add karna, bina purane data ko delete kiye.

file = open("data.txt", "a")
file.write("New data\n")
file.close()


# Suppose ek website/app mein user login history store karni hai:
file = open("login.txt", "a")
file.write("Aman logged in\n")
file.close()
# Har baar user login karega, new entry last mein add hoti jayegi.


# with Statement
# Normally file ke saath hume manually close() karna padta hai

with open("data.txt", "r") as file:
    data = file.read()
print(data)

# with ka fayda
# Agar file ke saath koi error bhi aa jaye, Python properly file ko close karne ka management karta hai.

# 3. Check if a File Exists
# Kabhi-kabhi program ko pehle check karna hota hai ki file actually exist karti hai ya nah

import os
if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")