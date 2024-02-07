quantity = int(input())
hearthstone = 0
fortnite = 0
overwatch = 0
others = 0

for i in range(quantity):
    game = input()
    if game == 'Hearthstone':
        hearthstone += 1
    elif game == 'Fornite':
        fortnite += 1
    elif game == 'Overwatch':
        overwatch += 1
    else:
        others += 1

print(f'Hearthstone - {hearthstone / quantity * 100:.2f}%')
print(f'Fornite - {fortnite / quantity * 100:.2f}%')
print(f'Overwatch - {overwatch / quantity * 100:.2f}%')
print(f'Others - {others / quantity * 100:.2f}%')
