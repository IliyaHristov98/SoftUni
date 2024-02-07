from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

created_items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

item_values = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    total = textile + medicament

    if total in item_values:
        created_items[item_values[total]] += 1
    elif total > 100:
        created_items["MedKit"] += 1
        medicaments[-1] += total - 100
    else:
        medicaments.append(medicament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for key, value in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    if value > 0:
        print(f"{key} - {value}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
elif textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
