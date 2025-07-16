import random
import string
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number.")
        return

    upperCase = uppercase_var.get()
    lowerCase = lowercase_var.get()
    numbers = numbers_var.get()
    symbols = symbols_var.get()

    characters = ''
    if upperCase:
        characters += string.ascii_uppercase
    if lowerCase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Selection Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_var.set(password)

# Get current year
current_year = datetime.now().year

# Create main window
window = Tk()
window.title("Password Generator")
window.geometry("450x520")
window.config(bg="#e0f7fa")

# Fonts
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 10)
entry_font = ("Consolas", 12)

# ----- Layout Frame -----
frame = Frame(window, bg="#e0f7fa")
frame.pack(expand=True)

# ----- Title -----
Label(frame, text="🔐 Password Generator", font=title_font, fg="#00796b", bg="#e0f7fa").grid(row=0, column=0, columnspan=2, pady=(20, 10))

# ----- Length Input -----
Label(frame, text="Password Length:", font=label_font, bg="#e0f7fa").grid(row=1, column=0, pady=5, sticky=E)
length_entry = Entry(frame, width=10, justify='center', font=entry_font)
length_entry.grid(row=1, column=1, pady=5, sticky=W)

# ----- Checkbox Options -----
uppercase_var = BooleanVar()
lowercase_var = BooleanVar()
numbers_var = BooleanVar()
symbols_var = BooleanVar()

Checkbutton(frame, text="Include Uppercase", variable=uppercase_var, bg="#e0f7fa", font=label_font).grid(row=2, column=0, columnspan=2, sticky=W, padx=40)
Checkbutton(frame, text="Include Lowercase", variable=lowercase_var, bg="#e0f7fa", font=label_font).grid(row=3, column=0, columnspan=2, sticky=W, padx=40)
Checkbutton(frame, text="Include Numbers", variable=numbers_var, bg="#e0f7fa", font=label_font).grid(row=4, column=0, columnspan=2, sticky=W, padx=40)
Checkbutton(frame, text="Include Symbols", variable=symbols_var, bg="#e0f7fa", font=label_font).grid(row=5, column=0, columnspan=2, sticky=W, padx=40)

# ----- Generate Button -----
Button(frame, text="Generate Password", command=generate_password,
       bg="#00796b", fg="white", font=("Helvetica", 11), width=25).grid(row=6, column=0, columnspan=2, pady=15)

# ----- Display Result -----
result_var = StringVar()
Entry(frame, textvariable=result_var, width=35, justify='center', font=entry_font).grid(row=7, column=0, columnspan=2, pady=10)

# ----- Footer -----
footer_text = f"© {current_year} @Prashob Preman – App Version: V1"
Label(window, text=footer_text, font=("Arial", 9), fg="#555", bg="#e0f7fa").pack(side="bottom", pady=15)

# Run the app
window.mainloop()
