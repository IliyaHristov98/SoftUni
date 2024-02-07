months = int(input())
electricity_total = 0
water_total = 20 * months
internet_total = 15 * months
other_total = 0

for month in range(months):
    electricity = float(input())
    electricity_total += electricity
    other_total += (20 + 15 + electricity) * 1.2

bills_total = electricity_total + water_total + internet_total + other_total

print(f'Electricity: {electricity_total:.2f} lv\n'
      f'Water: {water_total:.2f} lv\n'
      f'Internet: {internet_total:.2f} lv\n'
      f'Other: {other_total:.2f} lv\n'
      f'Average: {bills_total / months:.2f} lv')
