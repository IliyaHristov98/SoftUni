strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())

raspberry_price = strawberry_price * 0.5
banana_price = raspberry_price * 0.2
orange_price = raspberry_price * 0.6

total_price = strawberry_price * strawberries + raspberry_price \
              * raspberries + banana_price * bananas + orange_price * oranges
print(f'{total_price:.2f}')
