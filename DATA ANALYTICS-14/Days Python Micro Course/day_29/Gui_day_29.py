import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os

# -------------------- Helper Functions --------------------

def browse_input_file():
    path = filedialog.askopenfilename(
        title="Select Excel File",
        filetypes=[("Excel Files", "*.xlsx *.xls")]
    )
    input_file_var.set(path)


def browse_output_folder():
    path = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(path)


def reset_paths():
    input_file_var.set("")
    output_folder_var.set("")


def reset_checkboxes():
    remove_duplicates_var.set(False)
    remove_blank_rows_var.set(False)
    trim_text_var.set(False)
    title_case_var.set(False)


def clean_data():
    input_file = input_file_var.get()
    output_folder = output_folder_var.get()

    if not input_file or not output_folder:
        messagebox.showerror("Error", "Please select input file and output folder")
        return

    try:
        df = pd.read_excel(input_file)

        # Identify text columns
        text_columns = df.select_dtypes(include=['object']).columns

        # Apply selected cleaning options
        if remove_blank_rows_var.get():
            df = df.dropna(how='all')

        if remove_duplicates_var.get():
            df = df.drop_duplicates()

        if trim_text_var.get():
            df[text_columns] = df[text_columns].apply(lambda col: col.str.strip())

        if title_case_var.get():
            df[text_columns] = df[text_columns].apply(lambda col: col.str.title())

        # Save cleaned file
        base_name = os.path.basename(input_file)
        output_path = os.path.join(output_folder, f"Cleaned_{base_name}")
        df.to_excel(output_path, index=False)

        messagebox.showinfo("Success", f"Cleaned file saved at:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# -------------------- GUI Setup --------------------

root = tk.Tk()
root.title("Dynamic Data Cleaning Automation")
root.geometry("650x480")

# Variables
input_file_var = tk.StringVar()
output_folder_var = tk.StringVar()

remove_duplicates_var = tk.BooleanVar()
remove_blank_rows_var = tk.BooleanVar()
trim_text_var = tk.BooleanVar()
title_case_var = tk.BooleanVar()

# -------------------- Layout --------------------

# Input File Section
frame_input = tk.LabelFrame(root, text="Input Excel File", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=5)

tk.Entry(frame_input, textvariable=input_file_var, width=70).pack(side="left", padx=5)
tk.Button(frame_input, text="Browse", command=browse_input_file).pack(side="left")

# Cleaning Options Section
frame_options = tk.LabelFrame(root, text="Data Cleaning Options", padx=10, pady=10)
frame_options.pack(fill="x", padx=10, pady=5)

tk.Checkbutton(frame_options, text="Remove duplicate rows", variable=remove_duplicates_var).pack(anchor="w")
tk.Checkbutton(frame_options, text="Remove blank rows", variable=remove_blank_rows_var).pack(anchor="w")
tk.Checkbutton(frame_options, text="Remove leading & trailing spaces (Text columns only)", variable=trim_text_var).pack(anchor="w")
tk.Checkbutton(frame_options, text="Convert text columns to Title Case", variable=title_case_var).pack(anchor="w")

# Output Folder Section
frame_output = tk.LabelFrame(root, text="Output Folder", padx=10, pady=10)
frame_output.pack(fill="x", padx=10, pady=5)

tk.Entry(frame_output, textvariable=output_folder_var, width=70).pack(side="left", padx=5)
tk.Button(frame_output, text="Browse", command=browse_output_folder).pack(side="left")

# Buttons Section
frame_buttons = tk.Frame(root, pady=20)
frame_buttons.pack()

tk.Button(frame_buttons, text="Clean Data", width=15, command=clean_data).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Reset Paths", width=15, command=reset_paths).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Reset Checkboxes", width=18, command=reset_checkboxes).grid(row=0, column=2, padx=10)

# Run Application
root.mainloop()