# A for loop in Python is used to iterate (loop) over a sequence like a list, tuple, string, dictionary, or range. It executes a block of code once for each item in the sequence. 


numbers = [1, 2, 3, 4]
for num in numbers:
    print(num)

    # Loop over String
    name = "Aman"
for ch in name:
    print(ch)

    # Loop over Dictionary
data = {"name": "Aman", "age": 19}
for key in data:
    print(key, data[key])   

    # Using break, continue, pass

for i in range(5):
    if i == 3:
     break
    print(i)