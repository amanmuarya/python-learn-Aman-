# A list is a mutable (changeable), ordered collection that can store multiple values (even different data types).

lst = [1, 2, 3]
lst.append(4)
lst.insert(1, 10)
lst.extend([5, 6])
lst.remove(3)
lst.pop()
lst.reverse()
lst.sort()

print(lst)

# Slicing 
# Used to get a part of a list.
lst = [10, 20, 30, 40, 50]

print(lst[1:4])   # [20, 30, 40]
print(lst[:3])    # [10, 20, 30]
print(lst[::2])   # [10, 30, 50]

# Concatenation (+)
a = [1, 2]
b = [3, 4]
print(a + b)   # [1, 2, 3, 4]

# append()
# Adds element at the end.
lst = [1, 2, 3]
lst.append(4)
print(lst)   # [1, 2, 3, 4]

# insert()
# Adds element at a specific position.
lst = [1, 2, 3]
lst.insert(1, 100)

print(lst)   # [1, 100, 2, 3]


# Nested Lists 
# List inside another list.

lst = [[1, 2], [3, 4], [5, 6]]
print(lst[0])      # [1, 2]
print(lst[1][1])   # 4