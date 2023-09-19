number_of_days = int(input())
hours = int(input())

current_day = 1
final_total = 0
for day in range(1, number_of_days + 1):
    daily_total = 0

    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            daily_total += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            daily_total += 1.25
        else:
            daily_total += 1
    print(f'Day: {current_day} - {daily_total:.2f} leva')
    current_day += 1
    final_total += daily_total

print(f'Total: {final_total:.2f} leva')
