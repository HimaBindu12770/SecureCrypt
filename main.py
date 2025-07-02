import tkinter as tk
from tkinter import messagebox

# Window create
window = tk.Tk()
window.title("SecureCrypt - Password Manager")
window.config(padx=40, pady=40)

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(row=0, column=0)

username_label = tk.Label(text="Username/Email:")
username_label.grid(row=1, column=0)

password_label = tk.Label(text="Password:")
password_label.grid(row=2, column=0)

# Entries
website_entry = tk.Entry(width=35)
website_entry.grid(row=0, column=1, columnspan=2)

username_entry = tk.Entry(width=35)
username_entry.grid(row=1, column=1, columnspan=2)

password_entry = tk.Entry(width=21)
password_entry.grid(row=2, column=1)

# Mainloop
window.mainloop()
