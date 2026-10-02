"""Checkbutton Widget 
A Checkbutton is used when the user can select zero, one, or multiple options."""

import tkinter as tk

root = tk.Tk()
python = tk.BooleanVar()
java = tk.BooleanVar()
javascript = tk.BooleanVar()

tk.Checkbutton(root, text="Python", variable=python).pack()
tk.Checkbutton(root, text="Java", variable=java).pack()
tk.Checkbutton(root, text="JavaScript", variable=javascript).pack()

root.mainloop()