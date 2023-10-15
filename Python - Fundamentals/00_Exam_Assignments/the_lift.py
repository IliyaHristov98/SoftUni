people_waiting = int(input())
lift = [int(x) for x in input().split()]
index = 0
lift_full = False
all_fit = False
while people_waiting > 0:
    if lift[index] == 4:
        index += 1
        continue

    lift[index] += 1
    people_waiting -= 1

    if sum(lift) / len(lift) == 4:
        lift_full = True
        break

if people_waiting == 0:
    all_fit = True

if lift_full and not all_fit:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
if not lift_full and all_fit:
    print(f"The lift has empty spots!")

print(" ".join(map(str, lift)))
