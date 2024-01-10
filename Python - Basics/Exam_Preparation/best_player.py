name = input()
achieved_hattrick = False
most_goals = 0
current_best = ''
while not name == 'END':
    goals = int(input())
    if goals >= 3:
        achieved_hattrick = True

    if goals > most_goals:
        current_best = name
        most_goals = goals

    if goals >= 10:
        break
    name = input()

print(f'{current_best} is the best player!')
if achieved_hattrick:
    print(f'He has scored {most_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {most_goals} goals.')
