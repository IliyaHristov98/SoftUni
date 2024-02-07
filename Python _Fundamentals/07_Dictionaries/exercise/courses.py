database = {}

while True:
    given_input = input().split(" : ")
    if given_input[0] == "end":
        break
    course = given_input[0]
    student = given_input[1]
    if course not in database:
        database[course] = [student]
    else:
        database[course] += [student]

for course, students in database.items():
    print(f"{course}: {len(database[course])}")
    for student in students:
        print(f"-- {student}")
