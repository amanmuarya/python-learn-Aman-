# sub() in Python — Substituting a Pattern 

# Python की re module में re.sub() का use किसी pattern को find करके 
# उसके place पर दूसरा text डालने के लिए किया जाता है।
# re.sub() = Find + Replace

# pattern → क्या ढूँढना है
# replacement → उसकी जगह क्या डालना है
# string → किस text में search करना है

import re

text = "I like Java. Java is powerful."
result = re.sub(r"Java", "Python", text)
print(result)

# findall() → Find all 
# finditer() → Find all + details 
# sub() → Find + Substitute/Replace