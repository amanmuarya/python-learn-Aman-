# findall() searches the entire string and returns all matching values in a list.
import re
text = "I have 10 apples, 20 bananas and 30 mangoes."
result = re.findall(r"\d+", text)
print(result)

# next example
import re
text = "Python is easy and Python is powerful Python ."
result = re.findall(r"Python", text)
print(result)