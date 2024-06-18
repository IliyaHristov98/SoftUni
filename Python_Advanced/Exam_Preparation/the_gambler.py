n = int(input())

money = 100
matrix = []
position = []
all_lost = False
jackpot = False

directions = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for i in range(n):
    matrix.append(list(input()))

    if "G" in matrix[i]:
        position = [i, matrix[i].index("G")]
        matrix[i][matrix[i].index("G")] = "-"

while True:
    command = input()

    if command == "end":
        break

    r = position[0] + directions[command][0]
    c = position[1] + directions[command][1]
    position = [r, c]

    if not (0 <= r < n and 0 <= c < n):
        all_lost = True
        break

    slot = matrix[r][c]
    matrix[r][c] = "-"

    if slot == "W":
        money += 100
    elif slot == "P":
        money -= 200
    elif slot == "J":
        money += 100000
        jackpot = True
        break

    if money <= 0:
        all_lost = True

matrix[position[0]][position[1]] = "G"

if all_lost:
    print("Game over! You lost everything!")
elif jackpot:
    print(f"You win the Jackpot! \nEnd of the game. Total amount: {money}$")
    print(*["".join(row) for row in matrix], sep="\n")
else:
    print(f"End of the game. Total amount: {money}$")
    print(*["".join(row) for row in matrix], sep="\n")
