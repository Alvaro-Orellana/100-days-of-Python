import  tkinter as tk
from tkinter import messagebox
import random
import string

print("Welcome to Password Manager!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_textfield.delete(0, tk.END)

    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!#$%&()*+"

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = random.choices(letters, k=nr_letters) + random.choices(symbols, k=nr_symbols) + random.choices(numbers, k=nr_numbers)
    random.shuffle(password)
    password_textfield.insert(tk.END, "".join(password))
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_textfield.get()
    email = username_textfield.get()
    password = password_textfield.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="Error", message="Please fill all fields")
        return

    is_ok = messagebox.askokcancel(title="Save Password",
                                   message=f"These are your details entered:\n" f"Password: {password}\n" f"Email: {email}\n")

    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website}, {email}, {password}\n")

    website_textfield.delete(0, tk.END)
    password_textfield.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(padx=50, pady=50)
window.title("Password Manager")

logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(height=200, width=200)
canvas.create_image(100, 100, image=logo)


website_label  = tk.Label(text="Website:")
username_label = tk.Label(text="Email/Username:")
password_label = tk.Label(text="Password:")

website_textfield  = tk.Entry(width=35)
website_textfield.focus()
username_textfield = tk.Entry(width=35)
username_textfield.insert(0, "somemail@gmail.com")
password_textfield = tk.Entry(width=21)

generate_password_button = tk.Button(text="Generate Password",command=generate_password)
add_button = tk.Button(text="Add", width=36, command=save)

# UI positioning
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_textfield.grid(row=1, column=1, columnspan=2)
username_textfield.grid(row=2, column=1, columnspan=2)
password_textfield.grid(row=3, column=1)

generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1)


window.mainloop()

