secret_message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")

    if command[0] == "InsertSpace":
        index = int(command[1])
        left = secret_message[:index]
        right = secret_message[index:]
        secret_message = left + " " + right

    elif command[0] == "Reverse":
        substring = command[1]
        if substring not in secret_message:
            print("error")
            continue
        else:
            secret_message = secret_message.replace(substring, "", 1)
            secret_message += substring[::-1]

    else:
        substring = command[1]
        replacement = command[2]
        while substring in secret_message:
            secret_message = secret_message.replace(substring, replacement)

    print(secret_message)

print(f"You have a new text message: {secret_message}")
