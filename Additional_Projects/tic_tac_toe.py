class InvalidSignError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass


class PositionTakenError(Exception):
    pass


def check_for_winner(board, combinations, sign):
    for combo in combinations:
        if board[combo[0][0]][combo[0][1]] == sign \
                and board[combo[1][0]][combo[1][1]] == sign \
                and board[combo[2][0]][combo[2][1]] == sign:
            return True


def validate_sign(chosen_sign):
    if chosen_sign.upper() not in ["X", "O"]:
        raise InvalidSignError


def validate_number(choice, valid_choices):
    if choice not in valid_choices.keys():
        raise InvalidChoiceError


def validate_position(board, r, c):
    if board[r][c] != " ":
        raise PositionTakenError


field_dict = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
}

winning_combinations = [
    [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)],
]

p1_name = input("Player one name: ")
p2_name = input("Player two name: ")
p1_sign = input(f"{p1_name}, would you like to play 'X' or 'O'? ")

try:
    validate_sign(p1_sign)
except InvalidSignError:
    print("Please enter a correct sign: 'X' or 'O'!")
    p1_sign = input(f"{p1_name}, would you like to play 'X' or 'O'? ")

p2_sign = ""

if p1_sign == "X":
    p2_sign = "O"
elif p1_sign == "O":
    p2_sign = "X"

field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

print(f"{p1_name} starts first!")

moves = 1

while True:

    try:
        current_player = p1_name if moves % 2 != 0 else p2_name
        current_sign = p1_sign if current_player == p1_name else p2_sign

        player_choice = int(input(f"{current_player}, please choose a free position [1-9]: "))
        validate_number(player_choice, field_dict)

        row, col = field_dict[player_choice]
        validate_position(field, row, col)

    except InvalidChoiceError:
        print(f"Please enter a valid number between 1 and 9")
        continue

    except PositionTakenError:
        print(f"This position is already taken!")
        continue

    field[row][col] = current_sign
    moves += 1

    for i in field:
        print(f"| {' | '.join(map(str, i))} |")

    if check_for_winner(field, winning_combinations, current_sign):
        print(f"{current_player} won!")
        break

    if moves == 10:
        print("Draw!")
        break
