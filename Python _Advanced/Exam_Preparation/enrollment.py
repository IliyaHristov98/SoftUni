def gather_credits(num_of_credits, *args):
    courses = []
    gathered_credits = 0
    result = ""
    for name, course_credits in args:
        if gathered_credits < num_of_credits and name not in courses:
            gathered_credits += course_credits
            courses.append(name)

    if gathered_credits >= num_of_credits:
        result += f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
                  f"Courses: {', '.join(sorted(courses))}"
    else:
        result += f"You need to enroll in more courses! " \
                  f"You have to gather {num_of_credits - gathered_credits} credits more."

    return result
