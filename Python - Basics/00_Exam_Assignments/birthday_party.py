rent = float(input())

cake = rent * 0.2
drinks = cake - (cake * 0.45)
animator = (1 / 3) * rent

budget = rent + cake + drinks + animator
print(budget)