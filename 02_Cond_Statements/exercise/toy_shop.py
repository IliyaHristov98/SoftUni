PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_TOY_PRICE = 2.00

vacation_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_toy_count = int(input())

puzzle_total_price = puzzle_count * PUZZLE_PRICE
talikng_doll_total_price = talking_doll_count * TALKING_DOLL_PRICE
teddy_bear_total_price = teddy_bear_count * TEDDY_BEAR_PRICE
minion_total_price = minion_count * MINION_PRICE
truck_toy_total_price = truck_toy_count * TRUCK_TOY_PRICE

total_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + truck_toy_count
total_money_from_the_order = puzzle_total_price + talikng_doll_total_price + \
                             teddy_bear_total_price + minion_total_price + truck_toy_total_price

if total_count >= 50:
    total_money_from_the_order = total_money_from_the_order - total_money_from_the_order * 0.25

rent = total_money_from_the_order * 0.1

final_total = total_money_from_the_order - rent

enough = final_total - vacation_price
not_enough = vacation_price - final_total

if final_total >= vacation_price:
    print(f"Yes! {enough :.2f} lv left.")
else:
    print(f"Not enough money! {not_enough :.2f} lv needed.")

