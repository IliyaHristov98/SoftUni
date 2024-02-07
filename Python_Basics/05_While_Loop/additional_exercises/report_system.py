needed_money = int(input())
cash_money = 0
cash_count = 0
card_money = 0
card_count = 0
turn = 1
total_money = 0
money_is_collected = True
product_price = input()

while total_money < needed_money:
    if product_price == 'End':
        money_is_collected = False
        break
    price = int(product_price)
    if turn % 2 != 0:
        if price > 100:
            print('Error in transaction!')
        else:
            total_money += price
            cash_money += price
            cash_count += 1
            print('Product sold!')
    else:
        if price < 10:
            print('Error in transaction!')
        else:
            total_money += price
            card_money += price
            card_count += 1
            print('Product sold!')
    turn += 1
    if total_money >= needed_money:
        break
    else:
        product_price = input()

if money_is_collected:
    print(f'Average CS: {cash_money / cash_count:.2f}\n'
          f'Average CC: {card_money / card_count:.2f}')
elif not money_is_collected:
    print(f'Failed to collect required money for charity.')
