# A deep copy creates a completely independent copy, including all nested objects.

# Think: “Everything is cloned fully”
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 100

print(original)  # [[1, 2], [3, 4]]
print(deep)      # [[100, 2], [3, 4]]

# Outer list copied ✅
# Inner lists also copied ✅ (different memory)
# Where to use Deep Copy?

# Data is nested (list inside list, dict inside dict)
# You want completely independent objects
# No side effects allowed