from collections import deque

times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times and tasks:
    time = times.popleft()
    task = tasks.pop()
    total = time * task

    if total > 240:
        times.append(time)
        tasks.append(task - 2)
    elif total > 180:
        ducks["Small Yellow Rubber Ducky"] += 1
    elif total > 120:
        ducks["Big Blue Rubber Ducky"] += 1
    elif total > 60:
        ducks["Thor Ducky"] += 1
    elif total >= 0:
        ducks["Darth Vader Ducky"] += 1

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in ducks.items():
    print(f"{duck}: {count}")
