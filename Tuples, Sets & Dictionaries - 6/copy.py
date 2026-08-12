# A shallow copy creates a new outer object, but inner objects are still shared (same reference).

import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 100
print(original)    # [[100, 2], [3, 4]]
print(shallow)   # [[100, 2], [3, 4]]

# A deep copy creates a completely independent copy, including all nested objects.

import copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 100
print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[100, 2], [3, 4]]