import re

strings = input()
pattern = r"\b_([A-Za-z0-9]+)\b"

regex = re.findall(pattern, strings)

print(",".join(regex))
