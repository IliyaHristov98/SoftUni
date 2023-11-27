n = int(input())
heroes = {}

for _ in range(n):
    hero = input().split()
    heroes[hero[0]] = [int(hero[1]), int(hero[2])]

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    action = command[0]
    name = command[1]

    if action == "CastSpell":
        mana_needed = int(command[2])
        spell_name = command[3]
        if heroes[name][1] >= mana_needed:
            heroes[name][1] -= mana_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name][1]} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif action == "TakeDamage":
        damage = int(command[2])
        attacker = command[3]
        if damage >= heroes[name][0]:
            print(f"{name} has been killed by {attacker}!")
            del heroes[name]
        else:
            heroes[name][0] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name][0]} HP left!")

    elif action == "Recharge":
        amount = int(command[2])
        if heroes[name][1] + amount > 200:
            print(f"{name} recharged for {200 - heroes[name][1]} MP!")
            heroes[name][1] = 200
        else:
            heroes[name][1] += amount
            print(f"{name} recharged for {amount} MP!")

    else:
        amount = int(command[2])
        if heroes[name][0] + amount > 100:
            print(f"{name} healed for {100 - heroes[name][0]} HP!")
            heroes[name][0] = 100
        else:
            heroes[name][0] += amount
            print(f"{name} healed for {amount} HP!")

for key, value in heroes.items():
    print(f"{key}\n  HP: {value[0]}\n  MP: {value[1]}")
