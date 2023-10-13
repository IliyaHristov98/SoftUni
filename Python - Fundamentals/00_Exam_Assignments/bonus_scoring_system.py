from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
attendance_list = []


if lectures_count == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
else:
    for i in range(students_count):
        attendance = int(input())
        attendance_list.append(attendance)
    max_attendance = max(attendance_list)
    max_bonus = max_attendance / lectures_count * (5 + additional_bonus)

    print(f"Max Bonus: {ceil(max_bonus)}. \n"
          f"The student has attended {max_attendance} lectures.")
