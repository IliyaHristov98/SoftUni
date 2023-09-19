type = input()
rows = int(input())
columns = int(input())
price = 0

if type == 'Premiere':
    price = 12
elif type == 'Normal':
    price = 7.50
else:
    price = 5

total_price = rows * columns * price
print(f'{total_price:.2f} leva')