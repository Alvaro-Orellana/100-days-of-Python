import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = (
    [random.choice(string.ascii_letters) for _ in range(nr_letters)] +
    [random.choice('!#$%&()*+') for _ in range(nr_symbols)] +
    [random.choice(string.digits) for _ in range(nr_numbers)]
)
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your final password is: {password}")
