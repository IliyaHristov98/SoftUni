from collections import deque

monsters = deque([int(x) for x in input().split(",")])
power = [int(y) for y in input().split(",")]

killed = 0

while monsters and power:
    armor = monsters.popleft()
    hit = power.pop()

    if hit >= armor:
        hit -= armor
        killed += 1
        if power:
            power[-1] += hit
        elif hit > 0 and not power:
            power.append(hit)
    else:
        armor -= hit
        monsters.append(armor)

if not monsters:
    print("All monsters have been killed!")
if not power:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed}")
