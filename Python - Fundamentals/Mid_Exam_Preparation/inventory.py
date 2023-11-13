items_list = input().split()
while True:
    input_command = input()
    if input_command == "Craft!":
        break
    command = input_command.split(" - ")

    if command[0] == "Collect":
        if command[1] not in items_list:
            items_list.append(command[1])

    elif command[0] == "Drop":
        if command[1] in items_list:
            items_list.remove(command[1])

    elif command[0] == "Combine Items":
        new_items = command[1].split(":")
        old_item = new_items[0]
        new_item = new_items[1]
        if old_item in items_list:
            old_item_index = items_list.index(old_item)
            items_list.insert(old_item_index + 1, new_item)

    elif command[0] == "Renew":
        if command[1] in items_list:
            items_list.remove(command[1])
            items_list.append(command[1])

final_list = [i for i in items_list if i != ""]
print(", ".join(final_list))
