import  tkinter as tk
print("Welcome to Password Manager!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
username_textfield = tk.Entry(width=35)
password_textfield = tk.Entry(width=21)

generate_password_button = tk.Button(text="Generate Password")
add_button = tk.Button(text="Add", width=36)

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

