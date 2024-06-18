targets = [int(x) for x in input().split()]
while True:
    given_command = input().split()
    command = given_command[0]
    if command == "End":
        break
    index = int(given_command[1])
    value = int(given_command[2])
    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f"Invalid placement!")

    elif command == "Strike":
        if index - value < 0 or index + value > len(targets):
            print(f"Strike missed!")
        else:
            for i in range(2 * value + 1):
                targets.pop(index - value)

print(f"{'|'.join(map(str, targets))}")
