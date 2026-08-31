# finditer() also finds all matches, but instead of returning a list of strings, 
# it returns an iterator containing Match objects.

"""import re
text = "I have 10 apples and 20 bananas."
matches = re.finditer(r"\d+", text)
for match in matches:
    print(match)"""


    # Getting the actual matched value
import re
text = "I have 10 apples and 20 bananas."
matches = re.finditer(r"\d+", text)
for match in matches:
    print(match.group())