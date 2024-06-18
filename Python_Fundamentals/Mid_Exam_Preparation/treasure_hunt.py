initial_loot = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    if command[0] == "Loot":
        for item in command[1:]:
            if item in initial_loot:
                continue
            else:
                initial_loot.insert(0, item)

    elif command[0] == "Drop":
        if 0 <= int(command[1]) < len(initial_loot):
            popped_item = initial_loot.pop(int(command[1]))
            initial_loot.append(popped_item)

    elif command[0] == "Steal":
        stolen_items = []
        if int(command[1]) >= len(initial_loot):
            stolen_items = list(initial_loot)
            initial_loot = []
        else:
            for x in range(int(command[1])):
                item = initial_loot.pop()
                stolen_items.insert(0, item)

        print(", ".join(map(str, stolen_items)))

    command = input().split()

if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = 0
    for x in initial_loot:
        average_treasure_gain += len(x)
    average_treasure_gain /= len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
