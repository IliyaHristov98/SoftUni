database = {}

while True:
    command = input().split(" -> ")

    if command[0] == 'End':
        break

    company = command[0]
    employee = command[1]

    if company not in database:
        database[company] = [employee]
    else:
        if employee not in database[company]:
            database[company] += [employee]

for key, value in database.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")
