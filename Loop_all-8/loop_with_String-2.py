# Python string "Python" ko ek sequence ki tarah dekhta hai. 

# word = "Python"
# for letter in word:
#     print("Letter:", letter)

    # String ke characters ko count karna

hee = "hello world"
count = 0
for letter in hee:
    count += 1 
print(count)

# for loop with Dictionary
# Dictionary mein key-value pairs hote hain.

student = {
    "name": "Aman",
    "age": 20,
    "course": "CSE"
} 

# A. Dictionary ki keys access karna
# Normally dictionary par for loop lagane par keys milti hain
student = {
    "name": "Aman",
    "age": 20,
    "course": "CSE"
}
for key in student:
    print(key)

#     Values access karna
# .values() use kar sakte hain:
for value in student.values():
    print(value)

#     Keys + Values dono access karna
# .items() use karte hain

