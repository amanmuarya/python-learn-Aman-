# Star pattern using for loops

# concept

# Outer loop  → Rows control karta hai
# Inner loop  → Har row mein kya print hoga, control karta hai

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()