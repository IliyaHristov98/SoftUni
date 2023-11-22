import re

n = int(input())
attacked = []
destroyed = []
for _ in range(n):
    message = input()
    star_pattern = r"[STARstar]+"
    star_regex = re.findall(star_pattern, message)
    star_count = 0
    for i in star_regex:
        for x in i:
            star_count += 1

    decrypted_message = ""
    for char in message:
        decrypted_message += chr(ord(char) - star_count)

    value_pattern = r"@([A-Za-z]+)[^\@\-\!\:\>]*?:([0-9]+)[^\@\-\!\:\>]*?\!([AD])\![^\@\-\!\:\>]*?->([0-9]+)"

    if re.search(value_pattern, decrypted_message):
        value_regex = re.search(value_pattern, decrypted_message)
        planet = value_regex.group(1)
        population = int(value_regex.group(2))
        attack_type = value_regex.group(3)
        soldiers = int(value_regex.group(4))

        if attack_type == "A":
            attacked.append(planet)
        else:
            destroyed.append(planet)

attacked.sort()
destroyed.sort()
print(f"Attacked planets: {len(attacked)}")
for x in attacked:
    print(f"-> {x}")
print(f"Destroyed planets: {len(destroyed)}")
for y in destroyed:
    print(f"-> {y}")
