# ^ — Start of String

import re   
text = "Python is easy"
print(re.findall(r"^Python", text))


# ? — Zero or One
# ? का मतलब है पिछला character 0 या 1 बार आ सकता है।
text = "color colour"
print(re.findall(r"colou?r", text))

# यहाँ u? का मतलब है u optional है।


# {} — Exact Number
# {n} का मतलब है character exactly n times.
text = "aa aaa aaaa"
print(re.findall(r"a{3}", text))


# कम से कम n और ज्यादा से ज्यादा m times.
text = "a aa aaa aaaa aaaaa"
print(re.findall(r"a{2,4}", text))

# [] — Character Class
# [] के अंदर दिए गए characters में से कोई एक character match होता है।
text = "cat bat rat"
print(re.findall(r"[cbr]at", text))


# [^] — NOT
# Character class के अंदर ^ का मतलब है इन characters के अलावा कोई character.
text = "cat bat rat"
print(re.findall(r"[^c]at", text))
# [^c] → c के अलावा कोई character.

# ध्यान दें:
# ^abc → string की शुरुआत में abc
# [^abc] → a, b, c के अलावा कोई character



# () — Group
# () characters को एक group में रखता 
text = "apple banana apple"
print(re.findall(r"(apple)", text))