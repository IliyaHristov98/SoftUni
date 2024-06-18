import re

text = input()

all_numbers = re.findall(r"\d", text)
cool_threshold = int(all_numbers[0])
for i in all_numbers[1:]:
    cool_threshold *= int(i)

print(f"Cool threshold: {cool_threshold}")

regex_emoji = r"(::|\*\*)([A-Z][a-z]{2,})\1"
emojis_count = re.findall(regex_emoji, text)
print(f"{len(emojis_count)} emojis found in the text. The cool ones are:")

for match in re.finditer(regex_emoji, text):
    coolness = 0
    for char in match.group(2):
        coolness += ord(char)
    if coolness >= cool_threshold:
        print(f"{match.group(1)}{match.group(2)}{match.group(1)}")
