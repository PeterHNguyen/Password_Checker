# Python Tracker done by Peter Nguyen 
# Date 2/5/2025 
# Project: Strong Password Checker for Cyber Security

import string
import random
import tkinter as tk
import re
from pyzxcvbn import zxcvbn 
from tkinter import *
from tkinter import messagebox

# Function to check password strength  
def password_strength(password): 
    if len(password) < 8: 
        return "❌ Weak: At least 8 characters", "red"

    # Define complexity criteria  
    password_criteria = [
        r"[a-z]",  # At least one lowercase letter
        r"[A-Z]",  # At least one uppercase letter  
        r"[0-9]",  # At least one digit (0-9)  
        r"[!@#$%^&]"  # At least one special character  
    ]

    # Count how many criteria are met  
    correct_criteria = sum(bool(re.search(pattern, password)) for pattern in password_criteria)

    if correct_criteria < 3: 
        return "Weak, Use uppercase, lowercase, numbers, & special characters.", "red"

    # Use zxcvbn to analyze password strength  
    result = zxcvbn(password)

    if result['score'] <= 2: 
        return "Medium, Consider a longer & more complex password.", "orange"
    else:
        return "Strong", "green"

# Function to update password strength dynamically  
def update_strength_label(*args):
    user_password = password_var.get()
    if " " in user_password:
        password_var.set(user_password.replace(" "," "))
        messagebox.showarning("Spaces not allowed in password!")
    # Default state if no password is entered
    if not user_password:
        strength_text, color = "Start typing...", "gray"
    else:
        strength_text, color = password_strength(user_password)

    # Update the strength label with text & background color
    strength_label.config(text=strength_text, bg=color, fg="white", font=("Arial", 12, "bold"), padx=20, pady=5)

# Function to generate a strong password  
def generate_password():
    length = 12  # Default password length
    characters = string.ascii_letters + string.digits + "!@#$%^&*"  # All character types  
    new_password = "".join(random.choice(characters) for _ in range(length))  
    password_var.set(new_password)  

# Function to manually check password strength  
def check_password():
    user_password = password_var.get()
    if not user_password:
        messagebox.showwarning("Warning", "Please enter a password to check!")
        return
    
    strength_text, color = password_strength(user_password)
    messagebox.showinfo("Password Strength", f" {strength_text}")

# Function to toggle password visibility  
def toggle_password():
    if show_password_var.get():  
        entry.config(show="")  # Show password  
    else:  
        entry.config(show="*")  # Hide password  

# GUI Setup  
root = Tk()
root.title("🔐 Live Password Strength Checker")  
root.geometry("900x550")  

# Password variable to track input changes  
password_var = StringVar()
password_var.trace_add("write", update_strength_label)  

# Labels & Entry Box  
Label(root, text="Enter Your Password:", font=("Arial", 12)).pack(pady=10)  
entry = Entry(root, textvariable=password_var, show="*", width=30, font=("Arial", 12))  
entry.pack(pady=5)  

# Checkbox to toggle password visibility  
show_password_var = BooleanVar()
Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password).pack()

# Strength label (color-changing background)
strength_label = Label(root, text="🔍 Start typing...", font=("Arial", 12), fg="white", bg="gray", padx=20, pady=5)  
strength_label.pack(pady=10)  

# Buttons  
Button(root, text="🔍 Check Password", command=check_password, font=("Arial", 12), bg="blue", fg="white").pack(pady=5)  
Button(root, text="🔄 Generate Password", command=generate_password, font=("Arial", 12), bg="green", fg="white").pack(pady=10)  

# Run the GUI  
root.mainloop()
