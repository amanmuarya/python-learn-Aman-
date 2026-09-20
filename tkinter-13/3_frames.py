import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.title("My Application")

label1 = tk.Label(window, text="Hello World", bg="green")
label1.pack(side="left",fill='both', expand=True)

label2 = tk.Label(window, text="Hello, have a nice day", bg="pink")
label2.pack(side="left",fill='both', expand=True)

label3 = tk.Label(
    window,
    text="Hello, how are you? I think you are well",
    bg="red"
)
label3.pack(side="left",fill='both', expand=True)
window.mainloop()

#  python  3_frames.py