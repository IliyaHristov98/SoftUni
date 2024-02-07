first = set(int(x) for x in input().split())
second = set(int(y) for y in input().split())

for _ in range(int(input())):

    command_one, command_second, *numbers = input().split()

    if command_one == "Add":
        if command_second == "First":
            [first.add(int(number)) for number in numbers]
        else:
            [second.add(int(number)) for number in numbers]
    elif command_one == "Remove":
        if command_second == "First":
            [first.discard(int(number)) for number in numbers]
        else:
            [second.discard(int(number)) for number in numbers]
    else:
        print(first.issubset(second) or second.issubset(first))

print(*sorted(first), sep=", ")
print(*sorted(second), sep=", ")
