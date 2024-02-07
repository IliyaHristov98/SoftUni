students = {}
given_course = None
while True:
    command = input()
    if ":" not in command:
        given_course = command
        break
    student, number, course = command.split(":")
    students[student] = {int(number): course}

for current, value in students.items():
    for student_id, student_course in value.items():
        if given_course.startswith(student_course[0:3]):
            print(f"{current} - {student_id}")
