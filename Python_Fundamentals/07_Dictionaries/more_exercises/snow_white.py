dwarfs = {}
colors_count = {}
while True:
    command = input()
    if command == "Once upon a time":
        break
    command = command.split(" <:> ")
    name = command[0]
    color = command[1]
    physics = int(command[2])
    to_compare = name + ":" + color
    if name not in dwarfs:
        dwarfs[to_compare] = physics
    else:
        if name in dwarfs and color not in dwarfs:
            dwarfs[to_compare] = physics
        else:

            if dwarfs[to_compare] < physics:
                dwarfs[to_compare] = physics

    if color in colors_count:
        colors_count[color] += 1
    else:
        colors_count[color] = 1

sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda item: (-item[1], -colors_count[item[0].split(":")[1]])))

for key, value in sorted_dwarfs.items():
    name, color = key.split(":")
    print(f"({color}) {name} <-> {value}")
