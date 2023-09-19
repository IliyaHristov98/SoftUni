number_of_days = int(input())
total_liters = 0
alcohol = 0

for day in range(number_of_days):
    liters = float(input())
    alcohol_percentage = float(input())
    total_liters += liters
    alcohol += alcohol_percentage * liters

final_alcohol_percentage = alcohol / total_liters
print(f'Liter: {total_liters:.2f}\n'
      f'Degrees: {final_alcohol_percentage:.2f}')

if final_alcohol_percentage < 38:
    print(f'Not good, you should baking!')
elif final_alcohol_percentage < 42:
    print(f'Super!')
else:
    print(f'Dilution with distilled water!')
