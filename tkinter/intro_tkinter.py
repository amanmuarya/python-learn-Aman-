import tkinter as tk

window = tk.Tk()

window.title("Name App")
window.geometry("400x250")

label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

def show_name():
    name = entry.get()
    result.config(text="Hello " + name)

button = tk.Button(window, text="Submit", command=show_name)
button.pack()

result = tk.Label(window, text="")
result.pack()

window.mainloop()