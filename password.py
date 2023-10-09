import tkinter as tk
import random
import string
import tkinter.messagebox as mbox
import xerox

def generate_password():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_label.configure(text=password)
    generated_password = password

def copy_password():
    generated_password = password_label.cget("text")
    try:
        xerox.copy(generated_password)
        mbox.showinfo("Copy Successful", "Password has been copied to the clipboard.")
    except Exception:
        mbox.showerror("Copy Failed", "Unable to copy password to clipboard.")

# Window
window = tk.Tk()
window.title("Password Generator")

# Label
length_label = tk.Label(window, text="Password Length:")
length_label.pack()

# Label (Entry)
length_entry = tk.Entry(window)
length_entry.pack()

# Button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Label
password_label = tk.Label(window, text="")
password_label.pack()

# Button
copy_button = tk.Button(window, text="Copy", command=copy_password)
copy_button.pack()


window.mainloop()

