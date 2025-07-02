import tkinter as tk
from tkinter import messagebox
import json
from cryptography.fernet import Fernet
import os

# Generate encryption key if it doesn't exist
def generate_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

# Load encryption key
def load_key():
    return open("key.key", "rb").read()

generate_key()

# Save password with encryption
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields!")
        return

    # Encrypt password
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode()).decode()

    new_data = {
        website: {
            "username": username,
            "password": encrypted_password
        }
    }

    # Save to JSON file
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            data.update(new_data)
    except FileNotFoundError:
        data = new_data
        def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please enter website to search!")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        if website in data:
            username = data[website]["username"]
            encrypted_password = data[website]["password"]

            key = load_key()
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

            messagebox.showinfo(title=website, message=f"Username: {username}\nPassword: {decrypted_password}")
        else:
            messagebox.showwarning(title="Not Found", message="No details for that website found.")

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
        save_button = tk.Button(text="Add Password", width=14, command=save_password)
save_button.grid(row=3, column=1)
search_button = tk.Button(text="Search Password", width=14, command=find_password)
search_button.grid(row=3, column=2)



    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    messagebox.showinfo(title="Success", message="Password saved securely!")

# ---------------------------- UI SETUP ------------------------------- #
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

# Save Button
save_button = tk.Button(text="Add Password", width=14, command=save_password)
save_button.grid(row=3, column=1)

# Mainloop
window.mainloop()
