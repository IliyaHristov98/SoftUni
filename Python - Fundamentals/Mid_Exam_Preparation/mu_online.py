health = 100
btc = 0
rooms = input().split("|")
is_dead = False
for x in rooms:
    room = x.split()
    action = room[0]
    value = int(room[1])

    if action == "potion":
        if health == 100:
            print(f"You healed for 0 hp.")
        elif health + value <= 100:
            print(f"You healed for {value} hp.")
            health += value
        elif health + value > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        print(f"Current health: {health} hp.")

    elif action == "chest":
        btc += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health <= 0:
            is_dead = True
            print(f"You died! Killed by {action}.\n"
                  f"Best room: {rooms.index(x) + 1}")
            break
        else:
            print(f"You slayed {action}.")

if not is_dead:
    print(f"You've made it!\n"
          f"Bitcoins: {btc}\n"
          f"Health: {health}")
