age = int(input())
washer_price = float(input())
toy_price = int(input())

toy_count = 0
money = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money += 5 * birthday - 1
    else:
        toy_count += 1

money_from_toys = toy_price * toy_count
total_money = money_from_toys + money

if total_money >= washer_price:
    print(f'Yes! {total_money - washer_price:.2f}')
else:
    print(f'No! {washer_price - total_money:.2f}')
