class FullColumnError(Exception):
    pass


class InvalidColumnError(Exception):
    pass


ROWS = 6
COLS = 7


def print_board(board):
    for row in board:
        print(row)


def validate_input(column):
    if 0 < column < COLS:
        return True
    else:
        raise InvalidColumnError


def add_player_choice(col, board, player):
    for i in range(ROWS - 1, -1, -1):
        if board[i][col] == 0:
            board[i][col] = player
            break
    else:
        raise FullColumnError


game = []

for _ in range(ROWS):
    game.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a column: "))
        validate_input(column)
        column_index = int(column) - 1
        add_player_choice(column_index, game, player)
    except FullColumnError:
        print("This column is already full!")
        continue
    except (ValueError, InvalidColumnError):
        print("Invalid input!")
        continue

    turns += 1
    print_board(game)
