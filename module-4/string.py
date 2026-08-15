# | Method         | Purpose                                         | Example                       | Output          |
# | -------------- | ----------------------------------------------- | ----------------------------- | --------------- |
# | `count()`      | Counts occurrences of a substring               | `"banana".count("a")`         | `3`             |
# | `upper()`      | Converts all letters to uppercase               | `"python".upper()`            | `"PYTHON"`      |
# | `lower()`      | Converts all letters to lowercase               | `"PYTHON".lower()`            | `"python"`      |
# | `title()`      | Capitalizes the first letter of each word       | `"hello world".title()`       | `"Hello World"` |
# | `capitalize()` | Capitalizes only the first letter of the string | `"hello".capitalize()`        | `"Hello"`       |
# | `swapcase()`   | Swaps uppercase and lowercase letters           | `"Hi PY".swapcase()`          | `"hI py"`       |
# | `startswith()` | Checks if the string starts with a prefix       | `"Python".startswith("Py")`   | `True`          |
# | `endswith()`   | Checks if the string ends with a suffix         | `"file.pdf".endswith(".pdf")` | `True`          |


# Bilkul! 😊 Niche ek real-world example diya hai jisme membership, strip, replace, count, case methods, startswith(), endswith() sabhi string operations ka use kiya gaya hai.

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


# another example

text = "   Welcome to Python Programming   "

print("Original:", text)

# strip
text = text.strip()
print("Strip:", text)

# Membership
print("'Python' exists:", "Python" in text)

# Replace
text = text.replace("Python", "Java")
print("Replace:", text)

# Count
print("Count of 'a':", text.count("a"))

# Cases
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Title:", text.title())

# Start and End
print("Starts with Welcome:", text.startswith("Welcome"))
print("Ends with Programming:", text.endswith("Programming"))