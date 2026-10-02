# The Dot Metacharacter and Character Classes in Python

import re
text = "cat"
result = re.search(r"c.t", text)
print(result.group())
# But . represents only one character.


 # Dot with +
 # You can combine . with +.
import re
text = "Hello Python"
result = re.search(r"H.+n", text)
print(result.group())

#  .+  one or more characters.


# Dot with  r".*"  zero or more characters.
import re
text = "Hello Python"
result = re.search(r"H.*n", text)
print(result.group())

# Character Classes []
# A character class allows you to specify which characters are allowed at a particular position.
import re
text = "cat"
result = re.search(r"c[aeiou]t", text)
print(result.group())

# Character Ranges
# Instead of writing every character, you can specify a range.
import re
text = "b.tech"
result = re.findall(r"[a-z]", text)
print(result)

# [0-9]
# Any digit from 0 to 9:


# Combining Ranges
# You can combine multiple ranges:
#   [a-zA-Z0-9]
import re
text = "Aman123@"
result = re.findall(r"[a-zA-Z0-9]", text)
print(result)