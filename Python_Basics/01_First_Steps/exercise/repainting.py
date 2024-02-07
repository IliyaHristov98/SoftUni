NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
DISOLVER_PRICE = 5.00

nylon = int(input())
nylon_final = nylon + 2

paint = int(input())
paint_final = paint + paint * 0.1

disolver = int(input())
bags = 0.40
hours = int(input())

supplies_price = nylon_final * NYLON_PRICE + paint_final * PAINT_PRICE + disolver * DISOLVER_PRICE + bags
worker_price = hours * supplies_price * 0.3
final_total = supplies_price + worker_price
print(final_total)




