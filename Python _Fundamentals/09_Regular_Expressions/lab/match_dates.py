import re

dates = input()
pattern = r"(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})"
regex = re.findall(pattern, dates)

for date in regex:
    day = date[0]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
