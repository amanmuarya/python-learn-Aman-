# Separator and padding


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

label1 = ttk.Label(root, text="Personal Information")
label1.pack(pady=10)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", padx=20, pady=10)

label2 = ttk.Label(root, text="Contact Information")
label2.pack(pady=10)

root.mainloop()


"""Padding
Padding means adding extra space around or inside widgets."""

import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Hello Aman")
label.pack(padx=50, pady=30)

root.mainloop()