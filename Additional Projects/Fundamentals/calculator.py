def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division with 0 is not possible!"
    else:
        return a / b


while True:
    print(f"Menu:\n"
          f"{2 * ' '}1. Addition\n"
          f"{2 * ' '}2. Subtraction\n"
          f"{2 * ' '}3. Multiplication\n"
          f"{2 * ' '}4. Division\n"
          f"{2 * ' '}5. Quit\n")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
        print("Goodbye!")
        break

    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))

    if choice == '1':
        print(plus(first, second))
    elif choice == '2':
        print(minus(first, second))
    elif choice == '3':
        print(multiply(first, second))
    elif choice == '4':
        print(divide(first, second))
    else:
        print("Invalid choice!")
