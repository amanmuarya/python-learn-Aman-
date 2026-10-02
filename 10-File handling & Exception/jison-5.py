# The json module**  in python , **The pickle module**  , **Pickle and exception handling  


#  Python Dictionary → JSON
# Python mein hum dictionary ko JSON string mein convert kar sakte hain using

import json

student = {
    "name": "Aman",
    "age": 20,
    "course": "B.Tech"
}
data = json.dumps(student)
print(data)
print(type(data))


#  `json.dump()`  | JSON ko file mein write karta hai                   
#  `json.dumps()` | JSON string banata hai                              
#  `json.load()`  | JSON file se data read karta hai                    
#  `json.loads()` | JSON string ko Python object mein convert   karta hai 
