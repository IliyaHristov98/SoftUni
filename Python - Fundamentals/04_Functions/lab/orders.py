def order_price(item, quantity):
    item_price = 0
    if item == "coffee":
        item_price = 1.50
    elif item == "water":
        item_price = 1.00
    elif item == "coke":
        item_price = 1.40
    elif item == "snacks":
        item_price = 2.00

    return item_price * quantity


ordered_item = input()
item_count = int(input())
result = f'{order_price(ordered_item,item_count):.2f}'
print(result)
