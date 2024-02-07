first_line = input().split()
second_line = input().split()
third_line = input().split()
all_lines = first_line + second_line + third_line
winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

game_is_draw = True
for combination in winning_combinations:
    if all_lines[combination[0]] == all_lines[combination[1]] == all_lines[combination[2]] == '1':
        print('First player won')
        game_is_draw = False
        break
    elif all_lines[combination[0]] == all_lines[combination[1]] == all_lines[combination[2]] == '2':
        print('Second player won')
        game_is_draw = False
        break

if game_is_draw:
    print('Draw!')
