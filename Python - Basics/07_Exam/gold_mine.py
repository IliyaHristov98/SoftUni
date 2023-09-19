locations = int(input())

for location in range(locations):
    total_yield = 0
    expected_daily_yield = float(input())
    days_of_mining = int(input())

    for day in range(days_of_mining):
        daily_yield = float(input())
        total_yield += daily_yield
        average_daily_yield = total_yield / days_of_mining
    if average_daily_yield >= expected_daily_yield:
        print(f"Good job! Average gold per day: {average_daily_yield:.2f}.")
    else:
        print(f"You need {expected_daily_yield - average_daily_yield:.2f} gold.")
