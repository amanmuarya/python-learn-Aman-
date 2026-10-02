# What is random in Python?

# random Python ka built-in module hai jo random values generate karne ke liye use hota hai.

import random
num = random.randint(1, 10)
print(num)

# Random decimal number — random()
import random
num = random.random()
print(num)

# List se random item — choice()
import random
fruits = ["Apple", "Mango", "Banana", "Grapes"]
fruit = random.choice(fruits)
print(fruit)

# List ko randomly shuffle karna — shuffle()
# Original list ka order change ho gaya.
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

# Real-life example: Dice
import random
dice = random.randint(1, 6)
print("You got:", dice)