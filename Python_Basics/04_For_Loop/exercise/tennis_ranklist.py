from math import floor

tournaments_count = int(input())
starting_points = int(input())

total_points = starting_points
tournaments_won = 0

for tournament in range(tournaments_count):
    outcome = input()
    if outcome == 'W':
        total_points += 2000
        tournaments_won += 1
    elif outcome == 'F':
        total_points += 1200
    elif outcome == 'SF':
        total_points += 720

print(f'Final points: {total_points}')
print(f'Average points: {floor((total_points - starting_points) / tournaments_count)}')
print(f'{tournaments_won/tournaments_count * 100:.2f}%')
