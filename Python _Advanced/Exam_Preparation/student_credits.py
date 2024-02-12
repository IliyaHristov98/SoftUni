def students_credits(*args):
    total_credits = 0
    courses_credits = {}
    result = ""

    for arg in args:
        course, creds, max_points, points = arg.split("-")
        received_credits = int(creds) * (int(points) / int(max_points))
        courses_credits[course] = received_credits
        total_credits += received_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits."
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma."

    sorted_courses = sorted(courses_credits.items(), key=lambda x: -x[1])

    for course, points in sorted_courses:
        result += f"\n{course} - {points:.1f}"

    return result
