import re

line = input()

while line:
    pattern = r"\d+"
    regex = re.findall(pattern, line)
    if regex:
        print(" ".join(regex), end=" ")
    line = input()
