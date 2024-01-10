name = input()
days = int(input())
tickets = int(input())
price = float(input())
cinema_profit_percentage = int(input())

total_revenue = days * tickets * price
cinema_profit = total_revenue * (cinema_profit_percentage / 100)
total_profit = total_revenue - cinema_profit
print(f'The profit from the movie {name} is {total_profit:.2f} lv.')
