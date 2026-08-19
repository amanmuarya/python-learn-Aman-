# Pickle kya hai?

# pickle Python ka built-in module hai jo Python objects ko save aur restore karne ke liye use hota hai.

# Serialization → Python object ko bytes format mein convert karna
# Deserialization → bytes ko wapas Python object mein convert karna

import pickle
student = {
    "name": "Aman",
    "age": 20,
    "skills": ["Python", "React", "JavaScript"]
}
with open("student.pkl", "wb") as file:
    pickle.dump(student, file)


# Pickle file ko read karna

import pickle

with open("student.pkl", "rb") as file:
    student = pickle.load(file)

print(student)


# | JSON                                  | Pickle                                

#  Human-readable hota hai                | Binary format hota hai                
#  Multiple languages support karti hain  | Mainly Python ke liye                 
#  APIs mein commonly used                | Python objects save karne mein useful 
#  Text format                            | Binary format                         
#  Relatively portable                    | Python-specific                       
#  `json.dump()`                          | `pickle.dump()`                       
