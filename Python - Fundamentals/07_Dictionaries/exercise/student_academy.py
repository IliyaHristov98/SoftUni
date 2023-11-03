n = int(input())
database = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in database:
        database[name] = [grade]
    else:
        database[name] += [grade]

for student, grade in database.items():
    average_grade = sum(database[student]) / len(database[student])

    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
