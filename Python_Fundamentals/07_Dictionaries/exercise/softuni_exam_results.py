scores = {}
languages = {}

while True:
    command = input()
    if command == "exam finished":
        break
    list_of_commands = command.split("-")

    if list_of_commands[1] == "banned":
        del scores[list_of_commands[0]]

    else:
        username = list_of_commands[0]
        language = list_of_commands[1]
        points = int(list_of_commands[2])

        if username not in scores:
            scores[username] = points
        else:
            if points > scores[username]:
                scores[username] = points

        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

print("Results:")
for key, value in scores.items():
    print(f"{key} | {value}")

print("Submissions:")
for key, value in languages.items():
    print(f"{key} - {value}")
