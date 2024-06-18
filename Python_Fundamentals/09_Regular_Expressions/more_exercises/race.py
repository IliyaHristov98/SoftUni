import re

results = {}
names = input().split(", ")

for i in names:
    results[i] = 0
given_input = input()

while given_input != "end of race":
    name_pattern = r"[A-Za-z]+"
    kms_pattern = r"[0-9]+"
    name_regex = re.findall(name_pattern, given_input)
    kms_regex = re.findall(kms_pattern, given_input)
    name = "".join(name_regex)
    kms = 0

    for element in kms_regex:
        for x in element:
            kms += int(x)

    if name in names:
        results[name] += kms

    given_input = input()

sorted_results = sorted(results.items(), key=lambda y: y[1], reverse=True)

for i, (key, value) in enumerate(sorted_results[:3]):
    place = i + 1
    if place == 1:
        print(f'{place}st place: {key}')
    elif place == 2:
        print(f'{place}nd place: {key}')
    elif place == 3:
        print(f'{place}rd place: {key}')
    else:
        break
