chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

order_price = chicken_menus * 10.35 + fish_menus * 12.40 + vegetarian_menus * 8.15
dessert = order_price * 0.2

total_order_price = order_price + dessert + 2.50
print(total_order_price)