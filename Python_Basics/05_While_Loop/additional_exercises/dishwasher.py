bottles_count = int(input())
detergent_mls = bottles_count * 750
used_detergent = 0
cycles = 1
count = input()
dish_count = 0
pot_count = 0
enough_detergent = True
while used_detergent <= detergent_mls:
    if count == "End":
        if used_detergent > detergent_mls:
            enough_detergent = False
        break
    if cycles % 3 == 0:
        used_detergent += int(count) * 15
        pot_count += int(count)
    else:
        used_detergent += int(count) * 5
        dish_count += int(count)
    cycles += 1
    if detergent_mls >= used_detergent:
        count = input()
    else:
        enough_detergent = False
        break

if enough_detergent:
    print(f"Detergent was enough!")
    print(f"{dish_count} dishes and {pot_count} pots were washed.")
    print(f"Leftover detergent {detergent_mls - used_detergent} ml.")
elif not enough_detergent:
    print(f"Not enough detergent, {used_detergent - detergent_mls} ml. more necessary!")
