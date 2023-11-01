products = {}
given_products = input().split()
for i in range(0, len(given_products), 2):
    key = given_products[i]
    value = int(given_products[i + 1])
    products[key] = value

print(products)
