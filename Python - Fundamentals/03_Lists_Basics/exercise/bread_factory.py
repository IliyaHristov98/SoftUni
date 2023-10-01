energy = 100
coins = 100
list_of_events = input().split('|')
all_handled = True
for event in list_of_events:
    current_event = event.split("-")
    event_value = int(current_event[1])
    type_of_event = current_event[0]
    if type_of_event == 'rest':
        current_energy = energy
        energy += event_value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy
        print(f'You gained {gained_energy} energy.\n'
              f'Current energy: {energy}.')
    elif type_of_event == 'order':
        if energy >= 30:
            coins += int(current_event[1])
            energy -= 30
            print(f'You earned {event_value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= event_value:
            coins -= event_value
            print(f'You bought {type_of_event}.')
        else:
            print(f'Closed! Cannot afford {type_of_event}.')
            all_handled = False
            break

if all_handled:
    print(f'Day completed!\n'
          f'Coins: {coins}\n'
          f'Energy: {energy}')
