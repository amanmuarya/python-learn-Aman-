# Negated Character Class [^]
# A ^ inside a character class means NOT.
import re

text = "Aman123"
result = re.findall(r"[^0-9]", text)
print(result)
# Any character that is NOT a digit.


