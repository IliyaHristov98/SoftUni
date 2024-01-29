def softuni_students(*data, **course_info):
    students_info = {}
    invalid = []
    result = []
    for course_id, name in data:
        if course_id not in course_info:
            invalid.append(name)
        else:
            students_info[name] = course_info[course_id]

    students_info = sorted(students_info.items())

    result.extend(
        f"*** A student with the username {name} has successfully finished the course {course}!" for name, course in
        students_info)

    if invalid:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid))}")

    return "\n".join(result)
