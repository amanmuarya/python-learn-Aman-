# instance method 
# define inside a class witch is bound to / associated with instance / boject 

# help(list)

class student1:
    """this is class student to manage info and activitiecs """

    def study(self): 
        print(f"self is {self}")
        print("Aman kushwaha read book every Day ") 

s1 = student1()

s1.study()
print(f"the object is {s1}")

""" when we call an instance method using the object / instance of the class python pass the object itself as the first argument to that method 
That first argument is by standerd is self """