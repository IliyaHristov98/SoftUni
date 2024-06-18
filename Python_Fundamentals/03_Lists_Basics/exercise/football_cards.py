string = input()
list_of_red_cards = string.split()
team_a = 11
team_b = 11
players_out = []
game_was_terminated = False
for card in list_of_red_cards:
    if card not in players_out:
        players_out.append(card)
    else:
        continue

    if card[0] == 'A':
        team_a -= 1
    elif card[0] == 'B':
        team_b -= 1

    if team_a < 7 or team_b < 7:
        game_was_terminated = True
        break

print(f'Team A - {team_a}; Team B - {team_b}')
if game_was_terminated:
    print("Game was terminated")
