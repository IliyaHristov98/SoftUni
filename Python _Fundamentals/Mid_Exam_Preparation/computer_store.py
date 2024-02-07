total_tax = 0
total_price = 0
while True:
    command = input()
    if command == "special" or command == "regular":
        break

    price = float(command)

    if price < 0:
        print("Invalid price!")
        continue

    total_price += price
    total_tax += price * 0.2

final_price = total_price + total_tax
if final_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        final_price = final_price - (final_price * 0.1)
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {total_tax:.2f}$\n"
          f"-----------\n"
          f"Total price: {final_price:.2f}$")
