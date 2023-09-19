movie = input()
package = input()
tickets = int(input())
price = 0
if movie == "John Wick":
    if package == "Drink":
        price = 12
    elif package == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if package == "Drink":
        price = 18
    elif package == "Popcorn":
        price = 25
    else:
        price = 30
else:
    if package == "Drink":
        price = 9
    elif package == "Popcorn":
        price = 11
    else:
        price = 14

if movie == "Star Wars" and tickets >= 4:
    price = price * 0.7
elif movie == "Jumanji" and tickets == 2:
    price = price * 0.85

total_price = tickets * price
print(f'Your bill is {total_price:.2f} leva.')
