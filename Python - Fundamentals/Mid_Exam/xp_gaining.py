needed_xp = float(input())
battles_count = int(input())
total_xp = 0
battles = 0
for i in range(battles_count):
    xp_to_gain = float(input())
    battles += 1
    if battles % 15 == 0:
        xp_to_gain = xp_to_gain * 1.05

    if battles % 5 == 0:
        xp_to_gain = xp_to_gain * 0.9

    if battles % 3 == 0:
        xp_to_gain = xp_to_gain * 1.15

    total_xp += xp_to_gain
    if total_xp >= needed_xp:
        break

if total_xp >= needed_xp:
    print(f"Player successfully collected his needed experience for {battles} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_xp-total_xp:.2f} more needed.")

