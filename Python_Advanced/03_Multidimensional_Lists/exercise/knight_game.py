n = int(input())

board = [list(input()) for _ in range(n)]

moves = {
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
}

removed_knights = 0

while True:
    strongest = 0
    strongest_pos = []
    for row in range(n):
        for col in range(n):
            current_strength = 0

            if board[row][col] == "K":
                for move in moves:
                    if 0 <= row + move[0] < n and 0 <= col + move[1] < n:
                        if board[row + move[0]][col + move[1]] == "K":
                            current_strength += 1

                if current_strength > strongest:
                    strongest = current_strength
                    strongest_pos = [row, col]
    if strongest > 0:
        board[strongest_pos[0]][strongest_pos[1]] = "0"
        removed_knights += 1
    else:
        print(removed_knights)
        break
