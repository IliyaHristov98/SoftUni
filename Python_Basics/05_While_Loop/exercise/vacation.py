needed_money = float(input())
owned_money = float(input())
days_counter = 0
spending_counter = 0
managed_to_save = True

while owned_money < needed_money and spending_counter < 5:
    spend_or_save = input()
    amount = float(input())
    days_counter += 1
    if spend_or_save == 'save':
        owned_money += amount
        spending_counter = 0
    elif spend_or_save == 'spend':
        owned_money -= amount
        spending_counter += 1
        if owned_money < 0:
            owned_money = 0

if spending_counter == 5:
    managed_to_save = False
if owned_money >= needed_money:
    managed_to_save = True

if not managed_to_save:
    print(f"You can't save the money.\n"
          f"{days_counter}")
else:
    print(f'You saved the money for {days_counter} days.')
