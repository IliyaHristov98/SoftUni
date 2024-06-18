pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
max_health = int(input())
stalemate = True

while True:
    command = input().split(" ")
    action = command[0]
    if action == "Retire":
        break
    if action == "Fire":
        fire_index = int(command[1])
        damage_1 = int(command[2])
        if 0 <= fire_index < len(warship):
            warship[fire_index] -= damage_1
            if warship[fire_index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                stalemate = False
                break

    elif action == "Defend":
        start = int(command[1])
        end = int(command[2])
        damage_2 = int(command[3])
        if (start < len(pirate_ship) > end) and start >= 0 and end > 0:
            for section in range(start, end + 1):
                pirate_ship[section] -= damage_2
                if pirate_ship[section] <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    stalemate = False
                    break

    elif action == "Repair":
        repair_index = int(command[1])
        health = int(command[2])
        if 0 <= repair_index < len(pirate_ship):
            pirate_ship[repair_index] += health
            if pirate_ship[repair_index] > max_health:
                pirate_ship[repair_index] = max_health

    elif action == "Status":
        in_need_of_repair = 0
        for x in pirate_ship:
            if int(x) < 0.2 * max_health:
                in_need_of_repair += 1
        print(f"{in_need_of_repair} sections need repair.")

if stalemate:
    pirate_sum = sum(pirate_ship)
    warship_sum = sum(warship)

    print(f"Pirate ship status: {pirate_sum}\n"
          f"Warship status: {warship_sum}")
