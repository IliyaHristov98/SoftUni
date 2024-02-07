total_budget = float(input())
people_count = int(input())
clothes_price_per_person = float(input())

decor_price = total_budget * 0.1
total_clothes_price = people_count * clothes_price_per_person

if people_count > 150:
    total_clothes_price = total_clothes_price - (total_clothes_price * 0.1)

total_price_all_included = decor_price + total_clothes_price

if total_budget < total_price_all_included:
    print("Not enough money!")
    print(f"Wingard needs {total_price_all_included - total_budget :.2f} leva more.")
elif total_budget >= total_price_all_included:
    print("Action!")
    print(f"Wingard starts filming with {total_budget - total_price_all_included :.2f} leva left.")