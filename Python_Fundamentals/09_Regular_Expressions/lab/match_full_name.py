import re
names = input()
pattern = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
regex = re.findall(pattern, names)

for name in regex:
    print(name, end=" ")