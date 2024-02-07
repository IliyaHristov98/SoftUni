inheritance_money = float(input())
year = int(input())

spent_money = 0
age = 17
for travel_year in range(1800, year + 1):
    if travel_year % 2 == 0:
        spent_money += 12000
    else:
        age += 2
        spent_money += 12000 + 50 * age

if spent_money <= inheritance_money:
    print(f"Yes! He will live a carefree life and will have {inheritance_money - spent_money:.2f} dollars left.")
else:
    print(f"He will need {spent_money - inheritance_money:.2f} dollars to survive.")
