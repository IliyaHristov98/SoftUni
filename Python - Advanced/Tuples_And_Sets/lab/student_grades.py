n = int(input())
student_grades = {}

for _ in range(n):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in student_grades:
        student_grades[name] = [grade]
    else:
        student_grades[name].append(grade)

for key, value in student_grades.items():
    average = sum(value) / len(value)
    formatted_value = [f"{x:.2f}" for x in value]
    print(f"{key} ->", *formatted_value, f"(avg: {average:.2f})")
