tickets = input().replace(" ", "")
tickets = tickets.split(',')
count = 0
symb = ''
allowed = ["@@@@@@", "$$$$$$", "######", "^^^^^^"]


def check_next(symbol, first, second):
    back = 6
    for i in range(7, 11):
        if (i * symbol) in first and (i * symbol) in second:
            back += 1
    return back


for ticket in tickets:
    if len(ticket) != 20:
        print('invalid ticket')
        continue
    left = ticket[0:10]
    right = ticket[10:]
    combo_found = False

    for combos in allowed:
        if combos in right and combos in left:
            count = check_next(combos[0], left, right)
            symb = combos[0]
            combo_found = True

    if not combo_found:
        print(f'ticket "{ticket}" - no match')
        continue

    if count != 10:
        print(f'ticket "{ticket}" - {count}{symb}')
    else:
        print(f'ticket "{ticket}" - {count}{symb} Jackpot!')
