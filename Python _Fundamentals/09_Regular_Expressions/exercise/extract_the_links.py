import re

line = input()
pattern = r"www\.[A-Za-z0-9-]+\.[\.?a-z]+"

while line:
    valid_website = re.findall(pattern, line)
    if valid_website:
        for i in valid_website:
            print(i)

    line = input()
