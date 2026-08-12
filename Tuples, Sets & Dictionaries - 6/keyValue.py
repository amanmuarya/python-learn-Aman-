student = {
    "name": "Aman",
    "age": 20,
    "course": "B.Tech"
}

print(student)


# example basic orperation
student = {"name": "Aman", "age": 20}
# Add
student["city"] = "Varanasi"
# Update
student["age"] = 21
# Access
print(student.get("name"))
# Delete
student.pop("city")
# Loop
for k, v in student.items():
    print(k, v)