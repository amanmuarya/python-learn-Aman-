# strip() Method

# The strip() method removes unwanted characters from the beginning and end of a string.
# By default, it removes whitespace (spaces, tabs, newlines).

text = "   Hello Python   "
print(text.strip())



# Operations on strings - membership, strip, replace , count, cases, start, end  to use make simple example

# User input
name = "   aman kushwaha   "
course = "python programming"
email = "aman@gmail.com"

# 1. strip()
name = name.strip()
print("Name:", name)

# 2. title() (Case Method)
name = name.title()
print("Title Case Name:", name)

# 3. upper() (Case Method)
print("Upper Case:", course.upper())

# 4. lower() (Case Method)
print("Lower Case:", course.lower())

# 5. replace()
course = course.replace("python", "Java")
print("Updated Course:", course)

# 6. Membership (in)
print("gmail" in email)

# 7. Membership (not in)
print("yahoo" not in email)

# 8. count()
print("Letter 'a' in name:", name.count("a"))

# 9. startswith()
print(email.startswith("aman"))

# 10. endswith()
print(email.endswith(".com"))