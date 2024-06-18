from itertools import cycle

key = [int(x) for x in input().split()]
while True:
    string = input()
    new_string = ""
    loot = ""
    coordinates = ""
    loot_found = False
    if string == "find":
        break

    cycle_key = cycle(key)

    for character in string:
        number = next(cycle_key)
        to_add = ord(character) - number
        new_string += chr(to_add)

    for i in range(len(new_string)):
        if new_string[i] == "&" and not loot_found:
            for m in range(i + 1, len(new_string)):
                if new_string[m] == "&":
                    loot_found = True
                    break
                else:
                    loot += new_string[m]

        if new_string[i] == "<":
            for m in range(i + 1, len(new_string)):
                if new_string[m] == ">":
                    break
                else:
                    coordinates += new_string[m]

    print(f"Found {loot} at {coordinates}")
