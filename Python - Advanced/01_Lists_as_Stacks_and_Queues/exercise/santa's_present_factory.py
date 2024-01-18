from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])
crafted_presents = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    curr_material = materials.pop()
    curr_magic_level = magic_levels.popleft()
    total_magic = curr_magic_level * curr_material

    if curr_material == 0 and curr_magic_level == 0:
        continue
    elif curr_material == 0:
        magic_levels.appendleft(curr_magic_level)
    elif curr_magic_level == 0:
        materials.append(curr_material)

    if presents.get(total_magic):
        crafted_presents.append(presents[total_magic])
    elif total_magic < 0:
        materials.append(curr_material + curr_magic_level)
    elif total_magic > 0:
        materials.append(curr_material + 15)

if {"Doll", "Train"}.issubset(crafted_presents) or {"Teddy bear", "Bicycle"}.issubset(crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted_presents.count(toy)}") for toy in sorted(set(crafted_presents))]
