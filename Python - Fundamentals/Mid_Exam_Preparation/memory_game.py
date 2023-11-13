elements = input().split()
moves = 0

while True:
    given_command = input()
    if given_command == "end":
        break

    moves += 1
    command = given_command.split()
    first = int(command[0])
    second = int(command[1])

    if (first == second) or \
            first >= len(elements) \
            or first < 0 \
            or second >= len(elements) \
            or second < 0:
        print(f"Invalid input! Adding additional elements to the board")
        middle = int(len(elements) / 2)
        to_insert = f"-{moves}a"
        elements.insert(middle, to_insert)
        elements.insert(middle + 1, to_insert)

    elif elements[first] == elements[second]:
        print(f"Congrats! You have found matching elements - {elements[first]}!")
        if first < second:
            elements.pop(first)
            elements.pop(second - 1)
        else:
            elements.pop(second)
            elements.pop(first - 1)

    elif elements[first] != elements[second]:
        print(f"Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break

if len(elements) > 0:
    print(f"Sorry you lose :(\n"
          f"{' '.join(elements)}")
