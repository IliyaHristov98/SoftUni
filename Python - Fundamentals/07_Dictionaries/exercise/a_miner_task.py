help_list = []
dictionary = {}
count = 0
while True:
    given_input = input()
    if given_input == "stop":
        break
    count += 1
    help_list.append(given_input)

for i in range(0, len(help_list), 2):
    if help_list[i] not in dictionary:
        dictionary[help_list[i]] = int(help_list[i + 1])
    else:
        dictionary[help_list[i]] += int(help_list[i + 1])

for key, value in dictionary.items():
    print(f"{key} -> {value}")
