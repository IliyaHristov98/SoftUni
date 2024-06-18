schedule = input().split(", ")
while True:
    command = input()

    if command == "course start":
        break
    else:
        input_command = command.split(":")

    if input_command[0] == "Add":
        lesson = input_command[1]
        if lesson not in schedule:
            schedule.append(lesson)

    elif input_command[0] == "Insert":
        lesson = input_command[1]
        index = int(input_command[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)

    elif input_command[0] == "Remove":
        lesson = input_command[1]
        if lesson in schedule:
            schedule.remove(lesson)

    elif input_command[0] == "Swap":
        first_lesson = input_command[1]
        second_lesson = input_command[2]
        if first_lesson in schedule and second_lesson in schedule:
            index_first = schedule.index(first_lesson)
            index_second = schedule.index(second_lesson)
            schedule[index_first], schedule[index_second] = \
                schedule[index_second], schedule[index_first]
            if f'{first_lesson}-Exercise' in schedule:
                schedule.remove(f'{first_lesson}-Exercise')
                schedule.insert(index_second + 1, f'{first_lesson}-Exercise')
            if f'{second_lesson}-Exercise' in schedule:
                schedule.remove(f'{second_lesson}-Exercise')
                schedule.insert(index_first + 1, f'{second_lesson}-Exercise')

    elif input_command[0] == "Exercise":
        lesson = input_command[1]
        if lesson not in schedule:
            schedule.append(lesson)
            schedule.insert(len(schedule), f'{lesson}-Exercise')
        elif lesson in schedule and f'{lesson}-Exercise' not in schedule:
            lesson_index = schedule.index(lesson)
            schedule.insert(lesson_index + 1, f'{lesson}-Exercise')

for index, lab in enumerate(schedule):
    print(f"{index + 1}.{lab}")
