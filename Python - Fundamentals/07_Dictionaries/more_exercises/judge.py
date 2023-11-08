courses = {}
individual = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, i = command.split(" -> ")
    points = int(i)

    if username not in individual:
        individual[username] = 0

    if contest not in courses:
        courses[contest] = {username: points}
        individual[username] += points
    else:
        if username not in courses[contest]:
            courses[contest][username] = points
            individual[username] += points
        else:
            if courses[contest][username] < points:
                individual[username] -= courses[contest][username]
                courses[contest][username] = points
                individual[username] += points

for course, results in courses.items():
    print(f"{course}: {len(results)} participants")
    sorted_results = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    count = 1
    for student, result in sorted_results:
        print(f"{count}. {student} <::> {result}")
        count += 1

print("Individual standings:")
sorted_individual = sorted(individual.items(), key=lambda y: -y[1])
count_two = 1
for key, value in sorted_individual:
    print(f"{count_two}. {key} -> {value}")
    count_two += 1
