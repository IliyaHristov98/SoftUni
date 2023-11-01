database = {}

while True:
    given_product = input()
    if given_product == "statistics":
        break

    product_key, product_value = given_product.split(": ")
    if product_key in database:
        database[product_key] += int(product_value)
    else:
        database[product_key] = int(product_value)

print("Products in stock:")
for key, value in database.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(database.keys())}\n"
      f"Total Quantity: {sum(database.values())}")
