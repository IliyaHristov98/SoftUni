import re

pieces = []
prices = []
pattern = r">>([A-Za-z]+)<<([\d\.]+)\!(\d+)"

while True:
    furniture = input()
    if "Purchase" in furniture:
        break

    valid = re.match(pattern, furniture)
    if valid:
        pieces.append(str(valid.group(1)))
        prices.append(float(valid.group(2)) * int(valid.group(3)))

print("Bought furniture:")
for item in pieces:
    print(item)
print(f"Total money spend: {sum(prices):.2f}")
