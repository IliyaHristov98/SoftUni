password = input()
new_password = password

while True:
    command = input()
    if command == "Done":
        break

    command = command.split()
    if command[0] == "TakeOdd":
        new_password = new_password[1::2]
        print(new_password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        sub_string = new_password[index:index + length]
        new_password = new_password.replace(sub_string, "", 1)
        print(new_password)

    elif command[0] == "Substitute":
        sub_string = command[1]
        substitute = command[2]
        if sub_string in new_password:
            new_password = new_password.replace(sub_string, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {new_password}")
