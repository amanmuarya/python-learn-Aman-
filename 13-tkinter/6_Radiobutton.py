"""Radiobutton Widget 
A Radiobutton is used when the user must select only one option from a group."""


import tkinter as tk

root = tk.Tk()

choice = tk.StringVar()

tk.Radiobutton(
    root,
    text="Python",
    variable=choice,
    value="Python"
).pack()

tk.Radiobutton(
    root,
    text="Java",
    variable=choice,
    value="Java"
).pack()

tk.Radiobutton(
    root,
    text="JavaScript",
    variable=choice,
    value="JavaScript"
).pack()

root.mainloop()