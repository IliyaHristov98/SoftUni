BITCOIN = 1168
YUAN = 0.15 * 1.76
DOLLAR = 1.76
EURO = 1.95

bitcoin_count = int(input())
yuan_count = float(input())
commision_percentage = float(input()) / 100

total_money = (bitcoin_count * BITCOIN + yuan_count * YUAN) / EURO
commision = total_money * commision_percentage

print(f'{total_money - commision:.2f}')