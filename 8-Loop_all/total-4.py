# Total using for loop

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total = total + num
# print("Total =", total)


# Highest number using loop
numbers = [10, 25, 7, 45, 18]

highest = numbers[0]

for num in numbers:
    if num > highest:
        highest = num
print("Highest =", highest)

# Lowest number using loop

numbers = [10, 25, 7, 45, 18]
lowest = numbers[0]
for num in numbers:
    if num < lowest:
        lowest = num
print("Lowest =", lowest)

# Total + Highest + Lowest

numbers = [10, 25, 7, 45, 18]

total = 0
highest = numbers[0]
lowest = numbers[0]

for num in numbers:
    total = total + num

    if num > highest:
        highest = num

    if num < lowest:
        lowest = num

print("Total =", total)
print("Highest =", highest)
print("Lowest =", lowest)

