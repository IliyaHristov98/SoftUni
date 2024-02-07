ticket_cost = 150
item_list = input().split('|')
budget = int(input())
list_of_spent_money = []
total_spent = 0
for item in item_list:
    can_be_bought = False
    current_item_and_price = item.split("->")
    current_price = float(current_item_and_price[1])
    current_item = current_item_and_price[0]
    if current_item == "Clothes" and current_price <= 50:
        can_be_bought = True
    elif current_item == "Shoes" and current_price <= 35:
        can_be_bought = True
    elif current_item == "Accessories" and current_price <= 20.50:
        can_be_bought = True

    if budget >= current_price and can_be_bought:
        budget -= current_price
        total_spent += current_price
        price_plus_profit = current_price * 1.4
        list_of_spent_money.append(f'{price_plus_profit:.2f}')
    else:
        continue
final_income = 0
for price in list_of_spent_money:
    final_income += float(price)
print(" ".join(list_of_spent_money))
print(f'Profit: {final_income - total_spent:.2f}')
if budget + final_income >= ticket_cost:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
