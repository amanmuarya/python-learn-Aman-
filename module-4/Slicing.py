a1 = "hello world"

print( a1[2:9:2])


# Characters:  P   y   t   h   o   n
# Indexes:     0   1   2   3   4   5
# Neg. Index: -6  -5  -4  -3  -2  -1

# | Code        | Output     | Explanation                  |
# | ----------- | ---------- | ---------------------------- |
# | `text[0:2]` | `'Py'`     | Characters from index 0 to 1 |
# | `text[2:6]` | `'thon'`   | Characters from index 2 to 5 |
# | `text[:4]`  | `'Pyth'`   | Start from the beginning     |
# | `text[2:]`  | `'thon'`   | Go until the end             |
# | `text[:]`   | `'Python'` | Copy the whole string        |


# start: Index where slicing begins (inclusive).
# stop: Index where slicing ends (exclusive).
# step: Number of positions to move each time (optional).
