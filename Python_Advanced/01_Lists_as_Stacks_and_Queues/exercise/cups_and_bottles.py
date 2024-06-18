from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(y) for y in input().split()]
wasted_water = 0

while cups and bottles:
    cup_current = cups.popleft()
    bottle_current = bottles.pop()

    if bottle_current >= cup_current:
        wasted_water += bottle_current - cup_current
    else:
        cup_current -= bottle_current
        cups.appendleft(cup_current)

if not cups:
    bottles.reverse()
    print(f'Bottles: {" ".join(map(str, bottles))}')
else:
    print(f"Cups: {' '.join(map(str, cups))}")
print(f"Wasted litters of water: {wasted_water}")
