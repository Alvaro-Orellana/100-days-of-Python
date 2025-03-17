import art

def add(n1: float, n2: float) -> float:
    return n1 + n2
def subtract(n1: float, n2: float) -> float:
    return n1 - n2
def multiply(n1: float, n2: float) -> float:
    return n1 * n2
def divide(n1: float, n2: float) -> float:
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
continue_calculating = False
result = 0

print(art.logo)

while True:
    if continue_calculating:
        first_number = result
    else:
        first_number = int(input("What's the first number"))

    print("+")
    print("-")
    print("*")
    print("/")

    operation = input("Pick an operation: ")
    second_number = int(input("What's the next number?:"))

    calculator = operations[operation]
    result = calculator(first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")

    answer = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if answer == "y":
        continue_calculating = True
    else:
        continue_calculating = False
        print("\n"*60),
        print(art.logo)
