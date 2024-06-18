quantity = int(input())
days_left = int(input())
christmas_spirit = 0
ornament_set = 0
skirt = 0
garland = 0
lights = 0

if days_left % 10 == 0:
    christmas_spirit -= 30

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        ornament_set += quantity
        christmas_spirit += 5
    if day % 3 == 0:
        skirt += quantity
        garland += quantity
        christmas_spirit += 13
    if day % 5 == 0:
        lights += quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        skirt += 1
        garland += 1
        lights += 1

total_cost = ornament_set * 2 + skirt * 5 + garland * 3 + lights * 15
print(f'Total cost: {total_cost}\n'
      f'Total spirit: {christmas_spirit}')
