budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_liter_price = flour_price * 1.25
loaves = 0
colored_eggs = 0
one_loaf_price = eggs_price + flour_price + milk_liter_price / 4
total_spent = 0

while total_spent + one_loaf_price < budget:
    loaves += 1
    colored_eggs += 3
    total_spent += one_loaf_price
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
print(f'You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget - total_spent:.2f}BGN left.')