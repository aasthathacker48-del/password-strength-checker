import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry.get()

    strength = "Weak"

    if len(password) >= 8:
        if re.search("[A-Z]", password) and re.search("[a-z]", password):
            if re.search("[0-9]", password):
                if re.search("[@#$%^&*!]", password):
                    strength = "Strong"
                else:
                    strength = "Medium"

    messagebox.showinfo("Password Strength", strength)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

label = tk.Label(root, text="Enter Password")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack()

button = tk.Button(root, text="Check", command=check_password)
button.pack(pady=20)

root.mainloop()
