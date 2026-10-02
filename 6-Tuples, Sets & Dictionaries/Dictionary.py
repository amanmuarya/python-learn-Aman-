student = {
    "name": "Aman",
    "age": 19,
    "course": "CSE"
}

print(student["name"])     # Aman
print(student.get("age"))  # 19

# All Operations Togethe
student = {"name": "Aman", "age": 19}
# Update
student["age"] = 20
student["city"] = "Varanasi"
# Delete
student.pop("age")

print(student)