level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
put_out_fires = []
for fire in range(len(level_of_fire)):
    current_fire = level_of_fire[fire].split()
    cell_value = int(current_fire[2])
    fire_type = current_fire[0]
    if (fire_type == "High" and 81 <= cell_value <= 125) or \
            (fire_type == "Medium" and 51 <= cell_value <= 80) or \
            (fire_type == "Low" and 1 <= cell_value <= 50):
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            effort += cell_value * 0.25
            put_out_fires.append(cell_value)
        else:
            continue
    else:
        continue

print("Cells:")
for cell in put_out_fires:
    print(f' - {cell}')
print(f"Effort: {effort:.2f}\n"
      f"Total Fire: {sum(put_out_fires)}")
