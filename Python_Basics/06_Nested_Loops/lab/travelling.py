destination = input()

while destination != 'End':
    budget = float(input())
    collected_money = 0
    while collected_money < budget:
        saved = float(input())
        collected_money += saved
    print(f'Going to {destination}!')
    destination = input()
