import os

while True:
    command, *info = input().split("-")

    if command == "Create":
        with open(f"resources\\{info[0]}", "w"):
            pass

    elif command == "Add":
        content = command[2]
        with open(f"resources\\{info[0]}", "a") as file:
            file.write(f"{content}\n")

    elif command == "Replace":
        old = info[0]
        new = info[1]
        try:
            with open(f"resources\\{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(new, old)

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print(f"An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"resources\\{info[0]}")
        except FileNotFoundError:
            print("An error occurred")

    elif command == "End":
        break
