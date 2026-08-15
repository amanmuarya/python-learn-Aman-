# Syntax Difference
# List
l = [1, 2, 3]
# Tuple
t = (1, 2, 3)
# Set
s = {1, 2, 3}


# all example

t = (1, 2, 2, 3, 4)
print(max(t))    # 4
print(min(t))    # 1
print(sum(t))    # 12
print(t.count(2))  # 2
print(t.index(3))  # 3


#   Feature     Tuple        List            

#  Mutability    Immutable   Mutable      |
#  Syntax      ()           []              |
#   Speed       Fast        | Slightly slower |
#  Use Case    Fixed data  | Dynamic data    |

# next

# | Situation             | Use   |
# | --------------------- | ----- |
# | Data change hota rahe | List  |
# | Fixed data (constant) | Tuple |
# | Unique values chahiye | Set   |
# | Fast lookup chahiye   | Set   |
# | Ordered + safe data   | Tuple |
