# Real-Life Example: Password Character Checking 🔐
# Suppose you want to check whether a password contains a digit.
import re
password = "Aman123"
result = re.search(r"[0-9]", password)
if result:
    print("Password contains a number")
else:
    print("No number found")