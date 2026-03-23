import tkinter as tk
from tkinter import messagebox
import time

# Luhn Algorithm Function
def luhn_check(number):
    total = 0
    for i in range(len(number) - 2, -1, -2):
        digit = int(number[i]) * 2
        if digit > 9:
            digit -= 9
        total += digit
    for i in range(1, len(number), 2):
        total += int(number[i])
    return total % 10 == 0

# Validation Handler
def validate_card():
    card_number = entry.get()
    clean_number = card_number.replace("-", "").replace(" ", "")
    
    if clean_number.isdigit() and len(clean_number) == 16:
        status_label.config(text="Checking length...", fg="blue")
        root.update()
        time.sleep(1)
        status_label.config(text="Phase 1 passed", fg="green")

        if luhn_check(clean_number):
            messagebox.showinfo("Result", "Phase 2 passed \nValid Credit Card Number")
        else:
            messagebox.showwarning("Result", "Phase 2 failed \nInvalid Credit Card Number")
    else:
        messagebox.showerror("Error", "Invalid Credit Card Number format")

# Tkinter GUI
root = tk.Tk()
root.title("Credit Card Validator")
root.geometry("400x250")

title_label = tk.Label(root, text="Credit Card Validator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter your credit card number:")
entry_label.pack()

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

validate_btn = tk.Button(root, text="Validate", font=("Arial", 12, "bold"), command=validate_card)
validate_btn.pack(pady=10)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=10)

root.mainloop()
