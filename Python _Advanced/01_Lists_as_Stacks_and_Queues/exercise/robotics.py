from collections import deque
from datetime import datetime, timedelta

robots = {}
for robot in input().split(";"):
    name, time = robot.split("-")
    robots[name] = [int(time), 0]

starting_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()

while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    product = products.popleft()
    starting_time += timedelta(0, 1)

    free_robots = []

    for name, value in robots.items():
        if value[1] != 0:
            robots[name][1] -= 1

        if value[1] == 0:
            free_robots.append([name, value])

    if not free_robots:
        products.append(product)
        continue

    robot_name, data = free_robots[0]
    robots[robot_name][1] = data[0]

    print(f"{robot_name} - {product} [{starting_time.strftime('%H:%M:%S')}]")
