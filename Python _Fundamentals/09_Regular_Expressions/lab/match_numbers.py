import re

numbers = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

regex = re.finditer(pattern, numbers)

for i in regex:
    print(i.group(), end=" ")
