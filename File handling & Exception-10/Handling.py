file = open("data.txt", "r")
data = file.read()
print(data)
file.close()


# file = open("data.txt", "w")
# file.write("Hello  , Every one my name Amen maurya")
# file.close()

# open() → open the notebook
# read() → read what is written
# write() → write something
# close() → close the notebook

# So, File Handling = Working with stored data in files using Python.

# Creating a File in Python
# We can create a file using the open() function.

file = open("data.txt", "w")
file.close()


# data.txt → name of the file
# "w" → write mode
# close() → closes the file
# If data.txt does not exist, Python will create it automatically.

# "w" → Write → Create/Overwrite
# "r" → Read  → Read existing data

# Create and write

with open("student.txt", "w") as file:
    file.write("Name: Aman\n")
    file.write("Course: B.Tech CSE\n")
    file.write("Language: Python\n")
# Read
with open("student.txt", "r") as file:
    data = file.read()
    print(data)