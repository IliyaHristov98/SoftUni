name = input()
winner_points = 0
winner_name = ''
while name != 'Stop':
    points = 0
    for n in range(len(name)):
        number = int(input())
        if number == ord(name[n]):
            points += 10
        else:
            points += 2

    if points > winner_points:
        winner_points = points
        winner_name = name
    elif points == winner_points:
        winner_name = name
    name = input()

print(f'The winner is {winner_name} with {winner_points} points!')
