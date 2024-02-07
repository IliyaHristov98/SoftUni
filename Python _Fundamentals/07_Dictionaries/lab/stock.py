stock = {}
given_products = input().split()

for i in range(0, len(given_products), 2):
    key = given_products[i]
    value = int(given_products[i + 1])
    stock[key] = value

products_to_search = input().split()
for product in products_to_search:
    if product in given_products:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
