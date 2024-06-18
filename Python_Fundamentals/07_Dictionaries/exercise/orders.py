quantities = {}
prices = {}

while True:
    given_input = input().split()
    if given_input[0] == "buy":
        break
    item = given_input[0]
    price = float(given_input[1])
    quantity = int(given_input[2])

    if item not in quantities:
        quantities[item] = quantity
    else:
        quantities[item] += quantity

    prices[item] = price

for key, value in quantities.items():
    total_price = value * prices[key]
    print(f"{key} -> {total_price:.2f}")
