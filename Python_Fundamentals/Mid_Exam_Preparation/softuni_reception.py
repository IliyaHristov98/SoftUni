students_per_hour_one = int(input())
students_per_hour_two = int(input())
students_per_hour_three = int(input())
total_students = int(input())
total_handled_students_per_hour = students_per_hour_one + students_per_hour_two + students_per_hour_three
total_hours = 0

while total_students > 0:
    total_hours += 1
    if total_hours % 4 == 0:
        continue
    else:
        total_students -= total_handled_students_per_hour

print(f"Time needed: {total_hours}h.")
