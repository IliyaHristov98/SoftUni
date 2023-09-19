sea_excursions = int(input())
mountain_excursions = int(input())
type_of_excursion = input()
mountain_count = 0
sea_count = 0

while type_of_excursion != 'Stop':
    if type_of_excursion == 'sea' and sea_count < sea_excursions:
        sea_count += 1
    elif type_of_excursion == 'mountain' and mountain_count < mountain_excursions:
        mountain_count += 1

    if sea_count == sea_excursions and mountain_count == mountain_excursions:
        print(f'Good job! Everything is sold.')
        break

    type_of_excursion = input()

profit = sea_count * 680 + mountain_count * 499
print(f'Profit: {profit} leva.')
