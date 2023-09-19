groups_count = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for people_per_group in range(groups_count):
    people = int(input())
    if people <= 5:
        musala += people
    elif people <= 12:
        montblanc += people
    elif people <= 25:
        kilimanjaro += people
    elif people <= 40:
        k2 += people
    else:
        everest += people

total_people = musala + montblanc + kilimanjaro + k2 + everest

print(f'{musala / total_people * 100:.2f}%')
print(f'{montblanc / total_people * 100:.2f}%')
print(f'{kilimanjaro / total_people * 100:.2f}%')
print(f'{k2 / total_people * 100:.2f}%')
print(f'{everest / total_people * 100:.2f}%')