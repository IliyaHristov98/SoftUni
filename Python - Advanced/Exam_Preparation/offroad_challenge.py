from collections import deque

altitude = 0
reached_altitudes = []

fuel = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

while needed_fuel:
    used_fuel = fuel.pop() - consumption_index.popleft()

    if used_fuel >= needed_fuel[0]:
        needed_fuel.popleft()
        altitude += 1
        reached_altitudes.append(f"Altitude {altitude}")
        print(f"John has reached: Altitude {altitude}")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break

if len(reached_altitudes) == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")
elif not needed_fuel:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
