team = input()
number_of_matches = int(input())

wins = 0
losses = 0
draws = 0

for match in range(number_of_matches):
    result = input()
    if result == 'W':
        wins += 1
    elif result == 'D':
        draws += 1
    else:
        losses += 1

total_matches = wins + losses + draws
points = wins * 3 + draws

if number_of_matches == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    win_rate = wins / total_matches * 100
    print(f'{team} has won {points} points during this season.\n'
          f'Total stats:\n'
          f'## W: {wins}\n'
          f'## D: {draws}\n'
          f'## L: {losses}\n'
          f'Win rate: {win_rate:.2f}%')
