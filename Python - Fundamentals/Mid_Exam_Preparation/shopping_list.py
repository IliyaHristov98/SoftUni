groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    current_command = command.split()

    if current_command[0] == "Urgent":
        item = current_command[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif current_command[0] == "Unnecessary":
        item = current_command[1]
        if item in groceries:
            groceries.remove(item)

    elif current_command[0] == "Correct":
        old = current_command[1]
        new = current_command[2]
        if old in groceries:
            old_index = groceries.index(old)
            groceries[old_index] = new

    elif current_command[0] == "Rearrange":
        item = current_command[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(f"{', '.join(groceries)}")
