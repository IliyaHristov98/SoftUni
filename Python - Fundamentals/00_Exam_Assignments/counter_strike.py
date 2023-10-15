energy = int(input())
battles = 0
not_dead = False
command = input()
while command != "End of battle":
    distance = int(command)

    if distance <= energy:
        battles += 1
        energy -= distance
    else:
        print(f"Not enough energy! Game ends with {battles} won battles and {energy} energy")
        break
    if battles % 3 == 0:
        energy += battles

    command = input()

if command == "End of battle":
    print(f"Won battles: {battles}. Energy left: {energy}")
