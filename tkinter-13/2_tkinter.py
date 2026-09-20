#  Label, title, minsize, pack

# Label, title, minsize, pack

import tkinter as tk
import tkinter.font as tfont

window = tk.Tk()

window.title("My Application")
window.minsize(width=800, height=500)

custom_font = tfont.Font(
    family="Times New Roman",
    size=34,
    weight="bold"
)

label = tk.Label(
    window,
    text="Hello World",
    font=custom_font
)

label.pack(side="top")

# Changing label text
label["text"] = "Have a nice day"

label.config(text="This is a new day")


def function_button():
    print("thank you to click ")
# Button

button = tk.Button(command= function_button, text="Click")
button.pack()

# take the usere input 
user_input = tk.Entry( width=45)
user_input.pack()

window.mainloop()