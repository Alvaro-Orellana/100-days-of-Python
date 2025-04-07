import tkinter as tk

window = tk.Tk()
window.title("Mile to km converter")
window.minsize(300, 300)

entry = tk.Entry(width=10)
miles_label = tk.Label(text="Miles")
is_equal_label = tk.Label(text="is equal to")
km_label = tk.Label(text="0")
km_sign_label = tk.Label(text="km")

def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    km_label.config(text="is equal to " + str(round(km, 2)) + " Km")

calculate_button = tk.Button(text="Calculate",command=calculate, width=10)


entry.grid(row=0, column=1)
miles_label.grid(row=0, column=2)

is_equal_label.grid(row=1, column=0)
km_label.grid(row=1, column=1)
km_sign_label.grid(row=1, column=2)

calculate_button.grid(row=2, column=1)

window.mainloop()









window.mainloop()