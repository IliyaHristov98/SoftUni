import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\_\.\-]*)@([a-z\-]+)(\.[a-z]+)+)\b"

regex = re.findall(pattern, sentence)
for i in regex:
    print("".join(i[0]))
