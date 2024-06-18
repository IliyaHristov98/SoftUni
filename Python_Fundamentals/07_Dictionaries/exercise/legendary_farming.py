chest = {"shards": 0, "fragments": 0, "motes": 0}
item_found = False

while True:
    materials = input().split()

    for i in range(0, len(materials), 2):
        value = int(materials[i])
        key = materials[i + 1].lower()

        if key not in chest:
            chest[key] = value
        else:
            chest[key] += value

        if "shards" in chest and chest["shards"] >= 250:
            chest["shards"] -= 250
            print("Shadowmourne obtained!")
            item_found = True
            break
        elif "fragments" in chest and chest["fragments"] >= 250:
            chest["fragments"] -= 250
            print("Valanyr obtained!")
            item_found = True
            break
        elif "motes" in chest and chest["motes"] >= 250:
            chest["motes"] -= 250
            print("Dragonwrath obtained!")
            item_found = True
            break

    if item_found:
        break

for item, number in chest.items():
    print(f"{item}: {chest[item]}")
