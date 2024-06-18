import re

pattern = r"\%([A-Z][a-z]+)\%[^\|\$\%\.]*?\<(\w+)\>[^\|\$\%\.]*?\|([0-9]+)\|[\w\-]*?([0-9.]+[0-9])(?=\$)"
total_income = 0

while True:
    command = input()
    if command == "end of shift":
        break

    if re.search(pattern, command):
        values = re.search(pattern, command)
        name = values.group(1)
        product = values.group(2)
        price = int(values.group(3)) * float(values.group(4))
        total_income += price
        print(f"{name}: {product} - {price:.2f}")

print(f"Total income: {total_income:.2f}")
