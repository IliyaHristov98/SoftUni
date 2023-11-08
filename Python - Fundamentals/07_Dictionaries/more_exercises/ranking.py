passwords = {}
results = {}

while True:
    command = input()
    if command == "end of contests":
        break
    contest, password = command.split(":")
    passwords[contest] = password

while True:
    command = input()
    if command == "end of submissions":
        break

    contest, password, username, points = command.split("=>")

    if contest in passwords and passwords[contest] == password:
        if username not in results:
            results[username] = {contest: int(points)}
        else:
            if contest in results[username]:
                if results[username][contest] < int(points):
                    results[username][contest] = int(points)
            else:
                results[username][contest] = int(points)

best_students = None
most_points = 0
for key, value in results.items():
    current = 0
    for i, points in value.items():
        current += points
    if current > most_points:
        most_points = current
        best_students = key
print(f"Best candidate is {best_students} with total {most_points} points.\nRanking:")

sorted_results = {k: v for k, v in sorted(results.items())}

for username, contests in sorted_results.items():
    sorted_contests = {k: v for k, v in sorted(contests.items(), key=lambda item: item[1], reverse=True)}

    print(f"{username}")
    for contest, points in sorted_contests.items():
        print(f"#  {contest} -> {points}")
