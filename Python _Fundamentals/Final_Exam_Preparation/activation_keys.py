raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        start = int(command[2])
        end = int(command[3])
        to_replace = raw_key[start:end]
        if command[1] == "Upper":
            raw_key = raw_key.replace(to_replace, to_replace.upper())
        else:
            raw_key = raw_key.replace(to_replace, to_replace.lower())
        print(raw_key)

    elif action == "Slice":
        start = int(command[1])
        end = int(command[2])
        to_delete = raw_key[start:end]
        raw_key = raw_key.replace(to_delete, "")
        print(raw_key)

print(f"Your activation key is: {raw_key}")
