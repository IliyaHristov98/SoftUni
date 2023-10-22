list_of_numbers = [int(x) for x in input().split()]
while True:
    given_input = input()
    if given_input == "Finish":
        break
    current_command = given_input.split()
    command = current_command[0]
    value = int(current_command[1])

    if command == "Add":
        list_of_numbers.append(value)
    elif command == "Remove":
        if value in list_of_numbers:
            list_of_numbers.remove(value)
    elif command == "Replace":
        for i in range(len(list_of_numbers)):
            if list_of_numbers[i] == value:
                list_of_numbers[i] = int(current_command[2])
                break
    elif command == "Collapse":
        new_list = []
        for y in list_of_numbers:
            if y >= value:
                new_list.append(y)
        list_of_numbers = new_list

print(" ".join(map(str, list_of_numbers)))
