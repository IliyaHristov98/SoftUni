from collections import deque

green_duration = int(input())
free_window = int(input())
cars = deque()
crashed = False
passed = 0
current = None
hit_index = 0
while True:
    command = input()
    if command == "END":
        break

    if command == 'green':
        time_left = green_duration
        while cars:
            current = cars.popleft()
            passed += 1
            if time_left >= current[1]:
                time_left -= current[1]
            else:
                left = current[1] - time_left
                if left > free_window:
                    hit_index = -(left - free_window)
                    crashed = True
                    passed -= 1
                break
        if crashed:
            break
    else:
        cars.append([command, len(command)])

if crashed:
    print(f"A crash happened!\n{current[0]} was hit at {current[0][hit_index]}.")
else:
    print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")
