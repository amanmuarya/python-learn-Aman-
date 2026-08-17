# A shallow copy creates a new outer object, but inner objects are still shared (same reference).

# Think: “New container, same contents inside”

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 100
print(original)  # [[100, 2], [3, 4]]
print(shallow)   # [[100, 2], [3, 4]]

# Where to use Shallow Copy?
# Use when:
# Data is flat (no nesting) OR
# You don’t care if inner objects change
# Faster & less memory usage